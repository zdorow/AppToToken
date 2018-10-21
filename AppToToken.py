import sys
import json
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from requests.exceptions import ConnectionError

root = Tk()
root.title("Vpp token to Adam ID mapper.")
root.configure(background='black')
#root.geometry("595x500")

token_list = []

api_token_test1 = ''
api_token_test2 = ''
api_token_test3 = ''

# token_list.append(api_token_test1)
# token_list.append(api_token_test2)
# token_list.append(api_token_test3)

adam_id_list = []

adam_id1 = "524297631"
adam_id2 = "1246284741"
adam_id3 = "586542460"
adam_id4 = "360593530"

# adam_id_list.append(adam_id1)
# adam_id_list.append(adam_id2)
# adam_id_list.append(adam_id3)
# adam_id_list.append(adam_id4)


def append_token_list(token_in):
    token_list.append(token_in)


def append_adam_id_list(adam_id_in):
    adam_id_list.append(adam_id_in)


def get_count_info(token_in, adam_id_in):
    try:
        api_url = 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/getVPPAssetsSrv?sToken=' + token_in + \
                  '&includeLicenseCounts=' + adam_id_in
        response = requests.get(api_url)
        json_response = response.json()
        if response.status_code == 200:
            for all_assets in range(len(json_response['assets'])):
                adam_id_search = json_response['assets'][all_assets]['adamIdStr']
                if adam_id_search == adam_id_in:
                    total_count = json_response['assets'][all_assets]['totalCount']
                    return total_count
                else:
                    return None
        else:
            messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n "
                                                     "Please check your internet connection.")
    except ConnectionError:
        messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n Please check your"
                                                 "internet connection.")


def destroy():
    root.destroy()


for token in range(len(token_list)):
    for adam_id in range(len(adam_id_list)):
        print(f"Token: {token + 1}")
        print(adam_id_list[adam_id])
        print(get_count_info(token_list[token], adam_id_list[adam_id]))

root.bind('<Alt_L><A>', lambda e: append_token_list())
root.bind('<Alt_L><a>', lambda e: append_token_list())
root.bind('<Alt_L><G>', lambda f: get_count_info())
root.bind('<Alt_L><g>', lambda f: get_count_info())
root.bind('<Alt_L><X>', lambda g: destroy())
root.bind('<Alt_L><x>', lambda g: destroy())

root.mainloop()