from tkinter import *
import speedtest


def speedchecker():
    st = speedtest.Speedtest()
    st.get_servers()
    down = str(round(st.download()/(10**6), 3))+ " Mbps"
    up = str(round(st.upload()/(10**6), 3))+ " Mbps"

    lb_down.config(text=down)
    lb_up.config(text=up)

tk = Tk()
tk.title("Internet Speed Tester")
tk.geometry("500x500")
tk.config(bg="Blue")

lb = Label(tk, text="Internet Speed Tester", font=("Arial", 30, "bold"), bg = "blue", fg = "white")
lb.place(x=50, y=40, height=50, width=400)

lb = Label(tk, text="Download Speed", font=("Arial", 10, "bold"), bg = "blue", fg = "white")
lb.place(x=50, y=100, height=50, width=400)
lb_down = Label(tk, text="00", font=("Arial", 15, "bold"), bg = "blue", fg = "white")
lb_down.place(x=50, y=130, height=50, width=400)

lb = Label(tk, text="Upload Speed", font=("Arial", 10, "bold"), bg = "blue", fg = "white")
lb.place(x=50, y=180, height=50, width=400)
lb_up = Label(tk, text="00", font=("Arial", 15, "bold"), bg = "blue", fg = "white")
lb_up.place(x=50, y=230, height=50, width=400)

button = Button(tk, text="Test Speed", font=("Arial", 15, "bold"), bg = "black", fg = "white", relief=RAISED, command=speedchecker)
button.place(x=50, y=300, height=50, width=400)

tk.mainloop()