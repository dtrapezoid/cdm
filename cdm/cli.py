"""cdm - Cassandra Data Manager

Usage:
    cdm search [<term>]
    cdm list [<term>]
    cdm show <dataset>
    cdm install [--host=<host>] [--keyspace=<keyspace>] [--dry-run] [--nocassandra] [--graph] [--search] <dataset>
    cdm update
    cdm stream <dataset>
    cdm web
    cdm tutorials <dataset>

Options:
    --debug

Examples:
    cdm install demo

"""

import sys
sys.path.append("")
import os
import os.path
from ConfigParser import SafeConfigParser
import logging

# 3rd party

from docopt import docopt
from cdm.util import *

DEBUG = False

# allow for schema management fun
os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = "1"

def main():
    arguments = docopt(__doc__)

    try:
        os.mkdir(CDM_CACHE)
    except OSError:
        pass


    if arguments["search"] or arguments["list"]:
        return list_datasets(arguments["<term>"])

    if arguments["update"]:
        return update_datasets()

    if arguments["install"]:
        tmp = arguments["<dataset>"].split("==")

        if len(tmp) == 1:
            tmp.append("master")

        # get defaults
        cqlshrc = os.path.expanduser("~/.cassandra/cqlshrc")
        if os.path.exists(cqlshrc):
            parser = SafeConfigParser()
            parser.read(cqlshrc)
            default_host = parser.get("connection", "hostname")
            default_port = parser.get("connection", "port")
        else:
            default_host = "localhost"

        host = arguments.get("--host") or default_host
        return install(tmp[0], tmp[1],
                       install_cassandra=not arguments['--nocassandra'],
                       install_graph=arguments['--graph'],
                       install_search=arguments['--search'],
                       host=host)



    if arguments["show"]:
        return show_dataset_details(arguments["<dataset>"])

    print "Done"




if __name__ == "__main__":
    main()
