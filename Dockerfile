# syntax=docker/dockerfile:1
FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
WORKDIR /challenge_web
COPY requirements.txt /challenge_web/requirements.txt
RUN pip install -r requirements.txt
COPY . /challenge_web
RUN chown -R $USER:$USER /challenge_web/
EXPOSE 8000

# Configure the main process to run when running the image
CMD ["python", "manage.py", "runserver", "0.0.0.0"]
