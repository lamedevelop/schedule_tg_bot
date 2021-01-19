import argparse
import importlib


class CliController:

    config_name = ''
    configs_folder = 'Configs'

    def getConfigName(self):
        parser = argparse.ArgumentParser(description='Cli args handler')
        parser.add_argument("-c", "--config", default="main", help="chose config Bot.py running with")
        args = parser.parse_args()
        self.config_name = args.config

    def getConfig(self):
        self.getConfigName()
        return importlib.import_module(f'{self.configs_folder}.{self.config_name}')

    def getMainConfig(self):
        return importlib.import_module(f'{self.configs_folder}.main')
