import tkinter as tk
from tkinter import messagebox
import sys
import subprocess
import os

class ValentineProposal:
    """
    A Valentine's Day proposal application with an interactive GUI.
    Features a title and two buttons (YES/NO), where the YES button grows
    each time NO is clicked, making it harder to resist the proposal.
    """

    def __init__(self):
        """
        Initialize the main application window and setup initial configurations.
        """
        self.root = tk.Tk()
        self.root.title("Valentine's Proposal")
        self.root.geometry("400x300")
        self.root.configure(bg='#FFE4E1')  # Light pink background
        
        self.yes_size = 14  # Initial font size for YES button
        self.create_widgets()
        
    def create_widgets(self):
        """
        Create and configure all GUI elements including title and buttons.
        """
        # Title configuration
        title = tk.Label(
            self.root,
            text="Will you be my Valentine?",
            font=('Comic Sans MS', 20, 'bold'),
            bg='#FFE4E1',
            fg='#FF69B4'  # Darker pink for text
        )
        title.pack(pady=30)
        
        # Frame for button organization
        button_frame = tk.Frame(self.root, bg='#FFE4E1')
        button_frame.pack(expand=True)
        
        # YES button configuration
        self.yes_button = tk.Button(
            button_frame,
            text="YES",
            font=('Comic Sans MS', self.yes_size, 'bold'),
            command=self.yes_clicked,
            bg='#98FB98',  # Light green
            fg='white',
            relief=tk.RAISED,
            borderwidth=3
        )
        self.yes_button.pack(side=tk.LEFT, padx=10)
        
        # NO button configuration
        self.no_button = tk.Button(
            button_frame,
            text="NO",
            font=('Comic Sans MS', 14, 'bold'),
            command=self.no_clicked,
            bg='#FF6B6B',  # Light red
            fg='white',
            relief=tk.RAISED,
            borderwidth=3
        )
        self.no_button.pack(side=tk.LEFT, padx=10)
        
        # Configure rounded borders for buttons
        self.yes_button.configure(borderwidth=4, relief="ridge")
        self.no_button.configure(borderwidth=4, relief="ridge")
        
    def yes_clicked(self):
        """
        Handle YES button click event.
        Shows a success message and run another script (in this case, launches a sunflower animation).
        """
        messagebox.showinfo(
            "¡Síii!, mi pequeña saltamontes c:",
            "Me acabas de hacer el hombre más feliz! ❤️\n\nAhora una sopresa para ti 🌻"
        )
        
        # Execute the sunflower animation script
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            ale_path = os.path.join(script_dir, "sunflower.py")
            subprocess.Popen([sys.executable, ale_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not execute sunflower.py: {str(e)}")
        
        self.root.quit()
        sys.exit()
        
    def no_clicked(self):
        """
        Handle NO button click event.
        Increases the size of the YES button by 50%.
        """
        self.yes_size *= 1.5
        self.yes_button.configure(font=('Comic Sans MS', int(self.yes_size), 'bold'))
        
    def run(self):
        """
        Start the application's main event loop.
        """
        self.root.mainloop()

if __name__ == "__main__":
    app = ValentineProposal()
    app.run()
