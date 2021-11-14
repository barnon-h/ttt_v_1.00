#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: M Barnon

# ####################### Imports ###########################
import sys
sys.path.append('./src')
from gui import Window
from tui import run
# ###########################################################



# ##################### Driver Code #########################
if __name__ == "__main__":
    if '-t' in sys.argv or '--tui' in sys.argv:
        run()
    else:
        w = Window()
    main()
# ###########################################################
# ######################### EOF #############################
