FROM python:3.10-slim

EXPOSE 8000

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /app
COPY . /app

CMD ["gunicorn", "app:app", "-c", "gunicorn.py"]
