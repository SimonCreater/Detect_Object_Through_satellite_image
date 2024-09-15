import os
from PIL import Image

def image_crop(x, y, img, save_path='cropimage_repository', file_name='cropped_image.jpg'):
  
    img_width, img_height = img.size

  
    left = max(0, x - 250)
    upper = max(0, y - 250)
    right = min(img_width, x + 250)
    lower = min(img_height, y + 250)

   
    if left >= right or upper >= lower:
        raise ValueError("크롭할 수 없는 범위")

    # 이미지 자르기
    cropping_img = img.crop((left, upper, right, lower))

    # 경로가 존재하지 않으면 디렉토리 생성
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 파일 저장 경로
    save_full_path = os.path.join(save_path, file_name)

    # 이미지 저장
    cropping_img.save(save_full_path, format='JPEG')
    print(f"크롭된 이미지가 {save_full_path}에 저장되었습니다.")

    return cropping_img

def process_images_in_directory(src_dir, dst_dir, x, y):
    # src_dir 경로에 있는 모든 파일을 순회
    for file_name in os.listdir(src_dir):
        if file_name.lower().endswith(('.jpg','.jpeg','.png')):
            img_path=os.path.join(src_dir,file_name)
            try:
                img=Image.open(img_path)
                cropped_image=image_crop(x,y,img,save_path=dst_dir,file_name=f'cropped_{file_name}')
            except Exception as e:
                print(f"파일 {file_name} 처리 중 오류 발생: {e}")



src_directory = 'imgerepository'  # 원본 이미지 디렉토리
dst_directory = 'cropimage_repository'  # 크롭된 이미지 디렉토리


x, y = 300, 300#임시값


process_images_in_directory(src_directory, dst_directory, x, y)
