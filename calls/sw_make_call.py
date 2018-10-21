import os
from signalwire.rest import Client as signalwire_client
import logging
#write requests & responses from SignalWire to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/signalwire/python3/calls/logs/signalwire_calls.log',
                    filemode='a')

project = os.environ.get('SIGNALWIRE_API_PROJECT')
token = os.environ.get('SIGNALWIRE_API_TOKEN')
client = signalwire_client(project, token, signalwire_space_url = 'tornado.signalwire.com')

call = client.calls.create(
                              from_='+14153587900',
                              url='http://your-application.com/docs/voice.xml',
                              to='+16466796505'
                          )

#print list of all call properties to console, useful for learning info available you can work with?
print(call.account_sid)
print(call.annotation)
print(call.answered_by)
print(call.api_version)
print(call.caller_name)
print(call.date_created)
print(call.date_updated)
print(call.direction)
print(call.duration)
print(call.end_time)
print(call.forwarded_from)
print(call.from_)
print(call.from_formatted)
print(call.group_sid)
print(call.parent_call_sid)
print(call.phone_number_sid)
print(call.price)
print(call.price_unit)
print(call.sid)
print(call.start_time)
print(call.status)
print(call.subresource_uris)
print(call.to)
print(call.to_formatted)
print(call.uri)

#create variable for this call
cdr = (call.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/signalwire/python3/calls/logs/" + str( cdr ) + ".log", "a")
#write list of all call properties to above file...
f.write("Account SID : " + str(call.account_sid) + "\n")
f.write("Annotation : " + str(call.annotation) + "\n")
f.write("Answered By : " + str(call.answered_by) + "\n")
f.write("API Version : " + str(call.api_version) + "\n")
f.write("Caller Name : " + str(call.caller_name) + "\n")
f.write("Date Created : " + str(call.date_created) + "\n")
f.write("Date Updated : " + str(call.date_updated) + "\n")
f.write("Direction : " + str(call.direction) + "\n")
f.write("Duration : " + str(call.duration) + "\n")
f.write("End Time : " + str(call.end_time) + "\n")
f.write("Forwarded From : " + str(call.forwarded_from) + "\n")
f.write("From : " + str(call.from_) + "\n")
f.write("From Formatted : " + str(call.from_formatted + "\n"))
f.write("Group SID : " + str(call.group_sid) + "\n")
f.write("Parent Call SID : " + str(call.parent_call_sid) + "\n")
f.write("Phone Number SID : " + str(call.phone_number_sid) + "\n")
f.write("Price : " + str(call.price) + "\n")
f.write("Price Unit : " + str(call.price_unit) + "\n")
f.write("SID : " + str(call.sid) + "\n")
f.write("Start Time : " + str(call.start_time) + "\n")
f.write("Status : " + str(call.status) + "\n")
f.write("Subresource URIs : " + str(call.subresource_uris) + "\n")
f.write("To : " + str(call.to) + "\n")
f.write("To Formatted : " + str(call.to_formatted) + "\n")
f.write("URI : " + str(call.uri) + "\n")
f.close()