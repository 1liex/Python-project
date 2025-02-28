import customtkinter as ctk # Import customtkinter module
import random # Import random module


def createPassWord(): # fun to generate password
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%" # all the characters that can be used in the password
    
    try: # try to generate password
        rang = int(user_input.get())  # get the length of the password from the user input
        password = ''.join(random.choice(char) for _ in range(rang)) # generate the password with the chosen length
        display.configure(text=f"Generated Password: {password}\n\nData seved, file name: password.txt") # display the password in the GUI
        user_input.delete(0, ctk.END) # clear the user input field
        with open("password.txt", "a") as f: # save the password in a file
            f.write(f"Your password is: {password}\n") # write the password in the file

    except ValueError: # if the user input is not a number
        display.configure(text="Error: Please enter a valid number") # display an error message
        user_input(0, ctk.END) # clear the user input field

#--- GUI ---
ctk.set_appearance_mode("dark") # set the theme to dark
ctk.set_default_color_theme("green") # set the default color theme to green

root = ctk.CTk() # create the main window
root.title("Create password") # set the title of the window
root.geometry("600x400") # set the size of the window
#--- Frame ---
frame = ctk.CTkFrame(root) # create a frame
frame.pack(pady=40, padx=40, expand=True, fill="both") # add the frame to the window
#--- Title
title = ctk.CTkLabel(frame, text=" Create password", font=("Helvetica", 30)) # create a label with the title
title.pack(pady=10, padx=20) # add the label to the frame
#--- Dispaly box --- 
display = ctk.CTkLabel(frame, text="", font=("Helvetica", 20)) # create a label to display the password
display.pack(pady=10, padx=20) # add the label to the frame
#--- User input ---
user_input= ctk.CTkEntry(frame, placeholder_text="Enter password lenght", width=200, height= 30, font=("Helvetica", 17 )) # create a entry field for the user to input the password length
user_input.pack(pady=20, padx=20) # add the entry field to the frame
#--- button ---
button = ctk.CTkButton(frame, text="Create", command=createPassWord) # create a button to generate the password
button.pack(pady=10, padx=20) # add the button to the frame

root.mainloop() # start the main loop of the GUI