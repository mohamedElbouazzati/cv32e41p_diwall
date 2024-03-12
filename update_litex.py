import os

# Path to the __init__.py file
init_file = os.path.join("third_party/litex/litex/soc/cores/cpu", "__init__.py")  # Replace with the actual path

# Lines to add to the __init__.py file
lines_to_add = [
            "# Add the 'cv32e41p_diwall' CPU class to the dictionary.\n",
            "from cv32e41p_diwall.core import CV32E41P_DIWALL\n",
            "CPUS['cv32e41p_diwall'] = CV32E41P_DIWALL\n"
]

# Open the __init__.py file and append the lines
with open(init_file, 'a') as file:
    file.writelines(lines_to_add)

print("Lines added to __init__.py successfully.")