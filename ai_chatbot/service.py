import re
import requests
from django.db import connection
from .prompts import SQL_GENERATION_PROMPT, RESPONSE_GENERATION_PROMPT

def generate_sql_from_prompt(user_prompt, system_db_design):
    prompt = SQL_GENERATION_PROMPT.format(
        user_prompt=user_prompt,
        system_db_design=system_db_design
    )
    response = requests.post("http://localhost:11434/api/generate", json={
        "prompt": prompt,
        "model": "gemma3",
        "stream": False
    })
    response.raise_for_status()
    raw = response.json().get("response", "").strip()
    raw = re.sub(r"(SQL query string\s*:\s*)|(```sql)|(```)|(<think>.*?</think>)", "", raw, flags=re.IGNORECASE | re.DOTALL).strip()
    return raw

def execute_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows] if columns else rows

def generate_response_from_result(user_prompt, result_list):
    prompt = RESPONSE_GENERATION_PROMPT.format(
        user_prompt=user_prompt,
        result_list=result_list
    )
    response = requests.post("http://localhost:11434/api/generate", json={
        "prompt": prompt,
        "model": "gemma3",
        "stream": False
    })
    response.raise_for_status()
    return response.json().get("response", "")