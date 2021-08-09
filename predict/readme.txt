1. kuangniu_data存放需要预测的图片，文件夹名可以在predict.py中修改
2. model中存放的是经过微调的resnet18预训练模型，以及所有的类别名
3. predict.py可以直接运行：python predict.py    ，也可以导入process()函数，代码通过传入模型路径，传入图片路径的上一级读取某文件夹下
的所有图片，恢复模型并进行预测，返回对应类别
4. 依赖包参考requirements.txt