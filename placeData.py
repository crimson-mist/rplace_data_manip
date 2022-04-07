#!/usr/bin/python3

if 0:
	results1 = ['2022-04-03 21:54:40.372 UTC,g8p3K/89V76AZkbh6KOIWmLfgBgGWllzJKCuSgugqZN270YfbsLGyefzqNpQMRsTBHSf3hFy4qoanyrurlTjBg==,#000000,"523,1699"\n', '2022-04-03 23:30:27.653 UTC,yIi+jjQ0NCoLTkqTExZR2xnRqsmtzI22ZJx+/D+bNI2wBMphDIypvRBwR52gFid8s5KgZmayo8SooWJjJFg2Og==,#FFD635,"523,1699"\n', '2022-04-04 02:13:44.98 UTC,/Qpd151Ec8i6oCbHy0+44JeeUZUKHETgsuu2RBm+ZXRCQJL4BS+gr7X7OKD/vudtbh1+Icev7qapKAu3sMAC4Q==,#DE107F,"523,1699"\n', '2022-04-04 05:44:25.06 UTC,XaU/okOQYzPeOLOS8zT4yFkTKLLdF6YI1yZMlxgcJUBLBlk4hdlie3o95K6OuT2H2AeKch1SFQwuWOmYB495Ug==,#7EED56,"523,1699"\n', '2022-04-04 23:42:09.613 UTC,kQSUQb7PRrZK0I6qTDzmB6Z/BqYYaX6ZTdeywPsFFmSR7S8j80fCNWby+fL/9RlEJVpMvMzhq9Umz5aY/ueE7w==,#FFFFFF,"523,1699"\n', '2022-04-04 21:06:09.603 UTC,t958h53OSbwSw1nIGsDHmxsTJ7csnAGk0wsjjmgcRw+wKsFS/rM+Qa5YcGWzTSWePn+nM9sPjiESwDNzKwqvIg==,#51E9F4,"523,1699"\n', '2022-04-04 21:06:36.261 UTC,R7i9ggFs8O13J0Z0uCjNHqko6okQ5+ZFy9k3uCLOsK1Wv/NniF7PDRrssdFo2/H/VNvQEBDZGWAgbLVbOnQiiw==,#7EED56,"523,1699"\n']
	results2 = ['2022-04-03 21:55:28.27 UTC,CAFMNcEK33vLNSibgnbvKE5dTbus+yRpMz7h8SImRwsxni7xYOl23VQKgN5He0Ef38R4WxDvN34pMDTAcURbLw==,#000000,"525,1699"\n', '2022-04-03 21:58:26.438 UTC,+dXYBlfHpdhcGxgNJEWe+mteIDULILeGdYWt4nAiqqPZf9EohsQw8VFY3s+pqOtOwiL6+R2F/fOCKt20c8yyrQ==,#FFA800,"525,1699"\n', '2022-04-03 21:58:50.076 UTC,NVRltFYGM3NWuQEODGANpMDXmMr+VnjeGCgMEgzRQqL+Wd18xDyOHhaAaODnyvNtZCCcMRXjPlgEpx7UQ7kzdQ==,#000000,"525,1699"\n', '2022-04-03 19:15:49.756 UTC,w2MJsEBwtCMLxZmSGDWzE8CLHKUE9Y5R6UJ9SxM2rZaNdSesKyqbJanHE/F66SScxy5FqVBOVNTbQN7WDAmIRg==,#7EED56,"525,1699"\n', '2022-04-03 23:31:53.153 UTC,t40gB3KGM/cBfK7pWlpCkiluqvSmMXzwWmrM6+NhTXwpl3r43HvBi6Ndo2XpKB0K0tDeR21a0wh96l2uE/txZA==,#FFD635,"525,1699"\n', '2022-04-04 02:16:35.64 UTC,VLpXFhsrdn8T+cYcn2jBh7TouZ+WopvuV+Cmvco+W9NM8zAl3UycN4O5/sS4AqT7c6byNIu0lpIIYfQ/D05PSw==,#DE107F,"525,1699"\n', '2022-04-04 02:23:20.409 UTC,pa7Sp+KPacaLtpXUFUh8SYGrSd0SsV3vPM2IXlimqnjIQFuRjDmmlB6C5qach3Jjr4yY/N1p3MuLsW/Fe6U8IQ==,#DE107F,"525,1699"\n', '2022-04-04 05:46:33.694 UTC,Rp71leVtFZfUR8H2V0FhibPUljnSlu3EdXAhLZ8uX2cKO8nPIbki3exFKHReLIGqtbsy53IGzwtgtF3ccGD6Nw==,#7EED56,"525,1699"\n', '2022-04-04 12:52:27.533 UTC,yQCI7c0+qBV02aXF0N0fV5MV6jHtVrbG9Ql5Dyf3IFGmVESswOwQrxTYfWETyu2QdhELkstR6MUrkUBTPm+xrQ==,#6D482F,"525,1699"\n', '2022-04-04 12:53:52.663 UTC,xYuMNvPbVeY+7yvMh7E3mFobwtxz7pwLXi5/wPKDqKGLBFmS08ZqMbKmunkhAZ5gk6jUJpt3BpqJ1ULRaY8bRw==,#7EED56,"525,1699"\n', '2022-04-04 23:48:41.611 UTC,/am1v5KlRbT3iXxBvhDqsnskUCHGUVHPjt5W4MPg2Dwv7iKHLDlZu+pMYEgz7mZs1cI9K9jEfWj0tu50sfEucQ==,#FFFFFF,"525,1699"\n', '2022-04-04 20:58:37.021 UTC,T0bI2SQ5ij253x282jpSjM4JmHpbyBv7L2vTLbeeDrtadSfGBwDU0PEXlUJLf46E22UyQAzg4nLEtYTXiWXwoQ==,#FF3881,"525,1699"\n', '2022-04-04 20:59:14.195 UTC,Rp71leVtFZfUR8H2V0FhibPUljnSlu3EdXAhLZ8uX2cKO8nPIbki3exFKHReLIGqtbsy53IGzwtgtF3ccGD6Nw==,#7EED56,"525,1699"\n']
else:
	f = open("2022_place_canvas_history.csv","rt")
	results1 = []
	i = 0

	for line in f:
		i = i + 1
		if i % 100000 == 0:
			print(i)
		# for j in range(3):
		# 	for k in range(3):
		# 		if "\"52" + str(j + 3) + ",169" + str(k + 6) + "\"" in line:
		# 			results1[j][k] = line
		# 			print(i, [520 + j, 1690 + k])
		if "2022-04-04 06:25" in line:
			print(1)
			if "\"512,1696\"" in line:
				print(2)
				results1.append(line)
	f.close();

print("Results 1")
for result in results1:
	print(result)


print("UserID Correlation:")
userIDs = []
for result in results1:
	userIDRegistered = False
	userID = result.split(",")[1]
	for registeredUserID in userIDs:
		if registeredUserID[0] == userID:
			registeredUserID[1] = registeredUserID[1] + 1
			userIDRegistered = True
			break
	if not userIDRegistered:
		userIDs.append([userID,1])
		userIDs = []

for uid in userIDs:
	print(uid)