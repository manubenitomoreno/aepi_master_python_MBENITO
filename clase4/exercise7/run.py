import timeit
import threading
from PIL import Image, ImageDraw, ImageFont
import random

def add_watermark(image_path, watermark_text):
    image = Image.open(image_path).convert('RGBA')

    # watermark
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)
    font = ImageFont.truetype('arial.ttf', 36)  # Select the font and size

    # Position
    watermark_text_size = draw.textbbox((0, 0), watermark_text, font=font)
    watermark_position = (
        random.randint(0, image.size[0] - watermark_text_size[2]),
        random.randint(0, image.size[1] - watermark_text_size[3])
    )

    fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 128)

    # Text in watermark
    draw.text(watermark_position, watermark_text, font=font, fill=fill_color)

    # Combine images
    watermarked_image = Image.alpha_composite(image, watermark)

    # Save the watermarked image
    final_image = Image.new('RGB', image.size)
    final_image.paste(watermarked_image, (0, 0), watermarked_image)

    # Overwrite the original image
    final_image.save(image_path)


image_paths = [r"{n}.png".format(n=n) for n in range(1, 9)]
watermark = 'Soy Batman'


def add_watermark_thread(image_path, watermark_text):
    add_watermark(image_path, watermark_text)
    print(f"Watermark added to {image_path}")


if __name__ == '__main__':
    start_time = timeit.default_timer()

    # Threading
    threads = []
    for image_path in image_paths:
        thread = threading.Thread(target=add_watermark_thread, args=(image_path, watermark))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    execution_time = timeit.default_timer() - start_time
    print(f"Execution time with threading: {execution_time} seconds")

    start_time = timeit.default_timer()

    for image_path in image_paths:
        add_watermark(image_path, watermark)

    execution_time = timeit.default_timer() - start_time
    print(f"Execution time without threading: {execution_time} seconds")
