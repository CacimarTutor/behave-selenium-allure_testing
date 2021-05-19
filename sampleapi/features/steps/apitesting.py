from behave import given, when, then, step
import requests

api_endpoints = {}
request_headers = {}
response_codes ={}
response_texts={}
request_bodies = {}
api_url=None

@given(u'I set sample REST API url')
def step_impl(context):
    global api_url
    api_url = '127.0.0.1:8000/sampleapi'

# START POST Scenario
@given(u'I Set POST posts api endpoint')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url+'/user'
    print('url :'+api_endpoints['POST_URL'])

@when(u'I Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    request_headers['Content-Type'] = header_content_type

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'Set request Body')
def step_impl(context):
    request_bodies['POST']={"username": "test","password": "testpass","first_name": "tester","last_name": "tester last"}

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'Send POST HTTP request')
def step_impl(context):
    # sending get request and saving response as response object
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'], headers=request_headers)
    #response = requests.post(url=api_endpoints['POST_URL'], headers=request_headers) #https://jsonplaceholder.typicode.com/posts
    # extracting response text
    response_texts['POST']=response.text
    print("post response :"+response.text)
    # extracting response status_code
    statuscode = response.status_code
    response_codes['POST'] = statuscode

@then(u'I receive valid HTTP response code 201')
def step_impl(context):
    print('Post rep code ;'+str(response_codes['POST']))
    assert response_codes['POST'] is 201
# END POST Scenario

