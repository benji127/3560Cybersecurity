#HaveIbeenPowned script python using API
# Sha-1 


import requests
import hashlib

password = input("What is the password?")
sha_password = hashlib.sha1(password.encode()).hexdigest()
#Divide password in 2 parts since the API asks for 5 first digitis as parameter in the URL
sha_prefix=sha_password[0:5]

sha_suffix = sha_password[5:].upper()

url = "https://api.pwnedpasswords.com/range/" + sha_prefix
payload={}
headers={}
response = requests.request("GET", url, headers=headers, data=payload)
pwnd_dict = {}

pwnd_list = response.text.split("\r\n")
for pwnd_pass in pwnd_list:
    pwnd_hash = pwnd_pass.split(":")
    
    pwnd_dict[pwnd_hash[0]]= pwnd_hash[1]
    
if sha_suffix in pwnd_dict.keys():
    print("Password has been compromised {0} times".format(pwnd_dict[sha_suffix]))
else:
    print("Passwaord is safe")