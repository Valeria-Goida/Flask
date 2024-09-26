from flask import Flask, render_template, request
import math

app = Flask(__name__)


def round_with_precision(value, precision):
    return round(value, precision)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            angle = float(request.form['angle'])
            unit = request.form['unit']
            func = request.form['function']
            precision = int(request.form['precision'])

            if unit == 'degrees':
                angle = math.radians(angle)

            if func == 'sin':
                result = math.sin(angle)
            elif func == 'cos':
                result = math.cos(angle)
            elif func == 'tan':
                result = math.tan(angle)

            result = round_with_precision(result, precision)
        except ValueError:
            result = "Ошибка: введите корректные данные."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
