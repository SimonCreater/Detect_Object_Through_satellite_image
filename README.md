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
### 5. 이미지 크로핑
1.imagerepository 폴더안에 사용자가 특정 이미지 저장.
2.imagerepository 폴더안에 있는 이미지를 크로핑 하고나면 cropimage_repository안에 저장됨.(여러 개의 이미지가 동시에 저장됨).
