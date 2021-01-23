import os
import argparse
import importlib


class CliArgsController:

    configs_folder = 'Configs'

    default_config_name = 'main'

    config_env_var_name = 'SCHEDULE_CONFIG_NAME'

    def parseArgs(self):
        """Parse Bot cli args and set environment variables.

        Currently available args is:
            -c --config Application configuration file choose
        """
        parser = argparse.ArgumentParser(description='Cli args bot handler')

        parser.add_argument(
            "-c",
            "--config",
            default=self.default_config_name,
            help="chose config Bot.py running with"
        )

        args = parser.parse_args()

        if args.config:
            CliArgsController.setEnv(
                self.config_env_var_name,
                args.config
            )

    @staticmethod
    def getConfig():
        """Get application config by config environment variable value."""

        config_name = os.environ.get(CliArgsController.config_env_var_name)
        if not config_name:
            config_name = CliArgsController.default_config_name
        return importlib.import_module(f'{CliArgsController.configs_folder}.{config_name}')

    @staticmethod
    def setEnv(env, val):
        """Set environment variable."""
        os.environ[env] = val
