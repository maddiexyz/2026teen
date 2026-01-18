from PIL import Image

def apply_rio_mask(background_img, overlay_img, output_img, opacity=0.45):
    background = Image.open(background_img).convert("RGBA")
    overlay = Image.open(overlay_img).convert("RGBA")

    overlay = overlay.resize(background.size, Image.LANCZOS)

    alpha = overlay.split()[3]
    alpha = alpha.point(lambda p: int(p * 0.45))
    overlay.putalpha(alpha)

    rio = Image.alpha_composite(background,overlay)

    rio.save(output_img)

apply_rio_mask("tmp/1.jpg", 'tmp/overlay.jpg', 'tmp/out.png')