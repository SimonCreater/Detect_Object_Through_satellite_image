
import torch
from PIL import Image
import requests
import json
from torchvision import models, transforms

def setup_resnet_model(device="cuda"):
    classifier = models.resnet50(pretrained=True)
    classifier.eval()
    classifier.to(device)
    return classifier

def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return preprocess(image)

def load_imagenet_labels():
    LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    response = requests.get(LABELS_URL)
    imagenet_labels = json.loads(response.text)
    return imagenet_labels

def classify_masked_region(image, mask, classifier, imagenet_labels, custom_labels, device="cuda"):
    masked_image = Image.fromarray(image * mask[..., np.newaxis])
    input_tensor = preprocess_image(masked_image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = classifier(input_tensor)

    _, predicted_class = output.max(1)
    original_label = imagenet_labels[predicted_class.item()]
    corrected_label = custom_labels.get(original_label, original_label)
    return corrected_label, original_label
