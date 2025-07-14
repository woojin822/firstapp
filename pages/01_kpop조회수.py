import requests
import re
from html import unescape
import plotly.graph_objects as go

def search_kpop_top_videos(keyword="kpop music video", max_results=5):
    query = keyword.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("유튜브 페이지를 불러올 수 없습니다.")
        return []

    html = response.text
    video_blocks = re.findall(r'{"videoRenderer":(.*?)},"trackingParams"', html)

    videos = []
    for block in video_blocks:
        try:
            title_match = re.search(r'"title":\{"runs":\[\{"text":"(.*?)"\}', block)
            title = unescape(title_match.group(1)) if title_match else "제목 없음"

            vid_match = re.search(r'"videoId":"(.*?)"', block)
            video_id = vid_match.group(1)
            url = f"https://www.youtube.com/watch?v={video_id}"

            views_match = re.search(r'"viewCountText":\{"simpleText":"([\d,]+) views"\}', block)
            views = views_match.group(1).replace(",", "")
            views_int = int(views) if views.isdigit() else 0

            videos.append((title, url, views_int))

        except Exception:
            continue

        if len(videos) >= max_results:
            break

    return videos

def plot_top_videos(videos):
    titles = [v[0] for v in videos]
    views = [v[2] for v in videos]
    urls = [v[1] for v in videos]

    fig = go.Figure(data=[
        go.Bar(
            x=titles,
            y=views,
            text=[f"<a href='{url}'>{title}</a>" for title, url in zip(titles, urls)],
            hovertemplate='%{text}<br>조회수: %{y:,}회<extra></extra>',
            marker_color='lightsalmon'
        )
    ])

    fig.update_layout(
        title="🔥 유튜브 K-pop 인기 영상 TOP 5",
        xaxis_title="영상 제목",
        yaxis_title="조회수",
        xaxis_tickangle=-30,
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial"),
        template="plotly_white"
    )

    fig.show()

# 실행
if __name__ == "__main__":
    results = search_kpop_top_videos()
    if results:
        plot_top_videos(results)
    else:
        print("영상을 불러오지 못했습니다.")
