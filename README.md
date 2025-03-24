# QR Code Generator  

## Project Overview  

### Objective:  
The project aims to create a QR Code Generator using both Python and a web-based interface. The application allows users to generate and download QR codes for any text or URL input.  

### Features:
- **Python-based QR Code Generator**: Uses the `qrcode` library to generate QR codes.
- **Web-based QR Code Generator**: Built using HTML, CSS, and JavaScript for an interactive QR code generation experience.
- **Dark Mode Support**: Allows users to switch between light and dark themes.
- **Downloadable QR Codes**: Users can download the generated QR code as an image.

---

## Project Structure  

- **QR_PY.py**: A Python script that generates and saves QR codes.
- **QR.html**: A web-based QR code generator with a stylish UI and dynamic functionalities.

---

## Key Steps  

### 1. Python-based QR Code Generator  
- Uses the `qrcode` library to generate a QR code for a given text.
- Saves the QR code as an image.

### 2. Web-based QR Code Generator  
- **HTML & CSS**: Provides a responsive UI with a dark mode toggle.
- **JavaScript**: Uses the `qrcodejs` library to generate QR codes dynamically.
- **Functionality**:
  - Users can input text or a URL.
  - Generates a QR code upon clicking the "Generate" button.
  - Allows users to download the QR code image.

---

## Technologies Used  

- **Python**: For backend QR code generation.  
- **qrcode (Python Library)**: To generate QR codes.  
- **HTML, CSS, JavaScript**: For the web interface.  
- **QRCode.js**: JavaScript library for QR code generation.  
- **FontAwesome**: For UI icons and buttons.  

---

## How to Use  

### Using Python Script:  
1. Install dependencies:  
   ```bash
   pip install qrcode[pil]
   ```
2. Run the script:  
   ```bash
   python QR_PY.py
   ```
3. The QR code image (`QR.png`) will be saved in the project folder.  

### Using Web Interface:  
1. Open `QR.html` in a browser.  
2. Enter the text or URL in the input field.  
3. Click **"Generate QR Code"** to display the QR code.  
4. Click **"Download"** to save the QR code as an image.  
5. Toggle **dark mode** using the button at the top-right corner.  

---

## Future Improvements  

- **Add logo support**: Allow users to embed logos in QR codes.  
- **Error correction levels**: Improve QR readability in different conditions.  
- **QR Styling**: Allow customization of QR colors and designs.  
- **Cloud Deployment**: Host the web-based generator online for easy access.  

---

### Conclusion  

This project provides an efficient QR Code Generator with both Python and web-based implementations. The Python script is lightweight and quick for offline use, while the web interface offers an interactive, user-friendly experience.  

---
