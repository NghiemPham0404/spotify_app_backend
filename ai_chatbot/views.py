import requests
import re
from django.db.models import Count, Q
from songs.models import Song
from users.models import User
from albums.models import Album
from artists.models import Artist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .service import generate_sql_from_prompt, execute_sql, generate_response_from_result
from .prompts import system_db_design
import json

# @csrf_exempt
# def deepseek_view(request):

#     if request.method == "POST":
#         data = json.loads(request.body)
#         user_prompt = data.get("prompt", "")

#         # 🧠 Example of injecting backend data (can be from models/db)
#         songs_with_view_count = (
#             Song.objects.annotate(
#                 view_count=Count('interaction', filter=Q(interaction__interaction_type='view'))
#             )
#             .values('title', 'view_count')
#         )
#         artists_in_sytem = Artist.objects.all().values_list('name')


#         system_user_count = len(User.objects.all())
#         song_count = len(Song.objects.all())
#         artist_count = len(Artist.objects.all())

#         # 📝 Format dữ liệu để đưa vào prompt
#         view_info = "\n".join(
#             f"- {song['title']}: {song['view_count']} views"
#             for song in songs_with_view_count
#         )

#         full_prompt = f"""
# System status:

# Songs title and their views count: 
# {view_info}
# Artists in system:
# {artists_in_sytem}

# Users count in system : {system_user_count}
# Songs count in system : {song_count}
# Artist count in system : {artist_count}

# User prompt (User request) : {user_prompt}
# """

#         payload = {
#             "prompt":full_prompt,
#             "model": "llama3.2:1b",
#             "stream": False
#         }

#         try:
#             response = requests.post("http://localhost:11434/api/generate", json=payload)
#             response.raise_for_status()
#             result = response.json()
#             return JsonResponse({"response": result.get("response")})
#         except requests.RequestException as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "POST only"}, status=405)

@csrf_exempt
def deepseek_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)
    user_prompt = data.get("prompt", "")

    try:
        sql = generate_sql_from_prompt(user_prompt, system_db_design)
        print(f"SQL query string : {sql}")
        result = execute_sql(sql)
        print(f"Query result  : {result}")
        ai_response = generate_response_from_result(user_prompt, result)
        return JsonResponse({"response": ai_response})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)