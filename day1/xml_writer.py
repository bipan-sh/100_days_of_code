import pandas as pd
import xml.etree.ElementTree as ET

# Read the CSV file and extract the desired column
csv_file = 'fruits.csv' #Replace with actual file name
column_name = 'Fruits'  # Replace with the actual column name
df = pd.read_csv(csv_file)
column_values = df[column_name].tolist()

# Load the XML file
xml_file = 'test.xml' #Replace with xml filee
tree = ET.parse(xml_file)
root = tree.getroot()

# Define the XML namespace
namespace = {'html': 'http://www.w3.org/TR/html4/'}

# Find the <tr> element to add <td> elements
tr_element = root.find('.//{http://www.w3.org/TR/html4/}tr')

# Find the <td> elements and update their text content
for value in column_values:
    td_element = ET.Element('{http://www.w3.org/TR/html4/}td')
    td_element.text = value
    tr_element.append(td_element)

# Save the updated XML file
updated_xml_file = 'updated_xml_file.xml'
tree.write(updated_xml_file, xml_declaration=True, encoding='utf-8', method='xml', default_namespace=namespace['html'])
