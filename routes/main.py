from app import app
from flask import render_template
from models import Plant, Employee, Salon


@app.route('/')
def main():
     plants = Plant.query.all()
     employees = Employee.query.all()
     salons = Salon.query.all()

     return render_template('index.html', plants=plants, employees=employees, salons=salons)


@app.route('/plant/<int:id>')
def plant(id):
     plant = Plant.query.get(id)
     return render_template('plant.html', plant=plant)

@app.route('/salon/<int:id>')
def salon(id):
     salon = Salon.query.get(id)
     return render_template('salon.html', salon=salon)

@app.route('/employee/<int:id>')
def employee(id):
     employee = Employee.query.get(id)
     if employee.department_type == "plant":
          employee.department = Plant.query.get(employee.department_id)
     elif employee.department_type == "salon":
          employee.department = Salon.query.get(employee.department_id)
     return render_template('employee.html', employee=employee)

