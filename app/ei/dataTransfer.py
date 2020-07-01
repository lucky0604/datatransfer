import os
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import xml.dom.minidom as xml


class DataTransfer(object):

    def __init__(self, dirName):
        self.dirName = dirName

    def transferData(self, file):
        if file.split('.')[2] != 'py' and file.split('.')[2] != 'xml':
            print(file, ' file -----')
            new_xml = ET.Element('annotations')
            object = ET.SubElement(new_xml, "object")
            doc = xml.Document()
            declaration = doc.toxml()
            xml_string = ET.tostring(new_xml)
            xml_write = parseString(xml_string).toprettyxml()[
                len(declaration):]
            print(xml_write)
            with open('test.xml', 'w') as handle:
                handle.write(xml_write)

    def getData(self, dirName):
        files = []
        for root, dirs, filename in os.walk(dirName):
            for singleFile in filename:
                self.transferData(os.path.join(root, singleFile))


transDir = DataTransfer('./')
transDir.getData('./')
