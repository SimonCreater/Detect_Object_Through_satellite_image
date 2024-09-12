# main.py
import sys
from image_visualization import load_and_display_image, show_anns
from sam_model import setup_sam_model, generate_masks, calculate_mask_percentages
from object_classification import setup_resnet_model, classify_masked_region, load_imagenet_labels
from save_results import calculate_mask_centers, save_to_csv
import torch
import numpy as np

# 이미지 로드 및 표시
image_path = "/content/sample_data/naver_map (9).jpg"
image = load_and_display_image(image_path)

# SAM 모델 설정 및 마스크 생성
sam_checkpoint = "sam_vit_h_4b8939.pth"
sam = setup_sam_model(sam_checkpoint)
masks = generate_masks(sam, image)

# 이미지 전체 면적 계산 (픽셀 수)
image_area = image.shape[0] * image.shape[1]

# 마스크 영역 퍼센트 계산
mask_percentages = calculate_mask_percentages(masks, image_area)

# 객체 분류 모델 설정 및 레이블 로드
classifier = setup_resnet_model()
imagenet_labels = load_imagenet_labels()

# 전체 임시 클래스 매핑 (필요한 경우 추가)
custom_labels = {
    "spotlight": "building",
    "street_sign": "road",
    "parking_meter": "car",
    "cleaver": "industrial",
    "tennis ball": "industrial",
    "ping-pong ball": "industrial",
    "brillard table": "others",
    "suspension bridge": "sea",
    "nematode": "others",
    "notebook computer": "others",
    "umbrella": "sea",
    "conch": "sea",
    "cauliflower": "sea",
    "safety pin": "others",
    "syringe": "natural environment",
}

# 객체 분류 및 레이블링
detected_labels = []
original_labels = []

for mask in masks:
    label, original_label = classify_masked_region(image, mask['segmentation'], classifier, imagenet_labels, custom_labels)
    detected_labels.append(label)
    original_labels.append(original_label)

# 마스크 중심 좌표 계산 및 CSV 저장
mask_centers = calculate_mask_centers(masks)
save_to_csv(detected_labels, mask_percentages, mask_centers)
