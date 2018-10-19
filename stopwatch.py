import time

print('Press ENTER to start. Press ENTER to record a lap. Press Ctrl-D to quit.')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

try :
	while True :
		input()
		lapTine=round(time.time() - lastTime, 2)
		totalTime=round(time.time() - startTime ,2)
		print('Lap #%s: %s' %(lapNum, totalTime))
		print('Time between Lap #%s and Lap #%s: %s' %(lapNum-1, lapNum, lapTine), end='')
		print('    ')
		lapNum+=1;
		lastTime=time.time()
except KeyboardInterrupt :
	print('\nDone')
