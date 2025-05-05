FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir -p /app/static

EXPOSE 8000

CMD ["gunicorn", "lost_and_found.wsgi:application", "--bind", "0.0.0.0:8000"]