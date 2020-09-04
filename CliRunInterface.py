import argparse
import importlib


class CliRunInterface:
    """
    Class CliController to run managers from command line
    Usage: 
        python3 CliRunInterface.py --manager={ManagerName without 'Manager'} --action={Action name}
    """

    managerName = ""
    actionName = ""
    param = ""

    manager = ""
    action = ""

    def parseCli(self):
        parser = argparse.ArgumentParser(description='Cli interface for schedule bot')
        parser.add_argument("--manager")
        parser.add_argument("--action")
        parser.add_argument("--param")
        args = parser.parse_args()
        self.managerName= args.manager + "Manager"
        self.actionName = args.action
        if args.param:
            self.param = args.param

    def getManager(self):
        foo = importlib.import_module(self.managerName)
        self.manager = getattr(foo, self.managerName)

    def runAction(self):
        self.action = getattr(self.manager, self.actionName)
        if self.param:
            self.action(self.manager, self.param)
        else:
            self.action(self.manager)

    def run(self):
        self.parseCli()
        self.getManager()
        self.runAction()


if __name__ == '__main__':
    cli = CliRunInterface()
    cli.run()
