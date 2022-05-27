import base64
import io
import PIL.Image
import os.path

def image_from_file(filename, size):
		img = PIL.Image.open(filename)
		cur_width, cur_height = img.size
		new_width, new_height = size

		scale = min(new_height/cur_height, new_width/cur_width)
		img = img.resize((int(cur_width*scale), int(cur_height*scale)))
		return img
	    
def image_from_array(data):
    return PIL.Image.fromarray(data)

def image_to_bytes(img):
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()