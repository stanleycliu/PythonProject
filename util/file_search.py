import os
import re

def find_string_in_files(folder_path,search_string,file_type=''):
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_type):
                file_path = os.path.join (root, file)
                if os.path.isfile(file_path):
                    try:
                        with open(file_path,'r',encoding='utf-8') as f:
                            contents = f.read()
                            if re.search(search_string, contents):
                                print(f"found '{search_string}' in file: {file_path}")
                    except:
                        pass 


        
if __name__=="__main__":
    keyword=['Harvard','Columbia']
    file_type='csv'
    #path = r'C:\code\PythonCode'
    path = r'C:\Users\chliu\OneDrive\Documents\Life\Ashley'
    
    for item in keyword:
        find_string_in_files(path,item,file_type)
    
    
                        
                    