import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps, ImageFilter
import numpy as np
import os
import cv2  # For camera capture

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Advanced Image Editor ✨")
        self.root.geometry("1020x750")
        self.root.configure(bg="#1e1e2e")
        self.image = None
        self.edited_image = None
        self.history = []  # For undo history

        title = tk.Label(root, text="Python Image Editor", font=("Helvetica", 24, "bold"), fg="#f1fa8c", bg="#1e1e2e")
        title.pack(pady=10)

        self.filename_label = tk.Label(root, text="No image selected", font=("Arial", 12), fg="#cdd6f4", bg="#1e1e2e")
        self.filename_label.pack()

        # Canvas with scrollbars
        canvas_frame = tk.Frame(root)
        canvas_frame.pack()
        self.canvas = tk.Canvas(canvas_frame, width=800, height=500, bg="#313244", bd=0, highlightthickness=0)
        self.scroll_x = tk.Scrollbar(canvas_frame, orient='horizontal', command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(canvas_frame, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.canvas.grid(row=0, column=0)
        self.scroll_x.grid(row=1, column=0, sticky="we")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        btn_frame = tk.Frame(root, bg="#1e1e2e")
        btn_frame.pack(pady=10)

        btn_style = {"font": ("Arial", 11, "bold"), "bg": "#89b4fa", "fg": "#1e1e2e", "padx": 8, "pady": 5}

        # Row 1
        tk.Button(btn_frame, text="Select Image", command=self.select_image, **btn_style).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Black & White", command=self.black_white, **btn_style).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Change Background", command=self.change_background, **btn_style).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(btn_frame, text="Add Flower Border", command=self.add_flower_border, **btn_style).grid(row=0, column=3, padx=5, pady=5)
        tk.Button(btn_frame, text="Capture from Camera", command=self.capture_from_camera, **btn_style).grid(row=0, column=4, padx=5, pady=5)

        # Row 2
        tk.Button(btn_frame, text="Blur", command=self.blur_image, **btn_style).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Sharpen", command=self.sharpen_image, **btn_style).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Sepia", command=self.sepia_image, **btn_style).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(btn_frame, text="Rotate 90°", command=self.rotate_image, **btn_style).grid(row=1, column=3, padx=5, pady=5)
        tk.Button(btn_frame, text="Flip Horizontal", command=self.flip_image, **btn_style).grid(row=1, column=4, padx=5, pady=5)

        # Row 3
        tk.Button(btn_frame, text="Undo", command=self.undo, **btn_style).grid(row=2, column=0, padx=5, pady=10)
        tk.Button(btn_frame, text="Show Result", command=self.show_result, **btn_style).grid(row=2, column=1, padx=5, pady=10)
        tk.Button(btn_frame, text="Save Image", command=self.save_image, **btn_style).grid(row=2, column=2, padx=5, pady=10)
        tk.Button(btn_frame, text="Quit", command=self.root.quit, bg="#f38ba8", fg="white", font=("Arial", 12, "bold")).grid(row=2, column=3, padx=5, pady=10)

    def push_history(self):
        if self.edited_image:
            self.history.append(self.edited_image.copy())

    def undo(self):
        if self.history:
            self.edited_image = self.history.pop()
            self.display_image(self.edited_image)
            self.filename_label.config(text="Undo: Reverted to previous state")
        else:
            messagebox.showinfo("Undo", "No more undo steps available.")

    def select_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.image = Image.open(path).convert("RGBA")
            self.edited_image = self.image.copy()
            self.history.clear()
            self.display_image(self.image)
            self.filename_label.config(text=f"Loaded: {os.path.basename(path)}")

    def display_image(self, img):
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.image = img_tk
        self.canvas.create_image(0, 0, anchor='nw', image=img_tk)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def black_white(self):
        if self.edited_image:
            self.push_history()
            self.edited_image = self.edited_image.convert("L").convert("RGB")

    def change_background(self):
        if self.edited_image:
            self.push_history()
            arr = np.array(self.edited_image)
            mask = (arr[:, :, 0] > 200) & (arr[:, :, 1] > 200) & (arr[:, :, 2] > 200)
            arr[mask] = [255, 255, 0, 255]  # Yellow background
            self.edited_image = Image.fromarray(arr)

    def add_flower_border(self):
        if self.edited_image:
            self.push_history()
            self.edited_image = ImageOps.expand(self.edited_image, border=40, fill=(255, 182, 193))  # Pink

    def blur_image(self):
        if self.edited_image:
            self.push_history()
            self.edited_image = self.edited_image.filter(ImageFilter.BLUR)

    def sharpen_image(self):
        if self.edited_image:
            self.push_history()
            self.edited_image = self.edited_image.filter(ImageFilter.SHARPEN)

    def sepia_image(self):
        if self.edited_image:
            self.push_history()
            img = np.array(self.edited_image)
            tr = 0.393 * img[:, :, 0] + 0.769 * img[:, :, 1] + 0.189 * img[:, :, 2]
            tg = 0.349 * img[:, :, 0] + 0.686 * img[:, :, 1] + 0.168 * img[:, :, 2]
            tb = 0.272 * img[:, :, 0] + 0.534 * img[:, :, 1] + 0.131 * img[:, :, 2]
            sepia = np.stack([tr, tg, tb], axis=-1)
            sepia = np.clip(sepia, 0, 255).astype(np.uint8)
            self.edited_image = Image.fromarray(sepia)

    def rotate_image(self):
        if self.edited_image:
            self.push_history()
            self.edited_image = self.edited_image.rotate(90, expand=True)

    def flip_image(self):
        if self.edited_image:
            self.push_history()
            self.edited_image = ImageOps.mirror(self.edited_image)

    def show_result(self):
        if self.edited_image:
            self.display_image(self.edited_image)
            self.filename_label.config(text="Previewing Edited Image")

    def save_image(self):
        if self.edited_image:
            path = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
            if path:
                self.edited_image.save(path)
                messagebox.showinfo("Image Saved", f"Saved to: {path}")

    def capture_from_camera(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Camera Error", "Cannot access the camera.")
            return
        
        messagebox.showinfo("Camera", "Press 'Space' to capture, 'Esc' to cancel.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Camera Error", "Failed to grab frame.")
                break
            
            cv2.imshow("Capture Image (Space to capture, Esc to exit)", frame)
            key = cv2.waitKey(1)
            
            if key % 256 == 27:  # ESC pressed
                break
            elif key % 256 == 32:  # SPACE pressed
                cap.release()
                cv2.destroyAllWindows()

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(frame)

                self.image = img
                self.edited_image = img.copy()
                self.history.clear()
                self.display_image(self.image)
                self.filename_label.config(text="Captured Image from Camera")
                return

        cap.release()
        cv2.destroyAllWindows()

# Launch
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditor(root)
    root.mainloop()
