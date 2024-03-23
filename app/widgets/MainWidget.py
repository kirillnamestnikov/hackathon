import io

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

from app.map.MapData import GeoMap
from app.parse.DataParsers import Parser

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import sip


class HMainWIndow(QMainWindow):

    def __init__(self, aParent=None) -> None:
        super(QMainWindow, HMainWIndow).__init__(self, aParent)
        self.__mMapWidget = QWebEngineView()

        self.resize(1280, 720)
        self.setCentralWidget(self.__mMapWidget)

        self.__mMapBytes = io.BytesIO()
        self.__mMapData = GeoMap()
        self.__init_map()

    def __init_map(self):
        rDataParser = Parser("data/realty.csv", ",", True)
        rData = rDataParser.parse()

        pDataParser = Parser("data/poi.csv", "|", False)
        pData = pDataParser.parse()

        self.__mMapData.initFeatureGroups(pData, rData)
        self.__mMapData.getMap().save(self.__mMapBytes, close_file=False)
        self.__mMapWidget.setHtml(self.__mMapBytes.getvalue().decode())
        self.__mMapWidget.resize(1280, 720)
        self.__mMapWidget.show()