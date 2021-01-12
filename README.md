#                                                                  T E N S O R F L O W-2.0 -  O B J E C T  D E T E C T I O N 

### Current System Configuration Present :
- Ubuntu 20.04 
- Graphic Card 2GB : GeoForce GT 755M
        
## STEP-1 :  Download Required Models and Packages

 **Download Object Detection API** : Visit To Link https://github.com/tensorflow/models and download the models repo. Or click 
 [OD-API-2.0](https://codeload.github.com/tensorflow/models/zip/master) to download. 
           
 **Download Tensorflow zoo model** : To Download the required model for your project visit [Model-Zoo-TF-2.0](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)    
           
**Download LabelImg tool and Install Required Packages** : For installing labelimg tool Visit [here](https://github.com/tzutalin/labelImg) and follow required steps 
        
**Downloading protobuf Library** : For conda environment run command `conda install -c anaconda protobuf` to install protobuf.
        
## STEP-2 : Set Up For Training Model
        
**conversion of protos file present in  *models/research/object_detection/protos* to *.py* file** : 
  1. Navigate to research folder and run command `protoc object_detection/protos/*.proto –python_out=.` 
              
**Install Object Detection API** :
  1. open setup.py file from models/research/object_detetcion/packages/tf2/ folder 
  1. comment line `tf-models-official` 
  1. navigate to research folder and run command `cp object_detetction/packages/tf2/setup.py` and `python -m pip install .`
             
**Image Annotations and train test split** : 
  1. Navigate to research folder 
  1. Create directory named images
  1. In images folder create two directories train and test and add train and test images in these directories 
  1. Now open labelImg tool and create annotations for all images in train and test directory
             
**Create label_map.pbtxt file and Edit** : 
  1. Create a folder *training* inside research folder
  1. Create file label_map.pbtxt in training/
  1. add classes in format  ` item { id : 1 , name: 'classname' }`
                                 
**create conda environment with tensorflow-gpu** : 
    * To create gpu environment run command `conda create --name tf_gpu tensorflow-gpu=2.1.0`
        
Extract the model downloaded from zoo and paste it inside the research folder
        
Now from extracted model folder copy  pipeline.conf file and paste in research/training/  folder 
        
**Change the pipeline.conf file as below**
   1. num_classes: 1 # Set this to the number of different label classes
   1. batch_size: 8 # Increase/Decrease this value depending on the available memory 
   1. fine_tune_checkpoint:  "pre-trained-models/ssd_resnet50_v1_fpn_640x640_coco17_tpu-  8/checkpoint/ckpt-0"  # Path to checkpoint of pre-trained model
   1. fine_tune_checkpoint_type: "detection" 
   1. label_map_path: "training/label_map.pbtxt"    #train_input_reader
   1. input_path: "train.record"  #train_input_reader
   1. label_map_path: "training/label_map.pbtxt"   # eval_input_reader
   1. input_path: "test.record"         # eval_input_reader
        
**Convert .xml files to tfrecord**
   1. Download file generate_tfrecord.py present inside scrpits folder ( [Here](scripts/generate_tfrecord.py) ) and keep it inside research folder
   1. run :  `python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record`
   1. run :   `python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record`
       
* Open the File models/research/object_detection/core/box_predictor.py and change the content at line `137` to  
     ```class KerasBoxPredictor(tf.compat.v1.keras.layers.Layer):```
        
* Download image_processing.py file inside script folder ( [Here](scripts/image_preprocessing.py) ) & Paste it inside 
           Anaconda3\envs\tflow2\Lib\site-packages\tensorflow_core\python\keras\layers\preprocessing
           
* Install Nvidia Driveer by running command `sudo apt install nvidia-driver-460` and reboot 
        
* Run command `nvidia-smi` to check if driver is installed or not  
        
* Copy file from  models/research/object_detection/model_main_tf2.py and paste in research folder 
        
## Step-3 : Start Training 
*  Run command :  `python model_main_tf2.py –model_dir=model_directory  --pipeline_config_path=training/pipeline.config`
        
## Reference :
 
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html
        
https://github.com/keras-team/autokeras/issues/1296
        
https://www.tensorflow.org/install/source
        
https://www.tensorflow.org/api_docs/python/tf/keras
        
https://github.com/tensorflow/models
        
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md        
