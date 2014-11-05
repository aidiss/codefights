"""
Author: Aidis Stukas, Jurgis Pralgauskis
"""
from boilerplate.SDK import SDK
import sys

#SDK.run(["", "--fight-me"])
SDK.run(sys.argv)



# Issues
### Myfighter and boxer are moved to SDK instead of separate files
### SDK.run uses shortcut instead of commandline argvs
###its always boxer