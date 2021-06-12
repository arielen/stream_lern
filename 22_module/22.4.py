speakers_file = open("speakers.txt", "r", encoding="utf-8")
sym_count = []
for i_string in speakers_file:
    print(i_string, end='')
    sym_count.append(str(len(i_string)))
sym_count_str = '\n'.join(sym_count)
speakers_file.close()

counts_file = open("sym_counts.txt", "w")
counts_file.write(sym_count_str)
counts_file.close()
