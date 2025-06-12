
from PIL import Image
import base64
from io import BytesIO

def base64_to_pil(base64_str):
    if base64_str.startswith("data:image"):
        base64_str = base64_str.split(",", 1)[1]
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))
    return image

def pil_to_base64(img_pil):
    buffered = BytesIO()
    img_pil.save(buffered, format="webp")
    output_img_str = base64.b64encode(buffered.getvalue()).decode()
    return output_img_str