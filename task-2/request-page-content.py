import requests 
r=requests.get('https://www.youtube.com/')
print(len(r.text))
file = open ("url Data.txt","w")
file.write(r.text)
file.close()