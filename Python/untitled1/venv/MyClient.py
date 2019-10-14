from http import client

hostName = "localhost"
hostPort = 8000
conn = client.HTTPConnection(hostName,hostPort)

print ("GET request")
conn.request("GET", "index")
response = conn.getresponse()
data = response.read()
print("GET response: " + data.decode())

print ("POST request")
data_to_post = "this is a test from the client"

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn.request("POST", "add_score", data_to_post.encode(), headers)
response = conn.getresponse()
data = response.read()
print("POST response: " + data.decode())