import argparse
import importlib


class CliController:


    manager = ""
    action = ""


    def parseCli(self):
        parser = argparse.ArgumentParser(description='Cli interface for schedule bot')
        parser.add_argument("--manager")
        parser.add_argument("--action")
        args = parser.parse_args()
        self.manager= args.manager + "Manager"
        self.action = args.action
        print(self.manager, self.action)


    def getController(self):
        i = importlib.import_module(self.manager)
        i.BotManager.sayHello(self)


if __name__ == '__main__':
    cli = CliController()
    cli.parseCli()
    cli.getController()