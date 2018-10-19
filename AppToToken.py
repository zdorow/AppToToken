import sys
import json
import requests
from tkinter import *
from tkinter import messagebox
from requests.exceptions import ConnectionError

api_token_test = ''
adam_id_test = "360593556"
# api_url_test = 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/getVPPAssetsSrv?sToken=' + api_token + \
#                '&includeLicenseCounts=' + adam_id


def get_token_info(api_token, adam_id):
    try:
        api_url = 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/getVPPAssetsSrv?sToken=' + api_token + \
                  '&includeLicenseCounts=' + adam_id
        response = requests.get(api_url)

        if response.status_code == 200:
            iTunesData = json.loads(response.content.decode('utf-8'))
            try:
                all_assets = json.dumps(iTunesData['assets'])
                all_apps = all_assets.split(",")
                app_count = get_app_counts(adam_id, all_apps)
                return app_count
            except KeyError:
                messagebox.showerror("Error Connecting", "There was an nothing returned from the iTunes URL.\n "
                                                         "Please check the VPP token.")
        else:
            messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n "
                                                     "Please check your internet connection.")
            return null
    except ConnectionError:
        messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n Please check your"
                                                 "internet connection.")


def get_app_counts(adam_id, all_apps):
    adam_id_search = " \"adamIdStr\": \"" + adam_id + "\""

    if adam_id_search in all_apps:
        totalCount = all_apps.index(adam_id_search) + 5
        licenseCount = all_apps[totalCount]
        numbersInCount = re.compile('\d+')
        finalCount = numbersInCount.findall(licenseCount)
        return finalCount[0]
    else:
        return "No App here"


print(get_token_info(api_token_test, adam_id_test))


# #Check variable
# def verify_input(name, value):
#     if value == "":
#         messagebox.showerror("Invalid Entry", "Please add at least one item to each box.")
#
#
# def check_tokens():
#     verify_variable("adam_id", adam_id)
#     verify_variable("adam_id", vpp_token)

