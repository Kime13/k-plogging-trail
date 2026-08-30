from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def curate_in_english(place_data: dict) -> str:
    """관광지 국문 데이터를 영어로 큐레이션"""
    prompt = f"""You are a travel guide for foreign visitors to Korea.
Based on the following Korean tourist spot information, write a short English description (2-3 sentences) that would appeal to international visitors doing a plogging activity (jogging while picking up trash).

Place name: {place_data.get('title', '')}
Address: {place_data.get('addr1', '')}

Write in a friendly, engaging tone. Focus on what makes this place special for outdoor activities."""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text


def generate_plogging_route(places: list, difficulty: str = "Moderate") -> str:
    """플로깅 코스 일정 생성"""
    place_list = "\n".join([f"{i+1}. {p['title']} ({p.get('addr1', '')})"
                            for i, p in enumerate(places[:5])])

    distance = {"Easy": "2-3km", "Moderate": "5-7km", "Challenge": "10km+"}[difficulty]

    prompt = f"""Create a structured plogging route for foreign tourists in Korea.

Difficulty: {difficulty} ({distance})
Spots:
{place_list}

Format your response exactly like this:

🗺️ ROUTE OVERVIEW
[One sentence summary of the route]

⏱️ Total Time: [X hours]
📏 Distance: {distance}
♻️ Plogging Gear: Gloves, trash bags, comfortable shoes

📍 STOP-BY-STOP GUIDE
[For each stop, write:]
▶ Stop N: [Name]
- What to do: [1 sentence]
- Plogging tip: [1 sentence about where to pick up trash]
- Time: [X minutes]

🏁 FINISH LINE
[Motivational closing sentence]

Write in English. Be concise and practical."""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text
