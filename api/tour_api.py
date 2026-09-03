import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TOUR_API_KEY")
BASE_URL = "https://apis.data.go.kr/B551011/KorService2"

def get_nearby_attractions(lat, lon, radius=3000, content_type=12):
    """위치 기반 관광지 조회"""
    url = f"{BASE_URL}/locationBasedList2"
    params = {
        "serviceKey": API_KEY,
        "numOfRows": 5,
        "pageNo": 1,
        "MobileOS": "ETC",
        "MobileApp": "KPloggingTrail",
        "arrange": "E",
        "contentTypeId": content_type,
        "mapX": lon,
        "mapY": lat,
        "radius": radius,
        "_type": "json"
    }
    try:
        response = requests.get(url, params=params, timeout=3)
        data = response.json()
        items = data["response"]["body"]["items"]["item"]
        return items if isinstance(items, list) else [items]
    except:
        return []

def get_nearby_restaurants(lat, lon, radius=3000):
    """주변 음식점 조회 (contentTypeId=39)"""
    return get_nearby_attractions(lat, lon, radius, content_type=39)

def get_nearby_accommodations(lat, lon, radius=3000):
    """주변 숙박 조회 (contentTypeId=32)"""
    return get_nearby_attractions(lat, lon, radius, content_type=32)

def format_place(place: dict) -> dict:
    """TourAPI 데이터 정제"""
    return {
        "title": place.get("title", ""),
        "addr": place.get("addr1", ""),
        "tel": place.get("tel", ""),
        "image": place.get("firstimage", ""),
        "lat": place.get("mapy", ""),
        "lon": place.get("mapx", ""),
        "dist": round(float(place.get("dist", 0)) / 1000, 1),
    }