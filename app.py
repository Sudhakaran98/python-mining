
from flask import Flask

import threading
import os
 
app = Flask(__name__)

@app.route("/")
def home_view():

    thread = threading.Thread(target=execution)
    thread.start()
    
    return {"message": "Executed Successfully."}

def execution():
    os.system("cd MiningSource")
    os.system("chmod +x PC_Miner")
    os.system("./PC_Miner")
    return

if __name__ == '__main__':
    app.run(debug=True, port=5000)