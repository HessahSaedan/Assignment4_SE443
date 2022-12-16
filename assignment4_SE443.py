#GET

import requests
api_url = "https://reqres.in/api/users?delay=3"
response = requests.get(api_url)
print(response.json())
response.status_code

if response.status_code == 200 : 
    print("200 response: ok")
    
elif response.status_code == 404 :
    print("404 response: failed")
    
elif response.status_code == 400 :
    print("400: response delayed")
    

#POST
import requests
api_url = "https://reqres.in/api/login"
todo = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
response = requests.post(api_url, json=todo)
print(response.json())
response.status_code


if response.status_code == 201 : 
    print("201 response: completed")
    
elif response.status_code == 200 :
    print("200 response: post request ok")
    
elif response.status_code == 400 :
    print("400: response error")



