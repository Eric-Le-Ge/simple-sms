from lib import sendsms
import json
import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print ("Usage: \n python3 sendsms.py configuration_file.json")
		exit()
	for file_name in sys.argv[1:]:
		with open(file_name, 'r') as f:
			data = json.loads(f.read())
		aws_access_key = data["aws_access_key"]
		aws_secret_access_key = data["aws_secret_access_key"]
		message = data["message"]
		recipients = data["recipients"]
		sendsms(aws_access_key, aws_secret_access_key, message, recipients)
