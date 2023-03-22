from flask import Flask, request, make_response, jsonify
#from flask_restful import Resource, Api
from flask_cors import CORS
from functools import wraps
import pymysql

app = Flask(__name__)
#api = Api(app)
cors = CORS(app)

@app.route('/users' , methods = ['GET'])
def get():
    conn = pymysql.connect(host = "localhost", user="root", password="", db="tcet")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM students")
    output = cur.fetchall()

    for x in output:
        print(x)
    conn.close()
    return jsonify(output);

@app.route('/usersedit' , methods = ['GET'])
def edit():
    conn = pymysql.connect(host = "localhost", user="root", password="", db="tcet")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    ID = int(request.args.get('ID'))
    sql = f"SELECT * FROM students WHERE ID ={ID}";
    cur.execute(sql)
    output = cur.fetchall()
    for x in output:
        print(x)
    conn.close()
    return jsonify(output);

@app.route('/users' , methods = ['DELETE'])
def delete():
    conn = pymysql.connect(host = "localhost", user="root", password="", db="tcet")
    cur = conn.cursor(pymysql.cursors.DictCursor)
    ID = int(request.args.get('ID'))
    sql = f"DELETE FROM students WHERE ID ={ID}";
    cur.execute(sql)
    output = cur.fetchall()
    conn.commit()
    print(cur.rowcount,"record deleteed")
    return jsonify("Record deleted successfully");


@app.route('/users' , methods = ['POST'])
def insert():
    conn = pymysql.connect(host = "localhost", user="root", password="", db="tcet")
    raw_json = request.get_json();
    Name = raw_json['Name'];
    Age = raw_json['Age'];
    City = raw_json['City'];
    sql = "INSERT INTO students (ID,Name,Age,City) VALUES (NULL,'"+Name+"','"+str(Age)+"', '"+City+"')";
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return jsonify("Record Inserted successfully");

@app.route('/users' , methods = ['PUT'])
def update():
    conn = pymysql.connect(host = "localhost", user="root", password="", db="tcet")
    raw_json = request.get_json();
    ID = raw_json['ID'];
    Name = raw_json['Name'];
    Age = raw_json['Age'];
    City = raw_json['City'];

    sql = "UPDATE students SET Name = '"+Name+"',Age = '"+str(Age)+"', City = '"+City+"' WHERE ID ='"+str(ID)+"'";
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return jsonify("Record Updated successfully");


if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=int("1234"), debug=True)
