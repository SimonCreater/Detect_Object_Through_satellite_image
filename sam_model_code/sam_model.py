#sam 모델 설정 및 마스크 생성
import sys
import torch
import numpy as np
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator

sys.path.append("..")

def setup_sam_model(checkpoint_path, model_type="vit_h", device="cuda"):
    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    sam.to(device=device)
    return sam

def generate_masks(sam, image):
    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(image)
    return masks

def calculate_mask_percentages(masks, image_area):
    mask_percentages = []
    for mask in masks:
        mask_area = np.sum(mask['segmentation'])  # 마스크 영역의 픽셀 수
        mask_percentage = (mask_area / image_area) * 100  # 퍼센트 계산
        mask_percentages.append(mask_percentage)
    return mask_percentages
