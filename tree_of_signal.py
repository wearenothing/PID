def get_tree_of_signal(sig):
    signal_tree = {
        "dfsdev": "pcs_east",
        "dfsdev2":  "pcs_east",
        "pcrl01": "pcs_east",
        "pcrl02": "pcs_east",
        "volume":   "efit_east",
        'cuxxvi':   "euv_east",
        'wuta':     "euv_east",
        "taue_mhd":     "energy_east",
        "lpcbuff":  "pcs_east",
        "pnbi1lsource": "analysis",
        "pnbi1rsource": "analysis",
        "pnbi2lsource": "analysis",
        "pnbi2rsource": "analysis",
        'picrfii': "analysis",
        'picrfni': "analysis",
        'picrfbi': "analysis",
        'pecrh1i': 'analysis',
        'pecrh2i': 'analysis',
        'pecrh3i': 'analysis',
        'pecrh4i': 'analysis',
        'drsep': "efitrt_east",
        #储能
        'wmhd/1000': "efitrt_east"

        # "jhg1":     "east_1",
        # "jhg4":     "east_1",
        # "jhg5":     "east_1",
        # "cdg1":     "east_1",
        # "dhg1":     "east_1",
        # "pjs205":   "east_1",
        # "pjs203":   "east_1",
        # "pas105":   "east_1",
        # "pas103":   "east_1",
        # "nbi1lhi":  "east_1",
        # "nbi1rhi":  "east_1",
        # "nbi2lhi":  "east_1",
        # "nbi2rhi":  "east_1",
        # "vpi20":    "east_1",
        # "g106":     "east_1",
        # "g107":     "east_1",
        # "g109":     "east_1",
        }
    if sig in signal_tree:
        return signal_tree[sig]
    else:
        return 'east_1'
