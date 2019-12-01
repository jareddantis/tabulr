from PIL import Image

background = Image.open("background.jpg")
foreground = Image.open("table.png")

background.paste(foreground, (0, 0), foreground)
background.show()