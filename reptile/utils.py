import string, random


def phone_num(num):
    all_phone_nums = set()
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                 '188',
                 '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    for i in range(num):
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        # res = start+end+'\n'
        res = start + end
        all_phone_nums.add(res)
        # with open('d:\\phone.txt','w',encoding='utf-8') as fw:
        #     fw.writelines(all_phone_nums)

    print(all_phone_nums)
    return all_phone_nums


phone_num(100)
