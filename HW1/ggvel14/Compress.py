# -*- coding: utf-8 -*-
import helper,sys
code=open(sys.argv[1]).read().split()
dic=helper.buildCodeDictionary(code)
helper.completeWrite(''.join([dic[x] for x in open(sys.argv[2]).read()]),sys.argv[3])