# find file on computer
# https://pythonprogramminglanguage.com
import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

# find returns a list, specify search and directory
result = find('*.zip', '/home/linux/Downloads/')
print(result)
