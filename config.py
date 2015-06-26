__author__ = 'MrMindImplosion'

import os
import shutil
import configparser


def getConfiguration(confName):
    """Copies default configurations when they don't exist.
    confName argument should be the configuration file - '.ini'
    """

    if os.path.exists(os.path.join("configs", confName+".ini")):
        config = configparser.ConfigParser()
        config.read(os.path.join("configs", confName+".ini"))

        defConfig = configparser.ConfigParser()
        defConfig.read(os.path.join("configs", "default", confName+".ini"))

        if config.get("versioning", "version") < defConfig.get("versioning", "version"):
            print("Warning: Your config file '%s' needs updating. You should probably stop here and edit it." % confName)
        else:
            return config
    else:
        print("No config for '%s' existed. Copying default. You should probably stop here and edit it." % confName)
        shutil.copy(os.path.join("configs", "default", confName+".ini"), os.path.join("configs", confName+".ini"))
        return getConfiguration(confName)

# unit test

if __name__ == "__main__":
    conf = getConfiguration("bot")
    print(conf.get("bot", "apikey"))