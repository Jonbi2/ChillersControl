from app import app

port = int(json.load(open('config.json'))['Port'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)