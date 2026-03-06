FROM python:3.11

# prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# prevent buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]