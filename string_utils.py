def split_before_each_uppercases(formula):
    if formula == "":
        return[]
    start = 0
    end = 1
    split_ = []
    for i in formula[1:]:
        if i.supper():
            split_formula.append(formula[start:end])
            start = end
            end = start + 1
        else:
            end += 1
        split_formula.append(formula[start:end])
        return(split_formula)
        


def split_at_first_digit(formula):
    digit_l = 1
    for i in formula[1:]:
        if i.isdigit():
            break
        else:
            digit_l += 1
            
        prefix = formula[:digit_l]
        num_p = formula[digit_l:]
        if digit_1 == len(formula):
            return (formula, 1)
    return(prefix, int(num_p))
    num_p = formula[digit_l:]
    if digit_1 == len(formula):
        return(formula, 1)
    return(prefix, int(num_p))
