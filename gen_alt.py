from PIL import Image, ImageFont

import common

# TODO - document

# -----------------------------------------------------------------------------

FONT = "resources/Alt.ttf"
OUTPUT_FILE = 'alt_out.png'

LEFT_COLOUR = (19, 8, 100)
RIGHT_COLOUR = (70, 157, 236)
FONT_SIZE = 500

# -----------------------------------------------------------------------------

user_text = "Test"
usr_font = ImageFont.truetype(FONT, FONT_SIZE)

text_width, text_height = common.determine_text_size(user_text, usr_font)
output_size = (text_width + 20, text_height + 50)

# Create background
bg = Image.new('RGBA', output_size, common.WHITE)

# Create gradient
gradient = common.create_horizontal_gradient(LEFT_COLOUR, RIGHT_COLOUR, output_size)

# Apply gradient to text
common.mask_text(bg, user_text, usr_font, gradient, output_size)

# Resample and save output
common.resample_image(bg, output_size)
bg.save(OUTPUT_FILE)

# TODO - add weird bar thing
