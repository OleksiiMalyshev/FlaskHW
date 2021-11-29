from app import app, db
from flask import render_template, request, redirect, url_for, session
from utils.helpers import encrypt_string
from models import Plant, Employee


@app.route('/')
def main():
     plants = Plant.query.all()
     employees = Employee.query.all()

     return render_template('index.html', plants=plants, employees=employees, session=session)


@app.route('/plant/<int:id>')
def plant(id):
     plant = Plant.query.get(id)
     return render_template('plant.html', plant=plant, session=session)


@app.route('/login')
def login():
     return render_template('login.html', session=session)

@app.route('/auth', methods=['POST'])
def auth():
     form = request.form
     user = Employee.query.filter(Employee.email == form['login']).filter(Employee.password == encrypt_string(form['password'])).first()
     if user is not None:
          session['user'] = user.serialize
     return redirect("http://localhost:8082/")


@app.route('/logout')
def logout():
     session.pop('user')
     return redirect(url_for('main'))

@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
     if session.get('user') is None:
         return redirect("http://localhost:8082/")
     plant = Plant.query.get(id)
     employees = Employee.query.all()
     return render_template('edit-plant.html', plant=plant, employees=employees, session=session)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
     if session.get('user') is None:
         return redirect("http://localhost:8082/")
     plant = Plant.query.get(id)
     form_data = request.form
     plant.name = form_data.get('name')
     plant.location = form_data.get('location')
     plant.director_id = form_data.get('director_id')
     db.session.add(plant)
     db.session.commit()
     return redirect(url_for('plant', id=id))

@app.route('/employee/<int:id>')
def employee(id):
     employee = Employee.query.get(id)
     return render_template('employee.html', employee=employee, session=session)