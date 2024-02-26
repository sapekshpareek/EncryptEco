import re

def finder(string, substring):
  indices = [m.start() for m in re.finditer(substring, string)]
  return indices


def convert(string):
  li = list(string.split(" "))
  return li
