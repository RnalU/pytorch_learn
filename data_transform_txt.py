import os


def spawn_train_txt(img_path, aim_path):
    """生成图片训练文件的txt label文件"""
    label = img_path.split('/')[-1]

    if os.path.exists(aim_path) is True:
        if os.listdir(aim_path).count(label):
            print(f"\"{label}\" 文件夹已于目录 \"{aim_path}\" 中存在！")
            raise FileExistsError
    else:
        os.mkdir(aim_path)

    for img_name in os.listdir(img_path):
        # print(os.path.join(img_path, img_name))
        # 生成txt文件
        spawn_path = os.path.join(aim_path, img_name.split('.')[0] + ".txt")
        file = open(spawn_path, "a+", encoding="GBK")
        file.seek(0)
        file.write(label)
        file.close()


if __name__ == '__main__':
    img_path = "Data_set/hymenoptera_data/val/ants"
    aim_path = "Data_set/hymenoptera_data/train1"
    spawn_train_txt(img_path, aim_path)
