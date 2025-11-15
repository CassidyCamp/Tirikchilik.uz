# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Kerakli paketlar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodni nusxalash
COPY . .

# Botni ishga tushirish
CMD ["python", "bot.py"]