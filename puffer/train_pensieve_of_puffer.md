https://groups.google.com/g/puffer-stanford/c/I2gD2n818EY  
修改 multi_video_sim里面的env里面的参数，以匹配puffer  
puffer论文里面3.3节提到了要把video chunk lenghth 改成2.002 seconds 以及 buffer thresh hold = 15 seconds  
VIDEO_CHUNCK_LEN = 2000.0  # millisec  
BUFFER_THRESH = 17.0 * MILLISECONDS_IN_SECOND  

# multi_video_sim成功运行，可以放在puffer上运行   
1.先运行generate_video.py，在同一目录下创建videos文件夹，以及在videos文件夹下创建一个空文件0即可运行，这个程序的作用是生成1000个视频的合成数据  
每个视频随机拥有3-10个码率等级，以及20-100个chunks，每个chunk的大小也是随机的  
2.在generate_test_video.py同一目录下创建test_video文件夹，然后在test_video文件夹里面创建一个空文件0，generate_test_video.py里面其他路径的文件是pensieve自带的，目的是生成一个test_video视频信息，这个test_video是真实存在的  
3.然后traces就是sim文件夹里面的设置：  
  cooked_traces里面放trainning_data(目前使用了pensieve提供的处理好的数据)  
  cooked_test_traces里面放test_data(目前使用了pensieve提供的处理好的数据)  
  
4.然后multi_agnet.py里面如果出现这个错误（会出现，因为pensieve的代码有点过时了)  
Tensorflow: 'module' object has no attribute 'scalar_summary'  
这个错误是因为tensorflow将一些原来的名称更换了，只要找到出错的位置把新的类或函数的名称改对就可以  
tf.mul should be renamed to tf.multiply  
tf.audio_summary should be renamed to tf.summary.audio  
tf.contrib.deprecated.histogram_summary should be renamed to tf.summary.histogram  
tf.contrib.deprecated.scalar_summary should be renamed to tf.summary.scalar  
tf.histogram_summary should be renamed to tf.summary.histogram  
tf.image_summary should be renamed to tf.summary.image  
tf.merge_all_summaries should be renamed to tf.summary.merge_all  
tf.merge_summary should be renamed to tf.summary.merge  
tf.scalar_summary should be renamed to tf.summary.scalar  
tf.train.SummaryWriter should be renamed to tf.summary.FileWriter  

pip install h5py --user  
Installing h5py will potentially solve the error below when using TFlearn: “hdf5 is not supported on this machine (please install/reinstall h5py for optimal experience)”  
pip install scipy --user  
for scipy not supported  

# puffer pensieve 
multi_agnet.py line 130  
if nn_model == None  # 正确做法  
if nn_model == "None" # 错误做法  
