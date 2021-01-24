import socket, time, datetime, logging

logging.basicConfig(filename="/logs/monitor.log", filemode="a", level=logging.DEBUG, format='%(asctime)s %(message)s')  


def internet(host="8.8.8.8", port=53, timeout=3):
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except socket.error as ex:
		return False

def statusChange(newstate):
	# push update
	print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " internet connection is " + ("up" if newstate else "down"))
	logging.info("internet connection is " + ("up" if newstate else "down"))



lastState = internet()

print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " uplink monitor started")
logging.info("uplink monitor started")
statusChange(lastState)

while True:
	currentState = internet()

	if currentState != lastState:
		# status changed, push update
		statusChange(currentState);
		lastState = currentState

	time.sleep(2)
