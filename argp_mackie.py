import json
import argparse

parser = argparse.ArgumentParser(description='write changed content in new file')
parser.add_argument('--inp_file', required=True, help=('write here name of the file'))
args = parser.parse_args()

def replace_voc(inp_file):

    with open(inp_file, encoding='utf-8') as poem_file:
        material = poem_file.read()
        jsondict = open('voc.json')
        dicto = json.load(jsondict)
        for voc, voc_num in dicto.items():
            material = material.replace(voc, str(voc_num))  
    
    with open('new_mackie.txt', 'a') as nf:
        nf.write(material + '\n' + '\n')
        nf.close()
    with open('new_mackie.txt') as nf:
        new_content = nf.read()
        return new_content

print(replace_voc(args.inp_file))
