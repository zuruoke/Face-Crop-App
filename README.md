# Face Crop App

This Application involves Training a RetinaNet to instinctively crop out scale and position-variant face(s) from pictures and save as a new image file. 

*If you want to know about the RetinaNet - I'd suggest you check [this kernel](https://github.com/zuruoke/Race-Detection-with-RetinaNet/blob/master/README.md), it's pretty intuitive*

I used a pre-trained RetinaNet with Resnet50 as the backbone and then fine-tuned it to classify and detect (to draw a bounding box around a human face). The bounding box output was used to crop out the specific object(s) in the image.

This Model is very pretty **scale** and **pose invariant**

Images from [flickr](https://www.flickr.com/) and [shutterstock](https://www.shutterstock.com/) constituted of the training dataset

The workflow are outlined as follows:

- Use labelimg to annotate (label and specify the bounding box cordinates) all the objects in the image in a [Pascal VOC format](http://host.robots.ox.ac.uk/pascal/VOC/#:~:text=The%20PASCAL%20VOC%20project%3A,and%20comparison%20of%20different%20methods)
- Run a xml script to convert the Pascal VOC format (xml) to csv as that's what a RetinaNet expects
- Load the Pretrained RetinaNet from keras and all it's dependencies and navigate to the main file directory
- Train the Pretrained RetinaNet by specifying a backbone (I used Retina50) and save the learned parameters after each epochs
- Convert the saved model to an inference graph to test on unseeen data
- Save the results as a Pandas DataFrame using the corresponding datapoints after testing on the test data
- Use OpenCV's imwrite function to save the cropped image to a folder

# Results
![220](https://user-images.githubusercontent.com/51057490/83917973-b221f600-a76f-11ea-8484-c82f6f8f0780.jpg) ![c5](https://user-images.githubusercontent.com/51057490/83918046-daa9f000-a76f-11ea-8543-64252f236f99.JPG)
![c6](https://user-images.githubusercontent.com/51057490/83918051-dda4e080-a76f-11ea-8a75-317637b17cc3.JPG)




![180](https://user-images.githubusercontent.com/51057490/83918128-062cda80-a770-11ea-8aa4-be090dbe9422.jpg)
![c1](https://user-images.githubusercontent.com/51057490/83918140-0a58f800-a770-11ea-843e-9d021fe6413a.JPG)


![160](https://user-images.githubusercontent.com/51057490/83918218-2e1c3e00-a770-11ea-8467-e0bc3b11860e.jpg)
![c8](https://user-images.githubusercontent.com/51057490/83918234-34121f00-a770-11ea-815a-c1e47965ca18.JPG)![c15](https://user-images.githubusercontent.com/51057490/83918408-9408c580-a770-11ea-84ee-60fb2a9e29f2.JPG)

![170](https://user-images.githubusercontent.com/51057490/83918480-b8fd3880-a770-11ea-88b8-f582965e32df.jpg)
![c7](https://user-images.githubusercontent.com/51057490/83918490-bef31980-a770-11ea-821e-dbe8f01a3af5.JPG)

![190](https://user-images.githubusercontent.com/51057490/83918539-dd591500-a770-11ea-856f-d55c068f66ac.jpg)
![c13](https://user-images.githubusercontent.com/51057490/83918552-ea760400-a770-11ea-9e4a-4b6e7dae56cc.JPG)
![c14](https://user-images.githubusercontent.com/51057490/83918589-fc57a700-a770-11ea-8b76-e0aa849aa63e.JPG)

![200](https://user-images.githubusercontent.com/51057490/83918699-2d37dc00-a771-11ea-97fa-8e0fed1b2e7a.jpg)
![c2](https://user-images.githubusercontent.com/51057490/83918812-5e181100-a771-11ea-822c-3d6926c50322.JPG)

![210](https://user-images.githubusercontent.com/51057490/83918942-991a4480-a771-11ea-84ef-e6875d7fc997.jpeg)
![c9](https://user-images.githubusercontent.com/51057490/83918965-a1727f80-a771-11ea-9bd6-d5441a8610f2.JPG)
![c10](https://user-images.githubusercontent.com/51057490/83918974-a59e9d00-a771-11ea-8a28-881d668a8802.JPG)


# SIGNIFICANCE

- This can be used to build an Image Dataset or Database

# Stack Technologies

- Python 3.7
- Tensorflow 2.x
- Keras
- Numpy 
- OpenCV
- Matplotlib
- Pillow
- Pandas







**P.S**: I had to fail (tune) the Training Process a little bit, so that the cropped image has a little background
