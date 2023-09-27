"""Author: Rawan Khaled """
import tkinter as tk
from tkinter import messagebox
import datetime

# Note this alarm uses the 24 hour system

global Alarm_list
Alarm_list=[]

def set_alarm():
    current_time = datetime.datetime.now().strftime("%H:%M")
    print("current_time ", current_time)
    for alarm in Alarm_list:
        print(alarm)
        if alarm == current_time:
            messagebox.showinfo("Alarm", "Go Do your Tasks!")

    root.after(5000, set_alarm)  # Check the alarms every 5000 milliseconds



# Add task function
def addalarm():
    alarm = entry.get()
    set_alarm()
    entry.delete(0, "end")

    if alarm:
        with open("Alarm.txt", "a") as alarmfile:
            alarmfile.write(f"\n{alarm}")
        Alarm_list.append(alarm)
        listbox2.insert("end", alarm)


# Delete task function
def deletealarm():
    task = str(listbox2.get("anchor"))
    if task in Alarm_list:
        Alarm_list.remove(task)
        with open("Alarm.txt", "w") as alarmfile:
            for alarm in Alarm_list:
                alarmfile.write(alarm + "\n")
        listbox2.delete("anchor")

def quit():
    # Clear the contents of the "alarm.txt" file
    with open("Alarm.txt", "w") as alarmfile:
        alarmfile.write("")
    root.quit()

root = tk.Tk()
root.title("Alarm Clock")
icon_image = tk.PhotoImage(file="analog-wall-clock.png")
root.iconphoto(False, icon_image)
root.resizable(False, False)

root.geometry("400x250")
back_image = tk.PhotoImage(file="analog-wall-clock.png")
back_label = tk.Label(root, image=back_image)
back_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the background image at the center
back_label.place(relwidth=2, relheight=3)  # Stretch the background to fill the entire window

custom_font = ("Times New Roman", 14, "bold")
custom_font2 = ("Times New Roman", 10, "bold")
label = tk.Label(root, text="Enter alarm time (HH:MM):", bg="black", font=custom_font, fg="white")
label.pack(pady=10)

entry = tk.Entry(root, font=custom_font, width=15)
entry.pack(pady=5)

frame = tk.Frame(root, bd=3, width=300, height=50)
frame.pack()

# Create the second Listbox with a smaller height
listbox2 = tk.Listbox(frame, width=50  ,height=1, bg="Light Gray", cursor="hand2")
listbox2.pack(side="left", fill="both", expand=True)

# Scroll bar for the second Listbox in vertical with matching height
scroll_bar2 = tk.Scrollbar(frame, orient="vertical")
scroll_bar2.pack(side="left", fill="y")  # Set fill to "y" to make the scrollbar cover the entire height

# Configure the Listbox to use the scrollbar
listbox2.config(yscrollcommand=scroll_bar2.set)
scroll_bar2.config(command=listbox2.yview)


# To add your alarm
button = tk.Button(root, text="Add Alarm", command=addalarm, width=10, height=2, bg="Light Gray", font=custom_font2)
button.pack(pady=5, side=tk.LEFT, padx=28)

# To delete an added task
Delete_Label = tk.Button(root, bg="Light Gray", command=deletealarm, text="Delete Alarm", width=10, height=2, font=custom_font2)
Delete_Label.pack(pady=5, side=tk.LEFT, padx=28)

quit_button = tk.Button(root, text="Quit", command=quit, width=10, height=2, bg="Light Gray", font=custom_font2)
quit_button.pack(pady=5, side=tk.LEFT, padx=28)

root.mainloop()
