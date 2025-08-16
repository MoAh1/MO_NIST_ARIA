# client.py

from MyAriaDialogAPI import MyAriaDialogAPI


EC2_PUBLIC_IP = 'aria-nist---.org'  

auth = {'api_key': 'rand_aria_testing_7enidjsweiw'}
api = MyAriaDialogAPI(endpoint=f'http://{EC2_PUBLIC_IP}:5000')

# Open a connection
success, message = api.OpenConnection(auth=auth)
if success:
    print(message)
    # Get the API version
    version = api.GetVersion()
    print(f"API Version: {version}")

    # Start a session
    success, message = api.StartSession()
    if success:
        print(message)
        # Send a prompt and get a response
        prompt = "I want to bake a chocolate cake. Can you help me?"
        response = api.GetResponse(prompt)
        if response['success']:
            print(f"Assistant: {response['response']}")
        else:
            print(f"Error: {response['response']}")
    else:
        print(f"Error: {message}")

    # Close the connection
    success, message = api.CloseConnection()
    if success:
        print(message)
    else:
        print(f"Error: {message}")
else:
    print(f"Failed to open connection: {message}")
