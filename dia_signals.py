# Signals under tree
Nodes = {
    'analysis':["pnbi1lsource","pnbi1rsource","pnbi2lsource","pnbi2rsource",'picrfii','picrfni','picrfbi','pecrh1i','pecrh2i','pecrh3i','pecrh4i'],

    'efit_east':['volume'],

    'efitrt_east':['drsep','wmhd/1000'],

    'euv_east':['bv','cuxxvi','liiii','wuta'],

    'pcs_east':['dfsdev','dfsdev2','pcrl01','pcrl02','lpcbuff','lpstarget','lpsda','sycvldl1']
}

# All tree names
Tree = list(Nodes.keys()) + ['east','east_1']

# tree name of corresponding signals
sig2tree = {}
for node in list(Nodes.keys()):
    for signal in Nodes[node]:
        sig2tree[signal]= node


# Classification of signals
exp2sigs={
    'NBI':["pnbi1lsource","pnbi1rsource","pnbi2lsource","pnbi2rsource"],
    'ICRF':['picrfii','picrfni','picrfbi'],
    'ECRH':['pecrh1i','pecrh2i','pecrh3i','pecrh4i'],
    'EUV': ['bv','cuxxvi','liiii','wuta'],
    'Energy':['wmhd/1000'],
    'Configuration':['drsep'],
    'Li_powder':['vldl1','vlds1'],
    'Li_pellet':['vlpd','igsgr','igsgf','vldh1','vlpt','igfc','freq'],
    'Bo_powder':['vldl1','idsg','idfm'],
    'neutral_pressure':['G109','G106']
}

# Explanation for each signal
sig2exp={
    'G109':'Neutral pressure of upper-divertor',
    'G106':'Neutral pressure of lower-divertor',
    'vldl1': 'Triggering waveform for Lithium/Boron dropper',
    'vlds1': 'Working waveform for Lithium dropper',
    'idsg': 'Working waveform for Boron dropper ',
    'idfm': 'Flow meter of boron dropper ',
    'wmhd/1000': 'Stored energy',
    'drsep': 'configuration',
    'bv': 'boron light emission',
    'cuxxvi': 'Cu impurity',
    'liiii': 'Lithium light emission',
    'wuta': 'Wu impurity'
}


# get tree name of one signal
def get_sig2tree(signal_name):
    signal_name = signal_name.lower()
    if signal_name in sig2tree:
        return sig2tree[signal_name]
    elif signal_name[-2:]=='_f':
        return 'east'
    else:
        return 'east_1'

def get_tree2sigs(tree_name):
    tree_name = tree_name.lower()
    if tree_name in Nodes:
        return Nodes[tree_name]
    else:
        return None

def get_exp2sigs(exp_name):
    exp_name = exp_name.lower()
    if exp_name in exp2sigs:
        return exp2sigs[exp_name]
    else:
        return None
def get_sig2exp(signal_name):
    signal_name = signal_name.lower()
    if signal_name in sig2exp:
        return sig2exp[signal_name]
    else:
        return None


def get_signals_tree(signal_list):
    classified_value = {}

    for signal in signal_list:
        tree = get_sig2tree(signal)
        if signal[-2:] == '_f':
            signal = signal[:-2]
        if tree in classified_value:
            classified_value[tree].append(signal)
        else:
            classified_value[tree] = [signal]

    return classified_value