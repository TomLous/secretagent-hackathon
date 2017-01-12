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
            str += '111111'
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



main()