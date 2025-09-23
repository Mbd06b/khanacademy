#!/usr/local/bin/python2.7
"""
Khan Academy startup with GAE template patch
"""
import sys
import os

# Apply the template library patch BEFORE importing main
sys.path.insert(0, os.path.dirname(__file__))
from gae_template_patch import patch_template_registration
patch_template_registration()

# Now import and run the main application
import main