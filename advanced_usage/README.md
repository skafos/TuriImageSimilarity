# Advanced Usage

The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building image classification models. 

## Tips and "Gotchas"

-  **Training Data**: In order for an image classifier to identify a particular type of image, it must have seen other images with the same label. For example, if a model was trained on dogs and cats, and it is shown a plant, it will identify that plant as either a dog or cat. To build an image classification model that identifies plants or other types of objects, you would need to retrain the model, using labeled images of the type you want.
-  **Model Runtime**: The out-of-the box model takes a long time to train on CPU. Try limiting the amount of data used to train the model. Likely, you don't need all 25,000 images of cats and dogs to get something working. Also, set `max_iterations` lower (default value is 10) in the `turicreate.image_classifier.create` function if you want something to train quickly (at the cost of reduced accuracy).
-  **Model Size**: In addition to the tips above, try using the `squeezenet_v1.1` model in the `turicreate.image_classifier.create` function which will reduce the size of the model significantly. This may also impact the classification abilities of the model to some degree.

## Resources

-  `images_in_turicreate.ipynb`: Gives some tips on wrangling image data in Turi Create, detailing proper formatting and several helper functions.

## Need Help?
Didn't find something you need? Confused by something? Need more guidance?

Please contact us with questions or feedback! Here are two ways:

-  [**Signup for our Slack Channel**](https://metismachine-skafos.slack.com/join/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos)

Also checkout Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/image_classifier/) on image classification basics.
