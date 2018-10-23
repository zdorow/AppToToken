import sys
import json
import requests
from tkinter import *
import pprint
from tkinter import messagebox
from tkinter import filedialog
from requests.exceptions import ConnectionError


token_list = []

api_token_test1 = 'eyJleHBEYXRlIjoiMjAxOS0wOC0wOFQwODoxNjo1OC0wNzAwIiwidG9rZW4iOiJDMzhMQ25aWDErd0xPZW1WRzZmNENKU21peW12Ni94YnlKb2Y2YjBTdGlZblpRS202RkdkYmNKYmx5U1c1cFo0YkVxS250WTE1Zmg5YWdtUnRoWUgyY2EyZ0o3a2ZUUGNSdVYxOFg1VG8vbz0iLCJvcmdOYW1lIjoiTmF0aW9uYWwgVGVjaG5vbG9neSBBc3NvY2lhdGVzIn0='
api_token_test2 = 'eyJleHBEYXRlIjoiMjAxOS0wOC0wOFQwODoxNjo1OC0wNzAwIiwidG9rZW4iOiJDMzhMQ25aWDErd0xPZW1WRzZmNENKU21peW12Ni94YnlKb2Y2YjBTdGlZblpRS202RkdkYmNKYmx5U1c1cFo0YkVxS250WTE1Zmg5YWdtUnRoWUgyY2EyZ0o3a2ZUUGNSdVYxOFg1VG8vbz0iLCJvcmdOYW1lIjoiTmF0aW9uYWwgVGVjaG5vbG9neSBBc3NvY2lhdGVzIn0'
api_token_test3 = 'eyJleHBEYXRlIjoiMjAxOS0wOC0wOFQwODoxNjo1OC0wNzAwIiwidG9rZW4iOiJDMzhMQ25aWDErd0xPZW1WRzZmNENKU21peW12Ni94YnlKb2Y2YjBTdGlZblpRS202RkdkYmNKYmx5U1c1cFo0YkVxS250WTE1Zmg5YWdtUnRoWUgyY2EyZ0o3a2ZUUGNSdVYxOFg1VG8vbz0iLCJvcmdOYW1lIjoiTmF0aW9uYWwgVGVjaG5vbG9neSBBc3NvY2lhdGVzIn0='

token_list.append(api_token_test1)
token_list.append(api_token_test2)
# token_list.append(api_token_test3)

adam_id_list = []

adam_id1 = "959161442"
adam_id2 = "625520018"
adam_id3 = "959161442"
adam_id4 = "625520018"

adam_id_list.append(adam_id1)
adam_id_list.append(adam_id2)
adam_id_list.append(adam_id3)
adam_id_list.append(adam_id4)


def append_token_list(token_in):
    token_list.append(token_in)


def append_adam_id_list(adam_id_in):
    adam_id_list.append(adam_id_in)


def get_count_info(token_in, adam_id_in):
    try:
        # api_url = 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/getVPPAssetsSrv?sToken=' + token_in + \
        #           '&includeLicenseCounts=' + adam_id_in

        headers = {'content-type': 'application/json', 'Cookie':'itvt=' + token_in}
        api_url = "https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&id=" + adam_id_in + "&p=mdm-lockup&caller=MDM&platform=enterprisestore&cc=us&l=en"

        response = requests.get(api_url, headers=headers)
        json_response = response.json()
        print(json_response)
    except ConnectionError:
        messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n Please check your"
                                                 "internet connection.")


for token in range(len(token_list)):
    for adam_id in range(len(adam_id_list)):
        print(f"Token: {token + 1}")
        print(adam_id_list[adam_id])
        print("Total Count: ", get_count_info(token_list[token], adam_id_list[adam_id]))

