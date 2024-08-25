import smtplib
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = sender_email_entry.get()
    sender_password = password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    message_body = message_entry.get("1.0", tk.END)

    if not (sender_email and sender_password and recipient_email and subject and message_body):
        messagebox.showwarning("Input Error", "All fields must be filled out")
        return
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the email account
            message = f"Subject: {subject}\n\n{message_body}"
            server.sendmail(sender_email, recipient_email, message)
            messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

# Create the main window
root = tk.Tk()
root.title("Simple Email Sender")

# Sender email
tk.Label(root, text="Sender Email:").pack(padx=10, pady=5)
sender_email_entry = tk.Entry(root, width=40)
sender_email_entry.pack(padx=10, pady=5)

# Password
tk.Label(root, text="Password:").pack(padx=10, pady=5)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack(padx=10, pady=5)

# Recipient email
tk.Label(root, text="Recipient Email:").pack(padx=10, pady=5)
recipient_email_entry = tk.Entry(root, width=40)
recipient_email_entry.pack(padx=10, pady=5)

# Subject
tk.Label(root, text="Subject:").pack(padx=10, pady=5)
subject_entry = tk.Entry(root, width=40)
subject_entry.pack(padx=10, pady=5)

# Message body
tk.Label(root, text="Message:").pack(padx=10, pady=5)
message_entry = tk.Text(root, height=10, width=40)
message_entry.pack(padx=10, pady=5)

# Send button
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()