# src/utils/logger.py

import logging
import os

class Logger:
    def __init__(self, name="npc_logger", log_file="npc_log.log", level=logging.INFO):
        """
        Initialize the Logger with a specific name, log file, and logging level.
        :param name: The name of the logger.
        :param log_file: The file to which logs will be written.
        :param level: The logging level (e.g., INFO, DEBUG, WARNING, ERROR).
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create file handler
        if log_file:
            if not os.path.exists(os.path.dirname(log_file)):
                os.makedirs(os.path.dirname(log_file))
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)

            # Create console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            # Create a logging format
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to the logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def log(self, level, message):
        """
        Log a message with the specified logging level.
        :param level: The logging level (e.g., INFO, DEBUG, WARNING, ERROR).
        :param message: The message to log.
        """
        if level == "DEBUG":
            self.logger.debug(message)
        elif level == "INFO":
            self.logger.info(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "CRITICAL":
            self.logger.critical(message)

    def debug(self, message):
        """Log a message at the DEBUG level."""
        self.logger.debug(message)

    def info(self, message):
        """Log a message at the INFO level."""
        self.logger.info(message)

    def warning(self, message):
        """Log a message at the WARNING level."""
        self.logger.warning(message)

    def error(self, message):
        """Log a message at the ERROR level."""
        self.logger.error(message)

    def critical(self, message):
        """Log a message at the CRITICAL level."""
        self.logger.critical(message)

