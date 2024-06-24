from dir_monitor import DirMonitor


if __name__ == '__main__':
    d1 = DirMonitor("tmp")
    print("The MP3 Converter starts")
    d1.watch()