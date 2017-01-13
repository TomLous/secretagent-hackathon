import sys
import binascii


def main():
    # https://www.aivdhackathon.nl/custom/theme/assets/images/aivd_hackathon.png
    # Whatch out for l vs 1, O vs 0
    # Probably base64 encoded

    decodedString = ""

    cypherText = "dGVnZ?GUg?yb29tIGluIHRlZ2VuIGRlIHN0cm9vbS?iB0ZWdlbiBkZSBzdHJ?0gaW4?dGVnZW4gZGUgc3Ryb29tIGlu"

    binaryChunks = "".join(map(lambda n:base64decode(cypherText[n:n+1]), range(0, len(cypherText)))).split("_")

    for ch in binaryChunks:
        chunk = ch
        maxValid = 0
        bestAttempt = None

        while True:
            asciiArr = binToASCIIArr(chunk)

            validChars = map(lambda c: validASCIIchr(c), asciiArr)
            middleValid = all(validChars[1:-1])
            numValid = validChars.count(True)

            if middleValid:
                bestAttempt = asciiArr
                break
            else:
                if numValid > maxValid:
                    maxValid = numValid
                    bestAttempt = asciiArr

                if (chunk[0:8] == '00000000'): #something went wrong
                    break

                # shift until middle valid
                chunk = '00' + chunk

        asciiArr = bestAttempt

        # first incorrect?
        if not validASCIIchr(asciiArr[0]):
            #print format(ord(asciiArr[0]),'b')
            asciiArr[0] = '_'

        if not validASCIIchr(asciiArr[-1]):
            # print format(ord(asciiArr[-1]), 'b')
            asciiArr[-1] = '_'

        # print asciiArr

        decodedString  += "".join(asciiArr)


    print cypherText
    print decodedString


def validASCIIchr(c):
    allowedChars = " abcdefghijklmnopqrstuvwxyz"
    return allowedChars.find(c) >= 0


def binToASCIIArr(binstr):
    return list(map(lambda b: chr(int(b, 2)), (binstr[0 + i:8 + i] for i in range(0, len(binstr), 8))))

def base64decode(c):
    base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    if c == '?':
        return "_"
    else:
        return bin(base64Chars.index(c))[2:].zfill(6)

main()