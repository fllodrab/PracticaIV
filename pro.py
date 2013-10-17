import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def pro():
  return "<html><title>Practica1</title><body><h1>Practica1</h1><center>Practica creada en Python y subida Paas Heroku.<br><br>Primera version, conforme vayamos avanzando en la asignatura de Desarrollo de aplicaciones para internet<br>avanzara en originalidad la app.<br><br> Rafael Carrasco. Ugr (Granada)<center></body></html>"
