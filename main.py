import requests
from datetime import datetime
#have made this global so that we can use it in our whole code
USERNAME = 'afreed'
TOKEN = 'qwertyuio12456mnbv'
GRAPH_ID = 'graph10'

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    'token':USERNAME,
    'username':TOKEN,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}
response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)


#creating the graph using the api and passing required parameters
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_configuration = {
    'id':GRAPH_ID,
    'name':'Cycling Graph',
    'unit':'kms',
    'type':'float',
    'color':'ajisai'
}

headers= {
    'X-USER-TOKEN': TOKEN
}

response=requests.post(url=graph_endpoint,json=graph_configuration,headers=headers)
# print(response.text)


#post value of the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_date={
    'date':today.strftime('%Y%m%d'),
    'quantity': int(input("How many kilometers did you cycle today? ")),
}

response=requests.post(url=pixel_creation_endpoint,json=pixel_date,headers=headers)
# print(response.text)


#update using put method
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data ={ 
    'quantity':'12.5',
    }
response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)


#delete pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)


