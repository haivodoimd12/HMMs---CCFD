import numpy as np

from clustering import KMeansClustering
from driver import Driver
from hidden_markov_model import HMM

from config import *


def get_input():
    while True:
        new_transaction = input('Nhap so tien giao dich moi (don vi nghin dong): ')
        if int(new_transaction) == TERMINATE:
            break
        new_transaction = k.predict(int(new_transaction))
        new_observation = np.append(observations[1:], [new_transaction])

        if h.detect_fraud(observations, new_observation, THRESHOLD):
            print('Phat hien gian lan')
        else:
            print('Giao dich binh thuong')


if __name__ == '__main__':
    d = Driver('C:/Users/DELL/Documents/Credit-Card-Fraud-Detection-master/Data/train_data.txt')

    h = HMM(n_states=STATES, n_possible_observations=CLUSTERS)
    k = KMeansClustering()

    observations = k.run(d.get_data()[0:192])
    h.train_model(observations=list(observations), steps=STEPS)

    get_input()
