#!/usr/bin/env python
# coding: utf-8

from .build import build
from .config import load_config
from .gh_deploy import gh_deploy
from .new import new
from .serve import serve
import sys


def arg_to_option(arg):
    """
    Convert command line arguments into two-tuples of config key/value pairs.
    """
    arg = arg.lstrip('--').replace('-', '_')
    if '=' in arg:
        return arg.split('=', 1)
    return (arg, True)


def main(cmd, args, options=None):
    """
    Build the documentation, and optionally start the devserver.
    """
    if cmd == 'serve':
        config = load_config(options=options)
        serve(config, options=options)
    elif cmd == 'build':
        config = load_config(options=options)
        build(config)
    elif cmd == 'gh-deploy':
        config = load_config(options=options)
        build(config)
        gh_deploy(config)
    elif cmd == 'new':
        new(args, options)
    else:
        print 'mkdocs [help|new|build|serve] {options}'


def main_entry_point():
    """
    Invokes main() with the contents of sys.argv

    This is a separate function so it can be invoked
    by a setuptools console_script.
    """
    cmd = sys.argv[1] if len(sys.argv) >= 2 else None
    opts = [arg_to_option(arg) for arg in sys.argv[2:] if arg.startswith('--')]
    main(cmd, args=sys.argv[2:], options=dict(opts))

if __name__ == '__main__':
    main_entry_point()
