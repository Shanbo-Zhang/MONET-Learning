import http.client

client = http.client.HTTPConnection(host = "127.0.0.1", port=1234)
client.request("GET", "/time")

response = client.getresponse()
print("Status: ", response.status)
print("Response: ", response.read())