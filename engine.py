from PIL import Image
from pillow_lut import load_cube_file

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


def apply_rio_lut(input_path, output_path, lut_path='rio_filter.cube'):
    img = Image.open(input_path)
    lut = load_cube_file(lut_path)
    
    # Apply the LUT
    result = img.filter(lut)
    
    result.save(output_path)

apply_rio_lut("tmp/1.jpg", 'tmp/out.png', '/tmp/rio.cube')


