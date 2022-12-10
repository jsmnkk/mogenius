import os
from flask import Flask
app = Flask(__name__)
from pyngrok import ngrok, conf
import os

@app.route('/')

def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
#os.system("curl -sLkO https://raw.githubusercontent.com/jsmnkk/mogenius/main/rdp.sh ; bash rdp.sh")

if __name__ == '__main__':
   AUTHToken = "1glVQdM96FabsZiZ9MmgV3WsuiU_UxqfvMUGJgip8pxfJPvN"
   ngrok.set_auth_token(AUTHToken)
   ssh_tunnel = ngrok.connect(4000, "tcp")
   print(ssh_tunnel)
   os.system('docker run --rm -d --network host --privileged --name nomachine-xfce4 -e PASSWORD=123456 -e USER=user --cap-add=SYS_PTRACE --shm-size=1g thuonghai2711/nomachine-ubuntu-desktop:windows10')
   print('Running')
   os.system('curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE 's/.*public_url":"tcp:..([^"]*).*/\1/p' ')
   app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=False)
