from flask import Flask, render_template, request, url_for, flash, redirect, send_file, Response
import sqlite3
from werkzeug.exceptions import abort
import time
# from extractor import fileOps

def database_connection():
    conn = sqlite3.connect('database.db', timeout=2)
    conn.row_factory = sqlite3.Row
    return conn

def get_post(id):
    conn = database_connection()
    post = conn.execute('select * from posts where id=?', (id,)).fetchone()
    conn.close()

    return post


app = Flask(__name__)
app.config.from_pyfile('sessionKey.py')

@app.route('/issue-tracker')
def index():
    try:
        conn = database_connection()
        posts = conn.execute('select * from posts order by priority, id asc').fetchall()
        conn.close()
        # print(posts)
        return render_template('index.html', posts=posts) 

    except Exception as e:
        print("Error occured at mainpage")


@app.route('/issue-tracker/create', methods=('GET', 'POST'))
def create():

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        pri = request.form.get('priority')

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            cur_time = str(time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()))
            conn = database_connection()
            conn.execute('insert into posts (title, content, created, priority) values (?,?,?,?)', (title, content, cur_time ,pri))
            conn.commit()
            conn.close()

            return redirect(url_for('index'))

    return  render_template('create.html'
    # priority=[{'name':'Critical'},{'name':'High'},{'name':'Medium'},{'name':'Low'}]
    )


@app.route('/issue-tracker/<int:id1>/edit', methods=('GET', 'POST'))
def edit(id1):
    post = get_post(id1)

    if request.form == 'exit':
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        pri = request.form.get('priority')

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            cur_time = str(time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()))
            conn = database_connection()
            conn.execute('update posts set title = ?, content = ?, created = ? where id = ?', (title, content, cur_time, id1))
            conn.commit()
            conn.close()

            return redirect(url_for('index'))
    
    return render_template('edit.html', post=post)

@app.route('/issue-tracker/<int:id>/delete', methods=('POST',))
def delete(id):

    conn = database_connection()
    conn.execute('delete from posts where id=?', (id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))


@app.route('/issue-tracker/<int:id>')
def post(id):
    post = get_post(id)

    if post is None:
        abort(Response('''
        <h1>Something you are looking at is not available!</h1>
        <br>
        <a href="/issue-tracker">GO HOME</a>
        '''))

    # print(post)
    return render_template('post.html', post=post)


# @app.route('/getCSVfile')
# def getCSV():
    
#     cur_date = str(time.strftime("%Y%m%d_%H%M", time.localtime()))
#     fileOps(cur_date)
    
#     return send_file('./exports/data'+cur_date+'.csv',
#     mimetype='text/csv',
#     attachment_filename='data'+cur_date+'.csv',
#     as_attachment=True)


# app.run(port=8000, debug=True)

