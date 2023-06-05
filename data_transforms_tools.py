from torchvision import transforms
import cv2 as cv

img_path = "Data_set/hymenoptera_data/train/ants/5650366_e22b7e1065.jpg"
img = cv.imread(img_path)

print(img)
tensor_tools = transforms.ToTensor()

tensor_img = tensor_tools(img)

print(tensor_img)
