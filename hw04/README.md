# Homework 4: DL 101

#### 1. Classification of a 2D dataset using ConvnetJS
ConvnetJS is a very simple yet powerful JavaScript library for Convolutional Neural Networks created by Andrei Karpathy, previously a Graduate Student at Stanford (under Fei-Fei Li) 
and now the leader of the Autonomous Driving project at Tesla.  The library runs directly in the browser and uses the CPU of your computer for training (just one core, so it will be woefully slow on large networks).  It is highly interactive, however, and enables you to rapidly experiment with small nets. You can read more about ConvNetJs and its api at http://cs.stanford.edu/people/karpathy/convnetjs/
Our first lab aligns with the 2D classification example available here: http://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html
Once you hit this page, the network starts running.  
* Add a few red dots in previously green areas by clicking the left mouse button.  Is the network able to adjust and correctly predict the color now?  
Answer: The boundaries of the network do adjust. However the time taken to adjust to any changes is very high.

* Add a few green dots in previously red areas by clicking the shift left mouse button.  Can the network adapt?  
Answer: The network adapts better in this case because the red dots are scattered and not concentrated to one location. 

* Review the network structure in the text box.  Can you name the layers and explain what they do?  
Answer:  
One input layer with 2 input points  
One fully connected tanh activation layer with 6 neurons  
One fully connected tanh activation layer with 2 neurons  
One softmax layer with 2 classes.  

* Reduce the number of neurons in the conv layers and see how the network responds. Does it become less accurate?  
Answer:  
There were no conv layers in the network to begin with; but adding a conv layer in place of a fc layer does generally make the network less accurate

* Increase the number of neurons and layers and cause an overfit.  Make sure you understand the concept  
Answer:  
Increasing the number or neurons per layer and/or the number of fc layers does cause an overfit. The network now adapts very well to the data points in the training set but cannot
generalize well to a test set.

* Play with activation functions.. -- relu vs sigmoid vs tanh... Do you see a difference ? Relu is supposed to be faster but less accurate.  
Answer: Yes. Relu seems faster than tanh. Sigmoid appears to be the most accurate and the slowest.

#### 2. ConvnetJS MNIST demo
In this lab, we will look at the processing of the MNIST data set using ConvnetJS.  This demo uses this page: http://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html
The MNIST data set consists of 28x28 black and white images of hand written digits and the goal is to correctly classify them.  Once you load the page, the network starts running and you can see the loss and predictions change in real time.  Try the following:

* Name all the layers in the network, make sure you understand what they do.  
Answer:  
For ref: The code within the text box appears like this:
layer_defs = [];  
layer_defs.push({type:'input', out_sx:24, out_sy:24, out_depth:1});  
layer_defs.push({type:'conv', sx:5, filters:8, stride:1, pad:2, activation:'relu'});  
layer_defs.push({type:'pool', sx:2, stride:2});  
layer_defs.push({type:'conv', sx:5, filters:16, stride:1, pad:2, activation:'relu'});  
layer_defs.push({type:'pool', sx:3, stride:3});  
layer_defs.push({type:'softmax', num_classes:10});  

net = new convnetjs.Net();  
net.makeLayers(layer_defs);  
The network has the following layers:
1. Input layer with a 24 X 24 black-and-white image (no depth)
2. A convolutional layer with a relu activation function. This layer has 8 filters of size 5 X 5 and an additional padding of 2.
The input to this layer is 24 X 24 X 1 (W1 = 24, H1 = 24, D1 = 1) and the output of the layer is
W2 = (W1 - sx + pad*2)/stride + 1 = (24 - 5 + 2*2)/1 + 1 = (24 - 5 + 4) + 1 = 24
H2 = (H1 - sy + pad*2)/stride + 1 = (24 - 5 + 2*2)/1 + 1 = (24 - 5 + 4) + 1 = 24
D2 = filters = 8
(W2, H2, D2) = (24, 24, 8)
3. A pooling layer which reduces the number of dimensions. In this case, the dimension of the o/p layer from pooling will be
W2 = (W1 - sx + pad*2)/stride + 1 = (24 - 2 + 0)/2 + 1 = 12
H2 = (H1 - sx + pad*2)/stride + 1 = (24 - 2 + 0)/2 + 1 = 12
D2 = D1 = 8
(W3, H3, D3) = (12, 12, 8)
4. Another convolutional layer with a relu activation function.
W2 = (W1 - sx + pad*2)/stride + 1 = (12 - 5 + 2*2)/1 + 1 = 12
H2 = (H1 - sy + pad*2)/stride + 1 = (12 - 5 + 2*2)/1 + 1 = 12
D2 = filters = 8
(W4, H4, D4) = (12, 12, 8)
5. Another pooling layer to reduce dimensions.
W2 = (W1 - sx + pad*2)/stride + 1 = (12 - 3 + 0)/3 + 1 = 4
H2 = (H1 - sx + pad*2)/stride + 1 = (12 - 3 + 0)/3 + 1 = 4
D2 = D1 = 8
6. A softmax layer which categorizes the input into 10 possibilities for the output each with a probability score.


* Experiment with the number  and size of filters in each layer.  Does it improve the accuracy?  
Answer: Increasing the number and/or size of the filter reduces the accuracy

* Remove the pooling layers.  Does it impact the accuracy?  
Answer:  
Removing pooling will possibly result in an overfitted model. Pooling generally helps in figuring out edges in an image and helps the model generalize better.
Therefore, on a test set, pooling might increase the accuracy of the network.

* Add one more conv layer.  Does it help with accuracy?  
Answer:  
It is unclear if adding more conv layers help increase the accuracy for this dataset. However, generally, adding more conv layers does not necessarily help with the accuracy of a training set.
It might still help in extracting more features from the dataset.

* Increase the batch size.  What impact does it have?  
Answer:
Increasing batch size results in decrease in accuracy. Also the neural network takes up more computational power to train.

* What is the best accuracy you can achieve? Are you over 99%? 99.5%?
Answer:  
With a batch size of 10 and adding one more conv and pooling layer, the validation accuracy of the network increased to 97% after a few iterations of training.

#### 3. Build your own model in Keras
Tried running the notebook on both TX2 and IBM cloud. Did not work on the TX2 but succeeded on the cloud VM.
The jupyter notebook from IBM cloud VM has been uploaded here.
