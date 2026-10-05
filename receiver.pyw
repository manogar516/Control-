import socket
import tkinter as tk
import threading

HOST = '0.0.0.0'
PORT = 9999

def show_popup(message, sender_ip):
    win = tk.Tk()
    win.title(f"Message from {sender_ip}")
    win.configure(bg="black")
    win.geometry("600x400")

    label = tk.Label(
        win,
        text=message,
        fg="#00FF00",           # hacker green; use "white" if you prefer
        bg="black",
        font=("Consolas", 14),
        wraplength=560,
        justify="left"
    )
    label.pack(padx=20, pady=20, expand=True, fill="both")

    btn = tk.Button(
        win, text="OK", command=win.destroy,
        bg="black", fg="#00FF00", font=("Consolas", 12),
        activebackground="#003300", relief="solid", bd=1
    )
    btn.pack(pady=10)

    win.mainloop()

def start_server():
    lock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lock_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        lock_socket.bind((HOST, PORT))
    except OSError:
        print("Already running or port in use.")
        return
    lock_socket.listen(5)
    print(f"Listening on port {PORT}...")

    while True:
        conn, addr = lock_socket.accept()
        try:
            data = conn.recv(1024).decode(errors="replace")
            if data:
                print(f"Message from {addr[0]}: {data}")
                threading.Thread(
                    target=show_popup, args=(data, addr[0]), daemon=True
                ).start()
        finally:
            conn.close()

if __name__ == "__main__":
    start_server()