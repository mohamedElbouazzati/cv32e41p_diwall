#!/usr/bin/env python3

from __future__ import print_function

import os
import cv32e41p_diwall

# Check if the module is found
print("cv32e41p_diwall module found.")

# Print some information about the module
print("cv32e41p_diwall module:", cv32e41p_diwall)
print("Module directory:", os.path.dirname(cv32e41p_diwall.__file__))


# Print the contents of the module directory
print("\nContents of the module directory:")
for item in os.listdir(os.path.dirname(cv32e41p_diwall.__file__)):
    print(item)
