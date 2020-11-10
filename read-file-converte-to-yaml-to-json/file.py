import yaml
import json
import ruamel.yaml
import sys
print (sys.stdout.encoding)

max_lenght_col = 100 

def add_char_to_str(str , char , max_lenght) :
    tmp = ""
    
    print(f" {max_lenght} - {len(str)} =  {max_lenght - len(str)}")
    for i in range(0 , max_lenght - len(str) , 1 ):
	    tmp += char 
	
    #return str+tmp+'\n'	
    return str+':\n'	

	
def traitement_string(str):
    s = str.replace('\t' ,'  ')	
    s = s.replace('\n' , '')
    s = s.replace('\r' , '')
    #s = s.replace('é' , 'e')
    #s = s.replace('è' , 'e')
    s = s.rstrip()
    s = s.lower()
    if(len(s) < max_lenght_col):
	    return  add_char_to_str(s , " " , max_lenght_col)
    else: 
        return s

    

fr = open("reponse-test.txt", "r" , encoding='utf-8')

#print(fr.read())

#for x in fr:  
#  print(f"{x}  length = {traitement_string(x)}")

lines = fr.readlines()
fr.close()

lines_proesses = ""
for l in lines:  
    lines_proesses += traitement_string(l)
    print(f"{traitement_string(l)}")
  
	
fw = open("reponse-test-format.txt", "w")
fw.write(lines_proesses) 
fw.close()

##  create object Python from yaml file
out_file = 'output.json'
yaml = ruamel.yaml.YAML(typ='safe')

##  create Json file from object Python 
#with open(in_file) as fpi:
#    data = yaml.load(fpi)
data = yaml.load(lines_proesses)
with open(out_file, 'w' ,encoding='utf-8') as fpo:
    json.dump(data, fpo, indent=2 , ensure_ascii=False )

