from PIL import Image

background = Image.open("samplebg.jpg")
foreground = Image.open("sampletable.png")

background.paste(foreground, (0, 0), foreground)
background.show()