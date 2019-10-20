import cbpro, time
class myWebsocketClient(cbpro.WebsocketClient):
    def on_open(self, config):
        """

        :return:
        """

        self.url = config["url"]
        self.products = config["products"]

    def on_message(self, msg):
        """

        :param msg:
        :return:
        """

        # check message timestamp and append it to dict for the hour of message
        # count messages for the hour and log it into log file
        # need access to mongodb here
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        """

        :return:
        """

        # closing the connection
        print("-- Goodbye! --")

wsClient = myWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products)
while (wsClient.message_count < 500):
    print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
    time.sleep(1)
wsClient.close()