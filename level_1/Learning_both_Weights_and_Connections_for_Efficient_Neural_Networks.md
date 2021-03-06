
文章提出三部剪植法:

    1.训练网络，学习重要的连接
    2.剪掉不重要的连接
    3.保持网络，调优保留的网络连接的参数
    
introduction:

    以45nm的CMOS进行说明，大的网络不适合在片上存储运算，并且计算实际耗费的功率，
    不适用手机等终端设备。这篇文章就是为了压缩模型的参数使其能够运行于手机端。
    在初始训练阶段，移除所有小于阈值的权重。这个pruning阶段将全连接和卷积层转化为稀疏层，
    这个阶段学习网络的拓扑结构，学习哪些连接重要，并移除非重要的连接。之后训练稀疏连接网络，
    补偿移除连接带来的损失。(这有点类脑机制）剪枝过程如fig
![fig](https://github.com/ffxz/PaperNotes/blob/master/fig/Learning_both_Weights_and_Connections_for_Efficient_Neural_Networks/fig.png)
    