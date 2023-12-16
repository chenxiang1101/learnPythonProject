def strSpam(listSpam):
    result = ''
    for i in range(len(listSpam)):
        if i != len(listSpam) - 1:
            result += listSpam[i] + ', '
        else:
            result += 'and ' + listSpam[i]
    print(result)
strSpam(['apples', 'bananas', 'tofu', 'cats'])