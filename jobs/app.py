from flask import Flask, render_template, g
import sqlite3

PATH="db/jobs.sqlite"
app = Flask(__name__)


def open_connection():
    connection=getattr(g, '_connectoin', None)
    if(connection == None):
        connection=g._connectoin=sqlite3.connect(PATH)
    connection.row_factory=sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=false, single=false):
    connection=open_connection()
    cursor=connection.execute(sql, values)
    if commit == true:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results


@app.teardown_appcontext
def close_connection(exception):
    connection=getattr(g, '_connectoin', None)
    if connection is not none:
        connection.close()

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
