import os
import torch
from torchvision import datasets, transforms
import numpy as np

# Data augmentation and normalization for training
# Just normalization for validation
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}


def process(model_path, pic_path):
    image_datasets = datasets.ImageFolder(pic_path, data_transforms['val'])
    dataloaders = {'val': torch.utils.data.DataLoader(image_datasets, batch_size=1, shuffle=False, num_workers=1)}
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.load(os.path.join(model_path, 'resnet18_finetuned.pth'))
    class_names = np.load(os.path.join(model_path, 'class_names.npy'))
    model.eval()
    with torch.no_grad():
        for i, (inputs, labels) in enumerate(dataloaders['val']):
            inputs = inputs.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            #prob = torch.softmax(outputs, 1, torch.float)
            for j in range(inputs.size()[0]):
                class_name = class_names[preds[j]]
                return class_name


if __name__ == '__main__':
    pic_path = 'kuangniu_data/val'
    model_path = 'model'
    print(process(model_path, pic_path))
