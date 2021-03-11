if isinstance(annot, list) is True:
    # assert type(value) == list, f'{param} failed annotation check(wrong type): value = {value}\n  was type {type_as_str(value)} ...should be type {type_as_str(annot)}'

    try:
        assert type(
            value) == list, f'{param} failed annotation check(wrong type): value = {value}\n  ' \
                            f'was type {type(value)} ...should be type {type(annot)}'

        if len(annot) == 1:
            for index in range(len(value)):
                self.check(param, anot[0], value[index])
        else:
            assert len(value) == len(annot)
            for index in range(len(value)):
                self.check(param, annot[index], value[index])
    except AssertionError:
        try:
            errormessage = f'{param} failed annotation check(wrong type): value = {value[index]}\n  ' \
                           f'was type {type_as_str(value[index])} ...should be type {type_as_str(annot)}'
            if len(annot) == 1:
                errormessage += f'\nlist[{index}] check: {annot[0]}'
            else:
                errormessage += f'\nlist[{index}] check: {annot[index]}'
        except UnboundLocalError:
            errormessage = f'{param} failed annotation check(wrong number of elements): value = {value}\n  annotation had {len(annot)} elements{annot}'
        raise AssertionError(errormessage)