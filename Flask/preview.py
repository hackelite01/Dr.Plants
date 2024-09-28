import torch
from torch.amp import autocast, GradScaler


pth_file = './Models/plantDisease-resnet34.pth'
state_dict = torch.load(pth_file, map_location=torch.device('cpu'))

for layer_name, weights in state_dict.items():
    print(f"Layer: {layer_name}")
    print(f"Weights: {weights.flatten()[:5]}")
    print("-" * 50)
