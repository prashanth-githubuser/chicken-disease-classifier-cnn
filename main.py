from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PreparebaseModelPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started\n")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n >>>>>>>\n\n\"{STAGE_NAME}\" Completed \n\n<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started\n")
    data_ingestion = PreparebaseModelPipeline()
    data_ingestion.main()
    logger.info(f"\n >>>>>>> \n\n\"{STAGE_NAME}\" Completed \n\n<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e