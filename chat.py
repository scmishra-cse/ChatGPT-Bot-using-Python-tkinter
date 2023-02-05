from tkinter import *
from tkinter import messagebox
import customtkinter
import openai
import os  # To interact with Operating System
import pickle  # To save our API in computer and Retrieve Easily

win = customtkinter.CTk()
win.title("ChatGPT Bot")
win.geometry("600x750")
win.iconbitmap("ai_lt.ico")  # ChatGPT Icon

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# ---All functions will be down there---
# Submit to ChatGPT
def speak():
    if chat_entry.get():
        # Define our filename
        filename = "api_key"
        try:
            if os.path.isfile(filename):
                # Open the file
                input_file = open(filename, "rb")
                # Load the data from the file into a variable
                stuff = pickle.load(input_file)
                # define our API key to CHatGPT
                openai.api_key = stuff
                # Create an instance
                openai.Model.list()

                # Define our Query/ Response
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=chat_entry.get(),
                    temperature=0,
                    max_tokens=60,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                my_response.insert(END, response["choices"][0]["text"])
            else:
                my_response.insert(
                    END,
                    "\n You need an API key to use ChatGPT!\n Visit: https://platform.openai.com/account/api-keys",
                    "WARNING",
                )

        except Exception as e:
            my_response.insert(END, f"\n\n There is an Error!\n\n {e}", "WARNING")
    else:
        my_response.insert(END, "\n\n Hey! You Forgot To Type Anything!", "WARNING")


# Clear the Screen
def clear():
    # Clear Response Screen
    my_response.delete(1.0, END)
    # Clear Query Box
    chat_entry.delete(0, END)


# Do Api Stuffs
def key():
    # Define our filename
    filename = "api_key"
    try:
        if os.path.isfile(filename):
            # Open the file
            input_file = open(filename, "rb")
            # Load the data from the file into a variable
            stuff = pickle.load(input_file)
            # Output the stuff into our entry box
            api_entry.insert(END, stuff)
        else:
            # Create a file
            input_file = open(filename, "wb")
            # Choose the file
            input_file.close()

        # Resize App Larger
        win.geometry("600x750")
        # Show API frame
        api_frame.pack(pady=30)

    except Exception as e:
        my_response.insert(END, f"\n\n There is an error!\n\n {e}", "WARNING")


# Do save your API
def save_key():
    # Define our filename
    filename = "api_key"
    try:
        # open file
        output_file = open(filename, "wb")
        # Actually add the data to the file
        pickle.dump(api_entry.get(), output_file)
        # Delete the entry Box
        api_entry.delete(0, END)

        # Hide API frame
        api_frame.pack_forget()
        # Resize App Smaller
        win.geometry("600x600")

    except Exception as e:
        my_response.insert(END, f"\n\n There is an error!\n\n {e}", "WARNING")

# Create Text Frame
text_frame = customtkinter.CTkFrame(win)
text_frame.pack(pady=20)

# Add Text Widget to Get ChatGPT Responses
my_response = Text(
    text_frame,
    bg="#343638",
    insertbackground="#D4D4D4",
    width=65,
    bd=1,
    fg="#d6d6d6",
    relief="flat",
    wrap=WORD,
    selectbackground="#1f538d",
    pady=10,
    padx=5,
)
my_response.grid(row=0, column=0)

# Create Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_response.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

# ADD THE SCROLLBAR TO THE TEXTBOX
my_response.configure(yscrollcommand=text_scroll.set)
my_response.tag_config("WARNING", foreground="red")

# Entry widget for Type Stuffs
chat_entry = customtkinter.CTkEntry(
    win,
    placeholder_text="Type Something To ChatGPT...",
    width=535,
    height=50,
    border_width=1,
)
chat_entry.pack(pady=10)

# Create Button Frame
button_frame = customtkinter.CTkFrame(win, fg_color="#242424")
button_frame.pack()

# Create Clear Button
clear_button = customtkinter.CTkButton(
    button_frame, text="Clear Response", command=clear
)
clear_button.grid(row=0, column=0, padx=25, pady=20)

# Create Submit Button
submit_button = customtkinter.CTkButton(
    button_frame, text="Speak to ChatGPT", command=speak
)
submit_button.grid(row=0, column=1, padx=25, pady=20)

# Create Change API Button
update_API_button = customtkinter.CTkButton(
    button_frame, text="Update API key", command=key
)
update_API_button.grid(row=0, column=2, padx=25, pady=20)

# ADD API key Frame
api_frame = customtkinter.CTkFrame(win, border_width=1)
api_frame.pack(pady=10)

# Add API Entry Widget
api_entry = customtkinter.CTkEntry(
    api_frame,
    placeholder_text="Enter Your API key...",
    width=350,
    height=50,
    border_width=1,
)
api_entry.grid(row=0, column=0, padx=20, pady=20)

# Add API Button
api_save_button = customtkinter.CTkButton(api_frame, text="Save Key", command=save_key, state=NORMAL)
api_save_button.grid(row=0, column=1, padx=10)

win.mainloop()
