#FASTAPI BACKEND BASE PROJECT WITH POSTGRESQl

Clone project:

git clone https://github.com/pawanlalganesh/base-fastapi

Create virtual environment and Install all requirements:

pip install -r requirements.txt

Run app:

uvicorn app.main:app --reload

Migration command:

alembic revision --autogenerate -m "First revision"

Migrate command:

alembic upgrade head

#HAVE FUN