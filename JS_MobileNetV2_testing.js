import * as tf from '@tensorflow/tfjs-node';

const model = await tf.loadGraphModel('file://./JS_MobileNetV2_fine_tuned/model.json');

model.predict('file://./extra_unlabeled_test_images/B.jpg');