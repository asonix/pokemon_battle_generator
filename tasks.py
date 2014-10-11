from collections import Counter

class IVTask(object):
    def __init__(self, iv_min, iv_max):
        self.a = iv_min
        self.b = iv_max
    def __call__(self):
        return self.__recurse__(self.a, self.b, 31, 6, [])
    def __str__(self):
        return "combinations range {} to {}".format(self.a, self.b)
    def __recurse__(self, _range_l, _range_u, _max, _depth, _list, _value=[]):
        return_list = []
        if len(_value) < 3:
            print(" "*(2*len(_value)+2) + "Example test: {}, example result: {}"
                    .format(_value,
                        _list[len(_list)-1] if len(_list) > 0 else "0"))
        if _depth == 3 and Counter(_value)[_max] == 0:
            _new = list(_value)
            _new.append(_max)
            _new.append(_max)
            _new.append(_max)
            self.__recurse__(0, _max, _max, 0, _list, _new)
        elif _depth == 2 and Counter(_value)[_max] == 1:
            _new = list(_value)
            _new.append(_max)
            _new.append(_max)
            self.__recurse__(0, _max, _max, 0, _list, _new)
        elif _depth == 1 and Counter(_value)[_max] == 2:
            _new = list(_value)
            _new.append(_max)
            self.__recurse__(0, _max, _max, 0, _list, _new)
        elif _depth != 0:
            for i in range(_max+1):
                if len(_value) != 0 or (len(_value) == 0 and i >= _range_l and i < _range_u):
                    _new = list(_value)
                    _new.append(i)
                    if len(_value) == 0:
                        return_list.append(self.__recurse__(0, _max, _max,
                                _depth-1, _list, _new))
                    else:
                        self.__recurse__(0, _max, _max, _depth-1, _list, _new)
        else:
            use = False
            for i in range(len(_value)):
                for j in range(len(_value)):
                    for k in range(len(_value)):
                        if _value[j] + _value[k] + _value[i] == _max*3:
                            if i != j and i != k:
                                use = True
                                break
            if tuple(_value) not in _list and use == True:
                _list.append(tuple(_value))

        if return_list != []:
            return return_list
        return _list


class EVTask(object):
    def __init__(self, ev_min, ev_max):
        self.a = ev_min
        self.b = ev_max
    def __call__(self):
        return self.__recurse__(self.a, self.b, 252, 12, 6, [], 508)
    def __str__(self):
        return "combinations range {} to {}".format(self.a, self.b)
    def __recurse__(self, _range_l, _range_u, _max, _scale,
            _depth, _list, _total, _value=[]):
        return_list = []
        if len(_value) < 3:
            print(" "*(2*len(_value)+2) + "Example test: {}, example result: {}"
                    .format(_value,
                        _list[len(_list)-1] if len(_list) > 0 else "0"))
        if _depth != 0:
            if _scale*sum(_value) <= _total:
                if _scale*sum(_value) == _total and _depth > 1:
                    _new = list(_value)
                    for i in range(_depth-1):
                        _new.append(0)
                    self.__recurse__(0, _max, _max, _scale,
                            _depth-1, _list, _total, _new)
                elif _scale*sum(_value)+_max < _total and _depth == 1:
                    pass
                elif _scale*sum(_value)+_max >= _total and _depth == 1:
                    _new = list(_value)
                    _new.append((_total-sum(_value)*_scale)/_scale)
                    self.__recurse__(0, _max, _max, _scale,
                            _depth-1, _list, _total, _new)
                else:
                    if sum(_value)*_scale <= _total:
                        for i in range(int((_max+1)/_scale)):
                            if len(_value) != 0 or (len(_value) == 0 and i*_scale > _range_l and i*_scale <= _range_u):
                                if sum(_value)*_scale + i*_scale <= _total:
                                    _new = list(_value)
                                    _new.append(i)
                                else:
                                    _new = list(_value)
                                    _new.append((_total-_scale*sum(_value))/_scale)
                                if len(_value) == 0:
                                    return_list.append(self.__recurse__(0, _max, _max, _scale,
                                            _depth-1, _list, _total, _new))
                                else:
                                    self.__recurse__(0, _max, _max, _scale,
                                            _depth-1, _list, _total, _new)
        else:
            if sum(_value)*_scale == _total:
                for i in range(len(_value)):
                    _value[i] *= _scale
                if tuple(_value) not in _list:
                    _list.append(tuple(_value))

        if return_list != []:
            return return_list
        return _list

