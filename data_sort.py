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

class data_sort:
    def saleae(self, file:str, data_type:str="SPI", file_type:str="CSV") -> list:
        if file_type.upper() in {"CSV"}:
            dat = []
            with open (file, 'r') as f:
                r = csv.reader(f)
                if data_type.upper() in {"SPI"}:
                    # Expected data format
                    # Column No. : 0,            1,          2,           3
                    # Column     : "Time [s]", "Packet ID", "MOSI",      "MISO"
                    # Data       : float,        int,        hex(0x..),   hex(0x..)

                    i = 0
                    line = []
                    dat_tmp =[]
                    for line in r:
                        if line == []:
                            break

                        if len(line) < 4 or line.count(""):
                            print("  # Invalid line skipped : {0}".format(line))
                            continue

                        if i == 0:
                            dat.append(line)
                        else:
                            if i == 1:
                                dat_tmp = line
                                pass
                            else:  
                                if line_pre[1] == line[1]:
                                    dat_tmp[2] = dat_tmp[2] + line[2][2:]  # cosndier using removeprefix() for python 3.9 and later
                                    dat_tmp[3] = dat_tmp[3] + line[3][2:]  # cosndier using removeprefix() for python 3.9 and later
                                else: 
                                    dat.append(dat_tmp)
                                    dat_tmp = line
                                        
                        i += 1
                        line_pre = line
                    else:
                        dat.append(dat_tmp)

        return dat





