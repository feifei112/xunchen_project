import yaml

from conftest import BASE_DIR


def data_yaml():
    # with open("./logn_data.yaml",encoding="utf-8") as f:
    with open(BASE_DIR + "/data/logn_data.yaml",encoding="utf-8") as f:

        data = yaml.safe_load(f)
        data_list = []
        for n in data:
            data_list.append((n.get("phone"),n.get("pwd")))
        print(data_list)
        return data_list

if __name__ == "__main__":
    print(data_yaml())
