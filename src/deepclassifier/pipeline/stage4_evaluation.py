from deepclassifier.config import ConfigurationManager
from deepclassifier.components import Evaluation
from deepclassifier import logger

STAGE_NAME = "Evaluation Stage"


def main():
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f"*******************************************")
        logger.info(f"******* stage: {STAGE_NAME} started *******")
        main()
        logger.info(f"******* stage: {STAGE_NAME} completed *******")
    except Exception as e:
        logger.exception(e)
        raise e
