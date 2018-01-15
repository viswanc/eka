"""
Eka - Core.
"""
from os import path
import yaml

# Helpers
# None, yet.

# Exports
def load(target_path):
  if path.isdir(target_path):
    target_path += '/master.yml'

  else:
    if not path.isfile(target_path):
      raise Exception('File not found: %s' % target_path)

  return yaml.safe_load(open(target_path, 'r'))
