import logging
import os
from dotenv import load_dotenv
from extract import extract
from transform import transform
from load import load

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))

log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'pipeline.log')

logging.basicConfig(filename=log_path,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("Pipeline started")

try:
    datas = extract()
    datas_clean = transform(datas)
    load(datas_clean)
    logger.info("Pipeline completed with successfully!")
except Exception as error:
    logger.error("Pipeline failed", exc_info=True)