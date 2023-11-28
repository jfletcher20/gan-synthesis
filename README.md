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

# Requirements

- Required Visual Studio (2019 for CUDA 11, 2022 for CUDA 12) - (if you want to run on GPU)

- Required VS Code

- Required VS Code Jupyter extensions

- Required Python (recommended v. 3.11.6., since 3.12. doesn't support torch installation)

- Required Python libraries - ipykernel, torch, matplotlib and others required by the script

- Note: torch installation might fail with `pip`, in which case Anaconda installation is recommended (install PyTorch in Anaconda Prompt via command pasted from official PyTorch website)


How to run .ipynb script on GPU (on Windows):

- Step 1. Have Nvidia GPU

- Step 2. Add to PATH: C:\Program Files (x86)\Microsoft Visual Studio\<VERSION>\Community\VC\Auxiliary\Build\vcvars64.bat

- Step 3. Install Nvidia CUDA (v. 11 if Visual Studio 2019, or v. 12 if Visual Studio 2022)

- Step 4. Run .ipynb script in VS Code


Otherwise, just use CPU (not recommended)
