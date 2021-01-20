import argparse
import importlib
import os

from Controllers.CliController import CliController


class RunManager:
    """
    Class RunManager to run managers from command line
    Usage: 
        python3 CliRunInterface.py --manager={ManagerName without 'Manager'} --action={Action name}
    """

    managerName = ""
    actionName = ""
    paramValue = ""
    scriptName = ""

    manager = None
    action = None
    script = None

    interpreter = "python3"
    scriptsFolder = "Scripts"

    def parseCli(self):
        parser = argparse.ArgumentParser(description='Cli interface for schedule bot')

        parser.add_argument("--manager")
        parser.add_argument("--action")
        parser.add_argument("--param")
        parser.add_argument("--script")
        parser.add_argument("--config")

        args = parser.parse_args()

        if args.manager:
            self.managerName = args.manager + "Manager"
        if args.action:
            self.actionName = args.action
        if args.param:
            self.paramValue = args.param
        if args.script:
            self.scriptName = args.script
        if args.config:
            os.environ[CliController.env_var_name] = args.config

    def getManager(self):
        foo = importlib.import_module(self.managerName)
        self.manager = getattr(foo, self.managerName)

    def runAction(self):
        self.action = getattr(self.manager, self.actionName)
        if self.paramValue:
            self.action(self.paramValue)
        else:
            self.action()

    def getScript(self):
        foo = importlib.import_module(f'{self.scriptsFolder}.{self.scriptName}')
        self.script = getattr(foo, "main")

    def run(self):
        self.parseCli()
        if self.managerName:
            self.getManager()
            self.runAction()
        elif self.scriptName:
            self.getScript()
            self.script()


if __name__ == '__main__':
    cli = RunManager()
    cli.run()
