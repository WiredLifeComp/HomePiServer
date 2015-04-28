from flask import Flask
from flask import request
from flask import Response
import json
import requests

app = Flask(__name__)


class Zone:
    def __init__(self):
        self.arrival = "2015-04-21T11:42:11.000+02:00"
        self.departure = "2015-04-21T11:58:32.000+02:00"
        self.latitude = 55.61592
        self.longitude = 12.987113


class Inventory:
    def __init__(self):
        self.resources = ["Dirt", "Dirt", "Stone"]
        self.items = ["DiamondPickAxe", "WoodenAxe"]


class User:
    def __init__(self):
        self.username = 'Julian'
        zone = Zone()
        inventory = Inventory()
        self.zones = [zone.__dict__]
        self.inventory = inventory.__dict__


class UserData:
    def __init__(self):

        user = User()
        self.user = user.__dict__
        self.unload = "2015-04-21T13:04:54.000+02:00"


class JsonEncoder:
    def __init__(self, obj):
        self.userData = obj

    def Encode(self):
        result = json.dumps(self.userData.__dict__, sort_keys=True, indent=4)
        return result


#Sends JSON package to Main Pi Server
@app.route('/WelcomeHome', methods=['POST'])
def SendPackageToMainPi():
    #encoder = JsonEncoder(request.data)
    r = requests.post("http://10.2.15.95:7070/data", data=request.data)
    print(r.status_code, r.reason)
    return Response(status=r.status_code)

if __name__ == "__main__":
    app.debug = True
    app.run(host="10.1.16.108", port=5000)
	

