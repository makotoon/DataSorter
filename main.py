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

import glob
import re

import data_sort
import data_analyze

data_sort    = data_sort.data_sort()
data_analyze = data_analyze.data_analyze()

def main():
   csv_dir   = "./csv_data"

   csv_files = glob.glob(csv_dir + "/*.csv")
   for csv_file in csv_files:
      if re.match(r'.*_analyzed\.csv', csv_file):
         print("# Skipping   : " + csv_file)
         continue
      else:
         print("# Processing : " + csv_file)
         dat           = data_sort.saleae(file=csv_file, data_type="SPI", file_type="CSV")
         dat_analyzed  = data_analyze.hex_log(list_data=dat, rule_file="./data_analysis_config.csv", org_file=csv_file, out_file=True, type="SPI")  

if __name__=='__main__':
   main()