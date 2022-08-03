import os

"""RUN AT YOUR OWN RISK"""

dir_name = os.getcwd()
test = os.listdir(dir_name)
c = 0

for item in test:
    if item.startswith("pinglog_") and item.endswith(".log"):
        print(f"Deleting <{item}>")
        c += 1
        os.remove(os.path.join(dir_name, item))
print(f"Deleted <{c}> items")
