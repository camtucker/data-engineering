import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def authenticate_google(token_file, scopes):
    # Dynamically resolve the full path of token_file
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directory of this script
    TOKEN_PATH = os.path.join(BASE_DIR, token_file)

    # If token.json exists, use it
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, scopes)
    else:
        # Reauthenticate and generate token.json
        print(f"Token file '{TOKEN_PATH}' not found. Reauthenticating...")
        flow = InstalledAppFlow.from_client_secrets_file(
            os.path.join(BASE_DIR, 'credentials.json'), scopes
        )
        creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
        print(f"New token file saved at '{TOKEN_PATH}'.")

    return creds
