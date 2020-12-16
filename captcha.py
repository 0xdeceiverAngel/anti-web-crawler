import pytesseract
from os import path
  
try:
    from PIL import Image
except ImportError:
    import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def handler(grays, threshold=150):
    """对灰度图片进行二值化处理
    默认阈值为160，可根据实际情况调整
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    anti = grays.point(table, '1')
    return anti



images = path.join(path.dirname(path.abspath(__file__)), 'pic.png')
gray = Image.open(images).convert('L')
images = handler(gray)
images.show()
print(pytesseract.image_to_string(images))