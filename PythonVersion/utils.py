import base64
import io
import PIL.Image
import os.path
import time

def time_as_int():
    return int(round(time.time() * 100))


def image_from_file(filename, max_size):
		img = PIL.Image.open(filename)
		cur_width, cur_height = img.size
		max__width, max_height = max_size
		scale = 1.0
		if cur_width > max__width:
			scale = max__width/cur_width
		if cur_height > max_height:
			scale = min(scale, max_height/cur_height)
		if scale != 1.0:
			img = img.resize((int(cur_width*scale), int(cur_height*scale)))
		return img
	    
def image_from_array(data):
    return PIL.Image.fromarray(data)

def image_to_bytes(img):
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()