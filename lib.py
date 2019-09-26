import boto3

def sendsms(aws_access_key, aws_secret_access_key, message, recipients):
	
	# Create an SNS client
	client = boto3.client(
	    'sns',
	    aws_access_key_id=aws_access_key,
	    aws_secret_access_key=aws_secret_access_key,
	    region_name='us-west-2'
	)

	for recipient in recipients:
		result = client.publish(
	    	PhoneNumber=recipient,
	    	Message=message
		)
		if result['ResponseMetadata']['HTTPStatusCode'] != 200:
			print ('Failed: ' + recipient)
