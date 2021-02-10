from wc_parameter import Parameter as pm

import io



paramListPath = "D:\MAIN DRIVE\RUN DRIVE\PYTHON\Projects\WordCloudMode\paramListPath.txt"
paramList = []

#each parameter of the wordclod main function is treated as an instance itself


with open(file=paramListPath,mode='r', encoding="UTF-8") as text_file:
    r = text_file.readlines()
    for line in r:
        name, defaut_value, target, data_type, value_mode = line.split(",")

        parameter = pm(name=name, defaut_value=defaut_value, target=target,data_type=data_type, value_mode=value_mode)
        paramList.append(parameter)
        
for x in paramList:
    print(x.name)
    








