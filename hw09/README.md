### How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
On a 2-node V-100 cluster (16 vCPU | 120 GB | 2 x V100 GPU), it took approximately 18 hours for the model to finish training with 30,000 steps.

## Do you think your model is fully trained? How can you tell?
The training loss appears to be converging to a value between 1.6 and 1.8. This means that the model has achieved a certain level of consistency on the training set and this value will not change considerably if the number of training steps are increased.  

## Were you overfitting?  
Looks like both the training loss and evaluation loss are at the same level after 50,000 iterations. This could be evidence that we are not overfitting. In the case of overfitting, we would see the training loss continuing to reduce while validation loss staying the same or increasing as the number of iterations increase.

## Were your GPUs fully utilized?



## Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?
## Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?
## How big was your training set (mb)? How many training lines did it contain?
## What are the files that a TF checkpoint is comprised of?
## How big is your resulting model checkpoint (mb)?
## Remember the definition of a "step". How long did an average step take?
## How does that correlate with the observed network utilization between nodes?
