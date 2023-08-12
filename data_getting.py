import pandas as pd
import numpy as np
import MDSplus as mds
from connection import cnn
import dia_signals as ds

def get_shot_signal(shot, signal):
    """
    Get 'signal' data from 'shot'
    :param shot: shot number
    :type shot: int
    :param signal: signal name
    :type signal: str
    :return: Series
    """
    tree = ds.get_sig2tree(signal)
    if signal[-2:] == '_f':
        signal = signal[:-2]
    cnn.openTree(tree,shot)

    # TODO: MDS Exception
    # Distinguish Nodata from NoNODE
    index = cnn.get(f'dim_of(\\{signal})').data()
    value = cnn.get(f'\\{signal}').data()
    cnn.closeTree(tree,shot)
    data = pd.Series(value,index=index)
    return data


