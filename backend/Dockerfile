FROM python:3.10.12-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --index-url https://pypi.tuna.tsinghua.edu.cn/simple/ -r /app/requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput 


# Run migrations 
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

# Run the application with Gunicorn 
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "todo.wsgi:application"]
