'''This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def pro():
  return "<html><title>Practica1</title><body><h1>Practica1</h1><center>Practica creada en Python y subida Paas Heroku.<br><br>Primera version, conforme vayamos avanzando en la asignatura de Desarrollo de aplicaciones para internet<br>avanzara en originalidad la app.<br><br> Rafael Carrasco. Ugr (Granada)<center></body></html>"
