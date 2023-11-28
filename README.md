# GAN-synthesis
GAN human face synthesis project for Biometric Systems course.

PyTorch + Jupyter Notebook implementation.

The preprocessor should be run separately to adjust the dataset by detecting faces and cropping them to 128x128 pixels.
This area can be changed by calling the `crop_face` function with a different tuple .
Adjust the directory paths as needed in `img-preprocessor.py`.

Script `gan.ipynb` can be tested in Visual Studio code with Python environment as kernel for Jupyter Notebook.

The `dataset` folder must be in the same directory as `gan.ipynb`. The `dataset` directory contains the `dataset` folder with the images and `classes.txt` files for the training of the generator and discriminator. If your folder structure is different, adjust the path variable as needed. Due to size constraints on GitHub, only the `classes.txt` folder is provided here, but not dataset folder with 100k preprocessed images from CelebA.
When using a different dataset (different image names or a different number of images), the `classes.txt` file must be updated, too. You can look to the preprocessor script to deduce how to get the list of file names in a directory.

`gan.ipynb` can be tested cell by cell with each result being seen at once.
The epochs are considerably faster if the program uses GPU rather than CPU on your device, so check the requirements for using GPU in the comments if necessary.
