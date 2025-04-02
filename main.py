import xml.etree.ElementTree as ET
import openpyxl

def load_excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    mappings = []

    for row in sheet.iter_rows(min_row=2,
    values_only=True): #min row 2 to account for header
        db,schema = row
        if db and schema:
            mappings.append((str(db).strip(),str(schema.strip())))

    return mappings

def load_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    #ET.dump(root)
    return tree,root

def update_introspection_scope(root, mappings):
    for data_source in root.findall(".//data-source"):
        schema_mapping = data_source.find("schema-mapping")
        if schema_mapping is None:
            schema_mapping = ET.SubElement(data_source, "schema-mapping")

        
        for scope in schema_mapping.findall("introspection-scope"):
            schema_mapping.remove(scope)

        
        new_scope = ET.SubElement(schema_mapping, "introspection-scope")
        top_node = ET.SubElement(new_scope, "node", negative="1")

        for db_name, schema_name in mappings:
            db_node = ET.SubElement(top_node, "node", kind="database", name=db_name)
            ET.SubElement(db_node, "node", kind="schema", name=schema_name)


#does not account for multiple data sources
def delete_all_introspection_scopes(root):
    for data_source in root.findall(".//data-source"):
        scopes = data_source.findall("introspection-scope")
        for scope in scopes:
            data_source.remove(scope)           
            

if __name__ == "__main__":  
    excel_path = "schema_map.xlsx"
    xml_path = "dataSources.local.xml"
    
    mappings = load_excel("schema_map.xlsx")
    tree,root = load_xml(xml_path)
    delete_all_introspection_scopes(root)
    update_introspection_scope(root,mappings)
    tree.write(xml_path, encoding="UTF-8", xml_declaration=True)

    print(f"updated {xml_path} with {len(mappings)} schema squeezins")
    
    
