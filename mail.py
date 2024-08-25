import smtplib
import tkinter as tk
from tkinter import messagebox

def create_main_window():
    window = tk.Tk()
    window.title("Email Sender")
    return window

def create_input_fields(window):
    tk.Label(window, text="Your Email:").pack(padx=10, pady=5)
    email_entry = tk.Entry(window, width=40)
    email_entry.pack(padx=10, pady=5)
    
    tk.Label(window, text="Your Password:").pack(padx=10, pady=5)
    password_entry = tk.Entry(window, show="*", width=40)
    password_entry.pack(padx=10, pady=5)
    
    tk.Label(window, text="Recipient Email:").pack(padx=10, pady=5)
    recipient_entry = tk.Entry(window, width=40)
    recipient_entry.pack(padx=10, pady=5)
    
    tk.Label(window, text="Email Subject:").pack(padx=10, pady=5)
    subject_entry = tk.Entry(window, width=40)
    subject_entry.pack(padx=10, pady=5)
    
    tk.Label(window, text="Email Message:").pack(padx=10, pady=5)
    message_textbox = tk.Text(window, height=10, width=40)
    message_textbox.pack(padx=10, pady=5)
    
    return email_entry, password_entry, recipient_entry, subject_entry, message_textbox

def on_send_button_click(email_entry, password_entry, recipient_entry, subject_entry, message_textbox):
    """Handle the send button click event."""
    sender_email = email_entry.get()
    sender_password = password_entry.get()
    recipient_email = recipient_entry.get()
    email_subject = subject_entry.get()
    email_message = message_textbox.get("1.0", tk.END)

    if not (sender_email and sender_password and recipient_email and email_subject and email_message):
        messagebox.showwarning("Input Error", "All fields must be filled out")
        return
    
    try:
        send_email(sender_email, sender_password, recipient_email, email_subject, email_message)
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

def send_email(sender_email, sender_password, recipient_email, email_subject, email_message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        email_body = f"Subject: {email_subject}\n\n{email_message}"
        server.sendmail(sender_email, recipient_email, email_body)

def main():
    """Main function to set up the GUI and run the application."""
    window = create_main_window()
    email_entry, password_entry, recipient_entry, subject_entry, message_textbox = create_input_fields(window)
    
    send_button = tk.Button(window, text="Send Email", 
                            command=lambda: on_send_button_click(email_entry, password_entry, recipient_entry, subject_entry, message_textbox))
    send_button.pack(padx=10, pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    main()
