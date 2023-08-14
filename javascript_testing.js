import { pipeline } from '@xenova/transformers';

// Paths to your local model and tokenizer
const modelPath = 'path/to/your/model';
const tokenizerPath = 'path/to/your/tokenizer';

// Create a text classification pipeline
let classifier = await pipeline('text-classification', modelPath, { tokenizer: tokenizerPath });

// Classify a text
let result = await classifier('I love transformers!');
console.log(result);
// Output might look like: [{'label': 'POSITIVE', 'score': 0.999817686}]
