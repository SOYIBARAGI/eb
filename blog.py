import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib

# 페이지 기본 설정
st.set_page_config(page_title="Kevin De Bruyne 분석 보고서", layout="wide")

# 제목 및 소개
st.title("⚽ 맨시티의 마에스트로: 케빈 더브라위너")
st.header("나의 축구 취향과 더브라위너의 플레이스타일 분석")
st.subheader("streamlit 블로그 만들기 기말 과제")
st.caption("By Hongik University, C521018 김은빈")

# 개요 마크다운
st.markdown("""
## 📌 개요
- 본 블로그는 **케빈 더브라위너** 선수를 중심으로 한 나의 축구 취향을 데이터 기반으로 분석한 블로그입니다.
- 사용된 기술 요소: `텍스트`, `차트`, `오디오/비디오`, `LaTeX`, `코드 블럭`, `표`, `컬럼`, `Callout` 등
""")
st.divider()

# 이미지와 영상
st.markdown("### 🖼️ 케빈 더브라위너 프로필")
st.image(
    "https://i.namu.wiki/i/Co-ImG4lO95ZP1At7QtcL7W72U8kF9na9cPEAEYjomg4oNsInr5_U8_NWSBJwP9FZtA4XZBn6CDN_75aPnw993ASzHjldb5SGbxMo3EXQx3KeGJmaR0LyI1Nol5cub7Se8tFQwfC8_QZQV-hepo4HQ.webp",
    caption="Kevin De Bruyne - Manchester City",
    width=300
)

st.markdown("### 🎥 케빈 더브라위너 하이라이트 영상")
st.video("https://youtu.be/RI96abvEfLc?si=0yMHq0kQ8EVrtQ2b")

# 색상 있는 텍스트
st.markdown("### 🎨 능력 색상 표현")
st.markdown("- :blue[냉정한 판단력] · :orange[창의적인 패스] · :green[지능적인 위치선정] · :red[위협적인 중거리슛]")



# 코드 블럭 + Echo
st.code("print('Kevin De Bruyne is the best attacking midfielder.')", language="python")
example_stat = "패스 성공률"
st.write(f"📊 이번 분석 항목: {example_stat}")


# 데이터프레임
df = pd.DataFrame({
    "시즌": ["2018/19", "2019/20", "2020/21", "2021/22", "2022/23"],
    "도움": [16, 20, 12, 15, 18],
    "골": [8, 13, 6, 10, 7],
})
st.dataframe(df)

# 메트릭 + 컬럼
st.markdown("### 📌 주요 스탯 메트릭")
col1, col2, col3 = st.columns(3)
col1.metric("도움", "18", "+3")
col2.metric("패스 성공률", "89%", "+2%")
col3.metric("슈팅 정확도", "67%", "+4%")

# 기본 차트
st.markdown("### 📈 시즌별 도움 추이")
st.line_chart(df.set_index("시즌")["도움"])
st.markdown("### 📊 시즌별 골 기록")
st.bar_chart(df.set_index("시즌")["골"])

st.markdown("## ⚽ 더브라위너 활동 분석 시각화")

# 1. 주요 활동 위치별 활동량
st.markdown("### 📊 위치별 활동량")
position_data = pd.DataFrame({
    "위치": ["왼쪽 하프 스페이스", "오른쪽 하프 스페이스", "중앙", "페널티 박스 앞"],
    "활동 점수": [75, 90, 85, 65]
})
st.bar_chart(position_data.set_index("위치"))

# 2. 시즌별 패스 성공률
st.markdown("### 📈 시즌별 패스 성공률")
pass_data = pd.DataFrame({
    "시즌": ["2018/19", "2019/20", "2020/21", "2021/22", "2022/23"],
    "패스 성공률 (%)": [85, 87, 88, 89, 90]
})
st.line_chart(pass_data.set_index("시즌"))

# 3. 활동 밀집도 (히트맵 스타일)
# ✅ 한글 깨짐 방지
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
matplotlib.rcParams['axes.unicode_minus'] = False

st.markdown("### 🧠 더브라위너 활동 밀도 히트맵 (개선 버전)")

heatmap_data = np.array([
    [0.3, 0.7, 0.5],
    [0.9, 1.0, 0.8],
    [0.2, 0.6, 0.4]
])

xticklabels = ["left", "middle", "right"]
yticklabels = ["backside", "middle", "front"]

fig, ax = plt.subplots(figsize=(3, 2))
sns.heatmap(
    heatmap_data,
    annot=True,
    cmap="YlGnBu",
    xticklabels=xticklabels,
    yticklabels=yticklabels,
    linewidths=0.3,
    cbar_kws={"label": "활동 강도"}
)
ax.set_title("더브라위너 활동 밀도 히트맵", pad=8)
plt.tight_layout()
st.pyplot(fig)


# LaTeX 수식
st.markdown("### 📐 포지션 기여도 수식")
st.latex(r"기여도 = \frac{공격 + 패스 + 전진성}{공 소유 시간}")

# 4. 포지션별 기여 지수

st.markdown("### 🧮 포지션별 기여 지수 비교")
contribution = pd.DataFrame({
    "포지션": ["공격형 미드필더", "중앙 미드필더", "측면 미드필더", "수비형 미드필더"],
    "기여 지수": [95, 80, 70, 60]
})
st.dataframe(contribution)

st.caption("※ 위 데이터는 발표용 예시로 생성된 가상 데이터입니다.")

# Callouts
st.info("📘 이 블로그는 데모 블로그입니다.")
st.success("✅ 모든 Streamlit 주요 기능을 포함합니다.")
st.warning("⚠️ 일부 데이터는 임의 생성된 예시입니다.")
st.error("❌ 일부 그래프는 모바일 화면에 적합하지 않을 수 있습니다.")

st.divider()
st.caption("ⓒ 2025 과제용 Streamlit 기술 시연 - Kevin De Bruyne Fan Project")
