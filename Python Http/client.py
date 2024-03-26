import http.client

client = http.client.HTTPConnection(host = "localhost", port=1234)
client.request("GET", "/time")

response = client.getresponse()
print("Status: ", response.status)
print("Response: ", response.read())