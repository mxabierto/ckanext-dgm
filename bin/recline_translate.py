import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import json
from shutil import copy

inputfile = '/usr/lib/ckan/default/src/ckan/ckanext/reclinepreview/theme/public/vendor/recline/recline.js'
outputfile = 'output1.js'
json_i18n = open('es.json', 'r')
data = json.load(json_i18n)


f = open(inputfile)
o = open(outputfile, 'a')

mydict = {}

for i in data['strings']:
    mydict.update(i)


def translate(text, mydict):
    rc = re.compile(r'(?<![\.\w])(?<![\(\'])(?<!\=\s)(?<![\&-]\s)(?<![\:\s])(' + '|'.join(mydict.keys()) + r')(?!\w)(?![\.\:])(?!\ = )(?![\(])')

    def replace_all(match):
        return mydict[match.group(0)]
    return rc.sub(replace_all, text)


for line in f:
    newline = translate(line, mydict)
    o.write(newline)
o.close()

copy(inputfile, inputfile+".bak")
copy(outputfile, inputfile)

copy('preview_recline_es.js', '/usr/lib/ckan/default/src/ckan/ckanext/reclinepreview/theme/public/preview_recline.js')
