import os
from dotenv import load_dotenv
import requests
load_dotenv()

client_id = os.getenv('NAVER_CLIENT_ID')  
client_secret =os.getenv('NAVER_CLIENT_SECRET')  


out_repository = 'staticmap_repository'
if not os.path.exists(out_repository):
    os.makedirs(out_repository)

def save_static_map(lat, lon, zoom=16, output_dir='staticmap_repository'):
   
    url = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
    
    # 요청 파라미터 설정
    params = {
        'center': f"{lon},{lat}",  # 경도, 위도
        'level': zoom,  # 줌 레벨
        'w': 1000,  # 이미지 너비
        'h': 1000,  # 이미지 높이
        'maptype': 'satellite'  # 위성 지도
    }
    
    # 헤더에 API 키 정보 설정
    headers = {
        'X-NCP-APIGW-API-KEY-ID': client_id,
        'X-NCP-APIGW-API-KEY': client_secret
    }
    
    # API 요청 보내기
    response = requests.get(url, headers=headers, params=params)
    
    # 응답 상태 확인 및 이미지 저장
    if response.status_code == 200:
        image_path = os.path.join(output_dir, f"static_map_{lat}_{lon}.jpg")
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"이미지가 저장되었습니다: {image_path}")
    else:
        print(f"HTTP 오류 발생: {response.status_code}")

# 좌표 리스트
coordinates = [
    (33.5059364, 126.4959513), 
    (33.45320693217409, 126.5093937376044),  
    # (33.4284190070879, 126.5531753980934),  
    # (33.42443553442781, 126.6173666832862),  
    # (33.39582331415505, 126.66462446723175), 
    # (33.34996941056425, 126.6307291340323),  
    # (33.30441069265054, 126.59615891785647), 
    # (33.27352576142578, 126.5742443478399),  
    # (33.25823995011956, 126.5597875)
]

# 각 좌표에 대해 지도 이미지 저장
for lat, lon in coordinates:
    save_static_map(lat, lon)

print("모든 이미지가 저장되었습니다.")
