# -*- coding: utf-8 -*-
import sys

#-------------------------------------------------------#
def read_file(plots_fname,names_fname):
    lines=[]
    for line in open(plots_fname,'r'):
        lines.append(line[:-1].split(','))

    for line in open(names_fname,'r'):
        name = line[:-1].split(',')

    return name,lines
#-------------------------------------------------------#
def write_file(name,lines,wfname):
    f = open(wfname,'w')

    f.writelines(["{","\n" ])
    f.writelines(['"nodes" : [',"\n" ])
    for i in range(len(name)):
        f.writelines(["{","\n"])
        f.writelines(['"id" : ', '"',str(i),'"',",","\n"])
        f.writelines(['"label" : ', '"',name[i],'"',",","\n"])
        f.writelines(['"x" : ', '"',str(float(lines[i][0])*1000000),'"',",","\n"])
        f.writelines(['"y" : ', '"',str(float(lines[i][1])*1000000),'"',",","\n"])
        f.writelines(['"size" : 3',"\n"])
        if len(name) - 1 != i :
            f.writelines(["},","\n"])
        else:
            f.writelines(["}","\n"])

    f.writelines(["],","\n"])

    f.writelines(['"edges" : [',"\n" ])
    # for i in range(len(name)):
    #     for j in range(i+1,len(name)):
    #         f.writelines(["{","\n"])
    #         f.writelines(['"id" : ', '"',str(i),str(j),'"',",","\n"])
    #         f.writelines(['"source" : ', '"',str(i),'"',",","\n"])
    #         f.writelines(['"target" : ', '"',str(j),'"',"\n"])
    #         if len(name) - 2 != i :
    #             f.writelines(["},","\n"])
    #         else:
    #             f.writelines(["}","\n"])
    f.writelines(["]","\n"])
    f.writelines(["}","\n"])

#-------------------------------------------------------#
def make_json(param):
    plots_fname = "./data/mds_plot.dat"
    names_fname = "./data/cv_list.dat"
    wfname = "./data/nodo_data.json"
    name,lines = read_file(plots_fname,names_fname)
    write_file(name,lines,wfname)
    print("output ",wfname)
#-------------------------------------------------------#
if __name__ == '__main__' :
    make_json(sys.argv)









