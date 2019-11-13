# Mini Amazon Go Hackathon

[Amazon Go](https://www.amazon.com/b?ie=UTF8&node=16008589011) is a new kind of store with no checkout required. With the "Just Walk Out Shopping" experience, simply use the Amazon Go app to enter the store, take any of the products, and go! No lines, no checkout. A little later, you will receive a receipt on the app with a charge to your Amazon account. This checkout-free shopping experience is made possible by the same types of technologies used in self-driving cars: *computer vision*, *sensor fusion*, and *deep learning*. The technology automatically detects when products are taken from or returned to the shelves and keeps track of them in a virtual cart. When the customers done shopping, they can just leave the store without checking out. At the moment they walk out of the door, the technology will capture the photos, detect the products,  automatically make the transactions, and send the cutomers the receipts.


Now, do you want to be involved in deep learning and contribute to the bleeding edge of technology of computer vision? In this Hackathon, we will empower you to team up and build a "Mini Amazon Go" from scratch. Complimentary food and drink are served (just don't dine and dash).


**Date: Nov.22, 2019
Location: LAX10**
Registration Form: https://trawler.amazon.com/



## Setup

To get you up and running, we will equip you with the essential hardwares and cloud computing resources. Benefit from the deep learning knowledge we taught in [Dive into Deep Learning](https://d2l.ai/) tutorial and the built-in computer vision packages in [GluonCV](https://gluon-cv.mxnet.io/), you will be mastering throughout the full process of Mini Amazon Go experience.


### Hardwares

For hardwares, there are two necessay parts: 

- [Raspberry Pi 4](https://www.amazon.com/gp/product/B07TXMDVPQ/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

The [Raspberry Pi](https://www.raspberrypi.org/) is a low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that can do everything you’d expect a desktop computer to do, from browsing the internet and playing high-definition video, to making spreadsheets, word-processing, and playing games. What’s more, the Raspberry Pi  has the ability to interact with the outside world, and has been used in a wide array of digital maker projects, from music machines and parent detectors to weather stations and tweeting birdhouses with infra-red cameras.

<img height="200" alt="portfolio_view" src="https://user-images.githubusercontent.com/3307514/66869709-c7ce7b00-ef54-11e9-8824-32cbcd40100d.png">


- [camera module](https://www.amazon.com/gp/product/B07PQ63D2S/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

This dedicated camera ribbon that can be used for a variety of tasks. For example, it can enable camera functions for a raspberry pi to take a Picture, record Video, time-Lapse photography, etc. Ideally for DIY camera projects.

<img height="200" alt="portfolio_view" src="https://user-images.githubusercontent.com/3307514/66869685-b8e7c880-ef54-11e9-969c-2ed21178d7ca.png">


Besides, you also need the [touch screen and protection case](https://www.amazon.com/gp/product/B07WRV48ZW/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) to assemble the hardwares together.



### Tutorial: AWS Kinesis Video Stream on Raspberry Pi

This [tutorial](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi.html) describes how you can set up and use the *Amazon Kinesis Video Streams C++ Producer SDK* on a Raspberry Pi device. The steps also include how to verify the installation using the GStreamer demo application. This tutorial includes critical topics such as *Join Your Raspberry Pi to Your Wi-Fi Network*, *Connect Remotely to Your Raspberry Pi*, *Configure the Raspberry Pi Camera*, *Stream Video to Your Kinesis Video Stream and View the Live Stream*, etc.


#### Notes

- The default region is `us-west-2`. Change to nearest region if applicable.
- Raspbian OS can use `apt-get` to install shared libs to accelerate compilation of Kinesis Producer C++ SDK (https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/install-instructions-linux.md#install-steps-for-ubuntu-17x-and-raspbian-stretch-using-apt-get)
- Setup IAM role for Kinesis Video Stream, and paste the secret key to raspberry
- There's a sample app to upload videos to KVS.
`./kinesis_video_gstreamer_sample_app -w <width> -h <height> -f <framerate> -b <bitrateInKBPS> Stream Name` (Note that not all resolution works, 640x480 works on Raspberry Pi 4 for me), or you can use [src/start_upload.sh](src/start_upload.sh).


#### Trouble shooting

The latency issue is one of the major bottlenecks of the long "waiting time" between you taking the videos and observing them on your screen. Here's potential fix for large latency: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/troubleshooting.html#troubleshooting-general



### Computing Resources: SageMaker Notebooks

Here, we provide you the sagemaker notebooks where you can run jupyter notebooks on multiple GPUs.

#### Access Permission

For SageMaker notebook to access KVS, it must have permission `AmazonKinesisVideoStreamsFullAccess` added to the SageMaker Execution Role when creating the notebook instance

#### Example notebook for processing KVS

See [VideoStream Example](src/VideoStream.ipynb).

#### Example of Training and Test

See [src/training_object_detector_yolo3.ipynb](src/training_object_detector_yolo3.ipynb) and [src/test_object_detector_yolo3.ipynb](src/test_object_detector_yolo3.ipynb) (Yolo3, Recommended)

Or see [src/training_object_detector.ipynb](src/training_object_detector.ipynb) and [src/test_object_detector.ipynb](src/test_object_detector.ipynb) (SSD)

Or see [Beijing CV hackathon](https://github.com/hetong007/d2l-1day-cv-hackathon)



## Evaluation

The evaluation of the final product will be evaluated with the following metrics, each with scale from 0 to 10.

- Accuracy: percentage of correctly detected transaction movements (grab cola + return cola is regarded as two transcations rather than one). Scale the percentage to 0 - 10
- UX(User experience): how satisfying the overall user experience is. Rated to (0, 10) by each group.
- Innovation: how you bring cool technologies into the pipeline. Rated to (0, 10) by each group.
