import os
import argparse
import importlib


class CliController:

    configs_folder = 'Configs'

    default_config_name = 'main'

    env_var_name = 'SCHEDULE_CONFIG_NAME'

    def getConfigName(self):
        parser = argparse.ArgumentParser(description='Cli args handler')
        parser.add_argument(
            "-c",
            "--config",
            default=self.default_config_name,
            help="chose config Bot.py running with"
        )
        args = parser.parse_args()
        return args.config

    def getConfigByArg(self):
        config_name = self.getConfigName()
        return importlib.import_module(f'{self.configs_folder}.{config_name}')

    def getConfig(self):
        config_name = os.environ.get(self.env_var_name)
        if not config_name:
            config_name = self.default_config_name
        return importlib.import_module(f'{self.configs_folder}.{config_name}')

    def getMainConfig(self):
        return importlib.import_module(f'{self.configs_folder}.{self.default_config_name}')

    def setConfigName(self, configName):
        os.environ[self.env_var_name] = configName

