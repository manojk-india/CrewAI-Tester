from behave import *
import requests

@given('the user hits the "/data" endpoint')
def step_impl(context):
    """
    Send a GET request to the /data endpoint.
    """
    context.response = requests.get("http://127.0.0.1:5000/data")

@then('the response code should be 200')
def step_impl(context):
    """
    Verify the response code is 200.
    """
    assert context.response.status_code == 200


