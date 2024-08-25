import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = "192.168.1.47"
PORT = 5213

# Create the main window
root = tk.Tk()
root.title("Chat Client")

# Create a scrolled text widget for displaying messages
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
text_area.config(state=tk.DISABLED)

# Create an entry widget for typing messages
entry = tk.Entry(root)
entry.pack(padx=10, pady=10, fill=tk.X, expand=True)

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                text_area.config(state=tk.NORMAL)
                text_area.insert(tk.END, f"Received: {message}\n")
                text_area.yview(tk.END)
                text_area.config(state=tk.DISABLED)
            else:
                break
        except:
            break

def send_message(event=None):
    message = entry.get()
    if message:
        client_socket.send(message.encode())
        entry.delete(0, tk.END)
        text_area.config(state=tk.NORMAL)
        text_area.insert(tk.END, f"You: {message}\n")
        text_area.yview(tk.END)
        text_area.config(state=tk.DISABLED)
    if message.lower() == 'exit':
        client_socket.close()
        root.quit()

# Bind the entry widget to the Enter key
entry.bind("<Return>", send_message)

# Start the thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start the Tkinter event loop
root.protocol("WM_DELETE_WINDOW", lambda: send_message('exit'))
root.mainloop()
