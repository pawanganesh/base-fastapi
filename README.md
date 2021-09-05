#FASTAPI BACKEND BASE PROJECT WITH POSTGRESQl

Clone project:
git clone https://github.com/pawanlalganesh/base-fastapi

Run app:
uvicorn app.main:app --reload

Migration commands:
alembic revision --autogenerate -m "First revision"
alembic upgrade head