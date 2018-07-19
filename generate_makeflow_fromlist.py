#!/usr/bin/python
#title           :generate_makeflow_fromlist.py
#author          :Bala
#date            :July-17-2018
#version         :1.0
#usage           :python program.py 
#notes           :Generates a makeflow file based on input values available from a file
#python_version  :2.7


def get_programargs_from_listfile(input_listfile):
    """ Get input file information """
    program_args = [ ]
    program_files = [ ]
    with open(input_listfile) as f:
        for line in f:
            new_line = line.rstrip()
            line_split = new_line.split(" ")
            if(len(line_split) > 2):
                file_list = [ ]
                inputref_file1 = line_split[11]
                inputref_file2 = line_split[13]
                input_file = line_split[15]
                output_file = line_split[19]
                file_list.append(inputref_file1) 
                file_list.append(inputref_file2) 
                file_list.append(input_file) 
                file_list.append(output_file) 
                program_files.append(file_list)
                program_args.append(new_line)
    return program_args, program_files


if __name__ == '__main__':
    """ Generate makeflow file from a design file"""
    wrapper_file = "wrapper.sh"
    exe_file = "SMOTNT_working_osg_static"
    wrapper_file_with_path = "./" + wrapper_file
    full_arg_list, file_list = get_programargs_from_listfile("argarray_1.txt")
    for i in range(1, len(full_arg_list)):
        input_file_with_path = "./exp1/"+file_list[i][2]
        print "  " 
        print file_list[i][3], ":", file_list[i][0], file_list[i][1], input_file_with_path, wrapper_file, exe_file
        print "     ", wrapper_file_with_path, full_arg_list[i]
        print "  " 
        



