from PIL import Image
import numpy as np
global lim,RX,RY,names
#HAPPY BIRTHDAY BRO
lim = 25
RX = 800
RY = 1000
def main():
	#NOTE: this is SHOCKING code. pls kids dont code like this. maybe i'll clean this up one day
	cowboy = Image.open('cowboy.jpg')
	cowboy2 = cowboy.resize((lim,lim))
	avatar = Image.open('avatar.jpg')
	avatar2 = avatar.resize((lim,lim))
	igor = Image.open('igor.jpg')
	igor2 = igor.resize((lim,lim))
	minecraft = Image.open('minecraft.jpg')
	minecraft2 = minecraft.resize((lim,lim))
	rm = Image.open('rick-and-morty.jpg')
	rm2 = rm.resize((lim,lim))
	texas = Image.open('texas.jpg')
	texas2 = texas.resize((lim,lim))
	val = Image.open('valentino.jpg')
	val2 = val.resize((lim,lim))
	lil = Image.open('lillardap.jpg')
	lil2 = lil.resize((lim,lim))
	alex = Image.open('Alex.jpg')
	avgVals = np.array([[0, 0, 0], [0, 0, 0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
	avgVals[0] = find_avg(cowboy2)
	avgVals[1] = find_avg(avatar2)
	avgVals[2] = find_avg(igor2)
	avgVals[3] = find_avg(minecraft2)
	avgVals[4] = find_avg(rm2)
	avgVals[5] = find_avg(texas2)
	avgVals[6] = find_avg(val2)
	avgVals[7] = find_avg(lil2)
	alex2 = alex.resize((RX,RY))
	names = [cowboy2,igor2,texas2,minecraft2,rm2]
	#-------------------------------------
	find_avgAlex(alex2,avgVals,names)
	alex.show()
	print("HAPPY BIRTH OF ALEX!!!!!!!")

def find_avg(photo):
	data = np.asarray(photo)
	datacopy = np.copy(data)
	color_sum = [0,0,0]
	for xi in range(lim):
		for yi in range(lim):
			color_sum += datacopy[xi][yi]
	avgR = color_sum[0] / (lim*lim)
	avgG = color_sum[1] / (lim*lim)
	avgB = color_sum[2] / (lim*lim)
	#add a color overlay to the random image to make the big image 
	return [avgR,avgG,avgB]
def find_avgAlex(photo,avgVals,names):
	
	data = np.asarray(photo)
	datacopy = np.copy(data)
	avgVals = avgVals
	stepy = int(RY / lim)
	stepx = int(RX / lim)
	for x in range(stepx):
		for y in range(stepy):
			color_sum = [0,0,0]
			for xi in range(lim):
				for yi in range(lim):
					color_sum += datacopy[yi+y*lim][xi + x*lim]
			avgR = color_sum[0] / (lim*lim)
			avgG = color_sum[1] / (lim*lim)
			avgB = color_sum[2] / (lim*lim)	
			avg = [avgR,avgG,avgB]
			thr = 1			
			for i in range(5):
				if np.allclose(avgVals[i],avg,thr):
					paste_im = names[i + np.random.randint(-1,1)]
					paste_im2 = np.array(paste_im)
					paste_im2[:,:,0],paste_im2[:,:,1],paste_im2[:,:,2] = (avg[0],avg[1],avg[2])
					paste_im3 = Image.fromarray(paste_im2)
					paste_im4 = Image.blend(paste_im,paste_im3,0.6)
					photo.paste(paste_im4,(x*lim,y*lim))

	photo.show()
	photo.save("ALEX_MOSAIC.jpg")			
	return 


main()
