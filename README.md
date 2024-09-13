# Segment Anything 모델 설치 및 실행 가이드



## 필수 조건

- Python 3.6 이상
- CUDA 지원이 있는 머신 (GPU 사용을 권장)
- `pip` 패키지 매니저

## 설치 단계

### 1. Segment Anything 저장소 설치

다음 명령어를 사용하여 GitHub 저장소에서 `segment-anything` 패키지를 설치

```bash
pip install 'git+https://github.com/facebookresearch/segment-anything.git'

Facebook Research에서 제공하는 사전 학습된 모델 가중치를 다운로드


```bash
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth


