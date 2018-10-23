import sys
import os
import json
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from requests.exceptions import ConnectionError


root = Tk()
root.configure(background='black')

top_frame = Frame(root, highlightbackground="green", highlightcolor="green", background='seashell3', highlightthickness=2)

middle_frame = Frame(root, highlightbackground="green", highlightcolor="green", background='seashell3', highlightthickness=2, width=100, height=100, bd= 0)

bottom_frame = Frame(root, highlightbackground="green", highlightcolor="green", background='seashell3', highlightthickness=2, width=100, height=100, bd= 0)

root.title("Map Tokens to Adam ID's")

root.resizable(False, False)

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


def get_adam_id_filename(entry):
	file_name = entry.get()
	if not os.access(file_name, os.W_OK):
		file_name = filedialog.askopenfilename()
		entry.delete(0, END)
		entry.insert(0, file_name)
		return file_name
	else:
		return file_name


def get_token_filename(scroll):
	file_name = scroll.get('1.0', END)
	if not os.access(file_name, os.W_OK):
		file_name = filedialog.askopenfilename()
		scroll.insert('1.0', file_name)
		return file_name
	else:
		return file_name


def save_filename(entry):
	file_name = entry.get()
	if not os.access(file_name, os.W_OK):
		file_name = filedialog.asksaveasfile().name
		entry.delete(0, END)
		entry.insert(0, file_name)
		return file_name
	else:
		return file_name



def append_token_list():
	token_info_in = tokenBox.get('1.0', END)

	if os.access(adam_id_info_in, os.W_OK):

		token_info_in_open = open(r"" + token_info_in)
		adam_id_check = token_info_in_open.read().replace('\n', '')
		ids = numbers_in_line.findall(adam_id_check)
		print(ids)

		if len(ids) % 9 == 0 and len(ids) != 0:
			new_id_list = [ids[idx:idx+9] for idx, val in enumerate(ids) if idx % 9 == 0]
			for all_ids in set(new_id_list):
				adam_id_list.append(all_ids)

				print(adam_id_list)
			adamIdEntryLabel.configure(text="Successfully Added VPP Token!\n")
			adamIdEntry.delete(0, 'end')
		else:
			messagebox.showerror("Error VPP Token!", "There was an inputting the VPP Token!\n "
			                                         "Please check the file input.")
	else:
		ids = numbers_in_line.findall(adam_id_info_in)
		string_ids = "".join(ids)
		print(string_ids)
		print(len(string_ids))
		if len(string_ids) % 9 == 0 and len(string_ids) != 0:
			new_id_list = [string_ids[idx:idx+9] for idx, val in enumerate(string_ids) if idx % 9 == 0]
			for ids in set(new_id_list):
				adam_id_list.append(ids)

			print(adam_id_list)
			adamIdEntryLabel.configure(text="Successfully Added VPP Token!\n")
			adamIdEntry.delete(0, 'end')
		else:
			messagebox.showerror("Error VPP Token!", "There was an inputting the VPP Token!\n "
			                                         "Please check the file input.")


def append_adam_id_list():
	adam_id_info_in = adamIdEntry.get()
	numbers_in_line = re.compile('\d+')

	if os.access(adam_id_info_in, os.W_OK):

		adam_id_list_open = open(r"" + adam_id_info_in)
		adam_id_check = adam_id_list_open.read().replace('\n', '')

		ids = numbers_in_line.findall(adam_id_check)
		string_ids = "".join(ids)

		if len(string_ids) % 9 == 0 and len(string_ids) != 0:
			new_id_list = [string_ids[idx:idx+9] for idx, val in enumerate(string_ids) if idx % 9 == 0]
			for all_ids in set(new_id_list):
				adam_id_list.append(all_ids)

				print(adam_id_list)
			adamIdEntryLabel.configure(text="Successfully Added Adam IDs!\n")
			adamIdEntry.delete(0, 'end')
		else:
			messagebox.showerror("Error Adam ID", "There was an error inputting the Adam IDs.\n "
			                                      "Please check the file input.")
	else:
		numbers_in_line = re.compile('\d+')

		ids = numbers_in_line.findall(adam_id_info_in)
		string_ids = "".join(ids)
		print(string_ids)
		print(len(string_ids))
		if len(string_ids) % 9 == 0 and len(string_ids) != 0:
			new_id_list = [string_ids[idx:idx+9] for idx, val in enumerate(string_ids) if idx % 9 == 0]
			for ids in set(new_id_list):
				adam_id_list.append(ids)

			print(adam_id_list)
			adamIdEntryLabel.configure(text="Successfully Added Adam IDs!\n")
			adamIdEntry.delete(0, 'end')
		else:
			messagebox.showerror("Error Adam ID", "There was an inputting the Adam IDs.\n "
			                                      "Please check your input.")



def clear_list(list_to_clear, label):
	label.configure(text="Cleared list.\n")
	del list_to_clear[:]


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

button_settings="\"bg=\"seashell3\", highlightbackground=\"seashell3\", fg=\"black\", font=\"Helvetica 11\","

adamIdEntryLabel = Label(top_frame, text="Please enter Adam IDs or the file path to a file with Adam IDs to add.",
                         fg="black", highlightbackground='seashell3', bg="seashell3", font="Helvetica 14", wraplength=350)

adamIdEntry = Entry(top_frame, width=35, highlightbackground='grey')

adamIdListButton = Button(top_frame, text=" Add to Adam ID List ", command=lambda: append_adam_id_list(), underline=1, bg="seashell3",
                          highlightbackground="seashell3", fg="black", font="Helvetica 12",)

clearAdamIDListButton = Button(top_frame, text=" Clear Adam ID list ", command=lambda: clear_list(adam_id_list, adamIdEntryLabel), bg="seashell3",
                               highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)

adamIdFilepathButton = Button(top_frame, text=" Set path to Adam ID file ", command=lambda: get_adam_id_filename(adamIdEntry), bg="seashell3",
                              highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)




tokenEntryLabel = Label(middle_frame, text="Paste the tokens in here or set the filepath for a token to add.",
                        fg="black", highlightbackground='seashell3', bg="seashell3", font="Helvetica 14", wraplength=350)

tokenBox = ScrolledText(middle_frame, width=45, height=15,  highlightbackground='grey')

addToTokenListButton = Button(middle_frame, text=" Add to Token List ", command=append_token_list, bg="seashell3",
                              highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)

setTokenFilepathButton = Button(middle_frame, text=" Set Path to VPP token ",
                                command=lambda: get_token_filename(tokenBox),bg="seashell3",
                                highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)

clearTokenListButton = Button(middle_frame, text=" Clear Token list ", command=lambda: clear_list(token_list, tokenEntryLabel), bg="seashell3",
                              highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)


outputFileNameEntryLabel = Label(bottom_frame, text="Enter the path desired for the file output or use the button to fill in"
                                                    " the path.", fg="black", highlightbackground='seashell3', bg="seashell3", font="Helvetica 14", wraplength=350)

outputFileName = Entry(bottom_frame, width=35, highlightbackground='grey')

buildListButton = Button(bottom_frame, text=" Build the list ", command=get_count_info, bg="seashell3",
                         highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)

setFilepathButton = Button(bottom_frame, text=" Set output file name ", command=lambda: save_filename(outputFileName),
                           bg="seashell3", highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=0)

exitButton = Button(bottom_frame, text=" Exit Program ", command=root.destroy, bg="seashell3",
                    highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)

top_frame.pack(padx=5, pady=5, fill="both", expand="yes")
adamIdEntryLabel.pack(padx=5, pady=5)
adamIdEntry.pack(padx=5, pady=5)
adamIdListButton.pack(side=LEFT, padx=5, pady=5)
clearAdamIDListButton.pack(side=LEFT, padx=5, pady=5)
adamIdFilepathButton.pack(side=LEFT, padx=5, pady=5)

middle_frame.pack(padx=5, pady=5, fill="both", expand="yes")
tokenEntryLabel.pack(padx=5, pady=5)
tokenBox.pack(padx=5, pady=5)
addToTokenListButton.pack(side=LEFT, padx=5, pady=5)
clearTokenListButton.pack(side=LEFT, padx=25, pady=5)
setTokenFilepathButton.pack(side=LEFT, padx=5, pady=5)

bottom_frame.pack(padx=5, pady=5,  fill="both")
outputFileNameEntryLabel.pack(padx=5, pady=5)
outputFileName.pack(padx=5, pady=5)
buildListButton.pack(side=LEFT, padx=5, pady=5)
setFilepathButton.pack(side=LEFT, padx=35, pady=5)
exitButton.pack(side=LEFT, padx=5, pady=5)


for token in range(len(token_list)):
	print(f"Token: {token + 1}")
	for adam_id in range(len(adam_id_list)):
		print(adam_id_list[adam_id])
		print(get_count_info(token_list[token], adam_id_list[adam_id]))

root.bind('<Alt_L><T>', lambda e: append_token_list())
root.bind('<Alt_L><T>', lambda e: append_token_list())
root.bind('<Alt_L><A>', lambda e: append_adam_id_list())
root.bind('<Alt_L><a>', lambda e: append_adam_id_list())
root.bind('<Alt_L><G>', lambda f: get_count_info())
root.bind('<Alt_L><g>', lambda f: get_count_info())
root.bind('<Alt_L><X>', lambda g: destroy())
root.bind('<Alt_L><x>', lambda g: destroy())

root.mainloop()
