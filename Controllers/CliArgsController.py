import os
import argparse
import importlib


class CliArgsController:

    config = ''

    configs_folder = 'Configs'

    default_config_name = 'main'

    config_env_var_name = 'SCHEDULE_CONFIG_NAME'

    def parseArgs(self):
        parser = argparse.ArgumentParser(description='Cli args bot handler')

        parser.add_argument(
            "-c",
            "--config",
            default=self.default_config_name,
            help="chose config Bot.py running with"
        )

        args = parser.parse_args()

        if args.config:
            os.environ[self.config_env_var_name] = args.config

    def getConfig(self):
        config_name = os.environ.get(self.config_env_var_name)
        if not config_name:
            config_name = self.default_config_name
        return importlib.import_module(f'{self.configs_folder}.{config_name}')
