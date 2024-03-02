import logging

# -------- Logging Format ------------
"""
%(lineno)s - the line number where logging was called
%(module)s - the module (name portion of file), here it's "basics1"
%(filename)s - the file name portion of pathname. here it's "basics1.py"
%(pathname)s - full pathname of source file where logging was called
%(thread)d - hread ID (if available)
%(threadName)s - Thread name (if available)
%(asctime)s - human readable time
%(created)f - time when log was created, uses time.time()
"""

def main():
    logging.basicConfig(
        level=logging.DEBUG, # This can be debug, info, warning, error or critical,
        format="%(asctime)s %(levelname)s %(message)s", # can optinally set the format of logs
        datefmt="%Y-%m-%d %H:%M:%S", # can optinally alter the date format
        # filename="sample.log" # enabling this, will save the logs to the file "sample.log"
    )

    logging.debug("This is a Debug Message")
    logging.info("This is an Info Message")
    logging.warning("This is a Warning Message")
    logging.error("This is an Error Message")
    logging.critical("This is a Critical Message")

if __name__ == "__main__":
    main()