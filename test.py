from rembg import remove
from PIL import Image

input_path = '/Users/skosovan/Documents/dress2.jpeg'
output_path = '/Users/skosovan/Documents/dress2_wb.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
