__author__ = 'J'
import requests


if __name__ == '__main__':
    requests.post("http://10.1.16.193:5000/HoneyImHome", data='{ "username" : "NewUser",   "isHome" : "true",  "ipAddress" : "10.1.16.193"}')

