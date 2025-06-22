from PIL import Image

def superimpose_with_resize(background: Image.Image, overlay: Image.Image) -> Image.Image:
    # Ensure both images have alpha channels
    background = background.convert("RGBA")#.resize([3840, 720])
    background.thumbnail([1920, 1080])
    overlay = overlay.convert("RGBA")
    overlay.thumbnail([1920, 1080])

    # Get areas
    bg_width, bg_height = background.size
    ov_width, ov_height = overlay.size

    bg_area = bg_width * bg_height
    ov_area = ov_width * ov_height

    # Check if overlay area > 50% of background
    if ov_area > 0.5 * bg_area:
        # Resize overlay to 25% of its original size
        overlay = overlay.resize((ov_width // 2, ov_height // 2))

    # Center the overlay on the background
    ov_width, ov_height = overlay.size
    position = ((bg_width - ov_width) // 2, (bg_height - ov_height) // 2)

    # Paste the overlay
    result = background.copy()
    result.paste(overlay, position, overlay)

    return result