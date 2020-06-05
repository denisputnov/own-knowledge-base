import PIL
from PIL import Image, ImageFont, ImageDraw
import math

class UnexpectedDataFormat(Exception):
	pass

class IncorrectParameters(Exception):
	pass

class UnexpectedChart(Exception):
	pass

if __name__ == '__main__':
	print(PIL.__path__)

def draw_graph(
	data,

	title_text=None,
	title_size=70,
	sub_title_text=None,
	sub_title_size=35,
	
	tile_color=(20, 20, 20),
	sub_title_color=(40, 40, 40),

	width=2000, 
	height=800,
	
	title_font='MullerMedium.ttf',
	sub_title_font='MullerRegular.ttf',
	watermark_font='MullerRegular.ttf',

	chart='column',
	radius=10,
	line_width=10,

	color=(128, 140, 255),
	end_color=(87, 255, 146),
	chart_background_color=(240, 240, 240),
	background_color=(248, 248, 248),
	
	gradient=True,
	show_values=True,

	watermark_text=None,
	watermark_size=20):
	
	graph_height = height * 0.9
	start_height = height

	if sub_title_text is not None and title_text is None:
		raise IncorrectParameters

	if not isinstance(data, dict): 
		raise UnexpectedDataFormat

	if title_font[-4:] != '.ttf':
		title_font += '.ttf'

	if sub_title_font[-4:] != '.ttf':
		sub_title_font += '.ttf'

	if watermark_text is not None:
		height += watermark_size
		watermark_font = ImageFont.truetype(watermark_font, watermark_size)
		watermark_width, watermark_heigth = watermark_font.getsize(watermark_text)
	else:
		watermark_width, watermark_heigth = 0, 0 
	

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


	img = Image.new('RGB', (width, height), background_color)
	draw = ImageDraw.Draw(img)

	if title_text is not None:
		draw.text(
			((width - title_width) / 2, 5), 
			title_text, font=title_font, fill=tile_color)

		if sub_title_text is None:
			draw.rectangle([20, 15 + title_heigth, width - 20, height - 15 - watermark_size], fill=chart_background_color)

			for y in range(5):
				draw.line([40, title_heigth + sub_title_heigth + start_height/10 + y * height/4,  width - 40, title_heigth + sub_title_heigth + start_height/10 + y * height/4 ], fill=(230, 230, 230), width=2)

		if sub_title_text is not None:
			draw.text(
				((width - sub_title_width) / 2, (5 + title_heigth + 5)), 
				sub_title_text, font=sub_title_font, fill=sub_title_color)

			draw.rectangle([20, 15 + title_heigth + sub_title_heigth, width - 20, height - 15 - watermark_size], fill=chart_background_color)

			for y in range(5):
				draw.line([40, title_heigth + sub_title_heigth + start_height/10 + y * height/4,  width - 40, title_heigth + sub_title_heigth + start_height/10 + y * height/4 ], fill=(230, 230, 230), width=2)

	if watermark_text is not None:
		draw.text(
			((width - watermark_width) / 2, (height - watermark_heigth - 5)), 
			watermark_text, font=watermark_font, fill=sub_title_color)

	if sub_title_text is None and title_text is None:
		draw.rectangle([20, 15 + title_heigth + sub_title_heigth, width - 20, height - 15 - watermark_size], fill=chart_background_color)

		for y in range(5):
				draw.line([40, title_heigth + sub_title_heigth + start_height/10 + y * height/4,  width - 40, title_heigth + sub_title_heigth + start_height/10 + y * height/4 ], fill=(230, 230, 230), width=2)

	dx = (width - 40) / len(data)
	dy = sum(data.values())/ len(data)
	maxy = max(data.values())
	
	values = list(data.values())
	max_value = max(values)
	keys = list(data.keys())

	if chart.lower() == 'column':
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
				draw.rectangle([5 + x, height - watermark_size - 15, x + dx, 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(value/(max_value/100)/100)], fill=color)

				if show_values and value == values[0]:
					draw.text(
						((5 + x + dx)/2, (height - 18 - watermark_size/2)), 
						str(keys[0]), 
						font=ImageFont.truetype(sub_title_font, 30), fill=sub_title_color
						)

				if show_values and value == values[-1]:
					draw.text(
						((width - dx/2 - 37), (height - 18 - watermark_size/2)), 
						str(keys[-1]), 
						font=ImageFont.truetype(sub_title_font, 30), fill=sub_title_color
						)
					
				x += dx
		else:
			for value in values:
				draw.rectangle([5 + x, height - watermark_size - 15, x + dx, 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(value/(max_value/100)/100)], fill=color)
				
				if show_values and value == values[0]:
					draw.text(
						((5 + x + dx)/2, (height - 18 - watermark_size/2)), 
						str(keys[0]), 
						font=ImageFont.truetype(sub_title_font, 30), fill=sub_title_color
						)

				if show_values and value == values[-1]:
					draw.text(
						((width - dx/2 - 37), (height - 18 - watermark_size/2)), 
						str(keys[-1]), 
						font=ImageFont.truetype(sub_title_font, 30), fill=sub_title_color
						)

				x += dx
	elif chart.lower() == 'line':
		x = 18 + dx/2
		

		draw.ellipse([x - radius, 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(values[0]/(max_value/100)/100) - radius, x + radius, 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(values[0]/(max_value/100)/100) + radius], fill=color)

		beforex = x
		beforey = 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(values[0]/(max_value/100)/100)

		for value in values[1:]:
			i = 2
			draw.ellipse([ x + dx - radius, 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(value/(max_value/100)/100) - radius, x + dx + radius, 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(value/(max_value/100)/100) + radius], fill=color, width=line_width)
			draw.line([ x + dx, 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(value/(max_value/100)/100), beforex, beforey], fill=color, width=5)
			x += dx
			beforex = x 
			beforey = 20 + title_heigth + sub_title_heigth + graph_height - graph_height*(value/(max_value/100)/100)

	else:
		raise UnexpectedChart

	if __name__ == '__main__':
		img.show()


if __name__ == '__main__':
	from random import randint
	data = {1: 114, 2: 147, 3: 199, 4: 253, 5: 306, 6: 367, 7: 438, 8: 495, 9: 658, 10: 840, 11: 1036, 12: 1246, 13: 1534, 14: 1836, 15: 2337, 16: 2777, 17: 3548, 18: 4149, 19: 4731, 20: 5389, 21: 6343, 22: 7497, 23: 8672, 24: 10131, 25: 11917, 26: 13584, 27: 15770, 28: 18328, 29: 21102, 30: 24490, 31: 27938, 32: 32008, 33: 36793, 34: 42853, 35: 47121, 36: 52763, 37: 57999, 38: 62773, 39: 68622, 40: 74588, 41: 80949, 42: 87147, 43: 93558, 44: 99399, 45: 106498, 46: 114431, 47: 124054, 48: 134687, 49: 145268, 50: 155370}
	# k = 1
	# for i in range(randint(7,60)):
	# 	data[i] = randint(1000, 50000)
		# data[i] = i * k
		# k *= 1.1

	print(data)

	draw_graph(data, title_text='Заголовок', watermark_text='Telegram | @pyInfoParserBot')
	print(len(data))