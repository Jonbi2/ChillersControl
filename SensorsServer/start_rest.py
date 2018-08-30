from app import app

import json
import requests

port = int(json.load(open('config.json'))['Port'])
access_hash = str(json.load(open('config.json'))['AccessHash'])

if not requests.get("http://88.198.250.240:3001/api/" + access_hash).json()['result']:
    print("Your API key is invalid fuck you...")
    exit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)