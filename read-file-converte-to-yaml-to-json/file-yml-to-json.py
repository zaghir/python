import yaml
import json
import ruamel.yaml

in_file = "reponse-test-format.yaml"
out_file = 'output.json'

s = ""
#with open(in_file) as f:
#    print(yaml.load(f))
#    print(json.dumps(yaml.load(f)))
#
#yaml = ruamel.yaml.YAML(typ='safe')

with open(in_file, 'r') as yaml_in, open(out_file, "w") as json_out:
    yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
    print(yaml_object)
    json.dump(yaml_object, json_out)


#yaml = ruamel.yaml.YAML(typ='safe')
#with open(in_file) as fpi:
#    data = yaml.load(fpi)
#with open(out_file, 'w') as fpo:
#    json.dump(data, fpo, indent=2)
