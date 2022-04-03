import requests, uuid, json

import time


# Add your subscription key and endpoint
subscription_key = "a2e893b822d14f8ba7f33007f69a4653"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.


location = "westus2"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'it',
    'to': ['en']
}

constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


salida = open('D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\programWordTranslated.txt', 'w+')

# You can pass more than one object in body.


with open('D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\programWordCleaned.txt','r') as file:
    # reading each line    
   for line in file:

        
        time.sleep(0.1)


        cadenaText = line
        


        body = [{
        'text': cadenaText.strip()
        }]


        #This two methods is send to the api and receive the word translated
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        #print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
        panorama = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))


        substring = "text"
        
       

        valor = panorama.find(substring)
        resubstring = panorama[(valor + 8):(valor + 24)]        
        
        commaPosition = resubstring.find(",")
        salidaString = resubstring[:(commaPosition-1)]
        
        print(salidaString)
        salida.write(salidaString.lower())
        salida.write("\n")
    
salida.close()
