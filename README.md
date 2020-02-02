# w251

## HW03

The repo has three files:  

### facecapture.py  
Uses opencv to capture a picture from the webcam whenever it detects a face. 
The content is then sent over to a local broker on TX2. The image is pushed to a topic called "facetopic". 
Because the subscriber for this message (forwarder) also resides on TX2, the probability that the image will not be 
delivered is extremely low. QoS for a publish is therefore set to 0.

### forwarder.py  
The forwarder subscribes to messages on "facetopic" and publishes them to a remote VM hosted on IBM cloud.
Messages are published to "remotefacetopic". The QoS here is set to 1 - because the message is being sent to a remote system
and we therefore need a guaranteed delivery. Also, our application on the remote VM can handle multiple images being sent to it.

### imagesaver.py  
This is the subscriber of "remotefacetopic". It receives images from the remote broker and saves them to s3.
It uses s3fs to setup a mount point on /mnt/s3files. This is mapped to the s3 bucket at
https://s3.console.aws.amazon.com/s3/buckets/w251-gk/hw03/?region=us-west-1&tab=overview
Each image is sufixed with a random number to make the identity of the file unique.

