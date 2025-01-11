from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Received webhook data", flush=True)
    
    try:
        # Get the JSON payload from the webhook
        webhook_data = request.get_json()
        if not webhook_data:
            print("No JSON payload received", flush=True)
            return 'Webhook received but no data', 400  # Bad Request

        # Extract required information
        repository_name = webhook_data.get('repository', {}).get('name', 'Unknown repository')
        #head_commit = webhook_data.get('head_commit', {})
        commit_id = head_commit.get('id', 'Unknown commit ID')
        changed_files = head_commit.get('modified', [])

        # Log the extracted data
        print(f"Repository Name: {repository_name}", flush=True)
        print(f"Commit ID: {commit_id}", flush=True)
        print(f"Changed Files: {changed_files}", flush=True)

        # Store the filtered data in a structured format
        filtered_data = {
            'github_repository_name': repository_name,
            'commit_id': commit_id,
            'changed_files': changed_files
        }

        # Ensure the directory exists
        output_dir = '/opt/simpleFlask'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'webhook_data.json')

        # Save the filtered data to a file
        with open(output_file, 'w') as f:
            json.dump(filtered_data, f, indent=4)
        
        print(f"Data saved to {output_file}", flush=True)
        return 'Webhook received and data logged', 200

    except Exception as e:
        # Log the exception and return a 500 response
        print(f"Error: {e}", flush=True)
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
