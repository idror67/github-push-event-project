import json
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers['Content-Type'] != 'application/json':
        abort(415)

    payload = request.json
    repository_name = payload['repository']['name']
    commit_id = payload['head_commit']['id']
    changed_files = [file['filename'] for file in payload['head_commit']['modified']]

    data = {
        "repository_name": repository_name,
        "commit_id": commit_id,
        "changed_files": changed_files
    }

    with open('webhook_output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return 'Webhook received', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)