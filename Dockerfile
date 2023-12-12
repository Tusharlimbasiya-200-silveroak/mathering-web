
FROM python:3.10.9-slim

RUN apt update && apt -y install libsndfile1 ffmpeg redis-server supervisor

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x ./init.sh && mkdir data

CMD ["./init.sh"]
