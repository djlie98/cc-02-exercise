from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)


mydb = mysql.connector.connect(
  host=os.environ["MYSQL_HOST"],
  user=os.environ["MYSQL_USER"],
  password=os.environ["MYSQL_PASSWORD"],
  database=os.environ["MYSQL_DB"]
)
cursor = mydb.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS posts(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), msg VARCHAR(255))')

@app.route('/', methods=["GET"])
def posts():
    cursor.execute('''
      SELECT * FROM posts
    ''')
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/', methods=["POST"])
def post():
    data = request.json
    cursor.execute('''
      INSERT INTO posts(id, name, msg) VALUES(DEFAULT, '%s', '%s')
    ''' % (data["name"], data["msg"]))
    mydb.commit()
    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)