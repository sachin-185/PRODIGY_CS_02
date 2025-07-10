# 🔐 Pixel-Based Image Protection System

A lightweight and secure image encryption-decryption tool using XOR-based pixel manipulation. This project enables users to encrypt or decrypt image files using a numeric key and visualize both the original and processed images. It provides a simple interface via command-line inputs and supports common image formats (e.g., PNG, JPEG).

---

## 🚀 Features

- 🖼️ Load and process any RGB or RGBA image
- 🔒 XOR-based encryption with customizable key (0–255)
- 🔓 Reversible decryption using the same key
- 💾 Save encrypted/decrypted images to specified output paths
- 📊 Visualize original and transformed images using matplotlib
- ✅ User-friendly CLI prompts with input validation

---

## 🛠 Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (`pip install pillow`)
- [NumPy](https://pypi.org/project/numpy/) (`pip install numpy`)
- [Matplotlib](https://pypi.org/project/matplotlib/) (`pip install matplotlib`)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/pixel-image-encryptor.git
cd pixel-image-encryptor
pip install -r requirements.txt

