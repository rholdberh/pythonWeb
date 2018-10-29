import os
from webProject.settings import BASE_DIR


def readMessageFromFile():
    message = open(os.path.join(BASE_DIR, "resources/reportMail.txt"), mode="r", encoding="UTF-8")
    return message.read()


def getBodyMesage(data):
    return readMessageFromFile()


def getListOfRecepients():
    with open("resources/emailList.txt", "r") as ins:
        contents = [x.strip() for x in ins.readlines()]
        return contents
