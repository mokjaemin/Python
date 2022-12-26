from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open("text_Image.png"), lang='kor')
print(text)

# with open("example.txt", "w", encoding="utf8") as f:
#     f.write(text)
#     f.write("\n\n\n")
#     f.write(text.replace(" ", ""))