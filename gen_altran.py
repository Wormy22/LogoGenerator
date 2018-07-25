from PIL import Image, ImageFont, ImageDraw

import common

OUTPUT = 'altran_out.png'
FONT = "resources/Altran.ttf"

LEFT_COLOUR = (19, 8, 100)
RIGHT_COLOUR = (70, 157, 236)


user_text = "frasssier"

# Create temporary image to determine length of text
temp_image = Image.new("RGBA", (1, 1), (0, 0, 0))
usr_font = ImageFont.truetype(FONT, 500)

text_width, text_height = ImageDraw.Draw(temp_image).textsize(user_text, usr_font)
output_size = (text_width + 20, text_height + 50)

# Create background
bg = Image.new('RGBA', output_size, (255, 255, 255))

# Create gradient
gradient = common.create_horizontal_gradient(LEFT_COLOUR, RIGHT_COLOUR, output_size)

# Apply gradient to text
common.mask_text(bg, user_text, usr_font, gradient, output_size)

# Resample and save output
common.resample_image(bg, output_size)
bg.save(OUTPUT, 'PNG')

# TODO - add weird bar thing
