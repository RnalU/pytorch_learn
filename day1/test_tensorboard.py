from torch.utils.tensorboard import SummaryWriter
from day1.read_data import MyDataSet

# 图片数据读取入口
root_path = "../Data_set/hymenoptera_data/train"
label_path = "ants"

dataReader = MyDataSet(root_path, label_path)
writer = SummaryWriter("../logs")

for img_idx in range(len(dataReader)):
    img, label = dataReader[img_idx]

    writer.add_image("ant", img, img_idx, dataformats="HWC")

"""y = x^2"""
# for x in range(100):
#     y = x ** 2
#     # writer.add_image()
#     writer.add_scalar("f(x) = x^2", y, x)

writer.close()
