import numpy as np
import matplotlib.pyplot as plt
from image_visualization import load_and_display_image
from sam_model import setup_sam_model, generate_masks, calculate_mask_percentages
from object_classification import setup_resnet_model, classify_masked_region, load_imagenet_labels
from save_results import calculate_mask_centers, save_to_csv

def main():
    # 이미지 로드 및 시각화
    image_path = "/content/sample_data/naver_map (9).jpg"
    image = load_and_display_image(image_path)

    # SAM 모델 설정 및 마스크 생성
    sam_checkpoint = "sam_vit_h_4b8939.pth"
    sam = setup_sam_model(sam_checkpoint)
    masks = generate_masks(sam, image)

    # 이미지 전체 면적 계산
    image_area = image.shape[0] * image.shape[1]
    mask_percentages = calculate_mask_percentages(masks, image_area)

    # ResNet 모델 설정 및 레이블 로드
    classifier = setup_resnet_model()
    imagenet_labels = load_imagenet_labels()

    # 사용자 정의 레이블 매핑
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

    # 객체 분류 및 라벨링
    detected_labels = []
    original_labels = []
    for mask in masks:
        label, original_label = classify_masked_region(image, mask['segmentation'], classifier, imagenet_labels, custom_labels)
        detected_labels.append(label)
        original_labels.append(original_label)

    # 8% 이상의 비율을 차지하는 마스크를 sea로 라벨링
    max_percentage = 0
    max_index = -1
    for i, percentage in enumerate(mask_percentages):
        if percentage >= 8 and percentage > max_percentage:
            max_percentage = percentage
            max_index = i

    # 가장 큰 비율을 차지하는 객체를 sea로 라벨링
    if max_index != -1:
        detected_labels[max_index] = "sea"

    # 마스크 중심 좌표 계산
    mask_centers = calculate_mask_centers(masks)

    # 결과를 CSV로 저장
    save_to_csv(detected_labels, mask_percentages, mask_centers)

    # 시각화: 마스크 및 라벨 시각화
    plt.figure(figsize=(20, 20))
    plt.imshow(image)
    for i, mask in enumerate(masks, 1):
        mask_np = mask['segmentation']
        y, x = np.where(mask_np)
        plt.text(x.min(), y.min(), f"{i}: {detected_labels[i-1]} ({mask_percentages[i-1]:.2f}%)", 
                 color='red', fontsize=12, bbox=dict(facecolor='white', alpha=0.6))
        plt.contour(mask_np, colors='red', linewidths=1)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
