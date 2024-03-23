import sys
import folium
sys.path.append(r"C:\Users\winte\source\repos\hackathon")

from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon
from folium.features import CircleMarker
from app.parse.DataParsers import Parser


class GeoCoord2D:

    def __init__(self, anLat:int, anLon:int) -> None:
        self.mnLat = anLat
        self.mnLon = anLon


class GeoMap:

    def __init__(self) -> None:
        # 59.936725612333184, 30.38607094222062 - SPB X | Y
        self.__mSPBMap = folium.Map(
            location=[59.936725612333184, 30.38607094222062],
            zoom_start=12
        )

        self.__mMapPOIFG = folium.FeatureGroup()
        self.__mMapRealtyFG = folium.FeatureGroup()

    def __initMapPOIFG(self, adPOIDict:dict={}) -> bool:
        print("Init POI...")

        for id in adPOIDict:
            data = adPOIDict.get(id)
            px = data.get("lat")
            py = data.get("lon")

            self.__mMapPOIFG.add_child(
                CircleMarker(
                    [px, py], radius=2,
                    color="red", fill_color="Red"
                )
            )

        return True

    def __initMapRealtyFG(self, adRealtyDict:dict={}) -> bool:
        print("Init Realty...")

        for id in adRealtyDict:
            data = adRealtyDict.get(id)
            px = data.get("point_x")
            py = data.get("point_y")

            self.__mMapRealtyFG.add_child(
                CircleMarker(
                    [py, px], radius=5,
                    color="blue", fill_color="Blue"
                )
            )

        return True

    def initFeatureGroups(self, adPOIDict:dict={}, adRealtyDict:dict={}) -> bool:
        self.__initMapPOIFG(adPOIDict)
        self.__initMapRealtyFG(adRealtyDict)

        self.__mSPBMap.add_child(self.__mMapPOIFG)
        self.__mSPBMap.add_child(self.__mMapRealtyFG)

        return True
    
    def getMap(self) -> folium.Map:
        return self.__mSPBMap

    def showMapInBrowser(self):
        self.__mSPBMap.show_in_browser()
