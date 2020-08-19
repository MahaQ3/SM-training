# train a custom model 

in this task , I created model to detecting apples 
to run model :
- download object detection api from [here](https://github.com/tensorflow/models/tree/master/research/object_detection) 
- copy apple-images , apple-training and ssd_mobilenet_v1_coco_2018_01_28 folders and past into object detection folder .
- execute commands writed [here](https://github.com/MahaQ3/SM-training/blob/master/task-7/commands.txt) on CMD or terminal .
- train model : `python train.py --train_dir=apple-training/ --pipeline_config_path=apple-training/ssd_mobilenet_v1_pets.config --logtostderr `
- Export inference graph:`python export_inference_graph.py --input_type image_tensor --pipeline_config_path apple-training/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training/model.ckpt-6537 --output_directory new_graph `

 
### refrence :
1- [part 1](https://youtu.be/C5-SEZ_IvaM)  
2- [part 2 ](https://youtu.be/_gGI91BmIdk)

