from matplotlib.pyplot import savefig, plot, legend, title, xticks
import csv
import numpy as np
	
def readcsv(filename):
	ifile = open(filename, "rU")
	reader = csv.reader(ifile, delimiter=";")
	
	x = []
	y = []
	
	for row in reader:
		x.append(float(row[0]))
		y.append(abs(float(row[1])))
		
	ifile.close()
	
	return x,y
	
	
basedir = "plots/"
plotname = ""
extension = ".png"

t = ""
legends = []
files = []

for i in xrange(len(files)):
	x, y  = readcsv(files[i])
	plot(x, y, label=legends[i])

title(t)
legend()
savefig(basedir + plotname + extension)