# vim: set fileencoding=utf-8 :
#
# License: GNU Affero General Public License v3 or later
# A copy of GNU AGPL v3 should have been included in this software package in LICENSE.txt.
"""Run the antiSMASH pipeline"""

import sys

import customsmash


def entrypoint() -> None:
    """This is needed for the script generated by setuptools."""
    try:
        sys.exit(customsmash.main(sys.argv[1:]))
    except KeyboardInterrupt:
        print("ERROR: Interrupted", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    entrypoint()
