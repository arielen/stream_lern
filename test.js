function div_count(number) {
    count = 0;
    while (number != 0) {
        number = number / 2
        if (number != 0) {
            max_number = number
        }
        count += 1
    }
    return count, max_number
}

div_count(1)