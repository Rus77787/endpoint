import json
from botocore.vendored import requests
from urllib.parse import parse_qs

def lambda_handler(event, context):
    
    data=parse_qs(event['params'])#параметры приходят согласно настройкам меппинга в гетавее
    event=data['event'][0]
    key=data['auth[application_token]'][0]
    
    #если это наш первый Битрикс24 стучится и если это событие создания нового лида в нем
    if (event=='ONCRMLEADADD' and key=='81rof1a1dbydthgdl34g5rxkdkqc2mxa'):
        
        lid_id=data['data[FIELDS][ID]'][0]
        
        #запросим из первого Б24 остальные параметры лида
        response = requests.get('https://rosasprings.bitrix24.ru/rest/290/81rof1a1dbydthgdl34g5rxkdkqc2mxa/crm.deal.get',{"id":lid_id})
        lead_data=response.json()
        
        #тут ищу более изящное решение - пока пусть будет так
        lead_data2 = {
            "fields" : {
                "NAME" : lead_data['result']['NAME'],
                "TITLE" : lead_data['result']['TITLE'],
                "PHONE" : dict(),
                "EMAIL" : dict()
            },
        'params' : {"REGISTER_SONET_EVENT" : "Y"}
        }
        
        try:
            phone={
                "VALUE" : lead_data['result']['PHONE'][0]['VALUE'], 
                "VALUE_TYPE" : lead_data['result']['PHONE'][0]['VALUE_TYPE']
                }
            
            lead_data2['fields']['PHONE']['0']=phone
        except:
            pass
        
        try:
            email={
                "VALUE" : lead_data['result']['EMAIL'][0]['VALUE'], 
                "VALUE_TYPE" : lead_data['result']['EMAIL'][0]['VALUE_TYPE']
                }
            
            lead_data2['fields']['EMAIL']['0']=email
        except:
            pass
        
        
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
