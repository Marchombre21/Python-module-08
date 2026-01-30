# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    construct.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/30 07:00:33 by bfitte            #+#    #+#             #
#    Updated: 2026/01/30 07:00:34 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

import sys


def main():
    if sys.prefix == sys.base_prefix:
        print("You're not in a virtual environment.")
        print(f"Your global environment's path is: {sys.prefix}")
        print("Current Python: ", sys.executable)
        print("If you want to be in, you have to do these things:")
        print("At the root of your project directory, type the command:")
        print("python3 -m venv .venv")
        print("This will create a hidden directory at the root of your"
              " repository that contain the configuration of your"
              " virtual environment")
        print("Then type the command:")
        print("source .venv/bin/activate")
        print("It will activate the virtual environment.")
        print("To check if you're in, type the command:")
        print("which python3")
        print("If you're in, the path will look like this:")
        print("/home/yourName/path/of/your/repo/.venv/bin/python3")
        print("else:")
        print("/usr/bin/python3")
        print("Currently your system have recorded these paths:")
        for sys_path in sys.path:
            print(sys_path)
        print("When you will be in a virtual environment, all path with"
              " 'package' will be replaced by one that store all packages"
              " of virtual environment.")
    else:
        print(f"You're in a virtual environment whose path is: {sys.prefix}")
        print(f"Your global environment's path is: {sys.base_prefix}")
        print("Current Python: ", sys.executable)
        print("The paths registered by your system are: ")
        for sys_path in sys.path:
            print(sys_path)
        print("If you want to leave this environment you have to type the"
              " command:")
        print("deactivate")


if __name__ == "__main__":
    main()
