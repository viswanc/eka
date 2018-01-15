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
    from os import path

    target_path = argv.pop(0)

    sys.argv = sys.argv[:1] + argv # Alter sys.argv so that the modules could process them.

    if target_path:
      if path.isdir(target_path):
        target_path += '/master.yml'

      print target_path

    else:
      show_usage()

def show_usage():
  print 'Usage:\n\t$ eka (path)'

if __name__ == '__main__':
  main()
