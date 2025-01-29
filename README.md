# 건물 탐지 (Building Detection) 프로젝트

## 프로젝트 개요

본 프로젝트는 위성 이미지를 활용하여 **건물 영역을 탐지**하는 *U-Net* 모델을 개발하는 것을 목표로 합니다. 위성 이미지에서 건물을 분할하여 탐지하는 것은 도시 계획, 재난 대응 및 지리 정보 시스템(GIS)에서 중요한 역할을 합니다.

## 데이터 설명

- **위성 이미지**: 실제 위성 데이터를 사용하여 건물 영역을 탐지합니다.
- **라벨 이미지**: 건물이 있는 영역을 **노란색**, 배경을 **보라색**으로 표시한 마스크 이미지입니다.

## 모델 설명

- **사용한 모델**: U-Net
- **학습 데이터**: 위성 이미지와 해당 이미지의 마스크 데이터
- **출력**: 주어진 위성 이미지에서 건물 영역을 탐지하여 마스크로 변환

## 주요 파일 설명

- `buildingDetectionwithUnet.ipynb`:
  - 데이터 로딩 및 전처리
  - U-Net 모델 학습 및 평가
  - 예측 결과 시각화
- `image.png`:
  - 위성 이미지 및 해당 이미지에 대한 마스크 시각화 결과

## 프로젝트 실행 방법

1. `buildingDetectionwithUnet.ipynb` Jupyter Notebook을 실행합니다.
2. 필요 라이브러리를 설치합니다.
   ```bash
   pip install tensorflow keras numpy matplotlib
   ```
3. 데이터를 로드하고 모델을 학습시킵니다.
4. 결과를 시각화하여 건물 탐지 성능을 평가합니다.

## 결과 분석

- 첫 번째 이미지는 **원본 위성 이미지**이며, 두 번째 이미지는 **실제 마스크**입니다.
- 두 번째 및 세 번째 이미지는 모델의 예측 결과이며, 실제 마스크와 비교하여 **모델의 성능을 평가**할 수 있습니다.
- 모델의 성능을 향상시키기 위해 **데이터 증강, 하이퍼파라미터 튜닝** 등을 고려할 수 있습니다.

## 개선 가능 사항

- 더 큰 데이터셋을 활용하여 **모델의 일반화 성능 향상**
- 다양한 이미지 처리 기법(예: 데이터 증강, 이미지 보정) 적용
- 다른 딥러닝 모델(예: *DeepLabV3, Mask R-CNN*)과 비교 분석

## 참고 자료

- U-Net 논문: [https://arxiv.org/abs/1505.04597](https://arxiv.org/abs/1505.04597)
- 위성 이미지 처리 관련 연구 및 데이터셋

## 라이선스

본 프로젝트의 데이터 및 코드는 자유롭게 활용 가능하며, 연구 및 교육 목적에 사용할 수 있습니다.




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

