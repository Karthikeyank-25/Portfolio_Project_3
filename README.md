# 🖼️ Image Watermark Adder

This is a Python-based GUI application that allows users to add custom text watermarks to images. Built using Tkinter and Pillow, the app provides a simple interface to select an image, add watermark text, and save the modified image.

---

## 🚀 Features

* 🖼️ Select any image from your system
* ✍️ Add custom watermark text
* 🌫️ Supports transparent watermark
* 💾 Save the watermarked image
* 🖥️ Simple and user-friendly GUI

---

## 🛠️ Technologies Used

* Python 🐍
* Tkinter 🖼️
* Pillow (PIL) 🎨

---

## 📂 Project Structure

```id="k4m9xp"
project-folder/
│
├── main.py
├── arial.ttf   # Font file (required)
└── README.md
```

---

## ⚙️ How It Works

1. User enters watermark text
2. Clicks **Select Image**
3. Chooses an image from the system
4. The app:

   * Converts image to RGBA format
   * Adds transparent text watermark
   * Combines watermark with original image
5. User selects location to save the new image

---

## ▶️ How to Run

### 1. Clone the repository

```bash id="x3k9lm"
git clone https://github.com/your-username/image-watermark-adder.git
cd image-watermark-adder
```

### 2. Install dependencies

```bash id="m7p2zx"
pip install pillow
```

### 3. Run the application

```bash id="q2l8vc"
python main.py
```

---

## 🧠 Example Workflow

* Enter text: `© Karthikeyan`
* Select an image
* Save the output image
* Watermarked image is generated and displayed

---

## ⚠️ Notes

* Make sure `arial.ttf` font file is available in the project folder
* Watermark position is fixed (can be customized in code):

```python id="z1k8ds"
position = (width + 20 ,height - 50 )
```

* Supports common image formats (JPG, PNG)

---

## 🚀 Future Improvements

* Allow custom positioning (drag & drop)
* Add image watermark support (logo)
* Adjustable font size and opacity
* Preview before saving
* Add multiple watermark styles

---

## 👨‍💻 Author

Karthikeyan

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
