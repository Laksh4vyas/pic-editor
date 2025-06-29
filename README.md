# 🎨 Advanced Image Editor (Streamlit Version)

An intuitive, modern, and powerful **Image Editor Web App** built using **Python, Streamlit, OpenCV, and Pillow**.

📸 **Upload or capture photos**, apply stunning visual **filters and effects**, and **download** your final masterpiece — all in one slick interface!

---

## 🌟 Key Features

- 📤 **Upload** images in `.jpg`, `.jpeg`, or `.png` formats
- 📷 **Capture** images directly from your **webcam**
- 🎨 Apply multiple **image filters and transformations**:
  - 🖤 Black & White
  - 🌫️ Blur
  - ✏️ Sharpen
  - 🌅 Sepia Tone
  - 🔁 Rotate (90°)
  - ↔️ Flip Horizontally
  - 🌸 Add Flower Border (Pink)
  - 🎨 Change Background Color (White → Yellow)
- 🖼️ View live previews of your edited image
- 💾 **Download** the final edited result in `.png`

---

## 🚀 How to Run Locally

### ✅ Prerequisites

Make sure you have **Python 3.7+** installed on your system.

### 📦 Install Required Packages

```bash
pip install streamlit pillow opencv-python numpy
▶️ Start the App
bash
Copy
Edit
streamlit run image_editor.py
Once launched, a browser window will open automatically. If not, open the link shown in your terminal (http://localhost:8501 by default).

🧠 Tech Stack
Layer	Technologies Used
Frontend	Streamlit (Python)
Image Ops	Pillow (PIL), OpenCV
Interface	Streamlit Widgets + Markdown
I/O	Webcam Capture (cv2) & File I/O
UX Design	Sidebar controls, Live Preview, Download

📁 Folder Structure
bash
Copy
Edit
image-editor/
├── image_editor.py             # Main Streamlit app
├── requirements.txt            # Dependencies
├── assets/                     # Screenshots or icons
│   ├── upload.png
│   └── edited.png
└── README.md                   # Project documentation
🎯 Use Case Scenarios
Quick photo editing without heavy tools like Photoshop

Fun photo filters for students and hobbyists

AI/ML projects that require basic image preprocessing

Web-based image filter playground for learning

🛠 Future Improvements
🌈 Add brightness/contrast sliders

🧠 AI-based background remover

📊 Histogram equalization

🖌️ Draw and annotate tools

💾 Save in different formats (.jpg, .webp, .pdf)

👤 Author
Laksh Vyas
📧 lakshvyas462006@gmail.com
🔗 LinkedIn (optional)
🌐 Portfolio: Coming Soon

📄 License
This project is licensed under the MIT License — you're free to use, fork, and enhance.

⭐ Support This Project
If you found this useful or cool:

⭐ Star this repo

🛠️ Fork and try your own version

📣 Share it with friends

Made with ❤️ using Python & Streamlit.
