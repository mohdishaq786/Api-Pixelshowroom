
from PIL import Image
import base64
from io import BytesIO
from PIL import Image
import requests

def url_to_pil(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def pil_to_base64(img_pil):
    buffered = BytesIO()
    img_pil.save(buffered, format="webp")
    output_img_str = base64.b64encode(buffered.getvalue()).decode()
    return output_img_str

def base64_to_pil(img_str):
    # Strip data URI scheme header if present
    if img_str.startswith('data:image'):
        img_str = img_str.split(',')[1]
    
    # Decode and load the image
    img_data = base64.b64decode(img_str)
    im = Image.open(BytesIO(img_data))
    return im