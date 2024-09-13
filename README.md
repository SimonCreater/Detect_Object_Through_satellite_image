# Segment Anything 모델 설치 및 실행 가이드

이 문서는 Google Colab 환경에서 Facebook Research의 "Segment Anything" 모델을 설치하고 실행하는 방법을 설명합니다.

## 설치 단계

### 1. Segment Anything 저장소 설치

GitHub에서 `segment-anything` 패키지를 설치합니다. 이 명령어는 모델 코드와 의존성을 설치합니다.

```bash
!pip install 'git+https://github.com/facebookresearch/segment-anything.git'

### 2. Segment Anything 저장소 설치

Segment Anything 모델을 사용하기 위해 사전 학습된 모델 가중치 파일을 다운로드해야 합니다.
				
```
!wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
