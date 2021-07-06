class bcolors:
    """Colors for 8/16 color bash"""
    
    # Set
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m' # Invert the foreground and background colors
    HIDDEN = '\033[8m' # Useful for passwords

    # Reset
    ENDC = '\033[0m'
    ENDBOLDBLINK = '\033[21m'
    ENDDIM = '\033[22m'
    ENDUNDERLINE = '\033[24m'
    ENDBLINK = '\033[25m'
    ENDREVERSE = '\033[27m'
    ENDHIDDEN = '\033[28m'

    # Foreground
    FDEFAULT = '\033[39m'
    FBLACK = '\033[30m'
    FRED = '\033[31m'
    FGREEN = '\033[32m'
    FYELLOW = '\033[33m'
    FBLUE = '\033[34m'
    FMAGENTA = '\033[35m'
    FCYAN = '\033[36m'
    FLIGHTGRAY = '\033[37m'
    FDARKGRAY = '\033[90m'
    FLIGHTRED = '\033[91m'
    FLIGHTGREEN = '\033[92m'
    FLIGHTYELLOW = '\033[93m'
    FLIGHTBLUE = '\033[94m'
    FLIGHTMAGENTA = '\033[95m'
    FLIGHTCYAN = '\033[96m'
    FWHITE = '\033[97m'

    # Foreground
    BDEFAULT = '\033[49m'
    BBLACK = '\033[40m'
    BRED = '\033[41m'
    BGREEN = '\033[42m'
    BYELLOW = '\033[43m'
    BBLUE = '\033[44m'
    BMAGENTA = '\033[45m'
    BCYAN = '\033[46m'
    BLIGHTGRAY = '\033[47m'
    BDARKGRAY = '\033[100m'
    BLIGHTRED = '\033[101m'
    BLIGHTGREEN = '\033[102m'
    BLIGHTYELLOW = '\033[103m'
    BLIGHTBLUE = '\033[104m'
    BLIGHTMAGENTA = '\033[105m'
    BLIGHTCYAN = '\033[106m'
    BWHITE = '\033[107m'

    
    
    
    def get(color=0):
        pass
