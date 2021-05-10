text = """vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo
        jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui
        dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo
        otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv
         up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst
        tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui
        dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip
        fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi
        uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj
        scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op
        gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui
        foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO
        bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip
        """
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
message = list(text.upper())
# Перевод букв в индексы алфавита
message_numbers = [(alphabet.index(letter) if letter in alphabet else letter) for letter in message]
# Сдвиг в индексах по шифру Цезаря
new_message = [(alphabet[(number + 25) % 26]
                if number in range(26) else number) for number in message_numbers]
# Замена символов "(" и "+"
for index, symbol in enumerate(new_message):
    if symbol == '(':
        new_message[index] = "'"
    elif symbol == '+':
        new_message[index] = '"'
new_text = ''.join(new_message).split()
# Разделение текста на строки
data = [-1]
for index, word in enumerate(new_text):
    if '/' in word:
        data.append(index)
result = []
for index in range(len(data) - 1):
    result.append(new_text[data[index] + 1:data[index + 1] + 1])
# Сдвиг в каждой строке
for index1, line in enumerate(result):
    for index2, word in enumerate(line):
        for _ in range(index1 + 3):
            line[index2] = line[index2][-1] + line[index2][:-1]
# Печать построчно без символа "/"
for line in result:
    print(' '.join(line)[:-1].capitalize())
