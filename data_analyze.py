# -*- coding: utf-8 -*-
#
# (https://github.com/makotoon/DataSorter)
#
# ======================================================================================
# Copyright (c) 2021 Makoto Maeda
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, 
# sublicense,and/or sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or 
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ======================================================================================
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





