# Turi Image Similarity

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training an image similarity model on Skafos using the [Turi Create framework](https://apple.github.io/turicreate/docs/userguide/image_similarity/). The example model is based on images from the popular open source images data set Caltech 101, containing images from 101 different categories. To get a list of these categories, check out the final page of [this research paper](http://www.vision.caltech.edu/feifeili/Fei-Fei_GMBV04.pdf)

## What is here?

The components of this repo are:
- `image_similarity.ipynb` - a Python notebook that trains and saves an image similarity model to use in your app. Start here.
- `utilities/` - a directory that contains helper functions used by `image_similarity.ipynb`.
- `advanced-usage/` - a directory that contains additional information about this image similarity model, how to incorporate your own data, advanced usage, and more. 
- `requirements.txt` - a file describing all required Python dependencies.

## About the model
- The data used to train this example model are 9,145 images from 101 different categories. This data set can be found [here](http://www.vision.caltech.edu/Image_Datasets/Caltech101/Caltech101.html). To get a list of these categories, check out the final page of [this research paper](http://www.vision.caltech.edu/feifeili/Fei-Fei_GMBV04.pdf)
- Once trained, you can give the model an image, and it will identify images similar to the photo you've provided. The model will perform better on new images that fall into the 101 categories the model was trained on. 
- To retrain this image similarity model on new data, we highly recommend doing it on a GPU. As benchmarks, we've found that training this Turi Create image similarity model takes about 60 minutes on a GPU and about a day and a half on Skafos with 6 CPU's and 10G of memory. [Read more about requesting a GPU](https://docs.metismachine.io/v1.3.1/docs/using-a-gpu).
## Going beyond the example
- If you wish to incorporate your own data or try another type of image similarity model, check out the `advanced_usage/` section. 
- Similar to Turi Create's image classifier model, Turi Create's image similarity uses `model='resnet-50'` by default. Using this model can result in a large `.mlmodel` file. If you are concerned about model size, using a smaller pre-trained model might help conserve memory without sacrificing a significant amount of accuracy. For more about this, read [here](https://apple.github.io/turicreate/docs/userguide/image_classifier/how-it-works.html). 

## Need Help?
Please contact us with questions or feedback! Here are two ways:


-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/image_similarity/) on image similarity basics.
