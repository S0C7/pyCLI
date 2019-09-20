import click
from pyfiglet import Figlet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
version='1.0.0'

class Config(object):

    def __init__(self):
        self.verbose=False
        self.version='1.0.0'

pass_config = click.make_pass_decorator(Config, ensure=True)
config = Config()
f = Figlet(font='slant')
#print(config.version)
print(Fore.CYAN + Style.BRIGHT + f.renderText('help cli'))
print(Fore.YELLOW + config.version)

@click.group()
@click.option('--verbose', is_flag=True,
                help="Enable verbose mode")
@pass_config
def cli(config, verbose):
    """
        This is main help cli which has a verbose OPTION and say COMMAND.
    """
    config.verbose=verbose

    # if verbose:
    #         click.echo('We are in verbose mode...')

@cli.command()
@click.option('--greeting', default='Hello', 
                help='Greeting name')
@click.option('--name', default='John', prompt='Your name',
                help='Name of the person to be greeted')
@click.option('--repeat', default=1, type=int, 
                help='Number of times the text should be repeated')
@click.argument('outfile', type=click.File('w'), default='-', 
                required=False)
@pass_config
def say(config, greeting, name, repeat, outfile):
    """
        This is a test cli to learn  CLICK framework 
    """
    #print(outfile)
    #print('Hello', greeting)
    #print(greeting,name+'!')
    if config.verbose:
        click.echo('We are in verbose mode!')
    for x in range(repeat):
        # click.echo(message=greeting+name+str(x+1), file=outfile)
        click.echo(click.style(greeting+name+str(x+1),fg='red',bg='white'))
    #print('Hello World!')