# Segment Anything 모델 설치 가이드

이 가이드는 Facebook Research의 "Segment Anything" 모델을 설치하는 방법을 설명합니다.

## 설치 단계

### 1. Segment Anything 저장소 설치

`segment-anything` 패키지를 GitHub 저장소에서 직접 설치할 수 있습니다. 이를 위해 아래 명령어를 실행하세요.

```bash
pip install 'git+https://github.com/facebookresearch/segment-anything.git'
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
