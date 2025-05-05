# Spotify
A music player app clonning Spotify using Django. FMDEditor stands for Fast MarkDown Editor.


# Requirement

## Prerequisites
- [Python>=3.11.2](https://www.python.org/downloads/)
- WSL (Or Cmder) is installed
- MySQL 

# Installation
0. Ensure that you already have all of the items above.
1. Clone this project to your local machine with this command:
```bash
git clone https://github.com/nghiempham0404/spotify_app_backend.git
cd FMDEditor
```
2. Install all requirements:
```bash
pip install -r requirements.txt
```
3. Migrate all changes:
```bash
python manage.py migrate
```
4. Create super user with your provided credentials:
```bash
python manage.py createsuperuser
```
5. Run project:
```bash
python manage.py runserver 0.0.0.0:8000
```
6. Now enter 127.0.0.1:8000 or {your_public_ip}:8000 to your browser's address bar to see the magic.

# Documentation

Developing...

# Issues, Bugs & Feature Requests

Just create new issue if you found any problems here: https://github.com/nghiempham0404/spotify_app_backend/issues

# Support & Questions

Need assisstance? Do not hesitate to ask for help at: https://github.com/nghiempham0404/spotify_app_backend/discussions
