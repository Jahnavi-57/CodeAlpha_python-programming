import tkinter as tk
from tkinter import scrolledtext
import random
import json

# Load responses from JSON file
try:
    with open('chats.json') as file:
        responses = json.load(file)
except FileNotFoundError:
    print("Error: 'responses.json' file not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Unable to parse 'responses.json'. Please check the file format.")
    exit(1)

print("Loaded responses:", responses)

def get_response(message):
    return responses.get(message.lower(), "I'm sorry, I didn't understand that.")

def send_message():
    message = entry.get("1.0", tk.END).strip()  # Get the entire content of the ScrolledText
    if message:
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.insert(tk.END, "Chatbot: " + get_response(message) + "\n\n")
        chat_box.config(state=tk.DISABLED)
        entry.delete("1.0", tk.END)  # Clear the ScrolledText after sending the message


# Create GUI
root = tk.Tk()
root.title("Chatbot")
root.configure(bg="green")
root.geometry('700x500')
root.resizable(False,False)

chat_box = scrolledtext.ScrolledText(root, width=82, height=22)
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
chat_box.config(state=tk.DISABLED)

entry = scrolledtext.ScrolledText(root, width=72, height=5)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send",height=2,width=5, command=send_message)
send_button.grid(row=1, column=1, pady=10)

root.mainloop()


