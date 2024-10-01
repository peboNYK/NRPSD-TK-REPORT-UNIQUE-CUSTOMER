import splunklib.client as client

HOST = "10.125.198.9"
PORT = 8089
SESSION_KEY = "<session_key>"

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    token=SESSION_KEY)

# Print installed apps to the console to verify login
for app in service.apps:
    print app.name