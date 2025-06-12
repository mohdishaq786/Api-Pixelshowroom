from utils.util import base64_to_pil,pil_to_base64
from rembg import remove
def remove_bg(input_img):
    output = remove(input_img)
    return output