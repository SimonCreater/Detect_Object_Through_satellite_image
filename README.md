# Segment Anything 모델 설치 및 실행 가이드

이 문서는 Google Colab 환경에서 Facebook Research의 "Segment Anything" 모델을 설치하고 실행하는 방법을 설명합니다.

## 설치 단계

### 1. Segment Anything 저장소 설치

GitHub에서 `segment-anything` 패키지를 설치. 이 명령어는 모델 코드와 의존성을 설치

```bash
pip install 'git+https://github.com/facebookresearch/segment-anything.git'
```
### 2. 사전 학습된 모델 가중치 다운로드
Facebook Research에서 제공하는 사전 학습된 모델 가중치를 다운로드
```
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
```
### 3. PyTorch 및 Torchvision 설치
```
pip install torch torchvision

```
### 4. 추가 종속성 설치
```
pip install opencv-python matplotlib

```
# 이미지 크롭 저장 프로그램

이 프로그램은 `imagerepository` 폴더에 저장된 모든 이미지를 크로핑한 후, 결과물을 `cropimage_repository` 폴더에 저장합니다.

## 5. 이미지 저장

사용자는 `imagerepository` 폴더 안에 이미지를 저장. 여러 개의 이미지를 동시에 넣을 수 있으며, 지원되는 파일 형식은 `.jpg`, `.jpeg`, `.png`.

### 예시
```bash
/imagerepository
    ├── image1.jpg
    ├── image2.png
    └── image3.jpeg
/cropimage_repository
    ├── cropped_image1.jpg
    ├── cropped_image2.png
    └── cropped_image3.jpeg

