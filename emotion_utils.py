import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
import io

# Load the model
def load_model(model_path):
    model = mobilenet_v2(weights=MobileNet_V2_Weights.DEFAULT)
    model.classifier[1] = torch.nn.Linear(model.last_channel, 4)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Preprocess the uploaded image
def preprocess_image(image_file):
    image = Image.open(image_file).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    return image_tensor

# Predict emotion
def predict_emotion(model, image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
    return predicted.item()

# Convert class index to label
def get_emotion_label(index):
    emotions = ['Angry', 'Happy', 'Sad', 'Neutral']
    return emotions[index]
