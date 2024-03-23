import csv


class Parser:

    '''
    Geodata csv parser
    '''

    def __init__ (self, asFilePath, asSeparator=",", abStringHeaders=False) -> None:
        self.msFilePath = asFilePath
        self.msSeparator = asSeparator
        self.mbStringHeaders = abStringHeaders
        self.msFile = open(self.msFilePath, "r+", encoding="utf-8", newline='')
        self.mnShift = 0
        self.maHeaders = []
        self.mdData = {}

        self.__readHeaders()

    def __readHeaders(self) -> None:
        if not self.msFile:
            raise Exception("Files doesn't exists")
        headers = self.msFile.readline()
        if self.mbStringHeaders:
            headers = headers.replace("\"", '')
        headers = headers.strip().split(self.msSeparator)

        if headers[0] == "":
            self.mnShift = 1

        self.maHeaders = headers

    def getHeaders(self) -> list:
        return self.maHeaders

    def parse(self) -> dict:
        csvdata = csv.reader(self.msFile, delimiter=self.msSeparator, quotechar="\"")

        for data in csvdata:
            innerData = {}
            for i in range(1 + self.mnShift, len(data)):
                innerData[self.maHeaders[i]] = data[i]
            self.mdData[data[0 + self.mnShift]] = innerData

        return self.mdData
