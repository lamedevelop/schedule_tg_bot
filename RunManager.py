import argparse
import importlib

from Controllers.CliArgsController import CliArgsController


class RunManager:
    """
    Class RunManager to run managers from command line.

    RunManager allows to run any static method of any manager.

    Usage: 
        >> python3 RunManager.py --manager={ManagerName without 'Manager'} --action={Action name}
        >> python3 RunManager.py --manager={ManagerName without 'Manager'} --action={Action name} --param={Single method parameter}
        >> python3 RunManager.py --script={Script name}
        >> python3 RunManager.py --script=utils.{Script name in utils folder}

        >> python3 RunManager.py --config={Config name} --script={Script name}
        >> python3 RunManager.py --config={Config name} --manager={ManagerName without 'Manager'} --action={Action name}
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
        """Parse cli args."""

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
            CliArgsController.setEnv(
                CliArgsController.config_env_var_name,
                args.config
            )

    def getManager(self):
        """Import manager by name."""
        foo = importlib.import_module(self.managerName)
        self.manager = getattr(foo, self.managerName)

    def runAction(self):
        """Run required action of manager."""
        self.action = getattr(self.manager, self.actionName)
        if self.paramValue:
            self.action(self.paramValue)
        else:
            self.action()

    def getScript(self):
        """Import script module."""
        foo = importlib.import_module(f'{self.scriptsFolder}.{self.scriptName}')
        self.script = getattr(foo, "main")

    def run(self):
        """Parse params and run action of manager or script."""
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
