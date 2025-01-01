## Welcome to your todobuddy! :dart:
This is a fullstack application for tracking your tasks and achieving your goals!
## Runnning backend:
**1) Django development server:**<br />
```source path/to/virtual/environment/activate```<br />
```python manage.py runserver 0.0.0.0:<port>```<br />
**2) Gunicorn wsgi server:**<br />
```gunicorn path/to/main_app.wsgi:application --bind 0.0.0.0:<port>```<br />
**3) Docker container :whale::**<br />
```sudo docker build -t <new_image_name> <export_path>```<br />
```docker run -d -p <port>:<port> <image_name> <new_container_name>```
## Running frontend:
**1) Node development server:**<br />
```npm run serve /*run it in the root directory of frontend app*/```<br />
**2) Using node's simple http-server:**<br />
```http-server```<br />
index.html will be served as the default  file  to  any  directory  re‐quests.<br />
**3) Docker container :whale::**<br />
```sudo docker build -t <new_image_name> <export_path>```<br />
```docker run -d -p <port>:<port> <image_name> <new_container_name>```
