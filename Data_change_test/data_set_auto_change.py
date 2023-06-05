import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """将XML元素进行格式化，添加适当的缩进"""
    rough_string = ET.tostring(elem, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def create_voc_xml(image_path, image_size, annotations):
    # 创建根节点
    root = ET.Element("annotation")

    # 添加图片信息
    folder = ET.SubElement(root, "folder")
    folder.text = image_path.split("/")[0]

    filename = ET.SubElement(root, "filename")
    filename.text = image_path.split("/")[-1]

    path = ET.SubElement(root, "path")
    path.text = image_path

    source = ET.SubElement(root, "source")
    database = ET.SubElement(source, "database")
    database.text = "Unknown"

    size = ET.SubElement(root, "size")
    width = ET.SubElement(size, "width")
    width.text = str(image_size[0])
    height = ET.SubElement(size, "height")
    height.text = str(image_size[1])
    depth = ET.SubElement(size, "depth")
    depth.text = str(image_size[2])

    segmented = ET.SubElement(root, "segmented")
    segmented.text = "0"

    # 添加标注框信息
    for annotation in annotations:
        obj = ET.SubElement(root, "object")
        name = ET.SubElement(obj, "name")
        name.text = annotation["transcription"]
        pose = ET.SubElement(obj, "pose")
        pose.text = "Unspecified"
        truncated = ET.SubElement(obj, "truncated")
        truncated.text = "0"
        difficult = ET.SubElement(obj, "difficult")
        difficult.text = "0"
        bndbox = ET.SubElement(obj, "bndbox")
        xmin = ET.SubElement(bndbox, "xmin")
        xmin.text = str(annotation["points"][0][0])
        ymin = ET.SubElement(bndbox, "ymin")
        ymin.text = str(annotation["points"][0][1])
        xmax = ET.SubElement(bndbox, "xmax")
        xmax.text = str(annotation["points"][2][0])
        ymax = ET.SubElement(bndbox, "ymax")
        ymax.text = str(annotation["points"][2][1])

    # 将XML元素进行格式化，添加缩进
    xml_string = prettify(root)

    # 保存为文件
    xml_file_path = image_path.replace(".jpg", ".xml")
    # xml_file_path = "C:\\Users\\Yymmcc\\paddlex_workspace\\Data_test\\number_test\\new_xml"
    with open(xml_file_path, "w", encoding="utf-8") as xml_file:
        xml_file.write(xml_string)

# 示例数据
# image_path = "JPEGImage/IMG20230603232159.jpg"
# image_size = (4000, 3000, 3)
# annotations = '[{"transcription": "119", "points": [[637, 1450], [956, 1450], [956, 1666], [637, 1666]], "difficult": False},{"transcription": "120", "points": [[1672, 1369], [1998, 1369], [1998, 1576], [1672, 1576]], "difficult": False},{"transcription": "110", "points": [[2785, 1724], [3275, 1724], [3275, 2008], [2785, 2008]], "difficult": False}]'
# print(eval(annotations))

if __name__ == '__main__':
    # 创建VOC格式的XML数据集文件
    image_size = (4000, 3000, 3)
    # label_file = open('Label.txt', 'r', encoding='GBK')
    label_file = open('Label.txt', 'r', encoding='GBK')
    false = False
    for line in label_file.readlines():
        image_path = line.split('\t')[0]
        annotations = (line.split('\t')[-1])
        create_voc_xml(image_path, image_size, eval(annotations))
    label_file.close()
