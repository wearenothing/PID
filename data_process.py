import pandas as pd


def median(data, windows):
    """
    对Series类型的信号数据进行中值滤波
    :param data: 信号数据，index是时间，value是信号值
    :type data: pd.Series
    :param windows: 中值滤波的窗口大小
    :type windows: int
    :return: 返回中值滤波之后的信号数据
    """
    return data.rolling(window=windows, center=True, min_periods=1).median()


def mean(data, windows):
    """
    对Series类型的信号数据进行均值滤波
    :param data: 信号数据，index是时间，value是信号值
    :type data: pd.Series
    :param windows: 均值滤波的窗口大小
    :type windows: int
    :return: 返回均值滤波之后的信号数据
    """
    return data.rolling(window=windows, center=True, min_periods=1).mean()


def median_df(data, windows, cols=None):
    """
    对DataFrame的指定列进行中值滤波，默认所有列
    :param data:
    :param windows: 中值滤波的窗口大小
    :param cols:if cols = None，means every column, else choose the specified columns
    :return:返回中值滤波之后的一组信号数据
    """
    if cols is None:
        return data.rolling(window=windows, center=True, min_periods=1).median()
    else:
        return data[cols].rolling(window=windows, center=True, min_periods=1).median()


def get_base(data):
    """
    返回信号的基底
    :param data: 信号（最好已经进行了中值滤波）
    :type data: Series
    :return: 0s之前信号的均值
    """
    return data[:0].mean()
    # return data[data.index < 0].mean()



# 归一化
