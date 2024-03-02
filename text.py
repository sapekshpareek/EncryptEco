def convert(string):
  li = list(string.split(" "))
  return li

def read(file):
  with open(file) as f:
    data = f.read()
    return data
