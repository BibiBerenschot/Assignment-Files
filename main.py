__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

def main():    

#----------------------------------------------------------------------

#Question 1
def clean_cache():
    import os.path, os, shutil
    current_directory = str(os.getcwd())
    cache_folder_in_directory = current_directory + '\\cache'
    cache_folder_exists = os.path.exists(cache_folder_in_directory)
    if cache_folder_exists == True:
        shutil.rmtree(cache_folder_in_directory)
    os.mkdir(cache_folder_in_directory)

#Question 2
def cache_zip(path_to_zip: str, path_to_cache_dir: str):
    from zipfile import ZipFile
    with ZipFile(path_to_zip, 'r') as zip_to_unpack:
        zip_to_unpack.extractall(path_to_cache_dir)

#Question 3
def cached_files():
    import os, os.path
    cache_folder = os.getcwd() + '\\cache'
    list_of_files_in_cache = os.scandir(cache_folder)
    list_of_absolute_paths = []
    for file in list_of_files_in_cache:
        absolute_path = os.path.abspath(file)
        list_of_absolute_paths.append(absolute_path)   
    return list_of_absolute_paths
    
#Question 4
def find_password(list_of_file_paths: list):
    for text_file in list_of_file_paths:
        with open(text_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'password' in line:
                    line_with_password = line[line.find(' ')+1:-1]
                    break
    return line_with_password

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
