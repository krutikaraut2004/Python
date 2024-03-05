from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create the main window
window = Tk()
window.title("⋆.˚✮Text Editor in Python✮˚.⋆")

# Create a Text widget for displaying and editing text
txt = Text(window, fg='black', bg='light pink', font='Poppins 14')
txt.pack()

# Function to open a file
def open_file():
    # Ask user to select a file
    filepath = askopenfilename(filetypes=[("Text file", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    # Clear the existing content in the Text widget
    txt.delete("1.0", END)
    # Read the content of the selected file and insert it into the Text widget
    with open(filepath, mode='r', encoding='utf-8') as input_file:
        text = input_file.read()
        txt.insert(END, text)
        # Update the window title with the current file path
        window.title(f'Text Editor - {filepath}')

# Function to save a file
def save_file():
    # Ask user to select a file and specify the file type
    filepath = asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    # Write the content of the Text widget to the selected file
    with open(filepath, mode='w', encoding='utf-8') as output_file:
        text = txt.get('1.0', END)
        output_file.write(text)
        # Update the window title with the current file path
        window.title(f'Text Editor - {filepath}')

# Word Count
def count_words(event=None):
    text = txt.get("1.0", END)
    words = text.split()
    word_count = len(words)
    status_var.set(f'Word Count: {word_count}')

# Bind the word count function to any key press event
txt.bind('<Key>', count_words)

# Display word count status
status_var = StringVar()
status_var.set('Word Count: 0')
status_label = Label(window, textvariable=status_var, bd=1, relief=SUNKEN, anchor=W)
status_label.pack(side=BOTTOM, fill=X)

# Create a menu bar
menu = Menu(window)
window.config(menu=menu)

# Create a "File" menu with options
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)

# Add "Open" and "Save As..." options to the "File" menu
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save As', command=save_file)

# Start the Tkinter event loop
window.mainloop()
