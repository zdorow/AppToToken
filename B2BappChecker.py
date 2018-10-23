import os
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from requests.exceptions import ConnectionError

root = Tk()
root.configure(background='black')

top_frame = Frame(root, highlightbackground="green", highlightcolor="green", background='seashell3',
                  highlightthickness=2)

middle_frame = Frame(root, highlightbackground="green", highlightcolor="green", background='seashell3',
                     highlightthickness=2, width=100, height=100, bd=0)

bottom_frame = Frame(root, highlightbackground="green", highlightcolor="green", background='seashell3',
                     highlightthickness=2, width=100, height=100, bd=0)

root.title(" Check B2B apps. ")
root.resizable(False, False)


def get_token_filename(scroll):
    file_name = scroll.get('1.0', END)
    if not os.access(file_name, os.W_OK):
        file_name = filedialog.askopenfilename()
        scroll.insert('1.0', file_name)
        return file_name
    else:
        return file_name


def get_adam_id():
    adam_id_info_in = adamIdEntry.get()
    numbers_in_line = re.compile('\d+')

    ids = numbers_in_line.findall(adam_id_info_in)
    string_ids = "".join(ids)

    if len(string_ids) == 9:
        return ids[0]
    else:
        messagebox.showerror("Error Adam ID", "There was an inputting the Adam IDs.\n "
                                              "Please check the Adam ID input.")


def get_token():
    token_info_in = tokenBox.get('1.0', END)

    if os.access(token_info_in, os.W_OK):
        token_info_in_open = open(r"" + token_info_in)
        token_info_read = token_info_in_open.read().replace('\n', '')
        return token_info_read
    else:
        return token_info_in.replace('\n', '')


def check_the_b2b(adam_id_in, token_in, output):
    try:
        headers = {'content-type': 'application/json', 'Cookie': 'itvt=' + token_in}
        api_url = "https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup?version=2&id=" \
                  + adam_id_in + "&p=mdm-lockup&caller=MDM&platform=enterprisestore&cc=us&l=en"
        for try_count in range(0, 5):
            response = requests.get(api_url, headers=headers)
            json_response = response.json()
            if response.status_code == 200:
                if len(json_response['results']) != 0:
                    app_name = json_response['results'][adam_id_in]['name']
                    output.configure(text=app_name + " has been confirmed in the app store.", fg="green")
                    break
                else:
                    output.configure(text=adam_id_in + f" try count: {try_count}")
                    try_count + 1
            else:
                messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n "
                                                         "Please check your internet connection.")

        if try_count >= 4:
            output.configure(text=f"{adam_id_in} is not in the app store for this Token.", fg="red")
    except ConnectionError:
        messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n Please check your"
                                                 "internet connection.")


def destroy():
    root.destroy()


adamIdEntryLabel = Label(top_frame, text="Please enter Adam ID of B2B app to check.", fg="black",
                         highlightbackground='seashell3', bg="seashell3", font="Helvetica 14", wraplength=350)

adamIdEntry = Entry(top_frame, width=35, highlightbackground='grey')

tokenEntryLabel = Label(middle_frame, text="Paste the token here or set the filepath for a token to add.",
                        fg="black", highlightbackground='seashell3', bg="seashell3", font="Helvetica 14",
                        wraplength=350)

tokenBox = ScrolledText(middle_frame, width=45, height=15, highlightbackground='grey')

setTokenFilepathButton = Button(middle_frame, text=" Set Path to VPP token ",
                                command=lambda: get_token_filename(tokenBox), bg="seashell3",
                                highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)


outputLabel = Label(bottom_frame, text=" Press the button to Check the App.\n ", fg="black",
                    highlightbackground='seashell3', bg="seashell3", font="Helvetica 14", wraplength=350)


checkAppButton = Button(bottom_frame, text=" Check the Adam ID", command=lambda: check_the_b2b(get_adam_id(),
                        get_token(), outputLabel), bg="seashell3", highlightbackground="seashell3", fg="black",
                        font="Helvetica 12")


exitButton = Button(bottom_frame, text=" Exit Program ", command=root.destroy, bg="seashell3",
                    highlightbackground="seashell3", fg="black", font="Helvetica 12", underline=1)

top_frame.pack(padx=5, pady=5, fill="both", expand="yes")
adamIdEntryLabel.pack(padx=5, pady=5)
adamIdEntry.pack(padx=5, pady=5)

middle_frame.pack(padx=5, pady=5, fill="both", expand="yes")
tokenEntryLabel.pack(padx=5, pady=5)
tokenBox.pack(padx=5, pady=5)
setTokenFilepathButton.pack(side=BOTTOM, padx=5, pady=5)

bottom_frame.pack(padx=5, pady=5, fill="both")
outputLabel.pack(padx=5, pady=5)
checkAppButton.pack(side=LEFT, padx=5, pady=5)
exitButton.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
