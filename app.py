from datetime import datetime
from flask import Flask, request
from suds.client import Client

app = Flask("__name__")
# client = Client('http://localhost:8090/?wsdl', cache=None)


@app.route('/')
def index():
    return "It's working!"


# @app.route('/showip', methods=['GET'])
# def host():
#     domain_name = request.args.get('domain_name')
#     if domain_name is None:
#         domain_name = 'google.com'
#     return client.service.res_name(domain_name)


if __name__ == "__main__":
    app.run(debug=True)
