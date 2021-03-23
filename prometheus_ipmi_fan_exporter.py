# configuration
import socket #can be removed if local ip is set manually
LOCAL_IP = socket.gethostbyname(socket.gethostname())
PORT = 9101

import subprocess,re
class ipmi():
	def getFanSpeed():
		returnStr = ""

		rawSensors = str(subprocess.run(["ipmitool","sensor"],capture_output=True))

		def regexQuery(i):
				try:
						return re.search(i+"\ +\| ([0-9]+\.[0-9]+)\ +",rawSensors).group(1)
				except: 
						return "0"

		for i in re.findall("Fan..", rawSensors):
				returnStr += "py_fans{"+i+"} "+regexQuery(i)+"\n"
		return returnStr

import http.server
class requestHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):

		#response headers
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()

		self.wfile.write(bytes(ipmi.getFanSpeed(),"utf-8"))

http.server.HTTPServer((LOCAL_IP,PORT),requestHandler).serve_forever()
