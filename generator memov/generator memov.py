from PIL import Image, ImageDraw, ImageFont

print("Гениратор мемов запущен!")
top_text = input("Введи верхний текст мема: ")
bottom_text = input("Введи нижний текст мема: ")
print(top_text, bottom_text)
print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
image_number = int(input("Введи нормер нужной картинки: "))
image = 0
if image_number == 1:
    image_file = "Кот в ресторане.png"
elif image_number == 2:
    image_file = "Кот в очках.png"

image = Image.open(image_file)

width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=70)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 20), top_text, font = font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font = font, fill="black")


image.save("new_meme.jpg")
