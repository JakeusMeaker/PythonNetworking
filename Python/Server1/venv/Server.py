from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3

class MyServer (BaseHTTPRequestHandler):

    db = sqlite3.connect('mydb.db')


    #Get a cursor object
    def CreateTable(self):
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
        db.commit()

    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response_data = "The server has sent you this reply"
        self.wfile.write(response_data.encode())

    def do_POST(self):
        print("DO POST:" + self.path);
        db = sqlite3.connect('mydb.db')

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        inData = str(post_data).split(',', 4)
        name = inData[0]
        phone = inData[1]
        email = inData[2]
        password = inData[3]
        print (name + phone + email + password)

        cursor = db.cursor()
        cursor.execute('''INSERT INTO users(name, phone, email, password)
                                        VALUES(?, ?, ?, ?)''', (name, phone, email, password))
        print('user inserted')
        db.commit()



        self.send_response(200)
        self.end_headers()

        print( "POST: ", post_data.decode())

hostName = "localhost"
hostPort = 8000

mySever = HTTPServer((hostName,hostPort), MyServer)

try:
    mySever.serve_forever()
except KeyboardInterrupt:
    pass

mySever.server_close()