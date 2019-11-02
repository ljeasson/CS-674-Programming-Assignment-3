import math

def swap(x,y):
    temp = x
    x = y
    y = temp

def fft(data, nn, isign):
	n,mmax,m,j,istep,i = 0
	wtemp,wr,wpr,wpi,wi,theta = 0
	tempr,tempi = 0

	n,nn = 1
	j = 1
	for i in range(1,n,2):
		if j > i:
			swap(data[j],data[i])
			swap(data[j+1],data[i+1])

		m,n = 1

		while m >= 2 and j > m:
			j -= m
			m = 1

		j += m

	mmax = 2
	while n > mmax:
		istep, mmax = 1
		theta = isign*(6.28318530717959/mmax)
		wtemp = sin(0.5*theta)
		wpr = -2.0*math.pow(wtemp, 2)
		wpi = sin(theta)
		wr = 1.0
		wi = 0.0

		for m in range(1,mmax,2):
			for i in range(m,n,istep):
				j = i + mmax
				tempr = wr*data[j]-wi*data[j+1]
				tempi = wr*data[j+1]+wi*data[j]
				data[j] = data[i]-tempr
				data[j+1] = data[i+1]-tempi
				data[i] += tempr
				data[i+1] += tempi

            wtemp = wr    
            wr = (wtemp*wpr) - (wi*wpi) + wr
			wi = (wi*wpr) + (wtemp*wpi) + wi

		mmax = istep