# _*_ encoding:utf-8 _*_
__author__ = 'JQXX'
__date__ = '2018/11/13 16:34'
import tensorflow as tf

tf.flags.DEFINE_float("dev_sample_percentage", 0.01, "Percentage of the training data to use for validation")
tf.flags.DEFINE_integer("vocab_size",6000, "Batch Size (default: 64)")

tf.flags.DEFINE_integer("embedding_dim", 50, "Dimensionality of character embedding")
tf.flags.DEFINE_string("filter_sizes", "3,4,5", "Comma-separated filter sizes (default: '3,4,5')")
tf.flags.DEFINE_integer("num_filters", 128, "Number of filters per filter size (default: 128)")
tf.flags.DEFINE_float("dropout_keep_prob",0.5, "Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_float("l2_reg_lambda", 0.0, "L2 regularization lambda (default: 0.0)")

tf.flags.DEFINE_integer("batch_size", 128, "Batch Size (default: 64)")
tf.flags.DEFINE_integer("num_epochs", 25, "Number of training epochs (default: 200)")
tf.flags.DEFINE_integer("evaluate_every", 100, "Evaluate model on dev set after this many steps (default: 100)")
tf.flags.DEFINE_integer("checkpoint_every", 100, "Save model after this many steps (default: 100)")
tf.flags.DEFINE_integer("num_checkpoints", 2, "Number of checkpoints to store (default: 5)")
tf.flags.DEFINE_bool("is_fine_tune",False,"is fine tune embedding layer")
tf.flags.DEFINE_integer("hidden_size",64, "Number of filters per filter size (default: 128)")
tf.flags.DEFINE_float("grad_clip", 10, "grad_clip")
tf.flags.DEFINE_float("lr", 1e-3, "lr")

tf.flags.DEFINE_string("data_path","./data/", "data path")
tf.flags.DEFINE_string("result_path","./result/", "result path")
tf.flags.DEFINE_string("test_data_path","./data/test.txt", "test data path")
tf.flags.DEFINE_string("model_save_path","./model/best_model/", "model save path")
tf.flags.DEFINE_string("z_model_save_path","./model/z_best_model/", "model save path")
tf.flags.DEFINE_float("z_threshold",0.7, "The larger the threshold, the better the result, but the smaller the number of words, and the maximum value is 1")
tf.flags.DEFINE_float("threshold",0.5, "The larger the threshold, the better the result, but the smaller the number of words, and the maximum value is 1")
tf.flags.DEFINE_float("new_threshold",0.4, "Threshold for new word discovery")
tf.flags.DEFINE_bool("is_use_gpu",True, "Whether GPU is used")
tf.flags.DEFINE_integer("step_size",10, "step size")
tf.flags.DEFINE_string("algorithm","TextRank", "algorithm TextRank TF-IDF")

tf.flags.DEFINE_integer("topK",20,"topK")
tf.flags.DEFINE_string("gpu_id","1", "Which GPU to use")
tf.flags.DEFINE_integer("win_size",10, "windows size")
tf.flags.DEFINE_integer("import_threshold",5, "import threshold")
tf.flags.DEFINE_integer("topN", -1, "topN,If the value is -1, use all the words found")
tf.flags.DEFINE_integer("ngram",3,"ngram")
tf.flags.DEFINE_bool("is_rnn",False,"is use rnn")
tf.flags.DEFINE_string("choice_model","cnn","is use rnn")
tf.flags.DEFINE_bool("is_sliding_window",False,"is use sliding window")
tf.flags.DEFINE_integer("min_split",-1,"Minimum level of segmentation,If the value is -1, use the minimum split value")


FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
if FLAGS.is_rnn:
    FLAGS.model_save_path = "./model/rnn_best_model/"
    FLAGS.z_model_save_path = "./model/z_rnn_best_model/"
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
    print("{}={}".format(attr.upper(), value))
print("")



class Config(object):
    DEBUG = False
    TESTING = False
    REQUEST_STATS_WINDOW = 15


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}