from PIL import Image

def superimpose_with_resize(background: Image.Image,
                            overlay: Image.Image,
                            overlay_area_ratio: float = 0.6) -> Image.Image:
    bg = background.convert("RGBA")
    ov = overlay.convert("RGBA")

    # Downscale background if needed, using LANCZOS
    bg.thumbnail((1920, 1080), resample=Image.Resampling.LANCZOS)

    bg_w, bg_h = bg.size
    target_area = overlay_area_ratio * (bg_w * bg_h)

    ov_w, ov_h = ov.size
    scale = (target_area / (ov_w * ov_h)) ** 0.5
    new_w = int(ov_w * scale)
    new_h = int(ov_h * scale)

    # Clamp so it never exceeds background
    max_scale = min(bg_w / ov_w, bg_h / ov_h)
    if scale > max_scale:
        new_w = int(ov_w * max_scale)
        new_h = int(ov_h * max_scale)

    # **Here’s the key line**:
    ov = ov.resize((new_w, new_h), resample=Image.Resampling.LANCZOS)

    pos = ((bg_w - new_w) // 2, (bg_h - new_h) // 2)
    result = bg.copy()
    result.paste(ov, pos, ov)
    return result
