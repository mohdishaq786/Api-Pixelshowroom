from PIL import Image

def paste_logo(base_image, logo_image, position, margin=10):
    w,h = base_image.size
    logo_image = logo_image.resize([int(w*0.1), int(h*0.1)]).convert('RGBA')
    result_image = base_image.copy()

    # Get dimensions
    base_w, base_h = result_image.size
    logo_w, logo_h = logo_image.size

    # Determine coordinates
    if position == 'top-left':
        pos = (margin, margin)
    elif position == 'top-right':
        pos = (base_w - logo_w - margin, margin)
    elif position == 'bottom-left':
        pos = (margin, base_h - logo_h - margin)
    elif position == 'bottom-right':
        pos = (base_w - logo_w - margin, base_h - logo_h - margin)
    else:
        raise ValueError("Position must be one of: 'top-left', 'top-right', 'bottom-left', 'bottom-right'")

    # Paste with transparency if available
    if logo_image.mode in ("RGBA", "LA"):
        result_image.paste(logo_image, pos, logo_image)
    else:
        result_image.paste(logo_image, pos)

    return result_image
