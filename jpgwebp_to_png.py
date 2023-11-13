import os
from tkinter import Tk, Button, filedialog, Label, Frame
from PIL import Image


def select_source_folder():
    global source_folder
    source_folder = filedialog.askdirectory()
    source_label.config(text="Выбрана папка: " + source_folder)

def select_destination_folder():
    global destination_folder
    destination_folder = filedialog.askdirectory()
    destination_label.config(text="Папка для сохранения: " + destination_folder)

def convert_images():
    if not source_folder or not destination_folder:
        return

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.jpg', '.webp')):
            img = Image.open(os.path.join(source_folder, filename))
            img.convert('RGB').save(os.path.join(destination_folder, filename.split('.')[0] + '.png'), 'PNG')

    conversion_label.config(text="Конвертация завершена")

# Создание основного окна
root = Tk()
root.title("JPG,WEBP to PNG converter")

# Дизайн
root.configure(bg='black')
frame =Frame(root,bg='black') # Создание рамки с темным фоном
frame.pack(pady=10)
source_label = Label(frame, text="Не выбрана папка с изображениями", bg='black', fg='white')
source_label.pack()

destination_label = Label(frame, text="Не выбрана папка для сохранения", bg='black', fg='white')
destination_label.pack()

conversion_label = Label(frame, text="", bg='black', fg='white')
conversion_label.pack()

# Кнопка с красным фоном и белым текстом
select_button = Button(frame, text="Выбрать папку с изображениями", command=select_source_folder, bg='red', fg='white')
select_button.pack()

save_button = Button(frame, text="Выбрать папку для сохранения", command=select_destination_folder, bg='red', fg='white')
save_button.pack()

convert_button = Button(frame, text="Конвертировать", command=convert_images, bg='red', fg='white')
convert_button.pack()

source_folder = ''
destination_folder = ''

root.mainloop()