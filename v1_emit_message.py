"""
    This program sends a message to a queue on the RabbitMQ server.

    Original Author: Denise Case
    Date: January 14, 2023
    Modified by: Kyle Hudson 31 Jan 2023

"""

# add imports at the beginning of the file
import pika

message = "This has taken me quite a while to get right"
# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user
print("[x] Sent", message)
# close the connection to the server
conn.close()
