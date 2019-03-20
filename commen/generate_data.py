import configparser
import os.path

class Data():

    def __init__(self):
        self.filePath = './config/config.ini'

    def get_test_data(self):
        config = configparser.ConfigParser()
        config.read(self.filePath)
        getHbib = config['ApiUrl']['GetHbib']
        hbibJson = config['SchemaName']['hbib']
        return getHbib,hbibJson