#FASTAPI BACKEND BASE PROJECT WITH POSTGRESQl

Run app
uvicorn app.main:app --reload

Migration commands:
alembic revision --autogenerate -m "First revision"
alembic upgrade head