from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import os

def apply_transformations(path: str, resize=None, grayscale=False, rotate=0, crop=None, flip=None,
                          compress=100, format=None, sepia=False, blur=False, sharpen=False,
                          watermark_text=None):
    img = Image.open(path).convert("RGB")

    if resize:
        try:
            w, h = map(int, resize.lower().split("x"))
            img = img.resize((w, h))
        except:
            pass

    if crop:
        try:
            x, y, w, h = map(int, crop.split(","))
            img = img.crop((x, y, x + w, y + h))
        except:
            pass

    if rotate:
        img = img.rotate(rotate, expand=True)

    if grayscale:
        img = ImageOps.grayscale(img)

    if sepia:
        sepia_img = ImageOps.colorize(ImageOps.grayscale(img), '#704214', '#C0A080')
        img = sepia_img

    if flip == "horizontal":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip == "vertical":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

    if blur:
        img = img.filter(ImageFilter.GaussianBlur(2))

    if sharpen:
        img = img.filter(ImageFilter.SHARPEN)

    if watermark_text:
        draw = ImageDraw.Draw(img)
        font_size = int(min(img.size) / 15)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = img.width - text_width - 10
        y = img.height - text_height - 10
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    base, ext = os.path.splitext(path)
    new_format = format.lower() if format else ext.replace('.', '')
    new_ext = f".{new_format}"
    new_path = f"{base}_transformed{new_ext}"

    img.save(new_path, quality=compress, format=new_format.upper())
    return os.path.basename(new_path)