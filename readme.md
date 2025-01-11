# GitHub Push Event Webhook

This project sets up a Flask application to handle GitHub push event webhooks. When a push event occurs, the webhook handler extracts the repository name, commit ID, and list of changed files, and writes this information to a JSON file.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd github-push-event-project
    ```

2. Install the required dependencies:
    ```sh
    pip install flask
    ```

3. Run the Flask application:
    ```sh
    python webhook.py
    ```

## Usage

1. Configure your GitHub repository to send push event webhooks to your server:
    - Go to your repository settings.
    - Click on "Webhooks".
    - Click "Add webhook".
    - Set the "Payload URL" to `http://<your-server-ip>:5000/webhook`.
    - Set the "Content type" to `application/json`.
    - Select "Just the push event".
    - Click "Add webhook".

2. When a push event occurs, the webhook handler will write the repository name, commit ID, and list of changed files to `webhook_output.json` in the project directory.

## Example

An example of the `webhook_output.json` file:
```json
{
    "repository_name": "example-repo",
    "commit_id": "abc123def456",
    "changed_files": [
        "file1.txt",
        "file2.txt"
    ]
}  
