import tkinter as tk
from cryptography.fernet import Fernet

root = tk.Tk()
root.title("Password Manager")


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)

# background info below
canvas = tk.Canvas(root, height=500, width=1000, bg="#002147")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


# background info above

def refresh():
    with open('passwords.txt', 'r') as f:  # read existing files
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            statement = str("Username: " + user + " | Password: " + fer.decrypt(passw.encode()).decode())
            label = tk.Label(frame, text=statement, bg="white", font="Arial")
            label.pack()


def start_screen():
    for widget in frame.winfo_children():
        widget.destroy()
    global addPassword
    addPassword = tk.Button(frame, text="Add Password", padx=10, pady=5,
                            fg="white", bg="#002147", command=PassApp, font="Arial")
    addPassword.pack()
    refresh()


def PassApp():
    for widget in frame.winfo_children():
        widget.destroy()
    backButton = tk.Button(frame, text="Go Back", padx=10, pady=5,
                           fg="white", bg="#002147", font="Arial", command=start_screen)
    backButton.pack()
    passLabel1 = tk.Label(frame, text="Username: ", bg="white", font="Arial")
    global inputtxt1
    inputtxt1 = tk.Text(frame, height=1, width=20)
    passLabel1.pack()
    inputtxt1.pack()
    passLabel2 = tk.Label(frame, text="Password: ", bg="white", font="Arial")
    global inputtxt2
    inputtxt2 = tk.Text(frame, height=1, width=20)
    passLabel2.pack()
    inputtxt2.pack()
    submitPass = tk.Button(frame, text="Submit", padx=10, pady=5, fg="white",
                           bg="#002147", command=getInput, font="Arial")
    submitPass.pack()


def getInput():
    pot_user = inputtxt1.get(1.0, "end-1c")
    pot_pass = inputtxt2.get(1.0, "end-1c")
    if pot_user != "" and pot_pass != "":
        new_username = pot_user
        new_password = pot_pass
        with open('passwords.txt', 'a') as o:
            o.write(new_username + "|" + fer.encrypt(new_password.encode()).decode() + "\n")
        start_screen()
        #


start_screen()

root.mainloop()
