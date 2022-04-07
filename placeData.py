#!/usr/bin/python3

if 0:
	final_pixels = ['2022-04-03 21:54:40.372 UTC,g8p3K/89V76AZkbh6KOIWmLfgBgGWllzJKCuSgugqZN270YfbsLGyefzqNpQMRsTBHSf3hFy4qoanyrurlTjBg==,#000000,"523,1699"\n', '2022-04-03 23:30:27.653 UTC,yIi+jjQ0NCoLTkqTExZR2xnRqsmtzI22ZJx+/D+bNI2wBMphDIypvRBwR52gFid8s5KgZmayo8SooWJjJFg2Og==,#FFD635,"523,1699"\n', '2022-04-04 02:13:44.98 UTC,/Qpd151Ec8i6oCbHy0+44JeeUZUKHETgsuu2RBm+ZXRCQJL4BS+gr7X7OKD/vudtbh1+Icev7qapKAu3sMAC4Q==,#DE107F,"523,1699"\n', '2022-04-04 05:44:25.06 UTC,XaU/okOQYzPeOLOS8zT4yFkTKLLdF6YI1yZMlxgcJUBLBlk4hdlie3o95K6OuT2H2AeKch1SFQwuWOmYB495Ug==,#7EED56,"523,1699"\n', '2022-04-04 23:42:09.613 UTC,kQSUQb7PRrZK0I6qTDzmB6Z/BqYYaX6ZTdeywPsFFmSR7S8j80fCNWby+fL/9RlEJVpMvMzhq9Umz5aY/ueE7w==,#FFFFFF,"523,1699"\n', '2022-04-04 21:06:09.603 UTC,t958h53OSbwSw1nIGsDHmxsTJ7csnAGk0wsjjmgcRw+wKsFS/rM+Qa5YcGWzTSWePn+nM9sPjiESwDNzKwqvIg==,#51E9F4,"523,1699"\n', '2022-04-04 21:06:36.261 UTC,R7i9ggFs8O13J0Z0uCjNHqko6okQ5+ZFy9k3uCLOsK1Wv/NniF7PDRrssdFo2/H/VNvQEBDZGWAgbLVbOnQiiw==,#7EED56,"523,1699"\n']
else:
	f = open("2022_place_canvas_history.csv","rt")
	f.readline()
	final_pixels = [[0 for j in range(2000)]
	for i in range(2000)]
	i = 0

	for line in f:
		i = i + 1
		if i % 100000 == 0:
			print(i)

		# Get pixel as x and y values
		pxl = line.split("\"")[1]
		x = int(pxl.split(",")[0])
		y = int(pxl.split(",")[1])

		final_pixels[x][y] = line
		
	f.close();

print("Results 1")
f = open("final_pixels.csv","w")
for i in range(2000):
	for j in range(2000):
		f.write(str(final_pixels[i][j]))
f.close()