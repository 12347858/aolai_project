import yaml



def read_yaml(filepath,test_key):
    with open("./data/"+filepath,"r",encoding="utf-8") as f:
        data = yaml.load(f)
        #print(data.values())
        data_dict = data[test_key]
        #print(data_dict)
        list_data =[]
        for i in data_dict.values():
            list_data.append(i)
        return list_data


