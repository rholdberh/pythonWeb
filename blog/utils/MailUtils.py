import os
from webProject.settings import BASE_DIR


def readMessageFromFile():
    print('READINF HILE')
    message = open(os.path.join(BASE_DIR, "resources/reportMail.txt"), mode="r", encoding="UTF-8")
    return message.read()


def getBodyMesage():
    return readMessageFromFile()


def getListOfRecepients():
    with open(os.path.join(BASE_DIR, "resources/emailList.txt"), mode="r", encoding="UTF-8") as ins:
        contents = [x.strip() for x in ins.readlines()]
        return contents

