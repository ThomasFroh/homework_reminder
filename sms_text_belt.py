import json
import requests

def send(nums: str, msg: str):

    resp = requests.post('https://textbelt.com/text', {
    'phone': '5158021908',
    'message': 'Hello world',
    'key': 'textbelt',
    })
    print(resp.json())
    # my_headers = {
    #     'Authorization': 'XXXXX',
    #     'Content-Type': 'application/json',
    #     'Accept': 'application/json',
    # }
    # data = { 
    #     "q": {
    #         "name": {
    #             "eq": "0aslam0"
    #         }
    #     }
    # }
    # payload = json.dumps(data)
        

if __name__ == '__main__':
    send('5158021908', 'test')