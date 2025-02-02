FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod a+x /app/scripts/app.sh

CMD ["uvicorn", "e_commerce.main:api", "--host", "0.0.0.0", "--port", "8000", "--reload"]