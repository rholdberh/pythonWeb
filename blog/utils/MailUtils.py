import os
from webProject.settings import BASE_DIR


def readMessageFromFile():
    message = open(os.path.join(BASE_DIR, "resources/reportMail.txt"), mode="r", encoding="UTF-8")
    return message.read()


def getBodyMesage(data):
    message = readMessageFromFile()
    return message % (data)


def getListOfRecepients():
    print("dd")
