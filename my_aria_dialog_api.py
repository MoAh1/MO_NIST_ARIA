# my_aria_dialog_api.py

from aria_dialog_api_base import AriaDialogAPI
from recipe_query import FoodRecipeChat

class MyAriaDialogAPI(AriaDialogAPI):
    """Implementation of the ARIA Dialog API using FoodRecipeChat."""

    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.connected = False
        self.session_started = False
        self.chat_instance = None

    def OpenConnection(self, auth=None):
        """Opens a connection to the application using the provided authentication code."""
        if auth is None:
            return False, "Authentication required."
        elif 'api_key' in auth and auth['api_key'] == self.auth_token:
            self.connected = True
            return True, "Connection opened successfully."
        else:
            return False, "Invalid authentication code."

    def CloseConnection(self):
        """Closes the open connection to the application."""
        if self.connected:
            self.connected = False
            self.session_started = False
            self.chat_instance = None
            return True, "Connection closed successfully."
        else:
            return False, "No open connection to close."

    def GetVersion(self):
        """Returns the version of the API implementation."""
        return "1.0"

    def StartSession(self):
        """Starts a new dialog session if connected."""
        if self.connected:
            self.session_started = True
            self.chat_instance = FoodRecipeChat()
            return True, "Session started successfully."
        else:
            return False, "Cannot start session without an open connection."

    def GetResponse(self, text):
        """Returns a response to the text prompt."""
        if self.session_started and self.chat_instance:
            try:
                assistant_response = self.chat_instance.food_recipe(text)
                return {'success': True, 'response': assistant_response}
            except Exception as e:
                return {'success': False, 'response': str(e)}
        else:
            return {'success': False, 'response': 'Session not started.'}
