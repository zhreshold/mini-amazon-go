# mini-amazon-go
Computer Vision Hackathon: Mini Amazon Go


# Setup

## Hardware

- [Raspberry Pi 4](https://www.amazon.com/gp/product/B07TXMDVPQ/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

<img height="200" alt="portfolio_view" src="https://user-images.githubusercontent.com/3307514/66869709-c7ce7b00-ef54-11e9-8824-32cbcd40100d.png">
- [touch screen + protection case](https://www.amazon.com/gp/product/B07WRV48ZW/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
- [camera module](https://www.amazon.com/gp/product/B07PQ63D2S/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)

<img height="200" alt="portfolio_view" src="https://user-images.githubusercontent.com/3307514/66869685-b8e7c880-ef54-11e9-969c-2ed21178d7ca.png">


## AWS Kinesis Video Stream

Tutorial: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi.html

### Notes


- The default region is `us-west-2`. Change to nearest region if applicable.
- Raspbian OS can use `apt-get` to install shared libs to accelerate compilation of Kinesis Producer C++ SDK (https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/install-instructions-linux.md#install-steps-for-ubuntu-17x-and-raspbian-stretch-using-apt-get)
- Setup IAM role for Kinesis Video Stream, and paste the secret key to raspberry
- There's a sample app to upload videos to KVS.
`./kinesis_video_gstreamer_sample_app -w <width> -h <height> -f <framerate> -b <bitrateInKBPS> Stream Name` (Note that not all resolution works, 640x480 works on Raspberry Pi 4 for me).

## SageMaker notebook

### Access Permission

For SageMaker notebook to access KVS, it must have permission `AmazonKinesisVideoStreamsFullAccess` added to the SageMaker Execution Role when creating the notebook instance

### Example notebook for processing KVS

See [VideoStream Example](src/VideoStream.ipynb).

### Example of Beijing CV hackathon

See https://github.com/hetong007/d2l-1day-cv-hackathon
