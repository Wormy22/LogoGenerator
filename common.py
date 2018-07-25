from PIL import Image, ImageFont, ImageDraw

# TODO - document

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def determine_image_size(text, font):
    temp_image = Image.new("RGBA", (1, 1), BLACK)

    return ImageDraw.Draw(temp_image).textsize(text, font)


def interpolate(f_co, t_co, interval):
    det_co = [(t - f) / interval for f, t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]


def create_horizontal_gradient(left_colour, right_colour, image_size):
    gradient = Image.new('RGBA', image_size, color=0)
    grad_draw = ImageDraw.Draw(gradient)

    for i, colour in enumerate(interpolate(left_colour, right_colour, image_size[0])):
        grad_draw.line([(i, 0), (i, image_size[1])], tuple(colour), width=1)

    return gradient


def create_vertical_gradient(top_colour, bottom_colour, image_size):
    gradient = Image.new('RGBA', image_size, color=0)
    grad_draw = ImageDraw.Draw(gradient)

    for i, colour in enumerate(interpolate(top_colour, bottom_colour, image_size[1])):
        grad_draw.line([(0, i), (image_size[0], i)], tuple(colour), width=1)

    return gradient


def mask_text(background, text, font, fill, output_size):
    '''Operates on background image!!!'''
    mask = Image.new('1', output_size)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.text((0, 0), text, font=font, fill='#ffffff')
    background.paste(fill, (0, 0), mask)


def resample_image(image, original_size):
    new_width = int(original_size[0] / 2)
    new_height = int(original_size[1] / 2)

    image.thumbnail((new_width, new_height), Image.ANTIALIAS)
