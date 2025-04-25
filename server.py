import time
import socket
import base64
import threading

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.all_client = [] # Создали список всех клиентов

        # Запускаем прослушивание соединений
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 протокол, tcp
        self.server.bind((self.ip, self.port)) # Начинаем прослшивание по определенному ip-порту
        self.server.listen(0) # Сервер модет прослушивать сколько угодно клиентов
        threading.Thread(target=self.connect_handler).start() # Запускаем поток, чтобы отслеживать новые соединения
        print("Сервер запущен")


    def connect_handler(self):
        while True:
            client, adress = self.server.accept()
            if client not in self.all_client:
                self.all_client.append(client)
                threading.Thread(target=self.message_handler, args=[client]).start()
                client.send("Успешное подключение к чату!".encode('utc-8'))
            time.sleep()

    def message_handler(self, client_socket):
        while True:
            message = client_socket.recv[1024]
            
            #---------------------------------
            print(message)
            #---------------------------------

            if message == b'exit':
                self.all_client.remove[client_socket]
                break
            
            for client in self.all_client:
                if client != client_socket:
                    client.send(message)
            time.sleep(1)

myserver = Server('127.0.0.1', 5555)