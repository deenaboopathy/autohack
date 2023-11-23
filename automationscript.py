# test file

print ( " hello world")
import requests
r = requests.get("http://34.105.137.169:8070/")
print(str(r.status_code) + '\n')
print(str(r.content) + '\n')
if("Hello, Docker Version Two" in str(r.content )):
    print("Sucess "+ '\n')
else:
    print("failure")