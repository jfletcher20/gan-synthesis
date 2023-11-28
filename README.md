# GAN-synthesis
GAN human face synthesis project for Biometric Systems course.

PyTorch + Jupyter Notebook implementation.

The preprocessor should be run separately to adjust the dataset by detecting faces and cropping in a 128x128 area around them.
This area can be changed by calling the crop_face function with a different tuple.
Adjust the directory paths as needed in `img-preprocessor.py`.

Script `gan.ipynb` can be tested in Visual Studio code with Python environment as kernel for Jupyter Notebook.

Requires `dataset` folder to be in the same directory as .ipynb file, which contains `dataset` folder with the images and `classes.txt` file for training of generator and discriminator. If your folder structure is different, adjust the paths as is needed. Due to size constraints on GitHub, only `classes.txt` folder is provided here, but not dataset folder with 100k images form CelebA. If using a different dataset (different image names or different number of images), then `classes.txt` file should be updated too.

.ipynb code can be tested cell by cell with results seen at once. Epochs are considerably faster if the program uses GPU rather than CPU on your device, so check requirements for using GPU in the comments if necessary.
