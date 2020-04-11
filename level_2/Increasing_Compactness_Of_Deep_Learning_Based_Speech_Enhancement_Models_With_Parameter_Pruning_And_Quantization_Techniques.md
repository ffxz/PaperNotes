
相关工作：

    pruning
    1.设定一个阈值，小于此阈值的weights在网络中去除来降低网络的参数量[16]
    2.应用稀疏约束（sparse constraints），减少模型中的filters[17]
    
    quantization
    1.通过减少比特数[18]
    2.k-means聚类尺度来量化参数值[19]
    
    compactness SE
    1.sun和li，将量化技术应用在增强模型上[20]
    2.ko等人调研了增强模型精确尺度和神经元数量的关系[21]
    3.两步量化方法[22]


提出的方法：
       
    PQ和PP技术的结合
![fig1](https://github.com/ffxz/PaperNotes/blob/master/fig/Increasing_Compactness_Of_Deep_Learning_Based_Speech_Enhancement_Models_With_Parameter_Pruning_And_Quantization_Techniques/fig1.png)

    PQ采用kmeans对训练好的参数进行聚类划分，如fig2所示，对网络参数分为四类并得到中心点数值，并通过量化位数检索的方式获取中心数值。并且通过计算压缩率是2.16（这种数值量化方式会损失一定的精度，但又优于直接量化带来的损失）
![fig2](https://github.com/ffxz/PaperNotes/blob/master/fig/Increasing_Compactness_Of_Deep_Learning_Based_Speech_Enhancement_Models_With_Parameter_Pruning_And_Quantization_Techniques/fig2.png)
    

实验验证：
    
    原文采用timit和一些noise数据集，并在时域采样点映射的FCN模型上进行测试
    压缩网络模型的方法：pruning, sparse constraints, quantization
    
    实验中提到了bound for acceptable performance drop (BAPD)，就是一个pesq和stoi的参考值。这个值的计算是取的noisy和clean语音的平均。增强后的音频的指标要高于此值。
    （个人目前没有找到这个bound的依据，所以，增强方法最好还是与其他方法进行对比）
    
    
