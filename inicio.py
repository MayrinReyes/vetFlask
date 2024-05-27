from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def inicio():
    return render_template("index.html")

@app.route('/nosotros')
def us():
    return render_template("nosotros.html")

@app.route('/conejos')
def conejo():
    return render_template("conejos.html")

@app.route('/contacto')
def cont():
    return render_template("contacto.html")

@app.route('/gatos')
def cat():
    return render_template("gatos.html")

@app.route('/nutrias')
def nut():
    return render_template("nutrias.html")

@app.route('/servicios')
def service():
    return render_template("servicios.html")


@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
