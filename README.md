# simple-sms

Simple-SMS is a lightweight framework to send scheduled group text messages built with the aws boto3 library. 

## requirements

* boto3 Library:

```
pip3 install boto3
```

* aws access key and secret key. You can obtain a keypair from the aws management console.

## usage

Fill out configuration.json with aws access key and secret key as well as the message and recipient phone numbers. Then, execute the script with:

```
python3 sendsms.py configuration.txt
```
