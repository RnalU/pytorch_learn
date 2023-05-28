import os
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import cv2 as cv


class MyDataSet(Dataset):
    """数据读取类"""
    def __init__(self, root_path, label_path):
        self.root_path = root_path
        self.label_path = label_path
        self.load_path = os.path.join(root_path, label_path)
        self.img_list = os.listdir(self.load_path)

    def __getitem__(self, index):
        self.img_name = self.img_list[index]
        self.img_path = os.path.join(self.load_path, self.img_name)
        self.img = cv.imread(self.img_path)
        self.img_label = self.label_path
        return self.img, self.img_label

    def __len__(self):
        return len(os.listdir(self.load_path))


if __name__ == '__main__':
    root_path = "./Data_set/hymenoptera_data/train"
    label_path = "ants"

    MyDataSET = MyDataSet(root_path, label_path)
    img, label = MyDataSET[0]
