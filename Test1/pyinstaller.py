import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts = ['app.py', '-w', '--icon=vase.ico']
    run(opts)