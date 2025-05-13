import streamlit as st

def main():
    st.markdown(
        '''
        <h1 style="text-align:center;">About the Dataset</h1>
        <h2>Brief Summary of the Dataset for Pneumonia Detection Model</h2>
        <p>The dataset used for the Pneumonia Detection Model primarily consists of chest X-ray images and includes both pneumonia and normal classes. It is sourced from multiple publicly available datasets and is typically used for building deep learning models that classify chest X-rays into the two categories: pneumonia and normal.

Key Points:
Dataset Size:

The dataset contains 900+ images in total, split between pneumonia and normal classes.

Approximately 450+ images for the pneumonia class and 450+ images for the normal class.

Image Types:

The images are chest X-ray scans, with the pneumonia images being a mix of bacterial and viral pneumonia cases, while the normal class contains healthy chest X-rays.

The images have different resolutions, with most of them being resized or preprocessed to a uniform size for model training (e.g., 150x150 or 256x256).

Class Labels:

The primary class labels are:

Pneumonia: Includes both bacterial and viral types.

Normal: Represents healthy individuals without any abnormalities in the chest X-rays.

Preprocessing:

Before feeding the images to the model, they are typically normalized to scale pixel values between 0 and 1.

Images are also resized to a standard input size (e.g., 150x150, 256x256) based on the model architecture used.

Source:

The dataset is sourced from publicly available repositories like Kaggle and NIH Chest X-ray dataset.

Kaggle dataset link: Chest X-ray Images (Pneumonia)

Purpose:
The dataset is mainly used for training deep learning models such as Convolutional Neural Networks (CNN) to detect pneumonia from chest X-rays. By leveraging this dataset, the model can classify unseen X-ray images into the pneumonia or normal categories, aiding medical professionals in early detection.</p>
        
        <h2>Brief Summary of the Dataset for Brain Tumor Detection Model</h2>
        <p>Key Points:
Dataset Size:

The dataset consists of over 750 MRI images, each labeled with the specific type of tumor (e.g., Meningioma, Glioma, Pituitary, and Normal).

The images are organized into different subfolders representing each class of brain tumor.

Image Types:

The images are MRI scans of the brain. They are typically high-resolution grayscale images, although some may include color enhancements for better visualization of the tumors.

The images are preprocessed to standardize their size, such as resizing to 150x150 pixels or 256x256 pixels, to ensure compatibility with deep learning models.

Class Labels:

The dataset includes four main categories of brain tumor types:

Meningioma: A type of tumor that develops from the meninges.

Glioma: A tumor that arises from glial cells in the brain.

Pituitary: Tumors that develop from the pituitary gland.

Normal: Representing MRI scans with no visible tumors.

Preprocessing:

Resizing: Images are resized to a standard dimension (e.g., 150x150 or 256x256) depending on the model's input requirement.

Normalization: Pixel values are normalized (scaled between 0 and 1) for effective training of deep learning models.

Augmentation: To improve model generalization, techniques such as flipping, rotation, zooming, and shearing may be used.

Source:

The dataset is often sourced from public repositories like Kaggle.

Kaggle Dataset Link: Brain Tumor MRI Dataset

Purpose:
This dataset is used to train deep learning models, particularly Convolutional Neural Networks (CNNs), to automatically detect and classify brain tumors from MRI scans. By analyzing these images, the model helps doctors and healthcare professionals in diagnosing brain tumors, improving the speed and accuracy of diagnosis.</p>
        ''',
        unsafe_allow_html=True,  # Required to render HTML properly
    ) 

if __name__ == '__main__':
    main()
