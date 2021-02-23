from pythonping import ping
import time
import telebot2
timestart = time.time()
li = ["192.168.0.1", "www.google.com", "8.8.8.8", "192.168.1.1"]


def run(hosts):
    while True:
        try :
            for host in hosts:
                x = ping(host, verbose=True, count=4)
                print(x.packet_loss)
                print(x.packets_lost)
                text = "the loss {}% for host is {}".format(x.packets_lost*100, host)
                print(text)
                if x.packets_lost > 0.05:
                    telebot2.bot.send_message(chat_id= -508787758, text=text)
            return 0
        except KeyboardInterrupt:
            exit()


if __name__ == '__main__':
    starttime = time.time()
    run(li)
    print(time.time()-starttime)