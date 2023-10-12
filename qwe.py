from flask import Flask
app = Flask(__name__)

@app.route('/')
def qwe():
	a = 4.
	b = 7.
	c = 4.

	d = b**2 - 4 * a * c

	if d > 0:
    		x1 = (-b + sqrt(d) / (2 * a))
    		x2 = (-b - sqrt(d) / (2 * a))
    		return(f'x1 = {x1:.2f}; x2 = {x2:.2f}')
	elif d == 0:
    		x1 = -b / (2 * a)
    		return(f'x1 = {x1:.2f}')
	else:
    		return('Нет корней')
