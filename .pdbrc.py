import pdb
from pygments.formatters import TerminalFormatter, Terminal256Formatter

class Config(pdb.DefaultConfig):
    sticky_by_default = True
    formatter = Terminal256Formatter(bg='dark', style='paraiso-dark')
