# import requests
# import json

# URL ="http://127.0.0.1:8000/student_api/"

# def get_data(id=None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     joson_data = json.dumps
#     r = requests.get(url=URL, data= joson_data)

#     data = r.json()
#     print(data)

# get_data()

import requests
import json

url = "your_api_endpoint"
data = {"key": "value"}

# Serialize the data using json.dumps
serialized_data = json.dumps(data)

# Use the data parameter to send the serialized data
response = requests.post(url, data=serialized_data, headers={'Content-Type': 'application/json'})

# Check the response
print(response.status_code)
print(response.json())