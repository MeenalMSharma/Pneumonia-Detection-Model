import streamlit as st


def main():
    st.markdown(
        '''
        <h1 align="center">
            Disease Detection Using Convolutional Neural Networks
        </h1><br>

        
## **Summary**
### Breaking Down the Problem:-
The Problem Statement required us to create a model for detection of Brain Tumour. Brain Tumour is usually detected by a Doctor by observing MRI Scan of the brain,after which several sophisticated medical tests such as biopsy are to confirm the tumour [1]. So we decided to use the MRI scan as input data for our model to predict whether the patient has a brain tumour or not, futhermore, we decided to classify the tumour if we get the data.
### Finding Dataset:-
We searched on Google for a suitable dataset and found a few datasets containing MRI scans of the brain labeled with various types of tumour. First one we found contained 1200 images in total and after scouring around the internet a little bit we found a dataset containing around 7000 images, belonging to 4 different classes which are No Tumour, Meningioma, Glioma and Pituitary, out of which 5700 were for training and 1300 for testing [2].
### Selecting Appropriate tools and Preprocessing Data:-After we found the data we uploaded it to Google Drive and used it from there by mounting the drive onto a Colab notebook. We used Google Colaboratory since it allows us to use a GPU which makes training faster and allows us to work collectively on the model. We used Pillow module for data preprocessing and then used the Tensorflow module to make our model. Our Data was organized as images put into folders depending upon the class of tumour they belonged to. We made csv files containing information about the image name, image tumour name, and the label encoding of the tumour for both of the training and testing datasets using the Pandas module. We then used the csv files to load the images into RAM and then preprocessed these images by converting them into RGB and into (224.224) shape.
### Learning About Machine Learning, Deep Learning and Transfer Learning:-
We then learned about basic Machine Learning techniques in scikit-learn [3] and slowly moved to learning about Deep Learning and CNNs in Tensorflow [4]. We also came across Transfer Learning Technique which is very popular in Image Classification problems and learning about it through some articles [5] [6].
### Making the Model:-
So now, equipped with knowledge of Machine Learning, Deep Learning and Transfer Learning, We set out to write our model,We used pretrained model to extract features from the images and then added hidden layers for classification. We tried out several different pretrained models for the feature extraction layer such as ResNet50, InceptionV3 , EfficientNetB2 etc and compared their results to select the best for our model. MobileNetV2 turned out to give the best results and gave best results out of all of them.

### Hosting our Model:-
Pneumonia Detection Model
## The Website
### Streamlit
We made and deployed the websites using the Streamlit module, it is incredibly easy to use and made our work very easy while making the website [7]. We made a homepage, About Data Page,About us page,Contact Us page and Prediction pages

### Additional Models
Since we were done early, We used the same architecture model and trained it on some other datasets,which are Covid 19 Chest X-Ray, Pneumonia Chest X-Ray , Blood Cells.
