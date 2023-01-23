# Import packages
import csv
import socket
import time

# Setup connection variables
host = "localhost"
port = 9999
address_tuple = (host,port)

socket_family = socket.AF_INET #IPV4
socket_type = socket.SOCK_DGRAM #UDP

# Create the socket opject
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Our data files
input_file = open("habitsample.csv", "r")
output_file = open("out9.txt", "w", newline='')

# Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
# use the built0in sorted() function to get them in chronological order
reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(reversed, delimiter=",")
# now create a writer
writer = csv.writer(output_file, delimiter=",")

for row in reader:
    Run,Type,Time,Distance,HR,Temp,Wind,Run2,Crosstrain,Strength,Sleep,RHR,HRV,Feeling,Stretch,Roll,Attitude,Water,Weight = row
    # Add a speed metric in miles per hour
    Speed = (float(Distance) / (int(Time) / 60))
    
    fstring_message = f"[{Run}, {Type}, {Time}, {Distance}, {HR}, {Temp}, {Wind}, {Run2},{Crosstrain},{Strength},{Sleep},{RHR},{HRV},{Feeling},{Stretch},{Roll},{Attitude},{Water},{Weight}]"
    MESSAGE = fstring_message.encode()

    sock.sendto(MESSAGE, address_tuple)
    writer.writerow([Run,Type,Time,Distance,Speed,HR,Temp,Wind,Run2,Crosstrain,Strength,Sleep,RHR,HRV,Feeling,Stretch,Roll,Attitude,Water,Weight])
    print (f"Sent line {row} on port {port}.")

    time.sleep(2)

output_file.close()
input_file.close()