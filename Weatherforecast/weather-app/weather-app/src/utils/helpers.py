import logging

def log_error(message):
    logging.error(message)

def format_date_time(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")