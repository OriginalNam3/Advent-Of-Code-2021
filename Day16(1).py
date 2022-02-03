# Had to get help on this one :(
# The question was also really wordy ;-; I don't really want to read a lot, that's why I did maths in the first place
# One big thing I learnt is to redefine python functions to make your life easier. Redefining int() to work with lists makes this much easier

dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111', }
total = 0
ns = input()
s = ''
for c in ns:
    s += dict[c]

pyint = int


def int(x, y=10):
    return pyint("".join(x), y)


p = list(s)


def operator(p):
    global total
    # print("".join(p))
    version = int(p[:3], 2)
    p[:] = p[3:]
    # print(version)
    total += version
    id = int(p[:3], 2)
    # print(id)
    p[:] = p[3:]
    if id == 4:
        while True:
            cont = p.pop(0)
            p[:] = p[4:]
            if cont == '0':
                break
        return
    else:
        length = p.pop(0)
        if length == '0':
            length = int(p[:15], 2)
            p[:] = p[15:]
            np = p[:length]
            p[:] = p[length:]
            while np:
                operator(np)
        if length == '1':
            length = int(p[:11], 2)
            p[:] = p[11:]
            for _ in range(length):
                operator(p)


operator(p)
print(total)

# def literal(p):
#     count = 0
#     literal_value = ''
#     while True:
#         s = p[5 * count: 5 + 5 * count]
#         literal_value += s[1:5]
#         if s[0] == '0':
#             return int(literal_value, 2)
#         count += 1
#
#
# def operator(p):
#     global total
#     packet_version = p[0:3]
#     total += int(packet_version, 2)
#     packet_type = p[3:6]
#     if packet_type == '100':
#         operator(p[11:len(p)])
#         return
#         # literal(packet[6: len(packet)])
#     packet_lengthID = int(p[6])
#     c = 22 - (packet_lengthID * 4)
#     subpacketlength = int(p[7:c], 2)
#     # print(packet_lengthID, subpacketlength)
#     if packet_lengthID:
#         operator(p[c:len(p)])
#     if not packet_lengthID:
#         operator(p[c: c + subpacketlength])
#         operator(p[c + subpacketlength: len(p)])

#
# operator(s)
# print(total)


# Code I copied from hyper-neutrino and changed to work for mine
# dict = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111',}
#
# ns = input()
# s = ''
# for c in ns:
#     s += dict[c]
#
# pyint = int
# k = list(s)
#
# def int(x, y = 10):
#     return pyint("".join(x), y)
#
# def parse(k):
#     version = int(k[:3], 2)
#     k[:] = k[3:]
#     typeid = int(k[:3], 2)
#     k[:] = k[3:]
#     if typeid == 4:
#         data = []
#         while True:
#             cont = k.pop(0)
#             data += k[:4]
#             k[:] = k[4:]
#             if cont == "0": break
#         data = int(data, 2)
#         return (version, typeid, data)
#     else:
#         packets = []
#         if k.pop(0) == "0":
#             length = int(k[:15], 2)
#             k[:] = k[15:]
#             d = k[:length]
#             k[:] = k[length:]
#             while d:
#                 packets.append(parse(d))
#         else:
#             num = int(k[:11], 2)
#             k[:] = k[11:]
#             for _ in range(num):
#                 packets.append(parse(k))
#         return (version, typeid, packets)
#
# def vsum(k): This stuff is crazy, I wouldn't even think to use this, they are so used to dealing with tuples and slicing
#     t = k[0]
#     if k[1] == 4:
#         return t
#     else:
#         return t + sum(map(vsum, k[2]))
#
# q = parse(k)
#
# print(vsum(q))
