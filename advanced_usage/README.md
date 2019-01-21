# Advanced Usage

The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building image similarity models. 

## Tips and "Gotchas"

-  **Training Data**: In order for an image similarity  model to propose similar images to a new image, the model must have already seen images in the category of the new image. For example, for a model to take an image of a boat and propose images of similar boats, the model must've seen instances of boats previously. To build an image similarity model that proposes similar plants, you would need to retrain the model using images of plants. We've provided a general model that was trained on 101 different categories, but for a more specific use case, it may make sense to change your training data set. Alternatively for a more general use case, Caltech also provides a data set using 256 categories. 
-  **Model Runtime**: The out-of-the box model takes a long time to train on CPU. Try limiting the amount of data used to train the model. Likely, you don't need all 9,145 images of from 101 different categories to get something working. You might want to try using 2 categories to begin with. Also, set `max_iterations` lower (default value is 10) in the `turicreate.image_similarity.create` function if you want something to train quickly (at the cost of reduced accuracy).
-  **Model Size**: In addition to the tips above, try using the `squeezenet_v1.1` model in the `turicreate.image_similarity.create` function which will reduce the size of the model significantly. This may also impact the filtering or proposal abilities of the model to some degree.

## Resources

-  `images_in_turicreate.ipynb`: Gives some tips on wrangling image data in Turi Create, detailing proper formatting and several helper functions.

## Need Help?
Please contact us with questions or feedback! Here are two ways:


-  [**Signup for our Slack Channel**](https://skafosai.slack.com/)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/image_similarity/) on image similarity basics.