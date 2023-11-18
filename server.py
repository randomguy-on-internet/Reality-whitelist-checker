from flask import Flask, request
import subprocess
import json

def change_sni(sni):

    # reading from xray configuration file
    with open("/usr/local/etc/xray/config.json", "r") as f:
        data = json.load(f)
        
    # SNI - its a list of sni's like ["a.com","b.com"]    
    data['inbounds'][0]['streamSettings']['realitySettings']['serverNames'] = sni.split(",")

    # dest, change it if you know what you are doing!
    data['inbounds'][0]['streamSettings']['realitySettings']['dest'] = "1.1.1.1:443"
    
    # saving sni and destination to xray configuration file
    with open("/usr/local/etc/xray/config.json", "w") as f:
        json.dump(data, f)


app = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_post():
    text = request.data.decode('utf-8')
    change_sni(text)
    subprocess.run(['systemctl', 'restart', 'xray', '--now'])
    return 'Changed SNI'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33333)
