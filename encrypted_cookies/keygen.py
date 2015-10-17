# -*- coding: utf-8 -*-
# (c) 2015 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
import optparse
import sys

from  cryptography.fernet import Fernet


def main(stdout=sys.stdout, argv=sys.argv[1:]):
    p = optparse.OptionParser(
        usage='%prog [options]\n\n'
              'Generates a suitable value to put in '
              'your ENCRYPTED_COOKIE_KEYS=[...] setting.')
    (options, args) = p.parse_args(argv)
    o = Fernet.generate_key()
    stdout.write(o.decode("utf-8"))


if __name__ == '__main__':
    main()
