import os
import logging
from elasticsearch import Elasticsearch
from datetime import datetime
class Logger:
    _logger = None
    @classmethod
    def get_logger(cls,name = os.getenv("LOGGERS_NAME", "my_logger"),
                   es_host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
                   ,index=os.getenv("ELASTIC_INDEX", "index_logges")
                   ,level=logging.DEBUG):

        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)
            class ESHandler(logging.Handler):
                def emit(self, record):
                    try:
                        es.index(index=index, document={
                            "timestamp": datetime.utcnow().isoformat(),
                            "level": record.levelname,
                            "logger": record.name,
                            "message": record.getMessage()
                        })
                    except Exception as e:
                        print(f"ES log failed: {e}")
            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())
            cls._logger = logger
            return logger

if __name__ == "__main__":
    logger = Logger.get_logger()
    logger.info("check")
    logger.error("oopss check")