# 지리 정보 geojson 불러오기
import json
with open("./file/SIG.geojson", "r", encoding='utf-8') as f:
    geo = json.load(f)

# df 
import pandas as pd
df = pd.read_csv('./file/Population_SIG.csv')

# 코드 정보의 데이터 타입 바꾸기 정수 -> 문자열
df['code'] = df.code.astype(str)

# 위도, 경도에 따른 대한민국 지도 사진 출력
import folium
map_sig = folium.Map(location=[36.5, 127.7], zoom_start=6,
                    width='80%', height='80%',
                    tiles='cartodbpositron')

# 등치지역도(단계구분도)
folium.Choropleth(geo_data=geo).add_to(map_sig)

# 단계 구간 정하기 : 요약 통계정보
df['pop'].describe()

# 인구 시리즈 데이터에서 20% 구간별 구간 나누기
df['pop'].quantile([0, 0.2, 0.4, 0.6, 0.8, 1])

# 단계구분도 만들기
folium.Choropleth(geo_data=geo,                    # 지도 데이터
                  data=df,                         # 통계 데이터
                  columns=('code', 'pop'),         # 데이터프레임 컬럼
                  key_on='feature.properties.SIG_CD',# geoJson 기준(행정구역)
                  bins=bins,                       # 계급 구간 정보
                  fill_color='YlGnBu',             # 지도 색상
                  fill_opacity=1,                  # 지도색상 투명도
                  line_opacity=0.5).add_to(map_sig)# 경계선 투명도 + 배경지도에 추가
map_sig
