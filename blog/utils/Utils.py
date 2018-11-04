import os
from webProject.settings import BASE_DIR


class Utils:

    def __init__(self):
        super(Utils)

    def readMessageFromFile(self):
        print('READINF HILE')
        file = open(os.path.join(BASE_DIR, "resources/reportMail.txt"), mode="r", encoding="UTF-8")
        message = file.read()
        file.closed
        return message

    def getBodyMesage(self):
        return self.readMessageFromFile()

    def getListOfRecepients(self):
        with open(os.path.join(BASE_DIR, "resources/emailList.txt"), mode="r", encoding="UTF-8") as ins:
            contents = [x.strip() for x in ins.readlines()]
        return contents
