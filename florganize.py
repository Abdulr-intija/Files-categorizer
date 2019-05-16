import os
import argparse
import subprocess
import extension_dictionary 
 
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--dir_path', type=str, help='Path to the directory whose files should be categorized')
arg_parser.add_argument('--op_type', type=str, help='Type of operation to be performed')
args = arg_parser.parse_args()

# some check ups before using specified path
assert (args.dir_path is not None), "You have to input a valid path to a directory first by setting --dir_path"
assert (args.op_type is not None and (args.op_type == "undo" or args.op_type == "smart" or args.op_type == "normal")), "You have to input the type of operation you want to perform e.g undo, smart, normal"
assert (len(os.listdir(args.dir_path)) != 0), "No files to categorize here. Must be a dir with FiLEs"



# get the extension of a file
def getExtension(file_name):
    dot_split = file_name.split('.')
    return dot_split[len(dot_split) - 1].lower()

# rename Existing file
def renameFile(file_name):
    arr = file_name.split('.')
    ext = arr[-1]
    file = arr[-2]
    last_char = file[-1]
    if last_char.isdigit():
        return file +str(int(last_char)+1)+"."+ext
    else:
        return file+"_1"+"."+ext


# move to specified directory
os.chdir(args.dir_path)

# check if a file has extension
def hasExtension(file_name):
    return len(file_name.split('.')) > 1
 
dictionary = extension_dictionary.dic()

#file to store name of new folders created 
memory = '.febvyrfrehfeyrfevfka3434ufdemeoy.txt' 
def s_categorize(dir_path): 
    print("\nCategorizing... chill for some millisecs\n")
    for current_file in os.listdir(dir_path):  
        if hasExtension(current_file):
            if getExtension(current_file) not in dictionary:
                new_dir = getExtension(current_file) + " files"
            else:
                new_dir = dictionary[getExtension(current_file)] 
            
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
                #write name of current created directory to memory
                o=open(memory,"a")
                o.write(new_dir+'\n')
                o.close()
            #prevent from categorizing memory file
            if current_file != memory:
                #check if file name conflict with any one in the new directory
                if current_file in os.listdir(dir_path+'\\'+new_dir):
                    temp_file = current_file
                    while temp_file in os.listdir(dir_path+'\\'+new_dir): 
                        temp_file = renameFile(current_file)
                    os.rename(current_file, new_dir +'/'+ temp_file)    
                else:    
                    os.rename(current_file, new_dir +'/'+ current_file)
    #hide the memory file            
    subprocess.check_call(["attrib","+H",memory])            
    print("Files categorized!..")

    
def n_categorize(dir_path ):
    print("\nCategorizing... chill for some millisecs\n")
    for current_file in os.listdir(dir_path):  
        if hasExtension(current_file):
            new_dir = getExtension(current_file) + " files"
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
                #write name of current created directory to memory
                o=open(memory,"a")
                o.write(new_dir+'\n')
                o.close()
            #prevent from categorizing memory file
            if current_file != memory :
                #check if file name conflict with any one in the new directory
                if current_file in os.listdir(dir_path+'\\'+new_dir):
                    temp_file = current_file
                    while temp_file in os.listdir(dir_path+'\\'+new_dir): 
                        temp_file = renameFile(current_file)
                    os.rename(current_file, new_dir +'/'+ temp_file)    
                else:    
                    os.rename(current_file, new_dir +'/'+ current_file)
    #hide the memory file            
    subprocess.check_call(["attrib","+H",memory])            
    print("Files categorized!..")
  
    
def undo( root_dir_path):
    #check if memory file is present.(If it's present, that folder has been categorized before.
    if memory in os.listdir(root_dir_path):    
        o=open(memory,"r")
        newly_created_dir = o.readlines()  
        for new in newly_created_dir:
            new_name = new.strip('\n')
            #folder that has been florganized before contains memory file and is left unaltered.
            if memory not in os.listdir(args.dir_path+'\\'+new_name): 
                for current_file in os.listdir(args.dir_path+'\\'+new_name) : 
                    os.rename(new_name+'/' +current_file, current_file)       
                os.rmdir(new_name)   
        o.close()
        os.remove(memory)
        print("Undo Successful!..")
    else:
        print('undo not enabled yet')
#checks whether the operation type argument        
if args.op_type == 'undo' :
    undo( args.dir_path)             
elif args.op_type == 'smart' :   
    s_categorize(args.dir_path )
elif args.op_type == 'normal' :
    n_categorize(args.dir_path )
     
