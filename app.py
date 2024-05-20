from flask import Flask, render_template

app = Flask(__name__)

# Определяем классы для сущностей
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

# Создаем объекты и добавляем их в массивы
students = [
    Student("Alice", 20, "Computer Science"),
    Student("Bob", 22, "Mechanical Engineering"),
    Student("Charlie", 21, "Mathematics"),
    Student("David", 23, "Physics"),
    Student("Eva", 20, "Biology")
]

cars = [
    Car("Toyota Camry", 2018, "Red"),
    Car("Honda Accord", 2020, "Blue"),
    Car("Ford Mustang", 2019, "Black"),
    Car("Chevrolet Malibu", 2017, "White"),
    Car("BMW 3 Series", 2021, "Silver")
]

@app.route('/')
def health_check():
    return render_template('health_check.html')

@app.route('/students')
def show_students():
    return render_template('students.html', students=students)

@app.route('/cars')
def show_cars():
    return render_template('cars.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)
