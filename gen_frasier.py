from PIL import Image, ImageFont

import common

# TODO - document

# -----------------------------------------------------------------------------

FONT = "resources/florentine regular.ttf"
OUTPUT_FILE = 'frasier_out.png'

TOP_COLOUR = (255, 199, 0)
BOTTOM_COLOUR = (254, 254, 200)
FONT_SIZE = 500

# -----------------------------------------------------------------------------

user_text = "altran".upper()
usr_font = ImageFont.truetype(FONT, FONT_SIZE)

# Todo - Make first bigger

text_width, text_height = common.determine_text_size(user_text, usr_font)
output_size = (text_width + 20, text_height + 30)

# Create background
bg = Image.new('RGBA', output_size, common.BLACK)

# Create gradient
gradient = common.create_vertical_gradient(TOP_COLOUR, BOTTOM_COLOUR, output_size)

# Apply gradient to text
common.mask_text(bg, user_text, usr_font, gradient, output_size)

# Save output
common.resample_image(bg, output_size)
bg.save(OUTPUT_FILE)

# TODO - skyline
