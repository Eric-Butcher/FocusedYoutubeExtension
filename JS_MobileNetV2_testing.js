import * as tf from '@tensorflow/tfjs';

const model = await tf.loadGraphModel('./JS_MobileNetV2_fine_tuned/model.json');
model.summary();
