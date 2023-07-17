from flask import Flask, request
import subprocess
import json

def change_sni(sni):
    with open("sing-box_config.json", "r") as f:
        data = json.load(f)
    data['inbounds'][0]['tls']['server_name'] = sni
    data['inbounds'][0]['tls']['reality']['handshake']['server'] = sni
    with open("sing-box_config.json", "w") as f:
        json.dump(data, f)


app = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_post():
    text = request.data.decode('utf-8')
    change_sni(text)
    subprocess.run(['systemctl', 'restart', 'sing-box', '--now'])
    return 'Changed SNI'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33333)
