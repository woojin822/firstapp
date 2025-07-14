import streamlit as st
import plotly.graph_objects as go

# ✅ 더미 데이터
def get_dummy_kpop_data():
    return [
        ("PSY - Gangnam Style", "https://youtu.be/9bZkp7q19f0", 5600000000),
        ("BLACKPINK - DDU-DU DDU-DU", "https://youtu.be/IHNzOHi8sJs", 2310000000),
        ("BLACKPINK - Kill This Love", "https://youtu.be/2S24-y0Ij3Y", 2110000000),
        ("BTS - Dynamite", "https://youtu.be/gdZLi9oWNZg", 1960000000),
        ("BTS - Boy With Luv", "https://youtu.be/XsX3ATc3FbA", 1860000000),
        ("BLACKPINK - BOOMBAYAH", "https://youtu.be/bwmSjveL3Lc", 1790000000),
        ("PSY - Gentleman", "https://youtu.be/ASO_zypdnsQ", 1680000000),
        ("BTS - DNA", "https://youtu.be/MBdVXkSdhwU", 1620000000),
        ("BTS - MIC Drop Remix", "https://youtu.be/kTlv5_Bs8aw", 1500000000),
        ("TWICE - TT", "https://youtu.be/ePpPVE-GGJw", 700000000)
    ]

# ✅ Plotly 그래프 생성 함수
def create_plot(videos):
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
        title="🔥 유튜브 K-pop 인기 영상 TOP 10",
        xaxis_title="영상 제목",
        yaxis_title="조회수",
        xaxis_tickangle=-30,
        hoverlabel=dict(bgcolor="white", font_size=12),
        template="plotly_white",
        height=600
    )

    return fig

# ✅ Streamlit 앱 실행
st.set_page_config(page_title="K-pop Top 10", layout="wide")
st.title("🎵 K-pop 유튜브 영상 TOP 10 (더미 데이터 기반)")

data = get_dummy_kpop_data()
fig = create_plot(data)
st.plotly_chart(fig, use_container_width=True)
