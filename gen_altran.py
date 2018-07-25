from PIL import Image, ImageFont, ImageDraw

OUTPUT = 'altran_out.png'
FONT = "resources/Altran.ttf"

def interpolate(f_co, t_co, interval):
    det_co = [(t - f) / interval for f, t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]


def create_gradient(width, height):
    gradient = Image.new('RGBA', (width, height), color=0)
    grad_draw = ImageDraw.Draw(gradient)

    left_colour = (19, 8, 100)
    right_colour = (70, 157, 236)
    for i, colour in enumerate(interpolate(left_colour, right_colour, width)):
        grad_draw.line([(i, 0), (i, height)], tuple(colour), width=1)

    return gradient

user_text = "frasier"

# Create temporary image to determine length of text
temp_image = Image.new("RGBA", (1, 1), (0, 0, 0))
usr_font = ImageFont.truetype(FONT, 500)

text_width, text_height = ImageDraw.Draw(temp_image).textsize(user_text, usr_font)
out_width = text_width + 20
out_height = text_height + 50

# Create background
bg = Image.new('RGBA', (out_width, out_height), (255, 255, 255))

# Create gradient
gradient = create_gradient(out_width, out_height)

# Apply gradient to text
mask = Image.new('1', (out_width, out_height))
mask_draw = ImageDraw.Draw(mask)
mask_draw.text((10, 0), user_text, font=usr_font, fill='#ffffff')
bg.paste(gradient, (0,0), mask)

# Resample and save output
bg.thumbnail((int(out_width/2), int(out_height/2)), Image.ANTIALIAS)
bg.save(OUTPUT, 'PNG')

# TODO - add weird bar thing
