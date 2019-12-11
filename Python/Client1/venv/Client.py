import http

from http import client

hostName = "localhost"
hostPort = 8000
conn = http.client.HTTPConnection(hostName, hostPort)


quitApp = False

def GET():

    print("GET request")
    conn.request("GET", "index")
    response = conn.getresponse()
    data = response.read()
    print("GET response: " + data.decode())

def POST():
    print('\n')
    print ('Add new User')
    name = input('Name: ')
    phone = input('Phone No.: ')
    email = input('Email: ')
    password = input('Password: ')
    
    print("POST request")
    data_to_post = str(name) + ',' + str(phone) + ',' + str(email) + ',' + str(password)

    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request("POST", "add_user", data_to_post.encode(), headers)
    response = conn.getresponse()
    data = response.read()
    print ("POST response: " + data.decode())

while quitApp is False:
    print ('\n')
    print ('HTTP Client testbed')
    print ('1..GET data')
    print ('2..Add User')
    print ('X..Quit')
    print ('\n')

    key = input('>')

    if key is '1':
        GET()

    if key is '2':
        POST()

    if key is 'x':
        quitApp = True

conn.close()