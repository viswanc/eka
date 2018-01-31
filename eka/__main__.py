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
    from eka.core import init
    init(argv)

def show_usage():
  print 'Usage:\n\t$ eka (path) [options]'

if __name__ == '__main__':
  main()
