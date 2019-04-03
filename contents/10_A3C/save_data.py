import json
import time

def text_save (data, path = None):
    path = str(int(time.time())) + '.txt' if path is None else path
    print(path)
    file = open(path, 'a')
    file.write(json.dumps(data))
    file.close()
