from xml.etree import ElementTree as et
import xml.dom.minidom as minidom

# 创建根节点
root = et.Element('school')
names = ['张三', '李四']
genders = ['男', '女']
ages = ['20', '18']
# 添加子节点
student1 = et.SubElement(root, 'student')
student2 = et.SubElement(root, 'student')
et.SubElement(student1, 'name').text = names[0]
et.SubElement(student1, 'gender').text = genders[0]
et.SubElement(student1, 'age').text = ages[0]
et.SubElement(student2, 'name').text = names[1]
et.SubElement(student2, 'gender').text = genders[1]
et.SubElement(student2, 'age').text = ages[1]
# 将根目录转化为树行结构
tree = et.ElementTree(root)
rough_str = et.tostring(root, 'utf-8')
# 格式化
reparsed = minidom.parseString(rough_str)
new_str = reparsed.toprettyxml(indent='\t')
f = open('test.xml', 'w', encoding='utf-8')
# 保存
f.write(new_str)
f.close()