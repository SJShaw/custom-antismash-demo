# License: GNU Affero General Public License v3 or later
# A copy of GNU AGPL v3 should have been included in this software package in LICENSE.txt.

"""

"""

import sys

import antismash
from antismash.__main__ import main as antismash_main
# import some modules from antiSMASH that won't be overridden
# in particula some generic module
from antismash.detection import cluster_hmmer, genefunctions
from antismash.modules import pfam2go

# import those modules that are defined only within this custom pipeline,
# the structure and naming here are just arbitrary examples and can be changed
# to suit
from customsmash.detection import custom_detection
from customsmash.modules import custom_analysis

# replace the normal antismash modules with any combination of antiSMASH modules
# and/or custom modules
antismash.main.replace_analysis_modules([custom_analysis, pfam2go])
antismash.main.replace_detection_modules([cluster_hmmer, custom_detection, genefunctions])


__version__ = "1.0"


def main(args: list[str]) -> int:
    # Any custom processing before or after running the pipeline can be added here

    # e.g. some extra console printing
    print("CustomSMASH: a pipeline that finds genes with identifiers that begin with 'A'")
    # The simplest version of running is to use antiSMASH's own main which will handle
    # all argument parsing. Alternatively, use antismash.main.run_antismash()
    # with the sequence file and the config object built via
    # antismash.config.build_config(). In either case, any command line arguments
    # defined by included modules will be handled automatically.

    # using main won't give much information about what went wrong, if it went wrong
    result_code = antismash_main(args)

    # but any following processing can still take place, e.g.
    print("CustomSMASH has finished")

    return result_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
