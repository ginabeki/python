from PIL import Image, ImageFilter
img = Image.open('./photos/pikachu.png')
filtered_img = img.convert('L')
crooked = filtered_img.rotate(90)
crooked.save('grey.png', 'png') # save, and give it a new name with an extension

