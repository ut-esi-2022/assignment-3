from suds.client import Client

client = Client('http://localhost:8090/?wsdl', cache=None)

print("Running Service 1 ...")
print(client.service.ping_host('www.facebook.com'))
print("Running Service 2 ...")
print(client.service.dns_lookup('www.google.com'))
print("\nRunning Service 3 ...")
print(client.service.dig_more('www.err.ee'))