# Segment Anything 모델 설치 및 실행 가이드

이 문서는 Facebook Research의 "Segment Anything" 모델을 설치하고 실행하는 방법을 설명합니다.

## 필수 조건

- Python 3.6 이상
- CUDA 지원이 있는 머신 (GPU 사용을 권장)
- `pip` 패키지 매니저

## 설치 단계

### 1. Segment Anything 저장소 설치

다음 명령어를 사용하여 GitHub 저장소에서 `segment-anything` 패키지를 설치하세요.

```bash
pip install 'git+https://github.com/facebookresearch/segment-anything.git'

wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth
