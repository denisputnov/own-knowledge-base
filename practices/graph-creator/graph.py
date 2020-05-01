import PIL
from PIL import Image, ImageFont, ImageDraw


class UnexpectedDataFormat(Exception):
	pass

class IncorrectParameters(Exception):
	pass

def draw_graph(
	data,

	title_text=None,
	title_size=70,
	sub_title_text=None,
	sub_title_size=35,
	
	tile_color=(20, 20, 20),
	sub_title_color=(40, 40, 40),

	width=1000, 
	height=400,
	
	title_font='MullerMedium.ttf',
	sub_title_font='MullerRegular.ttf',
	watermark_font='MullerRegular.ttf',

	chart='column',
	color=(128, 140, 255),
	end_color=(87, 255, 146),
	chart_background_color=(240, 240, 240),
	background_color=(248, 248, 248),
	gradient=True,


	watermark_text=None,
	watermark_size=0):


	if sub_title_text is not None and title_text is None:
		raise IncorrectParameters

	if not isinstance(data, dict):
		raise UnexpectedDataFormat

	if title_font[-4:] != '.ttf':
		title_font += '.ttf'

	if sub_title_font[-4:] != '.ttf':
		sub_title_font += '.ttf'
	
	if title_text is not None:
		height += title_size
		title_font = ImageFont.truetype(title_font, title_size)
		title_width, title_heigth = title_font.getsize(title_text)
	else:
		title_width, title_heigth = 0, 0

	if sub_title_text is not None:
		height += sub_title_size
		sub_title_font = ImageFont.truetype(sub_title_font, sub_title_size)
		sub_title_width, sub_title_heigth = sub_title_font.getsize(sub_title_text)
	else: 
		sub_title_width, sub_title_heigth = 0, 0

	if watermark_text is not None:
		watermark_size = 20
		height += watermark_size
		watermark_font = ImageFont.truetype(watermark_font, watermark_size)
		watermark_width, watermark_heigth = watermark_font.getsize(watermark_text)
	else:
		watermark_width, watermark_heigth = 0, 0 

	img = Image.new('RGB', (width, height), background_color)
	draw = ImageDraw.Draw(img)

	if title_text is not None:
		draw.text(
			((width - title_width) / 2, 5), 
			title_text, font=title_font, fill=tile_color)

		if sub_title_text is None:
			draw.rectangle([20, 15 + title_heigth, width - 20, height - 15 - watermark_size], fill=chart_background_color)

		if sub_title_text is not None:
			draw.text(
				((width - sub_title_width) / 2, (5 + title_heigth + 5)), 
				sub_title_text, font=sub_title_font, fill=sub_title_color)

			draw.rectangle([20, 15 + title_heigth + sub_title_heigth, width - 20, height - 15 - watermark_size], fill=chart_background_color)

	if watermark_text is not None:
		draw.text(
			((width - watermark_width) / 2, (height - watermark_heigth - 5)), 
			watermark_text, font=watermark_font, fill=sub_title_color)

	if sub_title_text is None and title_text is None:
		draw.rectangle([20, 15 + title_heigth + sub_title_heigth, width - 20, height - 15 - watermark_size], fill=chart_background_color)

	dx = (width - 40) / len(data)
	dy = sum(data.values())/ len(data)
	maxy = max(data.values())
	
	values = list(data.values())
	max_value = max(values)
	keys = list(data.keys())

	x = 18
	if gradient:
		dr = int((color[0]-end_color[0])/len(data))
		dg = int((color[1]-end_color[1])/len(data))
		db = int((color[2]-end_color[2])/len(data))
		changes_list = [(dr, 0), (dg, 1), (db, 2)]
		for value in values:
			# (128, 140, 255) -> (67, 152, 101)
			color = list(color)
			color[0] -= dr 
			color[1] -= dg 
			color[2] -= db 
			color = tuple(color)
			draw.rectangle([5 + x, height - watermark_size - 15, x + dx, 20 + title_heigth + sub_title_heigth + ((1000 - 1000*((value/(max_value/100))/100)))/3], fill=color)
			x += dx
	else:
		for value in values:
			draw.rectangle([5 + x, height - watermark_size - 15, x + dx, 20 + title_heigth + sub_title_heigth + ((1000 - 1000*((value/(max_value/100))/100)))/3], fill=color)
			x += dx

	img.show()


if __name__ == '__main__':
	from random import randint
	data = dict()
	for i in range(randint(7, 60)):
		data[i] = randint(1000, 50000)
	print(data)

	draw_graph(data)
	print(len(data))