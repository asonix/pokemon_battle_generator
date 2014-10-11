def wake(p_dict):
    """Cures status condition"""
    p_dict['status'] = p_dict['status'].replace('sleep', '')

