import tkinter as tk
from tkinter import scrolledtext
import random
import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_response(message):
    tokens = word_tokenize(message.lower())
    tagged_tokens = nltk.pos_tag(tokens)
    if "hello" in tokens:
        return "Hello!"
    elif "hi" in tokens:
        return "Hi there!"
    elif "how are you" in message:
        return "I'm good, thank you!"
    elif "goodbye" in tokens or "bye" in tokens:
        return "Goodbye! Take care!"
    if tagged_tokens and tagged_tokens[0][1].startswith('VB'):
        return random.choice(["Hello!", "Hi there!", "Hey!"])
    return random.choice(["I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure what you mean."])

def send_message():
    message = entry.get("1.0", tk.END)  # Get the entire content of the ScrolledText
    if message.strip() != "":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message)
        chat_box.insert(tk.END, "Chatbot: " + get_response(message) + "\n")
        chat_box.config(state=tk.DISABLED)
        entry.delete("1.0", tk.END)  # Clear the ScrolledText after sending the message

# Create GUI
root = tk.Tk()
root.title("Chatbot")
root.configure(bg="green")
root.geometry('700x500')

chat_box = scrolledtext.ScrolledText(root, width=82, height=22)
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
chat_box.config(state=tk.DISABLED)

entry = scrolledtext.ScrolledText(root, width=72, height=5)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send",height=2,width=5, command=send_message)
send_button.grid(row=1, column=1, pady=10)

root.mainloop()

