import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")
        self.root.config(bg="#B2D8D8")  
        self.tasks = []

        # configure apllication fonts
        self.font = "Inter"
        self.font_size = 13

        # Define application colour scheme
        self.bg_color = "#D9F7BE"  
        self.box_color = "#B2D8D8"  
        self.add_button_bg_color = "#2ECC40"  
        self.add_button_fg_color = "#000000"  
        self.delete_button_bg_color = "#FF3737" 
        self.delete_button_fg_color = "#000000"  
        self.task_fg_color = "#032B44" 

        # Create main application frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)

        # Create task entry input field
        self.task_entry = tk.Entry(self.main_frame, width=20, font=(self.font, self.font_size))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Create the Add task button
        self.add_task_button = tk.Button(self.main_frame, text="Add Task", command=self.add_task,
                                         font=(self.font, self.font_size), bg=self.add_button_bg_color, fg=self.add_button_fg_color)
        self.add_task_button.grid(row=0, column=1, sticky="ew")

        # Create the delete task button
        self.delete_task_button = tk.Button(self.main_frame, text="Delete Task", command=self.delete_task,
                                            font=(self.font, self.font_size), bg=self.delete_button_bg_color, fg=self.delete_button_fg_color)
        self.delete_task_button.grid(row=0, column=2, sticky="ew")

        # Create the task list box
        self.task_list = tk.Listbox(self.main_frame, width=20, height=10, font=(self.font, self.font_size), bg=self.box_color, fg=self.task_fg_color)
        self.task_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Bind Enter key to add_task method
        self.task_entry.bind("<Return>", self.add_task)

        # Configure grid columns to resize
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert("end", f"• {task}") 
            self.task_entry.delete(0, tk.END)  
            self.task_entry.focus_set()  
            
    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = ToDoListApp(root)
    root.mainloop()
