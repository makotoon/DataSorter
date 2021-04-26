import csv
import copy

class data_analyze:
    def hex_log(self, list_data:list, rule_file:str, org_file:str, out_file:bool=True, type:str="SPI") -> list:
        list_data_tmp = copy.deepcopy(list_data)
        if type.upper() in {"SPI"}:
            with open (rule_file, 'r', encoding="cp932") as f:
                # Column No. : 0,         1,           2
                # Detail     : Condition, Description, Target
                csv_rule = csv.reader(f)
                list_rule = [row for row in csv_rule]

            for data in list_data_tmp[1:]:  #list_data[0] is label
                data += ['', '']
                for rule in list_rule:
                    hex_str_mosi, hex_str_miso = data[2], data[3]


                    if rule[2].upper() in {"MOSI", "MASTER", "-"}:
                        if eval(rule[0].replace("hex_str", "hex_str_mosi")):
                            if data[4] != '':
                                data[4] = data[4] + "\n" + rule[1]
                            data[4]  = data[4] + rule[1] 

                    if rule[2].upper() in {"MISO", "SLAVE", "-"}:
                        if eval(rule[0].replace("hex_str", "hex_str_miso")):
                            if data[5] != '':
                                data[5] = data[5] + "\n" + rule[1]
                            data[5]  = data[5] + rule[1]

            if out_file == True:
                with open (org_file.rstrip(".csv") + "_analyzed.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(list_data_tmp)


        return list_data_tmp





