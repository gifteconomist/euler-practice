def is_mod_3_or_5(num: int) -> bool:
    if (num % 3 == 0) or (num % 5 == 0):
        return True
    return False


if __name__ == "__main__":
    multiples_3_or_5 = []
    ceiling = 1000
    for i in range(ceiling):
        if is_mod_3_or_5(i):
            multiples_3_or_5.append(i)

    print(sum(multiples_3_or_5))
