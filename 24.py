import configparser
config = configparser.ConfigParser()

print("Read the file")
config.read("config_24.txt")
print("\n")
print("Once you read you get the data in and can play with it")
l1 = config.sections()
print(config[l1[0]]['User'])
print("\n")
print("To access the DEFAULT section, do it directly - it won't show up in sections()")
print(config['DEFAULT']['ForwardX11'])
