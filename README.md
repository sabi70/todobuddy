# todobyddy :dart:
> This is a full stack application for tracking your tasks and achieving your goals!

<div align='center'>
  <img src='./frontend/src/assets/dartboard.png' alt='todobyddy preview' height='250px' />
</div>

## Features

1. Responsive and intuitive design.
2. Dark and light theme support.
3. Ease in usage.

## Setting up on local pc:
```git clone https://github.com/sabi70/todobuddy.git```<br />  

## Runnning backend:
**a) Django development server:**<br />
```source path/to/virtual/environment/activate```<br />
```python manage.py runserver 0.0.0.0:<port>```<br />
**b) Gunicorn wsgi server:**<br />
```gunicorn path/to/main_app.wsgi:application --bind 0.0.0.0:<port>```<br />
**c) Docker container :whale::**<br />
```sudo docker build -t <new_image_name> <export_path>```<br />
```docker run -d -p <port>:<port> <image_name> <new_container_name>```
## Running frontend:
**a) Node development server:**<br />
```npm run serve /*run it in the root directory of frontend app*/```<br />
**b) Using node's simple http-server:**<br />
```http-server```<br />
index.html will be served as the default  file  to  any  directory  re‐quests.<br />
**c) Docker container :whale::**<br />
```sudo docker build -t <new_image_name> <export_path>```<br />
```docker run -d -p <port>:<port> <image_name> <new_container_name>```

## Used technologies:
1) Backend:<br />
  > -Django<br />
  > -Gunicorn<br />
  > -Nginx<br />
  > -Postman<br />
  > -Docker<br />
  > -Git<br />
 2) Frontend:<br />
  > -Vue<br />
  > -Vuetify<br />
  > -Figma<br />
  > -GIMP<br />
  > -Git<br />
  > -Nginx<br />
  > -Docker<br />

## Author:

👤 **sabi70**

- Github: [@sabi70](https://github.com/sabi70)
