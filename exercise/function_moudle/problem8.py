def first_n_letter(data, n=3):
    # create out list data
    output = []
    for element in data:
        # slice n letter from target string
        output.append(element[0:n])
    return output


if(__name__ == '__main__'):
    print(first_n_letter(['Seoul', 'Daegu', 'Kwangju', 'Jeju']))