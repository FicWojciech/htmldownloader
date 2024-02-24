import os, sys
import urllib.parse
import validators
import requests
from datetime import datetime

print(f"Number of arguments: ",len(sys.argv))
print(f"Arguments list: ",sys.argv)

url = input("Provide the complete website address (including the https:// prefix): ")

if len(sys.argv) > 1:
    url = sys.argv[1]

print(f"Website to download {url}")

scriptDir = os.path.dirname(__file__)

os.chdir(scriptDir)
print(f"Current working dir: {os.getcwd()}")

if not os.path.exists("./websites"):
    os.mkdir("./websites")


parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl)

validFlag = validators.url(url)
if validFlag:
    print("URL:", url, "is valid.")
else:
    print(f"URL {url} is invalid.")
    raise Exception("Bad url!")

response = requests.get(url, allow_redirects=True)

if response.ok == True:
    print(f"Response ok from server for url {url}")
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y %H.%M.%S")
    print(dateString)
    fileName = "./websites/" + parsedUrl.netloc + " " + dateString + ".html"
    print(fileName)
    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()
