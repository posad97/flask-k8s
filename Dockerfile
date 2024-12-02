FROM python:3.8-alpine

WORKDIR /app

RUN pip install Flask flask-session

COPY . .

ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]