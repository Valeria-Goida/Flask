from flask import Flask, render_template, request
import math

app = Flask(__name__)


# Функция для округления результата до заданной точности
def round_with_precision(value, precision):
    return round(value, precision)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Получение данных из формы
            angle = float(request.form['angle'])
            unit = request.form['unit']
            func = request.form['function']
            precision = int(request.form['precision'])

            # Переводим градусы в радианы, если выбраны градусы
            if unit == 'degrees':
                angle = math.radians(angle)

            # Вычисление тригонометрической функции
            if func == 'sin':
                result = math.sin(angle)
            elif func == 'cos':
                result = math.cos(angle)
            elif func == 'tan':
                result = math.tan(angle)

            # Округляем результат до нужной точности
            result = round_with_precision(result, precision)
        except ValueError:
            result = "Ошибка: введите корректные данные."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
