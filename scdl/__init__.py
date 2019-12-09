# -*- encoding: utf-8 -*-

"""Python Soundcloud Music Downloader."""

import os

__version__ = 'v1.7.12'
CLIENT_ID = 'f17476445ba4b72bc5760aa679820d27'
ALT_CLIENT_ID = '822786d960574f9c8bcb1b93b973d6af'
ALT2_CLIENT_ID = 'NONE'

dir_path_to_conf = os.path.join(os.path.expanduser('~'), '.config/scdl')
if 'XDG_CONFIG_HOME' in os.environ:
    dir_path_to_conf = os.environ['XDG_CONFIG_HOME']

file_path_to_conf = os.path.join(dir_path_to_conf, 'scdl.cfg')
text = """[scdl]
auth_token =
path = .
"""

if not os.path.exists(dir_path_to_conf):
    os.makedirs(dir_path_to_conf)

if not os.path.exists(file_path_to_conf):
    with open(file_path_to_conf, 'w') as f:
        f.write(text)
