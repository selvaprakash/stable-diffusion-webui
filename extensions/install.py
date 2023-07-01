# Copyright (C) 2023 by Artem Khrapov (kabachuha)
# Read LICENSE for usage terms.

import launch

import os

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

with open(req_file) as file:

    for lib in file:

        lib = lib.strip()

        if not launch.is_installed(lib):

            launch.run_pip(f"install {lib}", f"text2video requirement: {lib}")
