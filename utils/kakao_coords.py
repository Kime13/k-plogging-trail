import requests
import os
from dotenv import load_dotenv

load_dotenv()

KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

def get_coords(place_name: str, region: str = "제주") -> list:
    """장소명으로 정확한 좌표 조회"""
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {
        "query": f"{region} {place_name}",
        "size": 1
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if data["documents"]:
            place = data["documents"][0]
            return [float(place["y"]), float(place["x"])]  # [lat, lon]
        return None
    except Exception as e:
        print(f"좌표 조회 실패: {place_name} - {e}")
        return None

def build_highlight_coords(courses: list) -> dict:
    """전체 코스 하이라이트 좌표 자동 생성"""
    coords = {}
    for course in courses:
        for highlight in course["highlights_en"]:
            if highlight not in coords:
                result = get_coords(highlight)
                if result:
                    coords[highlight] = result
                    print(f"✅ {highlight}: {result}")
                else:
                    print(f"❌ {highlight}: 좌표 없음")
    return coords

if __name__ == "__main__":
    from jeju_olle import JEJU_OLLE_COURSES
    coords = build_highlight_coords(JEJU_OLLE_COURSES)
    print("\n=== 최종 좌표 ===")
    for k, v in coords.items():
        print(f'"{k}": {v},')