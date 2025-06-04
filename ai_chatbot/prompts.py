SQL_GENERATION_PROMPT = """
You are an AI that translates natural language questions (in Vietnamese) into SQL queries.

Database design:
{system_db_design}

Use MySQL syntax.
Use the correct table names based on Django structure:
- artists_artist
- albums_album
- songs_song
- songs_interaction
- users_user
- playlists_playlist
- playlists_playlistsong
- artist_follow
- songs_participant

DO NOT EXPLAIN.
DO NOT THINKING.
DO NOT CONTAIN ANY string like 'sql, code, SQL query string....' 
JUST ONLY RETURN THE SQL QUERY. Example:

SELECT COUNT(*) FROM artist_artist;

NOTE : Minimize Table usings as possible

User prompt (user question):
{user_prompt}
"""

RESPONSE_GENERATION_PROMPT = """
question : {user_prompt}
result : {result_list}

make a response base on question and result (DON'T EXPLAIN)
"""

system_db_design = """

Table "songs_song" {
  "id" INT [pk, increment]
  "title" nVARCHAR(255) [not null]
  "duration" INT
  "genre" nVARCHAR(100)
  "release_date" DATE
  "audio_file" nVARCHAR(255)
  "image" nVarchar(255)
  "album_int" nVarchar(255)
}

Table "users_user" {
  "id" INT [pk, increment]
  "email" nVARCHAR(255) [not null]
  "password" nVARCHAR(255) [not null]
    "subscription_type" nVARCHAR(50)
  "profile_picture" nVARCHAR(255)
}

Table "albums_album" {
  "id" INT [pk, increment]
  "artist_id" INT [not null]
  "title" nVARCHAR(255) [not null]
  "description" TEXT
  "creation_date" DATE
  "publish_date" DATE
}

Table "artists_artist" {
  "id" INT [pk, increment]
  "name" nvarchar(255)
  "profile_picture" nVARCHAR(255)
  "biography" TEXT
}

Table "songs_participant" {
  "song_id" int
  "artist_id" int
  "role" nvarchar(255)
  
  Indexes {
    (song_id, artist_id) [pk]
  }
}

Table "songs_interaction" {
  "id" INT [pk, increment]
  "user_id" INT [not null]
  "song_id" INT [not null]
  "interaction_type" VARCHAR(50)
  "timestamp" DATETIME
}

Table "artists_follow" {
  "follower_id" INT [not null]
  "followee_id" INT [not null]
  "Timestamp" DATETIME

  Indexes {
    (follower_id, followee_id) [pk]
  }
}

Ref:"songs_song"."id" < "songs_interaction"."song_id"
Ref: "albums_album"."artist_id" > "artists_artist"."id"
Ref: "artists_artist"."id" < "songs_participant"."artist_id"
Ref: "songs_aarticipant"."song_id" > "songs_song"."id"
Ref: "artists_follow"."followee_id" > "artists_artist"."id"
Ref: "artists_follow"."follower_id" > "users_user"."id"
Ref: "songs_interaction"."user_id" > "uses_user"."id"
Ref: "songs_song"."album_id" < "albums_album"."id"

"""