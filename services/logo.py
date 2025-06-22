
from PIL import Image

def paste_logo(base_image: Image.Image,
               logo_image: Image.Image,
               position: str,
               margin: int = 10,
               scale: float = 0.1) -> Image.Image:
   

    # 1) Prepare base and logo
    base_w, base_h = base_image.size

    # Convert logo to RGBA so transparent pixels stay transparent
    logo = logo_image.convert("RGBA")

    # 2) Compute max dimensions for logo
    max_w = int(base_w * scale)
    max_h = int(base_h * scale)

    # Resize *in place*, preserving aspect ratio and fitting within (max_w, max_h)
    logo.thumbnail((max_w, max_h), Image.LANCZOS)

    logo_w, logo_h = logo.size

    # 3) Figure out where to paste
    if position == "top-left":
        pos = (margin, margin)
    elif position == "top-right":
        pos = (base_w - logo_w - margin, margin)
    elif position == "bottom-left":
        pos = (margin, base_h - logo_h - margin)
    elif position == "bottom-right":
        pos = (base_w - logo_w - margin, base_h - logo_h - margin)
    else:
        raise ValueError(f"Unknown position: {position!r}")

    # 4) Composite and return
    result = base_image.copy()
    result.paste(logo, pos, logo)
    return result
