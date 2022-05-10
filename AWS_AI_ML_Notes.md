AI - ML Notes:
Machine learning, or ML, is a modern software development technique that enables computers to solve problems by using examples of real-world data.

In supervised learning, every training sample from the dataset has a corresponding label or output value associated with it. As a result, the algorithm learns to predict labels or output values.

In reinforcement learning, the algorithm figures out which actions to take in a situation to maximize a reward (in the form of a number) on the way to reaching a specific goal.

In unsupervised learning, there are no labels for the training data. A machine learning algorithm tries to learn the underlying patterns or distributions that govern the data.

1. A model is an extremely generic program, made specific by the data used to train it.
2. Model training algorithms work through an interactive process where the current model iteration is analyzed to determine what changes can be made to get closer to the goal. Those changes are made and the iteration continues until the model is evaluated to meet the goals.
3. Model inference is when the trained model is used to generate predictions.

Clustering is an unsupervised learning task that helps to determine if there are any naturally occurring groupings in the data.
- A categorical label has a discrete set of possible values, such as "is a cat" and "is not a cat.
- A continuous (regression) label does not have a discrete set of possible values, which means there are potentially an unlimited number of possibilities.
- Discrete is a term taken from statistics referring to an outcome that takes only a finite number of values (such as days of the week).
- A label refers to data that already contains the solution.
- Using unlabeled data means you don't need to provide the model with any kind of label or solution while the model is being trained.

Working with data (collection, inspection, summary stats, and visualization) is the most important and most overlooked part of AI work.

The iterative process updates:
- Model parameters > settings or configurations that the training algo can change. Ex. weights and biases.
- Loss function > Codify's the model's distance from a goal.

**Models
Linear / 
Tree-based /
Deep learning /
 - FFNN: Feed Forward Neural Network: neuron in a layer containig weights
 - CNN: Convoutional Neural Networks: nested filters over grid-organized data
 - RNN/LSTM: Recurrent Neural Networks and/or Long Short-Term Memory 
 - Transformer: A modern replacement for RNN/LSTMs that enables larger data-sets.

Classical models scikit-learn 
Deep Learning: mxnet, tensorflow, pytorch