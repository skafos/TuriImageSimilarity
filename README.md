# Turi Image Similarity

The following repo contains code for training an image similarity model on Skafos using the Turi Create framework.

As much as possible, the code in this repo mimicks Turi Create's image similarity example which can be found [here](https://apple.github.io/turicreate/docs/userguide/image_similarity/). 

## What is here?

The two main components to this repo are:
- `image_similarity.py` - a Skafos job that trains an image similarity model and saves a core ml model
- `image_similarity.ipynb` - a python notebook with the same code as the above `image_similarity.py` job.

Additionallly, there exists:
- `metis.config.yml` - a file telling Skafos how the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `save_models.py` - a helper module to save the core ml model to Skafos

## Further notes:
- To get this to run, the model required training data. The training data for this example comes from the open source data set from Caltech's Computer Vision dept which can be found [here](http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz)
- For this project, we highly recommend running it on a GPU. We encourage you to do this once you've changed the data to reflect your use case. As benchmarks, we've found this takes about 60 minutes on a GPU and about 1.5 days on Skafos with 6 CPU's and 10G of memory. This can take considerably more time locally using only CPU. 