import logging

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