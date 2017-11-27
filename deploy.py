#!/usr/bin/env python
"""Main Deployment file"""

from install_rancher import rancher_install

RANCHER_VERSION = 'v0.6.1'

# Install Rancher
rancher_install(RANCHER_VERSION)

# Generate answers.txt

