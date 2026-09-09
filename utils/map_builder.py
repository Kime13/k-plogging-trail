import folium
import logging
from api.tour_api import format_place

logger = logging.getLogger(__name__)

def build_course_map(course, highlight_coords):
    """Builds a Folium map showing the course start and highlight points."""
    all_lats = [course['lat']]
    all_lons = [course['lon']]
    for h in course['highlights_en']:
        if h in highlight_coords:
            all_lats.append(highlight_coords[h][0])
            all_lons.append(highlight_coords[h][1])
    
    if all_lats and all_lons:
        center_lat = sum(all_lats) / len(all_lats)
        center_lon = sum(all_lons) / len(all_lons)
    else:
        center_lat, center_lon = 37.5665, 126.9780

    m = folium.Map(location=[center_lat, center_lon], zoom_start=13, tiles="OpenStreetMap")

    folium.CircleMarker(
        location=[course['lat'], course['lon']],
        radius=14, color="white", fill=True,
        fill_color="#2D6A4F", fill_opacity=1.0,
        popup=folium.Popup(f"<b>🚩 Start: {course['start_en']}</b>", max_width=200),
        tooltip=f"🚩 Start: {course['start_en']}"
    ).add_to(m)

    colors = ["blue", "purple", "orange", "red", "darkblue"]
    for i, highlight in enumerate(course['highlights_en']):
        if highlight in highlight_coords:
            coords = highlight_coords[highlight]
            folium.Marker(
                location=coords,
                popup=folium.Popup(f"⭐ {highlight}", max_width=200),
                tooltip=f"{i+1}. {highlight}",
                icon=folium.Icon(color=colors[i % len(colors)], icon="star", prefix="fa")
            ).add_to(m)

    legend_html = """
    <div style='position:fixed;bottom:30px;left:50px;z-index:1000;
                background:white;padding:10px 14px;border-radius:8px;
                border:1px solid #ccc;font-size:12px;line-height:2;
                box-shadow:2px 2px 6px rgba(0,0,0,0.15)'>
        🟢 Start Point<br>⭐ Highlights<br>🔴 Restaurants<br>🔵 Accommodations
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    return m

def add_poi_markers(map_obj, restaurants, accommodations):
    """Adds markers for nearby POIs to the map."""
    if restaurants:
        for r in restaurants[:4]:
            p = format_place(r)
            if p['lat'] and p['lon']:
                try:
                    folium.Marker(
                        location=[float(p['lat']), float(p['lon'])],
                        popup=folium.Popup(f"🍜 {p['title']}<br>{p['addr']}", max_width=200),
                        tooltip=f"🍜 {p['title']}",
                        icon=folium.Icon(color="red", icon="cutlery", prefix="fa")
                    ).add_to(map_obj)
                except Exception as e:
                    logger.warning(f"Failed to add restaurant marker for {p.get('title')}: {e}")
                    pass

    if accommodations:
        for a in accommodations[:4]:
            p = format_place(a)
            if p['lat'] and p['lon']:
                try:
                    folium.Marker(
                        location=[float(p['lat']), float(p['lon'])],
                        popup=folium.Popup(f"🏨 {p['title']}<br>{p['addr']}", max_width=200),
                        tooltip=f"🏨 {p['title']}",
                        icon=folium.Icon(color="cadetblue", icon="bed", prefix="fa")
                    ).add_to(map_obj)
                except Exception as e:
                    logger.warning(f"Failed to add accommodation marker for {p.get('title')}: {e}")
                    pass
    return map_obj
