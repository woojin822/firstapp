import streamlit as st
import plotly.graph_objects as go

# ✅ 여자 아이돌 직캠 Top 5 더미 데이터
def get_fancam_data():
    return [
        ("EXID 하니", "Up & Down", "https://youtu.be/jeX6oCv5V1g", 36080000),
        ("미쓰에이 수지", "Love Song", "https://youtu.be/ytcLRSGQ_EI", 30130000),
        ("BLACKPINK 리사", "Swalla + Take Me", "https://youtu.be/eRG5QjVwjpA", 29360000),
        ("BLACKPINK 제니", "Solo", "https://youtu.be/k6jqx9kZgPM", 23950000),
        ("선미", "Gashina", "https://youtu.be/sS0LCjOiIYg", 22590000),
    ]

# ✅ 그래프 생성
def create_plot(data):
    names = [f"{artist} - {song}" for artist, song, _, _ in data]
    views = [v[3] for v in data]
    urls = [v[2] for v in data]

    fig = go.Figure(data=[
        go.Bar(
            x=names,
            y=views,
            text=[f"<a href='{url}'>{name}</a>" for name, url in zip(names, urls)],
            hovertemplate='%{text}<br>조회수: %{y:,}회<extra></extra>',
            marker_color='hotpink'
        )
    ])

    fig.update_layout(
        title="🔥 여자 아이돌 직캠 조회수 TOP 5",
        xaxis_title="아이돌 - 곡명",
        yaxis_title="조회수",
        xaxis_tickangle=-20,
        template="plotly_white",
        height=600
    )

    return fig

# ✅ Streamlit 앱 실행
st.set_page_config(page_title="여자 아이돌 직캠 TOP 5", layout="wide")
st.title("🎥 여자 아이돌 직캠 조회수 TOP 5 (더미 데이터)")

data = get_fancam_data()
fig = create_plot(data)
st.plotly_chart(fig, use_container_width=True)
