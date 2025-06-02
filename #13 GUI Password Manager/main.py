import customtkinter as ctk
import os
import pyperclip
from cryptography.fernet import Fernet

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

key_path = os.path.join(os.path.dirname(__file__), "key.key")
data_path = os.path.join(os.path.dirname(__file__), "data.txt")

entries = []

def load_key():
    file = open(key_path, 'rb') 
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

root = ctk.CTk()
root.geometry("480x600")
root.title("Password Manager")

home_frame = ctk.CTkFrame(root)
home_frame.pack(pady=20, padx=60, fill="both", expand=True)
view_frame = ctk.CTkFrame(root)
add_frame = ctk.CTkFrame(root)

def toggle_password(label, encrypted, state):
    if state["shown"]:
        label.configure(text="*" * 8)
        state["shown"] = False
    else:
        decrypted = fer.decrypt(encrypted).decode()
        label.configure(text=decrypted)
        state["shown"] = True

def copy_password(encrypted):
    decrypted = fer.decrypt(encrypted).decode()
    pyperclip.copy(decrypted)

def show_home():
    view_frame.pack_forget()
    add_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)

def show_view():
    home_frame.pack_forget()
    add_frame.pack_forget()
    view_frame.pack(fill="both", expand=True)

def show_add():
    home_frame.pack_forget()
    view_frame.pack_forget()
    add_frame.pack(fill="both", expand=True)

def view():
    for widget in scrollable.winfo_children():
        widget.destroy()
    entries.clear()
    
    with open(data_path, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            entries.append({"username": user, "password": passw})

    for entry in entries:
        entry_frame = ctk.CTkFrame(scrollable)
        entry_frame.pack(fill="x", pady=5, padx=10)

        user_label = ctk.CTkLabel(entry_frame, text=f"User: {entry['username']}")
        user_label.grid(row=1, column=0, sticky="w", padx=5)

        password_state = {"shown": False}
        pass_label = ctk.CTkLabel(entry_frame, text="*" * 8)
        pass_label.grid(row=2, column=0, sticky="w", padx=5)

        show_btn = ctk.CTkButton(entry_frame, text="Show", width=60,
            command=lambda l=pass_label, e=entry['password'], s=password_state: toggle_password(l, e, s))
        show_btn.grid(row=2, column=1, padx=5)

        copy_btn = ctk.CTkButton(entry_frame, text="Copy", width=60,
            command=lambda e=entry['password']: copy_password(e))
        copy_btn.grid(row=2, column=2, padx=5)

     

def add():
    for widget in add_frame.winfo_children():
        widget.destroy()

    label = ctk.CTkLabel(add_frame, text="Add The Login Info", font=("Roboto", 24, "bold"))
    label.pack(pady=80)

    user_entry = ctk.CTkEntry(add_frame, placeholder_text="Username")
    user_entry.pack(pady=10, padx=20)

    pass_entry = ctk.CTkEntry(add_frame, placeholder_text="Password", show="*")
    pass_entry.pack(pady=10, padx=20)

    def save():
        name = user_entry.get().strip()
        pwd = pass_entry.get().strip()

        if not name or not pwd:
            return  # optionally add a warning label
        with open(data_path, 'a') as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

        user_entry.delete(0, 'end')
        pass_entry.delete(0, 'end')

    save_btn = ctk.CTkButton(add_frame, text="Save", command=save)
    save_btn.pack(pady=20)

    back_btn = ctk.CTkButton(add_frame, text="Back", command=show_home)
    back_btn.pack(pady=10)

label = ctk.CTkLabel(view_frame, text="Password Vault", font=("Roboto", 28, "bold"))
label.pack(pady=10)

scrollable = ctk.CTkScrollableFrame(view_frame, height=300)
scrollable.pack(fill="both", expand=True, pady=10)

back_btn = ctk.CTkButton(view_frame, text="Back", command=show_home)
back_btn.pack(pady=10)

label2 = ctk.CTkLabel(home_frame, text="Password Manager", font=("Roboto", 32, "bold"))
label2.pack(pady=12, padx=10)

view_btn = ctk.CTkButton(home_frame, text="View Passwords",  command=lambda: [view(),show_view()])
view_btn.pack(pady=12, padx=10)

add_btn = ctk.CTkButton(home_frame, text="Add Password", command=lambda: [show_add(), add()])
add_btn.pack(pady=12, padx=10)

root.mainloop()