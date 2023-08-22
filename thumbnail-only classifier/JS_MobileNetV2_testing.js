import * as tf from '@tensorflow/tfjs-node';
import * as fs from 'fs';



const model = await tf.loadGraphModel('file://./JS_MobileNetV2_fine_tuned/model.json');

const MOBILE_NET_INPUT_HEIGHT = 224;
const MOBILE_NET_INPUT_WIDTH = 224;

const CLASS_NAMES = ['Educational', 'Entertainment']

let start_time = new Date().getTime();

let prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/A.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

let highestIndex = prediction.argMax().arraySync();
let predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Second prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/B.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Third prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/B.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Fourth prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/B.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Fifth prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/A.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Sixth prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/B.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Seventh prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/A.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Eighth prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/B.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Ninth prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/B.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Tenth prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/A.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));
console.log("\n")

// Eleventh prediction
start_time = new Date().getTime();

prediction = tf.tidy(function() {
    const imageBuffer = fs.readFileSync('./extra_unlabeled_test_images/A.jpg');
    const imageTensor = tf.node.decodeImage(imageBuffer);
    let resizedimageTensor = tf.image.resizeBilinear(imageTensor, [MOBILE_NET_INPUT_HEIGHT, MOBILE_NET_INPUT_WIDTH], true);
    let normalizedImageTensor = resizedimageTensor.div(255);
    return model.execute(normalizedImageTensor.expandDims()).squeeze();
});

highestIndex = prediction.argMax().arraySync();
predictionArray = prediction.arraySync();

console.log('Prediction: ' + CLASS_NAMES[highestIndex]);
console.log("Time taken to predict: " + (new Date().getTime() - start_time + 'ms'));