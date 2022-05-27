import PySimpleGUI as sg
import os.path
import PIL.Image
import io
import base64
import numpy as np
from numpy import asarray
import math

numpydata = []

def convert_to_bytes(file_or_bytes, size):
    global numpydata
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    new_width, new_height = size

    scale = min(new_height/cur_height, new_width/cur_width)
    img = img.resize((int(cur_width*scale), int(cur_height*scale)))
    numpydata = asarray(img)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

def convert_to_bytes2(data):
    img = PIL.Image.fromarray(data)
    img.save('testrgb.png')
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

left_col = [[sg.Text('Path'), sg.In(size=(25,1), enable_events=True ,key='-FILE_PATH-'), sg.FileBrowse(file_types=(("AA AA", "*.jpg"), ))],
			[sg.Text(size=(40,1), key='-ITER-')]]

images_col = [[sg.Text('You choose from the list:')],
              [sg.Text(size=(40,1), key='-TOUT-')],
              [sg.Image(key='-IMAGE-')]]

images_col1 = [[sg.Text('Algorithm output:')],
              [sg.Text(size=(40,1), key='-TOUT1-')],
              [sg.Image(key='-IMAGE1-')]]

layout = [[sg.Column(left_col, element_justification='c'), sg.VSeperator(), sg.Column(images_col, element_justification='c'), sg.VSeperator(), sg.Column(images_col1, element_justification='c')]]

window = sg.Window('Multiple Format Image Viewer', layout).Finalize()
window.Maximize()

generation = []

def init(shape):
	global generation
	for i in range(10):
		generation.append(np.random.randint(0,256,shape,dtype=np.uint8))

def loss(target, pred):
	diff = pred - target
	differences_squared = diff ** 2
	mean_diff = differences_squared.mean()
	return mean_diff

def gener_son(parent):
	son = np.copy(parent)
	for i in range(np.random.randint(1,20)):
		#son[np.random.randint(parent.shape[0])][np.random.randint(parent.shape[1])][np.random.randint(parent.shape[2])] = np.random.randint(0,256)
		radius = np.random.randint(min(parent.shape[0] / 20, parent.shape[1] / 20))
		x = np.random.randint(parent.shape[0])
		y = np.random.randint(parent.shape[1])
		rgb = [np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)]
		for i in range (max(0, x - radius), min(parent.shape[0], x + radius)):
			for j in range (max(0, y - radius), min(parent.shape[1], y + radius)):
				son[i][j] = rgb
	return son

def make_gen():
	global generation
	for i in range(4):
		generation[2+i] = gener_son(generation[0])
		generation[6+i] = gener_son(generation[1])

def loss_sort(target):
	global generation
	losses = []
	for curr in range(len(generation)):
		losses.append([curr, loss(target/256, generation[curr]/256)])
	losses.sort(key = lambda x: x[1])
	print(losses[0][1])
	new_gen = []
	for i in losses:
		new_gen.append(generation[i[0]])
	generation = new_gen

running = False
iter = 0

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-FILE_PATH-':
        try:
            filename = values['-FILE_PATH-']
            window['-TOUT-'].update(filename)
            window['-TOUT1-'].update(filename)
            size = window.size[0]/2.5, window.size[1]/2.5
            dat = convert_to_bytes(filename, size)
            window['-IMAGE-'].update(data=dat)
            init(numpydata.shape)
            running = True
        except Exception as E:
            print(f'** Error {E} **')
            pass
    if running:
    	make_gen()
    	loss_sort(numpydata)
    	window['-IMAGE1-'].update(data=convert_to_bytes2(generation[0]))
    	iter = iter + 1
    	window['-ITER-'].update(iter)

window.close()