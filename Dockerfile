FROM python:3.11

RUN apt-get update && apt-get install -y git
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver"]
# BjR570"ZIahG423"RI%
# scp -r -i /Users/daniilnishpal/Downloads/danil_nishpal /Users/daniilnishpal/Projects/booking_app_backend  danil_nishpal@83.136.30.248:.