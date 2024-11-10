# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing and Painting App")
        self.root.geometry("800x600")

        # Canvas setup
        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(pady=20)

        # Create a blank image for saving the artwork
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Set initial brush color
        self.current_color = "black"

        # Add buttons
        self.color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.current_color = color

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color, width=2)
        self.draw.line([x1, y1, x2, y2], fill=self.current_color, width=2)

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 600, 400], fill="white")

    def save_image(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            self.image.save(filename)

# Set up the main window and application
root = tk.Tk()
app = DrawingApp(root)
root.mainloop()

