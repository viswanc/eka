r"""
__main__.py
===========

The console entry point of eka. It could both be used as a script or a python module.

Example:

  $ eka script.py [...]

  $ python -m eka script.py [...]

"""
def main():
  import sys
  argv = sys.argv[1:]

  if not argv:
    show_usage()

  else:
    target_path = argv.pop(0)

    if target_path:
      from . import core
      core.load(target_path)

    else:
      show_usage()

def show_usage():
  print 'Usage:\n\t$ eka (path)'

if __name__ == '__main__':
  main()
