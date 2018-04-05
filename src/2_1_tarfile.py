import tarfile
import glob


def create_tarfile():
    tfile = tarfile.open("mytarfile.tar", "w")
    for config_file in glob.glob("~"):
        tfile.add(config_file)
    tfile.close()


create_tarfile()