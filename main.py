import customtkinter
import tkinter
from PIL import Image, ImageTk
import requests
import io
from generateImage import generate_image


def generate():
    # Get user input from the GUI
    user_prompt = prompt_entry.get("0.0", tkinter.END)
    user_prompt += " in style: " + style_dropdown.get()

    # Call the function from generate_image.py to generate images
    image_urls = generate_image(user_prompt, num_images=int(number_slider.get()), image_size="512x512")
    print(image_urls)

    # Load and display generated images in the GUI
    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)

    def update_image(index=0):
        canvas.image = images[index]
        canvas.create_image(0, 0, anchor="nw", image=images[index])
        index = (index + 1) % len(images)
        canvas.after(3000, update_image, index)

    update_image()


root = customtkinter.CTk()
root.title("AI Image Generator")

customtkinter.set_appearance_mode("dark")

input_frame = customtkinter.CTkFrame(root)
input_frame.pack(side="left", expand=True, padx=20, pady=20)

prompt_label = customtkinter.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row=0, column=0, padx=10, pady=10)
prompt_entry = customtkinter.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

style_label = customtkinter.CTkLabel(input_frame, text="Style")
style_label.grid(row=1, column=0, padx=10, pady=10)
style_dropdown = customtkinter.CTkComboBox(input_frame, values=["Realistic", "Cartoon", "3D Illustration", "Flat Art"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

number_label = customtkinter.CTkLabel(input_frame, text="# Images")
number_label.grid(row=2, column=0)
number_slider = customtkinter.CTkSlider(input_frame, from_=1, to=10, number_of_steps=9)
number_slider.grid(row=2, column=1)

generate_button = customtkinter.CTkButton(input_frame, text="Generate", command=generate)
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10)

canvas = tkinter.Canvas(root, width=512, height=512)
canvas.pack(side="left")

root.mainloop()
