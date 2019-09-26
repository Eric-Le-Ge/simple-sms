# simple-sms

Simple-SMS is a lightweight framework to send scheduled group text messages built with the aws boto3 library. 

## Requirements

* boto3 Library:

```
pip3 install boto3
```

* aws access key and secret key. You can obtain a keypair from the aws management console.

## Usage

Fill out configuration.json with aws access key and secret key as well as the message and recipient phone numbers. Then, execute the script with:

```
python3 sendsms.py configuration.txt
```

For scheduled messages, you may schedule the execution of the script on your machine via [cron](https://en.wikipedia.org/wiki/Cron):

```
crontab -e
```

Then, add the desired schedule to the file. For example, the below command sends a group text message every Wednesday 2PM UTC:

```
0 14 * * 3 python3 PATH_TO_REPOSITORY/simple-sms/sendsms.py configuration.txt
```
