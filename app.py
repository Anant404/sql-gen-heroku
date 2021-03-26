from flask import Flask, render_template, request, jsonify
import psycopg2


import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )

mycursor = conn.cursor()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/join', methods=['POST', 'GET'])
def join():
    tablename = request.args.get('tablenameselected')
    joinm = request.args.get('joinmethod')
    pk = request.args.get('pk')
    columnselected = request.args.get('columnselected')
    return render_template('join.html', tablename=tablename, joinm=joinm, pk=pk, columnselected=columnselected)


@app.route('/say_what', methods=['POST', 'GET'])
def say_name1():
    table_name1 = request.get_json()
    sql_query = "SELECT* from " + table_name1 + " fetch first 5 rows only"
    mycursor.execute(sql_query)
    data1 = mycursor.fetchall()
    sql_query2 = "select column_name from information_schema.columns where table_name = '" + table_name1 + "'" + "order by ordinal_position"
    mycursor.execute(sql_query2)
    columnlist = mycursor.fetchall()

    return jsonify(res=table_name1, data1=data1, columnlist=columnlist)


@app.route('/say_column', methods=['POST', 'GET'])
def say_name2():
    table_name1 = request.get_json()

    sql_query2 = "select column_name from information_schema.columns where table_name = '" + table_name1 + "'" + "order by ordinal_position"
    mycursor.execute(sql_query2)
    columnlist = mycursor.fetchall()

    return jsonify(res=table_name1, columnlist=columnlist)


if __name__ == '__main__':
    app.run(debug=True)
