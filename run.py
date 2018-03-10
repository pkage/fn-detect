#!/usr/bin/env python

from fnd import create_app

def main():
    app = create_app()

    app.run(use_reloader=False, host='0.0.0.0')

if __name__ == '__main__':
    main()
