FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Test-task-tg-bot

# Install dependencies
COPY requirements.txt /Test-task-tg-bot/
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Copy project
COPY . /Test-task-tg-bot/

CMD ["python", "main.py"]
