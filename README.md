## 【0】Introduction

This repo is based on [YOLOv5 (5.0)](https://github.com/ultralytics/yolov5/releases/tag/v5.0) and aims at training the network with dataset [UA-DETRAC](https://detrac-db.rit.albany.edu/).

Running the repo in Colab is recommended, copy the file [YOLOv5_train_on_UA-DETRAC.ipynb](https://colab.research.google.com/drive/1a8VZepcpGkk7ZzMDNu-s3PPu43G1n9Fm?usp=sharing), then run it on Colab. (remember to change the runtime type to GPU in Colab)



## 【1】Environment (Colab user can skip this step) 

* Python >=3.7
* Pytorch >=1.7

Create a new conda called handobj, install pytorch-1.6.0
```
conda create --name YOLOv5 python=3.7
conda activate YOLOv5

# for GPU and CUDA 10.2
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.2 -c pytorch
```


## 【2】Installation

Clone the code
```
git clone https://github.com/forever208/yolov5_train_on_UA-DETRAC.git
```

Install all the python dependencies using pip:
```
cd yolov5_train_on_UA-DETRAC
pip install -qr requirements.txt
```

## 【3】Download dataset

Download and unzip the dataset by command line is recommended:
```
cd ..
wget https://detrac-db.rit.albany.edu/Data/DETRAC-train-data.zip
wget https://detrac-db.rit.albany.edu/Data/DETRAC-test-data.zip
unzip DETRAC-train-data.zip
unzip DETRAC-test-data.zip
rm -rf DETRAC-test-data.zip
rm -rf DETRAC-train-data.zip
```

Then download and unzip the annotation files (I saved the file in my GoogleDrive), download by command:
```
wget wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1f-4NA2sc6Tqo25Ilx-b5NaFGLjhf2AbK' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1f-4NA2sc6Tqo25Ilx-b5NaFGLjhf2AbK" -O DETRAC-Train-Annotations-XML.zip && rm -rf /tmp/cookies.txt

wget wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1Q0E-Dk3vL55m9ODOENeq2_ojiZwWMbdo' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1Q0E-Dk3vL55m9ODOENeq2_ojiZwWMbdo" -O DETRAC-Test-Annotations-XML.zip && rm -rf /tmp/cookies.txt

unzip DETRAC-Train-Annotations-XML.zip
unzip DETRAC-Test-Annotations-XML.zip
rm -rf DETRAC-Train-Annotations-XML.zip
rm -rf DETRAC-Test-Annotations-XML.zip
```

## 【3】Dataset preprocessing
We then need to do 3 things before training YOLOv5 using UA-DERTAC dataset:
- transform the annotation format from xml to txt (the label format of YOLOv5 is txt).
- organize the dataset folder structure to meet the requirment of YOLOv5 default setting.
- re-organize the training set and validation set because the original split of DETRAC is not good (refer to [this blog](https://zhuanlan.zhihu.com/p/373096271) for more details)

#### Transform xml to txt
Using python script `yolov5_train_on_UA-DETRAC/scripts/bigxml_txt.py` to do the transformation. Remember to change the path 

```
cd yolov5_train_on_UA-DETRAC/scripts/ 
python bigxml_txt.py
```

you should now get the following folder structure where is the txt labels.
<p align="left">
  <img src="https://github.com/forever208/yolov5_train_on_UA-DETRAC/blob/master/data/images/folder_structure_1.png" width='80%' height='80%'/>
</p>


