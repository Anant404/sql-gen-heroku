from flask import Flask, render_template, request, jsonify
import psycopg2

try:
    conn1 = psycopg2.connect(database="dvdrental", user="postgres", password="loseyourself",
                            host="localhost")

    conn = psycopg2.connect(database="d5u109emjosvrq", user="nvxofslbxssifl", password="c1331e187831ccad38ff2225f26f36d7e213fdd5616330f5fa28babbafdf3ab1",
                            host="ec2-54-155-226-153.eu-west-1.compute.amazonaws.com")
    print("connected")

except:
    print("unable to connect")

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
