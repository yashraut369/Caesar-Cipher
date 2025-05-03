# Caesar Cipher Tool

A professional GUI application for encrypting and decrypting text using the Caesar Cipher algorithm.

## Features

- **Encrypt text** using a specified shift value
- **Decrypt text** using a specified shift value
- Modern, intuitive graphical interface
- Copy encrypted/decrypted text to clipboard
- Support for keyboard shortcuts
- Clear all fields with one click

## Screenshots

![Caesar Cipher Tool Screenshot](screenshots/screenshot.png)

## Installation

### Prerequisites

- Python 3.6 or higher
- Required packages: `tkinter`, `pyperclip`

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yashraut369/Caesar-Cipher.git
   cd Caesar-Cipher
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python caesar_cipher_gui.py
   ```

## Usage

1. Enter the text you want to encrypt or decrypt in the input area
2. Set the shift value (1-25) for the encryption/decryption
3. Click "Encrypt" or "Decrypt" button to process the text
4. View the result in the corresponding output tab
5. Use the Copy buttons to copy the result to clipboard

### Keyboard Shortcuts

- `Ctrl+E`: Encrypt
- `Ctrl+D`: Decrypt
- `Ctrl+N`: New (Clear all fields)

## About Caesar Cipher

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

## Project Structure

```
caesar-cipher/
├── caesar_cipher.py    # Main application file
├── requirements.txt        # Required packages
├── README.md               # This file
├── LICENSE                 # License information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by Yash (Popeye)

---

Feel free to contribute to this project by submitting issues or pull requests.
