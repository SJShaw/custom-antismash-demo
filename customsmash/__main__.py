# vim: set fileencoding=utf-8 :
#
# License: GNU Affero General Public License v3 or later
# A copy of GNU AGPL v3 should have been included in this software package in LICENSE.txt.
"""Run the antiSMASH pipeline"""

import sys
from typing import List

import antismash

import customsmash

# set arg version to avoid cyclic imports
antismash.config.args.ANTISMASH_VERSION = f"CustomSMASH {customsmash.__version__} using antiSMASH {antismash.__version__}"


def entrypoint() -> None:
    """This is needed for the script generated by setuptools."""
    try:
        sys.exit(customsmash.main(sys.argv[1:]))
    except KeyboardInterrupt:
        print("ERROR: Interrupted", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    entrypoint()
