"""Console script for mchsr."""
import argparse
import sys
import mchsr.buffs

import mchsr.events

def main():
    """Console script for mchsr."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into " "mchsr.cli.main")

    ## TEST CODE TODO: RM
    damage = mchsr.events.Damage(None, None, 1.2, 7)
    damage.execute()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
