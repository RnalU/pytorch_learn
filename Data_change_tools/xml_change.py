import os.path
import xml.etree.ElementTree as ET

def modify_xml(xml_file, output):
    file_name = xml_file.split('/')[-1]
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 修改label
    # element = root.find('object')
    # name = element.find('name')
    # if name.text == 'Left':
    #     print(name.text)
    #     name.text = 'left'
    # if name.text == 'L&R':
    #     print(name.text)
    #     name.text = 'left_right'
    # 修改filename
    element = root.find('filename')
    # 修改元素的文本值
    inset_txt = element.text.split('/')[-1]
    element.text = inset_txt

    # 修改folder
    element = root.find('folder')
    element.text = 'JPEGImages'


    size = root.find('size')
    depth = size.find('depth')
    depth.text = '0'

    # 保存修改后的XML文件
    try:
        tree.write(os.path.join(output, file_name))
    except Exception as e:
        print(e)
    else:
        print(f"{xml_file.split('/')[-1]}文件已成功创建。")

output_path = './test'
# modify_xml('./IMG_20230611_124247.xml', output_path)
# # 读取xml文件
xml_load_path = 'C:\\Users\\Yymmcc\\paddlex_workspace\\datasets\\D0022\\Annotations - 副本'
for xml_name in os.listdir(xml_load_path):
    print(xml_name)
    xml_path = os.path.join(xml_load_path, xml_name)
    print(xml_path)
    modify_xml(xml_path, output_path)
