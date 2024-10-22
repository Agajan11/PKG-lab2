import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, ttk

def get_image_info(file_path):
    try:
        with Image.open(file_path) as img:
            file_name = os.path.basename(file_path)
            size = img.size
            dpi = img.info.get('dpi', (0, 0))
            color_depth = len(img.getbands()) * 8
            compression = img.info.get('compression', 'N/A')
            return file_name, size, dpi, color_depth, compression
    except Exception as e:
        return None

def load_images_from_folder(folder):
    supported_formats = ('.jpg', '.jpeg', '.gif', '.tif', '.tiff', '.bmp', '.png', '.pcx')
    image_info_list = []

    for filename in os.listdir(folder):
        if filename.lower().endswith(supported_formats):
            file_path = os.path.join(folder, filename)
            info = get_image_info(file_path)
            if info:
                image_info_list.append(info)

    return image_info_list

def display_results(data):
    root = tk.Tk()
    root.title("Image Information")

    tree = ttk.Treeview(root)
    tree['columns'] = ("Size", "Resolution", "Color Depth", "Compression")
    tree.heading("#0", text="File Name", anchor='w')
    tree.column("#0", anchor="w")
    tree.heading("Size", text="Size (px)")
    tree.heading("Resolution", text="Resolution (DPI)")
    tree.heading("Color Depth", text="Color Depth")
    tree.heading("Compression", text="Compression")

    for item in data:
        file_name, size, dpi, color_depth, compression = item
        tree.insert("", tk.END, text=file_name, values=(f"{size[0]}x{size[1]}", f"{dpi[0]}x{dpi[1]}", f"{color_depth} bit", compression))

    tree.pack(expand=True, fill='both')
    root.mainloop()

def main():
    folder_path = filedialog.askdirectory(title="Select a Folder with Images")
    if folder_path:
        image_data = load_images_from_folder(folder_path)
        if image_data:
            display_results(image_data)
        else:
            print("No valid image files found.")

if __name__ == "__main__":
    main()