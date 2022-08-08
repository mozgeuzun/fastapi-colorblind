FROM python:3.11.0a3-alpine3.15

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./app /app/
WORKDIR /
CMD ["uvicorn", "app.main:api", "--host","0.0.0.0","--reload","--port","8000"]