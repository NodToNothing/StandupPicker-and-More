import random
import os
from PIL import Image, ImageDraw, ImageFont
import colorsys

# List of names
names = ["Theo", "Ryker", "Clement", "Teddi", "Scott", "Andy", "Matt", "Eddie", "Tatiana", "Kathleen"]
chosen_name = random.choice(names)

# Attempt to load a font from common system paths
possible_fonts = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
    "/Library/Fonts/Arial.ttf",                              # macOS
    "C:\\Windows\\Fonts\\arial.ttf"                          # Windows
]
available_fonts = [f for f in possible_fonts if os.path.exists(f)]
font_path = random.choice(available_fonts) if available_fonts else None

# Font settings
font_size = 100
font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()

# Measure text bounding box
bbox = font.getbbox(chosen_name)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Create image with padding
padding = 20
img = Image.new('RGB', (text_width + 2 * padding, text_height + 2 * padding), color=(30, 30, 30))
draw = ImageDraw.Draw(img)

# Generate rainbow colors
def rainbow_colors(n):
    return [
        tuple(int(c * 255) for c in colorsys.hsv_to_rgb(i / n, 1.0, 1.0))
        for i in range(n)
    ]

colors = rainbow_colors(len(chosen_name))

# Draw each character individually with different colors
x = padding
y = padding - bbox[1]  # Adjust baseline
for i, char in enumerate(chosen_name):
    char_width = font.getlength(char)
    draw.text((x, y), char, font=font, fill=colors[i])
    x += char_width

# Show the result
img.show()
# img.save("random_name.png")
