import requests

def get_walking_route(coords: list) -> list:
    """
    OSRM 무료 API로 실제 도보 경로 좌표 조회
    coords: [[lat, lon], [lat, lon], ...]
    returns: [[lat, lon], ...] 경로 좌표 리스트
    """
    if len(coords) < 2:
        return coords

    # OSRM은 lon,lat 순서
    waypoints = ";".join([f"{lon},{lat}" for lat, lon in coords])
    url = f"https://router.project-osrm.org/route/v1/foot/{waypoints}"
    params = {
        "overview": "full",
        "geometries": "geojson"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        if data.get("code") == "Ok":
            # OSRM은 [lon, lat] 반환 → [lat, lon]으로 변환
            route_coords = data["routes"][0]["geometry"]["coordinates"]
            return [[lat, lon] for lon, lat in route_coords]
    except Exception as e:
        print(f"OSRM 경로 조회 실패: {e}")

    return coords  # 실패 시 원래 좌표 반환