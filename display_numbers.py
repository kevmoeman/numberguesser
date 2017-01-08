
from matplotlib import pyplot as plt

import numpy as np

def train_model():
    # with open(r'E:\Projects\numberguesser\train.csv', 'r') as train_file:
    #     for idx, line in enumerate(train_file):
    #         if idx == 0:
    #             continue
    #
    #         columns = [x.strip() for x in line.split(',')]
    #
    #         label = columns[0]
    #         img_data = columns[1:]
    #
    #         data = np.zeros( (28,28), dtype=np.uint8)
    #         for row in range(28):
    #             data[row,:] = img_data[row*28:row*28 + 28]
    #
    #         plt.imshow(data, interpolation='nearest')
    #         plt.show()
    #
    #         if idx > 0:
    #             break

    from sklearn.ensemble import RandomForestClassifier

    with open(r'E:\Projects\numberguesser\train.csv', 'r') as train_file:

        all_data =  np.zeros( (42000, 785), dtype=np.uint8)

        for idx, line in enumerate(train_file):
            if idx == 0:
                continue
            columns = [x.strip() for x in line.split(',')]
            all_data[idx-1,:] = columns

    clf = RandomForestClassifier(n_estimators=10,
                                 max_depth=None,
                                 min_samples_split=2,
                                 random_state=0)
    img = all_data[:,1:]
    target = all_data[:,0]
    clf.fit(img,target)
    predictions = clf.predict(all_data[-41500:,1:])

    accuracy = sum( [1 for idx, prediction in enumerate(predictions) if all_data[-41500+idx,0] == prediction])
    print(accuracy)
    return clf
