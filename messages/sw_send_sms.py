import os
from signalwire.rest import Client as signalwire_client
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/signalwire/python3/messages/logs/signalwire_sms.log',
                    filemode='a')

project = os.environ.get('SIGNALWIRE_API_PROJECT')
token = os.environ.get('SIGNALWIRE_API_TOKEN')
client = signalwire_client(project, token, signalwire_space_url = 'tornado.signalwire.com')


message = client.messages.create(
                              from_='+14153587900',
                              body='12:26 test',
                              to='+16466796505'
                          )

#print list of all message properties to console, useful for learning info available you can work with?
print(message.account_sid)
print(message.api_version)
print(message.body)
print(message.date_created)
print(message.date_sent)
print(message.date_updated)
print(message.direction)
print(message.error_code)
print(message.error_message)
print(message.from_)
print(message.messaging_service_sid)
print(message.num_media)
print(message.num_segments)
print(message.price)
print(message.price_unit)
print(message.sid)
print(message.status)
print(message.subresource_uris)
print(message.to)
print(message.uri)

#create variable for this message
cdr = (message.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/signalwire/python3/messages/logs/" + str( cdr ) + ".log", "a")
#write list of all message properties to above file...
f.write("Account SID : " + str(message.account_sid) + "\n")
f.write("API Version : " + str(message.api_version) + "\n")
f.write("Body : " + str(message.body) + "\n")
f.write("Date Created : " + str(message.date_created) + "\n")
f.write("Date Sent : " + str(message.date_sent) + "\n")
f.write("Date Updated : " + str(message.date_updated) + "\n")
f.write("Direction : " + str(message.direction) + "\n")
f.write("Error Code : " + str(message.error_code) + "\n")
f.write("Error Message : " + str(message.error_message) + "\n")
f.write("From : " + str(message.from_) + "\n")
f.write("Messaging SID : " + str(message.messaging_service_sid) + "\n")
f.write("Number of Media Files : " + str(message.num_media) + "\n")
f.write("Number of Segments : " + str(message.num_segments) + "\n")
f.write("Price : " + str(message.price) + "\n")
f.write("Price Unit : " + str(message.price_unit) + "\n")
f.write("SID : " + str(message.sid) + "\n")
f.write("Status : " + str(message.status) + "\n")
f.write("Subresource URIs : " + str(message.subresource_uris) + "\n")
f.write("To : " + str(message.to) + "\n")
f.write("URI : " + str(message.uri) + "\n")
f.close()