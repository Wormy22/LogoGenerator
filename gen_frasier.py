from PIL import Image, ImageFont, ImageDraw

import common

FONT = "resources/florentine regular.ttf"

TOP_COLOUR = (255, 199, 0)
BOTTOM_COLOUR = (254, 254, 200)

user_text = "Test".upper()
# Todo - Make first bigger

# Create temporary image to determine length of text
temp_image = Image.new("RGBA", (1, 1), (0, 0, 0))
usr_font = ImageFont.truetype(FONT, 500)

text_width, text_height = ImageDraw.Draw(temp_image).textsize(user_text, usr_font)
output_size = (text_width + 20, text_height + 30)

# Create background
bg = Image.new('RGBA', output_size, (0, 0, 0))

# Create gradient
gradient = common.create_vertical_gradient(TOP_COLOUR, BOTTOM_COLOUR, output_size)

# Apply gradient to text
common.mask_text(bg, user_text, usr_font, gradient, output_size)

# Save output
common.resample_image(bg, output_size)
bg.save('frasier_out.png', 'PNG')

# TODO - skyline
