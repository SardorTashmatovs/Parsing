import tkinter as tk
from tkinter import Label, Entry, Button

import requests
from bs4 import BeautifulSoup
import os

def search_and_download(query, num_images=10, download_path='images'):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img', limit=10)

    img_count = 1

    for img_tag in img_tags:
        img_url = img_tag.get('data-src')
        if not img_url:
            img_url = img_tag.get('src')

        if img_url and img_url.startswith('http'):
            img_filename = os.path.join(download_path, f"{query}_{img_count}.jpg")
            with open(img_filename, 'wb') as f:
                f.write(requests.get(img_url).content)
            print(f"Downloaded {img_filename}")
            img_count += 1

def on_search_button_click():
    query = entry_query.get()
    search_and_download(query)

root = tk.Tk()
root.title("Поиск")

label_query = Label(root, text="Ведите запрос для поиска изображений: ")
label_query.pack(pady=5)

entry_query = Entry(root, width=40)
entry_query.pack(pady=5)

search_button = Button(root, text="Искать и сохранить", command=on_search_button_click)
search_button.pack(pady=10)

root.mainloop()



