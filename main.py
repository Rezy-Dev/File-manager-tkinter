import os
import tkinter as tk
from tkinter import filedialog

class FileHandler:
    def __init__(self, master):
        self.master = master
        master.title("File Manager - Rezy Dev")


        self.title = tk.Label(master, text="________________FILE MANAGER________________")
        self.title.pack(side="top")


        self.create_button = tk.Button(master, text="Create File", command=self.create_file)
        self.rename_button = tk.Button(master, text="Rename File", command=self.rename_file)
        self.delete_button = tk.Button(master, text="Delete File", command=self.delete_file)


        self.create_button.pack()
        self.rename_button.pack()
        self.delete_button.pack()


        self.footer = tk.Label(master, text="- by Rezy Dev")
        self.footer.pack(side="bottom")

    def create_file(self):
        directory = filedialog.askdirectory()

        filename = tk.simpledialog.askstring("File Name", "Enter file name:")
        file_path = os.path.join(directory, filename)
        open(file_path, "w").close()

    def rename_file(self):
        file_path = filedialog.askopenfilename()

        new_filename = tk.simpledialog.askstring("New File Name", "Enter new file name:")
        new_file_path = os.path.join(os.path.dirname(file_path), new_filename)
        os.rename(file_path, new_file_path)

    def delete_file(self):
        file_path = filedialog.askopenfilename()

        os.remove(file_path)

root = tk.Tk()
file_handler = FileHandler(root)
root.mainloop()
