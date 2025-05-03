"""
Caesar Cipher - Encryption and Decryption Tool
Created by Yash (Popeye)

A professional GUI application for encrypting and decrypting text using the
Caesar Cipher algorithm.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, Menu
import pyperclip
import re

class CaesarCipherApp:
    """Main application class for Caesar Cipher GUI."""
    
    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Caesar Cipher Tool")
        self.root.geometry("850x600")
        self.root.minsize(650, 500)
        
        # Set application icon
        try:
            self.root.iconbitmap("assets/icon.ico")
        except:
            pass  # Icon not available, continue without it
        
        # Set theme colors
        self.bg_color = "#f5f5f5"
        self.accent_color = "#3498db"
        self.text_color = "#2c3e50"
        self.button_color = "#2980b9"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_menu()
        self.create_widgets()
        self.setup_bindings()
        
        # Apply styling
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Segoe UI', 10))
        self.style.configure('TLabel', font=('Segoe UI', 11), background=self.bg_color)
        self.style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'), background=self.bg_color)
        
        # Status variable
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        # Create status bar
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def create_menu(self):
        """Create application menu bar."""
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.clear_fields)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy Encrypted", command=lambda: self.copy_text("encrypt"))
        edit_menu.add_command(label="Copy Decrypted", command=lambda: self.copy_text("decrypt"))
        
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Instructions", command=self.show_instructions)
        
    def create_widgets(self):
        """Create and place all GUI widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Caesar Cipher Encryption & Decryption", 
                            style='Header.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(input_frame, text="Enter your message:").pack(anchor=tk.W, pady=(5, 0))
        
        self.input_text = scrolledtext.ScrolledText(input_frame, height=6, wrap=tk.WORD)
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Shift value frame
        shift_frame = ttk.Frame(input_frame)
        shift_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(shift_frame, text="Shift Value:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.shift_var = tk.StringVar(value="3")
        self.shift_entry = ttk.Spinbox(shift_frame, from_=1, to=25, 
                                   textvariable=self.shift_var, width=5)
        self.shift_entry.pack(side=tk.LEFT)
        
        ttk.Label(shift_frame, text="(1-25)").pack(side=tk.LEFT, padx=(5, 0))
        
        # Buttons Frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=15)
        
        # Create visual separation
        ttk.Separator(buttons_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Action buttons
        action_frame = ttk.Frame(buttons_frame)
        action_frame.pack()
        
        self.encrypt_button = ttk.Button(
            action_frame, text="Encrypt", command=self.encrypt_text, 
            style='TButton', width=15
        )
        self.encrypt_button.pack(side=tk.LEFT, padx=5)
        
        self.decrypt_button = ttk.Button(
            action_frame, text="Decrypt", command=self.decrypt_text,
            style='TButton', width=15
        )
        self.decrypt_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = ttk.Button(
            action_frame, text="Clear All", command=self.clear_fields,
            style='TButton', width=15
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Output frame
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Output tabs
        self.output_tabs = ttk.Notebook(output_frame)
        self.output_tabs.pack(fill=tk.BOTH, expand=True)
        
        # Encrypted tab
        encrypt_tab = ttk.Frame(self.output_tabs)
        self.output_tabs.add(encrypt_tab, text="Encrypted")
        
        self.encrypted_text = scrolledtext.ScrolledText(encrypt_tab, height=6, wrap=tk.WORD)
        self.encrypted_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Decrypted tab
        decrypt_tab = ttk.Frame(self.output_tabs)
        self.output_tabs.add(decrypt_tab, text="Decrypted")
        
        self.decrypted_text = scrolledtext.ScrolledText(decrypt_tab, height=6, wrap=tk.WORD)
        self.decrypted_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Footer with creator info
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(fill=tk.X, pady=(15, 0))
        
        creator_label = ttk.Label(
            footer_frame, 
            text="Created by Yash (Popeye)", 
            font=('Segoe UI', 9, 'italic'),
            foreground="#555555"
        )
        creator_label.pack(side=tk.RIGHT)
        
    def setup_bindings(self):
        """Set up keyboard shortcuts."""
        self.root.bind("<Control-e>", lambda event: self.encrypt_text())
        self.root.bind("<Control-d>", lambda event: self.decrypt_text())
        self.root.bind("<Control-n>", lambda event: self.clear_fields())
        
    def encrypt_text(self):
        """Encrypt the input text using Caesar cipher."""
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showinfo("Info", "Please enter text to encrypt.")
                return
                
            shift = self.validate_shift()
            if shift is None:
                return
                
            encrypted = self.caesar_cipher(text, shift)
            
            self.encrypted_text.delete("1.0", tk.END)
            self.encrypted_text.insert("1.0", encrypted)
            
            self.output_tabs.select(0)  # Switch to encrypted tab
            self.status_var.set(f"Text encrypted with shift value: {shift}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during encryption: {str(e)}")
    
    def decrypt_text(self):
        """Decrypt the input text using Caesar cipher."""
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showinfo("Info", "Please enter text to decrypt.")
                return
                
            shift = self.validate_shift()
            if shift is None:
                return
                
            decrypted = self.caesar_cipher(text, -shift)
            
            self.decrypted_text.delete("1.0", tk.END)
            self.decrypted_text.insert("1.0", decrypted)
            
            self.output_tabs.select(1)  # Switch to decrypted tab
            self.status_var.set(f"Text decrypted with shift value: {shift}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during decryption: {str(e)}")
    
    def caesar_cipher(self, text, shift):
        """
        Apply Caesar cipher to the given text with specified shift.
        
        Args:
            text (str): The text to encrypt/decrypt
            shift (int): The shift value (positive for encryption, negative for decryption)
            
        Returns:
            str: The encrypted/decrypted text
        """
        result = ""
        # Ensure shift is within range 0-25
        shift = shift % 26
        
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                # Apply shift and wrap around
                shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
                result += chr(shifted)
            else:
                # Non-alphabetic characters remain unchanged
                result += char
                
        return result
    
    def validate_shift(self):
        """Validate the shift value entered by the user."""
        try:
            shift = int(self.shift_var.get())
            if 1 <= shift <= 25:
                return shift
            else:
                messagebox.showerror("Invalid Input", "Shift value must be between 1 and 25.")
                return None
        except ValueError:
            messagebox.showerror("Invalid Input", "Shift value must be a number.")
            return None
    
    def clear_fields(self):
        """Clear all input and output fields."""
        self.input_text.delete("1.0", tk.END)
        self.encrypted_text.delete("1.0", tk.END)
        self.decrypted_text.delete("1.0", tk.END)
        self.shift_var.set("3")
        self.status_var.set("Ready")
    
    def copy_text(self, output_type):
        """Copy the encrypted or decrypted text to clipboard."""
        if output_type == "encrypt":
            text = self.encrypted_text.get("1.0", tk.END).strip()
            if text:
                pyperclip.copy(text)
                self.status_var.set("Encrypted text copied to clipboard")
        else:
            text = self.decrypted_text.get("1.0", tk.END).strip()
            if text:
                pyperclip.copy(text)
                self.status_var.set("Decrypted text copied to clipboard")
    
    def show_about(self):
        """Show information about the application."""
        about_text = """
Caesar Cipher Tool v1.0

Created by Yash (Popeye)

A simple yet powerful tool for encrypting and decrypting 
messages using the Caesar Cipher algorithm.

© 2025 All rights reserved.
        """
        messagebox.showinfo("About", about_text.strip())
    
    def show_instructions(self):
        """Show usage instructions."""
        instructions = """
How to Use:

1. Enter the text you want to encrypt or decrypt in the input area.
2. Set the shift value (1-25) for the encryption/decryption.
3. Click 'Encrypt' or 'Decrypt' button to process the text.
4. View the result in the corresponding output tab.
5. Use the Copy buttons to copy the result to clipboard.

Keyboard Shortcuts:
- Ctrl+E: Encrypt
- Ctrl+D: Decrypt
- Ctrl+N: New (Clear all fields)
        """
        messagebox.showinfo("Instructions", instructions.strip())


def main():
    """Application entry point."""
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
