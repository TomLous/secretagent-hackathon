import sys
import binascii


def main():
    # input "dGVnZ???GUg??yb29tIG1uIHR1Z2V uIGR1IHNOcm9vbS??iBOZWdlbi BkZCBzdHJOgaW4?dGVnZ W4gZGUgc3Ryb29tIG1u" // https://www.aivdhackathon.nl/custom/theme/assets/images/aivd_hackathon.png

    base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    placeholder = '_'

    cypherText = "dGVnZ????GUg???yb29tIG1uIHR1Z2VuIGR1IHNOcm9vbS??iBOZWdlbiBkZCBzdHJOgaW4?dGVnZW4gZGUgc3Ryb29tIG1u"

    str = ""
    for n in range(0, len(cypherText)):
        c = cypherText[n:n+1]
        if c == '?':
            str += '000000'
        else:
            print "---"
            #print format(ord(c.encode()),'b')
            print bin(base64Chars.index(c))[2:].zfill(6)
            print base64Chars.index(c)
            str += bin(base64Chars.index(c))[2:].zfill(6)

        print c
        #print "\n"

    print cypherText
    print str
    print  binascii.unhexlify('%x' % int('0b' + str, 2))

    # # set the CBC parts. The first part is the IV
    # cypherTextIV = cypherText[0].decode('hex')
    # cypherTextC0 = cypherText[1].decode('hex')
    #
    # # define plaintexts
    # plainText = "Pay Bob 100$"
    # plainTextTarget = "Pay Bob 500$"
    #
    # # define paddings
    # paddingNum1 = str(len(cypherTextC0) - len(plainText))
    # padding1 = "".join([paddingNum1] * int(paddingNum1))
    #
    # paddingNum2 = str(len(cypherTextC0) - len(plainTextTarget))
    # padding2 = "".join([paddingNum2] * int(paddingNum2))
    #
    # # append to plaintext the paddings
    # plainText += padding1
    # plainTextTarget += padding2
    #
    # # XOR the plaintext to determine the value to XOR with
    # xorredPlainText = strxor(plainText, plainTextTarget)
    #
    # # Since the decription of c[0] is XORed with IV to retrieve the plaintext xor the IV with the desired mutation
    # newIV = strxor(xorredPlainText, cypherTextIV)
    #
    # # new CBC
    # print "New CBC\n", newIV.encode('hex'), cypherText[1]




# Output:
# New CBC
# 20814804c1767293bd9f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d


# xor two strings of different lengths
# def strxor(a, b):
#     if len(a) > len(b):
#         return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
#     else:
#         return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


main()