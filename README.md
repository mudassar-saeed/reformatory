# 🚀 ReFormatory

**ReFormatory** is a modern document conversion platform starting with a clean and efficient PDF → Word converter.

Built with performance, simplicity, and scalability in mind, this is Version 1.0 of a growing SaaS-ready system designed to evolve into a full document processing suite.

---

## ✨ Current Capabilities (v1.0)

- 📄 Convert PDF to editable Word (.docx)
- 🎯 Drag & Drop upload interface
- ⚡ Real-time animated button feedback (spinner → success tick)
- 🔐 Secure file validation
- 🧹 Automatic server-side file cleanup
- 💾 Memory-based streaming (no file locking issues)
- 🎨 Clean, modern Tailwind CSS UI
- 🧱 Structured Flask backend architecture

---

## 🛠 Technology Stack

- **Backend:** Python, Flask
- **Conversion Engine:** pdf2docx (will be added more as our project grows)
- **Frontend:** Tailwind CSS, Vanilla JavaScript
- **Architecture:** Single-route modular design (expandable)

---

## 🏗 Architecture Overview

ReFormatory is structured for future expansion into a multi-tool platform (I will keep updating the architecture as we go):

```
ReFormatory/
│
├── app.py
├── config.py
├── requirements.txt
├── converter/
│   └── pdf_converter.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── logo.png
│   └── favicon.png
│
├── uploads/
└── outputs/
```

The current implementation focuses on clean separation of concerns and safe file handling to support future scaling.

---

## ⚙️ Local Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mudassar-saeed/reformatory.git
cd reformatory
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

- Windows:
```bash
venv\Scripts\activate
```

- macOS / Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 🔮 Roadmap

ReFormatory is being built as a modular SaaS platform.

Planned features:


- PDF → Word
- Word → PDF
- PDF → Image (JPG / PNG)
- Image → PDF
- Merge PDFs
- Split PDFs
- Compress PDF
- PDF → Text
- Text → PDF
- PowerPoint → PDF
- Excel → PDF
- Image format conversions (JPG ↔ PNG ↔ WEBP)
- Video → Audio (MP4 → MP3)
- Audio format conversions (MP3 ↔ WAV)
- Batch file conversions

---

## 🎯 Vision

The long-term goal of ReFormatory is to become a streamlined, performance-focused document and media format conversion platform with:

- Clean UX
- Reliable backend processing
- Scalable architecture
- SaaS-ready deployment model

This repository represents the foundation of that vision.

---

## 👨‍💻 Author

Built and maintained by **Mudassar Saeed**

---

## 📜 License

MIT License
