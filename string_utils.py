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
    digit_place = 1
    for i in formula[1:]:
      if i.isdigit():
        break

      else:
        digit_place += 1

    prefix = formula[:digit_place]
    num_pos = formula[digit_place:]

    if digit_place == len(formula):
        return (formula, 1)

    return (prefix, int(num_pos))
