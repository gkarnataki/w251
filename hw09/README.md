### How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
On a 2-node V-100 cluster (16 vCPU | 120 GB | 2 x V100 GPU), it took approximately 18 hours for the model to finish training with 30,000 steps.

## Do you think your model is fully trained? How can you tell?
The training loss appears to be converging to a value between 1.6 and 1.8. This means that the model has achieved a certain level of consistency on the training set and this value will not change considerably if the number of training steps are increased.  

## Were you overfitting?  
Looks like both the training loss and evaluation loss are at the same level after 50,000 iterations. This could be evidence that we are not overfitting. In the case of overfitting, we would see the training loss continuing to reduce while validation loss staying the same or increasing as the number of iterations increase.

## Were your GPUs fully utilized?
It looks like GPUs were utilized most of the time. However, there were time slots where GPU utilization was down to 70%.
Please refer to the outputs of "nvidia-smi" command executed at regular intervals attached.

## Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?
Output from nmon attached. It does appear that there is high network traffic between nodes.

## Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?
The learning rate policy in the config file follows the "transformer policy" (also called "noam" policy)
  "lr_policy": transformer_policy,
  "lr_policy_params": {
    "learning_rate": 2.0,
    "warmup_steps": 8000,
    "d_model": d_model,
  },
This policy is based on the "Attention is all you need" (https://arxiv.org/pdf/1706.03762.pdf) paper which plots the learning rate like a "hat". The "noam" scheme puts the increase in learning rate (with a warmup) together with a decrease in learning rate. i.e. linear warmup for a given number of steps followed by exponential decay.

## How big was your training set (mb)? How many training lines did it contain?
958 MB with 4524868 lines

## What are the files that a TF checkpoint is comprised of?
There are three checkpoint files in TF
model.ckpt-0.data-00000-of-00001: value of each variable in the graph
model.ckpt-0.index: an id of the checkpoint
model.ckpt-0.meta: saved graph structure

## How big is your resulting model checkpoint (mb)?
Referring to the figure, the total size of all the three files is about 850 MB

## Remember the definition of a "step". How long did an average step take?
On an average, it takes about 1.53 seconds per step.

## How does that correlate with the observed network utilization between nodes?
The amount of data movement between nodes seems to be affecting the time taken to execute a step.

