import os 
from argparse import ArgumentParser
import sys

from weatherterm.core import parser_loader
from weatherterm.core import ForecastType
from weatherterm.core import Unit
from weatherterm.core import SetUnitAction

def _validate_forcast_args(args):
    if args.forcast_option is None:
        err_msg = ('one of these arguments must be used :-td/--today , -5d/--fivedays , -10d/--tendays , -w/--weekend')
        print(f'{argparser.prog}: error:{err_msg}' , file= sys.stderr)
        sys.exit()

parsers = parser_loader.load('./weatherterm/parsers')

argparser = ArgumentParser(prog = 'weatherterm' , description='weather info from weather.com on your terminal')

required = argparser.add_argument_group('required arguments')

required.add_argument('-p' , '--parser' , choices = parsers.keys(), required = True , dest = 'parser' , help = ('specify which parser is going to be used to scrape weather infomation'))

unit_values = [name.title() for name , value in Unit.__members__.items()]

argparser.add_argument('-u' , '--unit' , choices = unit_values , required = False , dest = 'unit', action = SetUnitAction , help = ('specify the unit that will be used to display the tempratures.'))

required.add_argument('-a' , '--areacode' , required = True , dest = 'area_code' , help = ('the code area to get the weather boadcast from it can be obtained at http://weather.com'))

argparser.add_argument('-v' , '--version' , action = 'version' , version = '%(prog)s 1.0')
argparser.add_argument('-td' , '--today' , dest = 'forecast_option' , action = 'store_const' , const = ForecastType.TODAY , help = 'show the weather forcast for the current day')

args = argparser.parse_args()

_validate_forecast_args(args)

cls = parsers[args.parser]
parser = cls()
results= parser.run(args)
for result in results:
    print(result)