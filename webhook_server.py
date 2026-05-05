from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("🚀 GitHub push received!")
    os.system("cd /home/azureuser/ai-cicd-agent && python3 agent.py")
    return "Triggered", 200

app.run(host='0.0.0.0', port=5000)
