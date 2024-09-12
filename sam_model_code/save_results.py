
import pandas as pd
import numpy as np

def calculate_mask_centers(masks):
    mask_centers = []
    for mask in masks:
        mask_np = mask['segmentation']
        y_coords, x_coords = np.where(mask_np)  # 마스크 영역의 좌표값 찾기
        center_x = int(np.mean(x_coords))  # x 좌표의 평균값 계산
        center_y = int(np.mean(y_coords))  # y 좌표의 평균값 계산
        mask_centers.append((center_x, center_y))  # 중심 좌표 저장
    return mask_centers

def save_to_csv(detected_labels, mask_percentages, mask_centers, filename="detected_objects.csv"):
    data = {
        'Label': detected_labels,
        'Percentage': mask_percentages,
        'Center_X': [center[0] for center in mask_centers],
        'Center_Y': [center[1] for center in mask_centers]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")
