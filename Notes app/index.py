from flask import Flask, render_template, request, url_for, flash, redirect, send_file
import sqlite3
from werkzeug.exceptions import abort
import time
from extractor import fileOps

def database_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(id):
    conn = database_connection()
    post = conn.execute('select * from posts where id=?', (id,)).fetchone()
    conn.close()

    if post is None:
        abort(404)

    return post


app = Flask(__name__)
app.config.from_pyfile('sessionKey.py')

@app.route('/')
def index():
    try:
        conn = database_connection()
        posts = conn.execute('select * from posts').fetchall()
        conn.close()
        # print(posts)
        return render_template('index.html', posts=posts) 

    except Exception as e:
        print("Error occured at mainpage")


@app.route('/create', methods=('GET', 'POST'))
def create():

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = database_connection()
            conn.execute('insert into posts (title, content) values (?,?)', (title, content))
            conn.commit()
            conn.close()

            return redirect(url_for('index'))

    return  render_template('create.html')


@app.route('/<int:id1>/edit', methods=('GET', 'POST'))
def edit(id1):
    post = get_post(id1)

    if request.form == 'exit':
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = database_connection()
            conn.execute('update posts set title = ?, content = ? where id = ?', (title, content, id1))
            conn.commit()
            conn.close()

            return redirect(url_for('index'))
    
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):

    conn = database_connection()
    conn.execute('delete from posts where id=?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))


@app.route('/<int:id>')
def post(id):
    post = get_post(id)
    # print(post)
    return render_template('post.html', post=post)


@app.route('/getCSVfile')
def getCSV():
    
    cur_date = str(time.strftime("%Y%m%d_%H%M", time.localtime()))
    fileOps(cur_date)
    
    return send_file('./exports/data'+cur_date+'.csv',
    mimetype='text/csv',
    attachment_filename='data'+cur_date+'.csv',
    as_attachment=True)


if __name__ == '__main__':
    app.run(port=8000, debug=True)

