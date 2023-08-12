import pandas as pd
import numpy as np
from MDSplus.connection import Connection
from tree_of_signal import get_tree_of_signal


def get_one_shot_one_signal(shot_number, sig, cnn=None, round=True) -> pd.Series:
    """
    返回某一炮的某一个信号的数据，用Series结构,
    :param round: set precision of time
    :param shot_number: 炮号
    :type shot_number: int
    :param sig: 信号名
    :type sig: str
    :param cnn: Connection
    :return: 时间和数值组成的Series
    """
    # TODO: Return None, if there is no data
    if cnn is None:
        cnn = Connection('mds.ipp.ac.cn')
    sig = sig.lower()
    tree = get_tree_of_signal(sig)
    cnn.openTree(tree, shot_number)

    time = cnn.get(f'dim_of(\\{sig})').data()
    if round:
        time = np.round(time, 4)
    values = cnn.get(f'\\{sig}').data()
    data = pd.Series(data=values, index=time)
    cnn.closeTree(tree, shot_number)
    return data


def get_many_signals_one_shot(shot_number, sigs, cnn=None,round=True) -> pd.DataFrame:
    """
    返回某一炮中一系列有采样时刻相同的信号数据，用dataframe表示
    如: ['jhg1','jhg4','jhg5',"CDG1", "DHG1"],['pjs205','pjs203','pas105','pas103'],
    ["nbi1lhi","nbi1rhi","nbi2lhi","nbi2rhi"],['g106','g107','g109']
    :param round:
    :type shot_number: int
    :param shot_number: 炮号
    :type sigs: list
    :param sigs: 同一系列信号名列表
    :type cnn: Connection
    :return: 时间和信号数值组成的DataFrame
    """
    if cnn is None:
        cnn = Connection('mds.ipp.ac.cn')
    data = pd.DataFrame()
    for sig in sigs:
        sig = sig.lower()
        data[sig] = get_one_shot_one_signal(shot_number, sig, cnn,round)
    return data


def get_one_signal_many_shots(shot_numbers, sig, cnn=None) -> pd.DataFrame:
    """
    返回多炮中同一信号的数据
    :type shot_numbers: list of int
    :param shot_numbers: 炮号数组
    :type sig: str
    :param sig: 信号名
    :type cnn: Connection
    """

    if cnn is None:
        cnn = Connection('mds.ipp.ac.cn')
    sig = sig.lower()
    # data_list = []
    # for shot_number in shot_numbers:
    #     data_list.append(get_one_shot_one_signal(shot_number, sig, cnn))
    # data = pd.concat(data_list, axis=1)
    data = pd.DataFrame()

    for shot_number in shot_numbers:
        data[shot_number] = get_one_shot_one_signal(shot_number, sig, cnn)

    return data


# TODO: 获得多炮的同一系列数据
def get_one_series_signal_many_shots() -> pd.DataFrame:
    pass


def get_many_signals_many_shots():
    pass


def get_da(shot_number,cn=None,position='l'):

    if cn is None:
        cn = Connection('mds.ipp.ac.cn')
    sig_list = []
    for i in range(1,14):
        sig_list.append(f'da{position}{i}')

    Da = get_many_signals_one_shot(shot_number,sig_list,cn)
    return Da

