import requests
import re
from html import unescape

def search_kpop_top_videos(keyword="kpop music video", max_results=5):
    query = keyword.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("유튜브 페이지를 불러올 수 없습니다.")
        return

    html = response.text

    # 초기 videoRenderer JSON 블록 추출
    video_blocks = re.findall(r'{"videoRenderer":(.*?)},"trackingParams"', html)

    videos = []
    for block in video_blocks:
        try:
            # 제목 추출
            title_match = re.search(r'"title":\{"runs":\[\{"text":"(.*?)"\}', block)
            title = unescape(title_match.group(1)) if title_match else "제목 없음"

            # videoId로 URL 생성
            vid_match = re.search(r'"videoId":"(.*?)"', block)
            video_id = vid_match.group(1)
            url = f"https://www.youtube.com/watch?v={video_id}"

            # 조회수 추출
            views_match = re.search(r'"viewCountText":\{"simpleText":"([\d,]+) views"\}', block)
            views = views_match.group(1) if views_match else "0"

            videos.append((title, url, views))

        except Exception:
            continue

        if len(videos) >= max_results:
            break

    return videos

# 실행
if __name__ == "__main__":
    print("🎵 K-pop 인기 유튜브 영상 Top 5:")
    results = search_kpop_top_videos()
    for i, (title, url, views) in enumerate(results, 1):
        print(f"{i}. {title} — {views} views")
        print(f"   🔗 {url}")
