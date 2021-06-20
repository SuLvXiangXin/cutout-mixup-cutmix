import matplotlib.pyplot as plt
import csv
import numpy as np


datasets = ['cifar10', 'cifar100']
models = ['resnet18', 'lenet', 'densenet', 'vgg']
methods = ['baseline', 'baseline+', 'cutout', 'mixup', 'cutmix']
for dataset in datasets:
    for model in models:
        name = dataset + '_' + model
        method = [[] for i in range(6)]
        with open('./results2/'+name+'.csv', 'r') as f:
            f_csv = csv.reader(f)
            k = 0
            for row in f_csv:
                k += 1
                if k == 1:
                    continue
                for i in range(6):
                    method[i].append(float(row[i]))

        method = np.array(method)
        for i in range(5):
            method[i+1] = 100 - 100*method[i+1]
        plt.clf()
        plt.xlabel('Epoch')
        plt.ylabel('Test Error(%)')
        plt.title(name)
        for i in range(5):
            plt.plot(method[0], method[i+1], label=methods[i])
        plt.legend(methods)
        plt.savefig('./figures/'+name+'.png', format='png')
        plt.show()
