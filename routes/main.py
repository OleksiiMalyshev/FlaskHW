from app import app, db
from flask import render_template, request, redirect, url_for
from models import Plant, Employee


@app.route('/')
def main():
    plants = Plant.query.all()
    employees = Employee.query.all()

    return render_template('index.html', plants=plants, employees=employees)


@app.route('/plant/<int:id>')
def plant(id):
    plant = Plant.query.get(id)
    return render_template('plant.html', plant=plant)


@app.route('/plant/<int:id>/edit')
def plant_edit_page(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('edit-plant.html', plant=plant, employees=employees)


@app.route('/plant/<int:id>/update', methods=['POST'])
def plant_update(id):
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
    return render_template('employee.html', employee=employee)


@app.route('/employee/<int:id>/update', methods=['POST'])
def employee_update(id):
    employee = Employee.query.get(id)
    form_data = request.form
    employee.name = form_data.get('name')
    employee.email = form_data.get('email')
    employee.department_type = form_data.get('department_type')
    employee.department_id = form_data.get('department_id')
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('employee', id=id))


@app.route('/employee/<int:id>/edit')
def employee_edit_page(id):
    employee = Employee.query.get(id)
    plants = Plant.query.all()
    return render_template('edit-employee.html', plants=plants, employee=employee)
