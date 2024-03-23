import io
import sys

sys.path.append(r"C:\Users\winte\source\repos\hackathon")

from app.map.MapData import GeoMap
from app.parse.DataParsers import Parser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtWebEngineWidgets import 


class HMapWidget(QWebEngineView):

    def __init__(self, parent=None) -> None:
        super(QWebEngineView, HMapWidget).__init__(parent)
        self.__mMapBytes = io.BytesIO()
        self.__mMapData = GeoMap()
        self.__init_map()

    def __init_map(self):
        rDataParser = Parser("data/realty.csv", ",", True)
        rData = rDataParser.parse()

        pDataParser = Parser("data/poi.csv", "|", False)
        pData = pDataParser.parse()

        self.__mMapData.initFeatureGroups(pData, rData)
        self.__mMapData.getMap().save(self.__mMapBytes, close_file="False")

        self.setHtml(self.__mMapBytes.getvalue().decode())
        self.resize(1280, 720)