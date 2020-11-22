import nlu.pipe_components
import sparknlp
from sparknlp.annotator import *
class ClassifierDl:
    @staticmethod
    def get_default_model():
        return ClassifierDLModel.pretrained() \
            .setInputCols("sentence_embeddings") \
            .setOutputCol("category")

    @staticmethod
    def get_pretrained_model(name, language):
        return ClassifierDLModel.pretrained(name,language) \
            .setInputCols("sentence_embeddings") \
            .setOutputCol("category")




    @staticmethod
    def get_trainable_model():
        return ClassifierDLApproach() \
            .setInputCols("sentence_embeddings") \
            .setOutputCol("category") \
            .setLabelColumn("y") \
           .setEnableOutputLogs(True)

    @staticmethod
    def get_offline_model(path):
        return ClassifierDLModel.load() \
            .setInputCols("sentence_embeddings") \
            .setOutputCol("category") \
            .setLabelColumn("label") \
            .setEnableOutputLogs(True)

        # .setBatchSize(64) \
            # .setMaxEpochs(20) \
            # .setLr(0.5) \
            # .setDropout(0.5)