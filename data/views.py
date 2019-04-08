from django.shortcuts import render
from django.http import HttpResponse
import cv2
import numpy as np
import matplotlib.pyplot as plt

import io
from matplotlib import figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
# Create your views here.

def data0(request):
	img = cv2.imread('data/brick.jpg')
	gray0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	corners0 = cv2.goodFeaturesToTrack(gray0,15,0.01,5)
	corners1 = np.int0(corners0)

	for i in corners1:
		x,y = i.ravel()
		cv2.circle(img,(x,y),3,255,-1)
	plt.imshow(img)
	f = figure.Figure()
	FigureCanvasAgg(f)
	buf = io.BytesIO()
	plt.savefig(buf,format = 'png')
	plt.close(f)
	response = HttpResponse(buf.getvalue(),content_type = 'image/png')
	return response