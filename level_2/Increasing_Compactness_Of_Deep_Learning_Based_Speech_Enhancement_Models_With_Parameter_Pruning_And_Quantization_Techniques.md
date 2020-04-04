
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
    


实验验证：
    
    原文采用timit和一些noise数据集，并在时域采样点映射的FCN模型上进行测试
    压缩网络模型的方法：pruning, sparse constraints, quantization
    
    
