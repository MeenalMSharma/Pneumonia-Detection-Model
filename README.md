# Project Mentor:<br>
Ms. Gaytri Gupta<br>
# Project Is Created By:<br>
Anant Pratap Singh<br>
Meenal sharma<br>
# PreCare Disease(Pneumonia and Brain Tumor) Detection Model<br>
## [Website Link](https://pneumonia-detection-model-65gvcfbcra9cdglppibsxu.streamlit.app/)
## **Summary**
### Breaking Down the Problem:-
The goal was to develop two intelligent systems:

One that detects pneumonia from chest X-ray images.

Another that classifies brain tumors (e.g., Meningioma, Glioma, Pituitary, or Normal) from MRI scans.
We began by understanding the nature of both diseases, the image modalities involved (X-rays vs. MRIs), and the output required (binary vs. multi-class classification).<br>
### Finding Dataset:-
We sourced open-access, labeled datasets:

Pneumonia: Chest X-ray dataset from Kaggle, containing ‘NORMAL’ and ‘PNEUMONIA’ classes.

Brain Tumor: MRI dataset from Kaggle with labeled images for different tumor types and healthy scans.<br>
We developed two deep learning-based diagnostic models:

The Pneumonia Detection Model was trained on a dataset of approximately 450 chest X-ray images, evenly distributed between pneumonia and normal cases. A Convolutional Neural Network (CNN) was used for binary classification.

The Brain Tumor Detection Model was trained using a dataset of around 750 MRI images, categorized into four classes: Meningioma, Glioma, Pituitary, and Normal. A CNN architecture was employed for multi-class classification.<br>
### Selecting Appropriate tools and Preprocessing Data:-
We used:

Python as the programming language.

TensorFlow/Keras for building and training models.

NumPy, PIL, and OpenCV for image preprocessing (resizing, normalization).

Streamlit for deploying the models as interactive web apps.

Images were resized to match the input shape expected by models, and pixel values were scaled (0–1). Labels were also one-hot encoded for classification.<br>
### Learning About Machine Learning, Deep Learning and Transfer Learning:-
We explored:

Machine Learning (ML) for traditional classification logic.

Deep Learning (DL), especially Convolutional Neural Networks (CNNs), for image-based predictions.

Transfer Learning using pre-trained models like ResNet, DenseNet, and AlexNet, which sped up training and improved accuracy due to their robust feature extraction.<br>
### Making the Model:-
For Pneumonia, a CNN and a few pre-trained models (ResNet, etc.) were trained and evaluated.

For Brain Tumor, a CNN model was built and trained from scratch or using transfer learning depending on data volume.

Models were saved using .keras format after training to preserve architecture and weights for deployment.<br>

### Hosting our Model:-
We used:

Streamlit to build a user-friendly interface for image upload and model inference.

Models were uploaded with the app and processed dynamically upon image submission.

The app was deployed on Streamlit Cloud, generating a public URL, which was shared in the GitHub README.md for open access.<br>
## **1. Backbone Feature Extractors used in Brain Tumor Detection Model**
### Inception  V3
 
The Inception V3 is a deep learning model for image classification that is built on convolutional neural networks. The Inception V3 is an improved version of the Inception V1 basic model, which was presented as GoogleNet in 2014 . Inception V3's model architecture can be seen in Figure 1.
![image](https://user-images.githubusercontent.com/108052351/184403575-031a720e-4412-4659-ba1f-90187bf5212d.png)
<p align="center">
  Fig 1: Model Architecture of Inception V3.
</p>

The model was trained over 20 epochs using the Adam Optimizer with a learning rate of 0.001 and a loss function of sparse cross categorical entropy. As it can observed in Fig.2, model accuracy increased steadily from 74% to 84% and the accuracy stabilized around 87% in 20 epochs.
![ba103912-8b3b-42d6-8a52-d115468a1487](https://user-images.githubusercontent.com/104026985/184408983-3bf79532-3938-414b-9855-f2f4e155c43f.jpg)
<p align="center">Fig 2: Accuracy for Inception V3 model.</p>

### VGG 19

VGG-19 is a convolutional neural network that is 19 layers deep. You can load a pretrained version of the network trained on more than a million images from the ImageNet database. The pretrained network can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals. As a result, the network has learned rich feature representations for a wide range of images. The network has an image input size of 224-by-224. VGG 19 model architecture can be seen in Figure 3.

![llustration-of-the-network-architecture-of-VGG-19-model-conv-means-convolution-FC-means](https://user-images.githubusercontent.com/104026985/184412049-86d9deb6-0d0e-4fae-9410-18a66114b6af.jpg)
<p align="center">Fig 3: Model Architecture of VGG 19.</p>
The model was trained over 20 epochs using the Adam Optimizer with a learning rate of 0.001 and a loss function of sparse cross categorical entropy.As it can observed in Fig 4, the model !
accuracy increased steadily from 60% to 80% and the accuracy stabilized around 85% in 20 epochs.

![96cf08d8-f6e0-4007-a49b-1b66e8d82019](https://user-images.githubusercontent.com/104026985/184411396-315438fa-e998-4351-a3c9-6f3a2f4dc5bd.jpg)
<p align="center">Fig 4: Accuracy for VGG 19 model.</p>

### DenseNet 201

DenseNet is a convolutional neural network where each layer is connected to all other layers that are deeper in the network, that is, the first layer is connected to the 2nd, 3rd, 4th and so on, the second layer is connected to the 3rd, 4th, 5th and so on.

![DenseNet-201-Architecture](https://user-images.githubusercontent.com/104026985/184411917-720436fa-8bf7-4a99-8703-549779546d9e.png)
<p align="center">Fig. 5: Model Architecture of DenseNet121.</p>
The model was trained on 20 epochs with adam optimizer at a learning rate of 0.001 and sparse categorical cross entropy as its loss function. As shown in Fig. 6, the model’s accuracy increases steadily from 76% to 84%. The accuracy of this model stabilized around 88% in 20 epochs.

![ee9c4da9-7c94-4efb-9678-b928cd781af4](https://user-images.githubusercontent.com/104026985/184412407-24b02406-cc81-4c2b-b739-ffba8a0a0fa2.jpg)
<p align="center">Fig 6: Accuracy for DenseNet201.</p>

### EfficientNet B2

EfficientNet is a convolutional neural network architecture and scaling method that uniformly scales all dimensions of depth/width/resolution using a compound coefficient. Unlike conventional practice that arbitrary scales these factors, the EfficientNet scaling method uniformly scales network width, depth and resolution with a set of fixed scaling coefficients. For example, if we want to use 2N times more computational resources, then we can simply increase the network depth by αN, width by βN, and image size by γN, where α, β, γ are constant coefficients determined by a small grid search on the original small model. EfficientNet uses a compound coefficient φ to uniformly scales network width, depth, and resolution in a principled way. The base EfficientNet-B0 network is based on the inverted bottleneck residual blocks of MobileNetV2, in addition to squeeze-and-excitation blocks. EfficientNets also transfer well and achieve state-of-the-art accuracy on CIFAR100 (91.7%), Flowers (98.8%), and 3 other transfer learning datasets, with an order of magnitude fewer parameters. Fig.7 shows the model architecture of EfficientNetB2.

![Architecture-of-EfficientNet-B0-with-MBConv-as-Basic-building-blocks](https://user-images.githubusercontent.com/104026985/184412776-ca61c8b5-6404-45f2-b0bc-03848cefffe1.png)
<p align="center">Figure 7: Model Architecture for EfficientNet B2.</p>
The model was trained on 20 epochs with adam optimizer at a learning rate of 0.001 and sparse categorical cross entropy as its loss function. The model’s accuracy fluctuates around 30% as shown in Fig.8 .

![fc0481b2-f640-4f24-b00e-42d52a03caf0](https://user-images.githubusercontent.com/104026985/184412949-693a8d53-0db1-400b-a96b-6296d2d20419.jpg)
<p align="center">Fig 8: Accuracy for EfficientNet B2.</p>

### InceptionResNet V2

InceptionResNetV2 is a convolutional neural network that is trained on more than a million images from the ImageNet database. The network is 164 layers deep and can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals. It is an extension of the Inception architecture applied in conjunction with residual blocks. Fig. 9 shows the model architecture of InceptionResNetV2.

![1_CYRgf1i1q_4hx5AcdcaSEg](https://user-images.githubusercontent.com/104026985/184413347-fb0b7429-47bf-4cfe-b0d9-f6078287dfb0.jpg)
<p align="center">Fig 9: Model Architecture for InceptionResNet V2.</p>
The Model is trained on 30 epochs with adam optimizer with learning rate of 0.001 and sparse categorical cross entropy as its loss function. The model’s accuracy barely increases from 74% to 82% and the final accuracy stabilized around 86% as seen in Figure.10 . 

![1d5b573b-a350-41a9-93c9-b341afeaa050](https://user-images.githubusercontent.com/104026985/184413582-de9abbf9-e0f2-4672-afbf-73af9acf8ff1.jpg)
<p align="center">Fig 10: Accuracy for InceptionResNet V2.</p>

### MobileNet V2

MobileNetV2 is a convolutional neural network architecture that seeks to perform well on mobile devices. It is based on an inverted residual structure where the residual connections are between the bottleneck layers.The intermediate expansion layer uses lightweight depthwise convolutions to filter features as a source of non-linearity. As a whole, the architecture of MobileNetV2 contains the initial fully convolution layer with 32 filters, followed by 19 residual bottleneck layers.

![The-architecture-of-the-MobileNetv2-network](https://user-images.githubusercontent.com/104026985/184413935-13547c6b-3a42-4952-8911-b75dd192c19f.png)
<p align="center">Fig 11: Model Architecture for MobileNet V2.</p>
The model is trained on 30 epochs with adam optimizer at a learning rate of 0.001 and sparse categorical cross entropy as its loss function.The model’s accuracy increases steadily from 76% to 88% as shown in Fig. 13. Since the model seems to have not stabilized around an accuracy, it was trained for 30 more epochs, the model’s accuracy still steadily increased from 88% to 94%. Since its accuracy was still improving a lot, it was trained for 20 more epochs, then the accuracy seemed to stabilize around 99% as shown in Fig. 14. This architecture is best suited for our model since it achieved 99% accuracy in just 80 epochs whereas other models stabilized around the 85% mark. The model achieved an accuracy of around 99% on the train set and 96% on the test set in just 90 epochs. This is the best architecture for our model and we finalized to use MobileNetV2 as our model.

![image](https://user-images.githubusercontent.com/108052351/184419535-d3e4e7ea-d099-4338-a89a-643259cbd01c.png)
<p align="center">Fig 12: Classification Report after 80 epochs for MobileNetV2.</p>

![image](https://user-images.githubusercontent.com/108052351/184414912-944d79f9-8aff-4716-8eb4-cce25a65757d.png)
<p align="center">Fig 13: Accuracy for MobileNet V2 during first 20 epochs.</p>

![image](https://user-images.githubusercontent.com/108052351/184414991-1acd8884-6ff9-4dde-bf10-74aeaa573516.png)
<p align="center">Fig 14:Accuracy for MobileNet V2 during last 20 epochs.</p><br>

## **1. Backbone Feature Extractors used in Pneumonia Detection Model**
### ResNet (Residual Network)

ResNet, short for Residual Network, introduces the concept of skip connections (also known as identity shortcuts) that jump over some layers. This allows the model to train much deeper neural networks without the vanishing gradient problem. ResNet effectively enables the flow of gradients directly through these skip connections, which helps in learning deeper representations.


<p align="center">Fig. 7: Model Architecture of ResNet.</p>
The model was trained for 20 epochs using the Adam optimizer with a learning rate of 0.001. The sparse categorical crossentropy loss function was used due to the multi-class classification nature of the brain tumor detection task. As shown in Fig. 8, the model shows a consistent increase in accuracy, stabilizing around 86% after 20 epochs.
![image](https://raw.githubusercontent.com/MeenalMSharma/Pneumonia-Detection-Model/main/test_files/resnet.jpeg)
<p align="center">Fig. 8: Accuracy for ResNet.</p><br>

### AlexNet

AlexNet was one of the first deep convolutional neural networks to achieve breakthrough performance in image classification. It introduced the use of ReLU activation, dropout for regularization, and data augmentation to combat overfitting. AlexNet consists of five convolutional layers, followed by three fully connected layers, and uses max pooling for downsampling.


<p align="center">Fig. 9: Model Architecture of AlexNet.</p>
The model was trained for 20 epochs using the Adam optimizer with a learning rate of 0.001. The sparse categorical crossentropy loss was used, suited for multi-class classification. As depicted in Fig. 10, the model showed a sharp rise in accuracy during the initial epochs and gradually converged around 84% by the end of training.


<p align="center">Fig. 10: Accuracy for AlexNet.</p><br>

### DenseNet

SAME AS BRAIN TUMOR!

## The Website
### Streamlit
We made and deployed the websites using the Streamlit module, it is incredibly easy to use and made our work very easy while making the website [7]. We made a homepage, About Data Page,About us page,Contact Us page and Prediction pages

### Additional Models
Since we were done early, We used the same architecture model and trained it on some other datasets,which are Covid 19 Chest X-Ray, Pneumonia Chest X-Ray , Blood Cells.



## References:
1)	https://www.cancer.net/cancer-types/brain-tumor/diagnosis
2)	https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset
3)	https://youtu.be/0B5eIE_1vpU
4)	https://youtu.be/tPYj3fFJGjk
5)	https://towardsdatascience.com/transfer-learning-for-image-classification-using-tensorflow-71c359b56673
6)	https://analyticsindiamag.com/transfer-learning-for-multi-class-image-classification-using-deep-convolutional-neural-network/
7) https://warlord-k-iitisoc-22-ai-ml-21-tumor-detection-appapp-zhwh17.streamlitapp.com/
8) https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset
9) https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
10) https://www.kaggle.com/datasets/paultimothymooney/blood-cells
