import urllib.request
import tarfile
import turicreate as tc
from skafossdk import *
import save_models as sm

ska = Skafos()

data_url = "http://www.vision.caltech.edu/Image_Datasets/Caltech101/101_ObjectCategories.tar.gz";
data_path = "101_ObjectCategories.tar.gz"

# pull the tar
ska.log("Retrieving the images from online", labels = ['image_similarity'])
retrieve = urllib.request.urlretrieve(data_url, data_path)

# extract the file
ska.log("Images downloaded, extracting the images", labels = ['image_similarity'])
tar = tarfile.open(data_path, "r:gz")
tar.extractall()
tar.close()

# load the reference data
ska.log("Loading the images into a Turi Create SFrame", labels = ['image_similarity'])
reference_data  = tc.image_analysis.load_images('./101_ObjectCategories')
reference_data = reference_data.add_row_number()

# build the model
ska.log("Building the model", labels = ['image_similarity'])
model = tc.image_similarity.create(reference_data)

ska.log("Saving the model", labels = ['image_similarity'])
# export model to coreml
coreml_model_name = "image_similarity.mlmodel"
res = model.export_coreml(coreml_model_name)

# compress the model
compressed_model_name, compressed_model = sm.compress_model(coreml_model_name)

# save model to Skafos
sm.skafos_save_model(skafos = ska, model_name = compressed_model_name,
								compressed_model = compressed_model,
								permissions = 'public')