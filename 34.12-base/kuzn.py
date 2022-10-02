import io
import table
#S-блок
kPi = [
        252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77,
        233, 119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193,
        249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5,
        132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235,
        52, 44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181,
        112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 21, 161,
        150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117,
        25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245,
        36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15,
        236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151,
        96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70,
        146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64,
        134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73,
        76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32, 113, 103, 164,
        45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230,
        244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182
]
#обратный S-блок
kRevPi = [
        0xa5, 0x2d, 0x32, 0x8f, 0x0e, 0x30, 0x38, 0xc0, 0x54, 0xe6, 0x9e, 0x39,
        0x55, 0x7e, 0x52, 0x91, 0x64, 0x03, 0x57, 0x5a, 0x1c, 0x60, 0x07, 0x18,
        0x21, 0x72, 0xa8, 0xd1, 0x29, 0xc6, 0xa4, 0x3f, 0xe0, 0x27, 0x8d, 0x0c,
        0x82, 0xea, 0xae, 0xb4, 0x9a, 0x63, 0x49, 0xe5, 0x42, 0xe4, 0x15, 0xb7,
        0xc8, 0x06, 0x70, 0x9d, 0x41, 0x75, 0x19, 0xc9, 0xaa, 0xfc, 0x4d, 0xbf,
        0x2a, 0x73, 0x84, 0xd5, 0xc3, 0xaf, 0x2b, 0x86, 0xa7, 0xb1, 0xb2, 0x5b,
        0x46, 0xd3, 0x9f, 0xfd, 0xd4, 0x0f, 0x9c, 0x2f, 0x9b, 0x43, 0xef, 0xd9,
        0x79, 0xb6, 0x53, 0x7f, 0xc1, 0xf0, 0x23, 0xe7, 0x25, 0x5e, 0xb5, 0x1e,
        0xa2, 0xdf, 0xa6, 0xfe, 0xac, 0x22, 0xf9, 0xe2, 0x4a, 0xbc, 0x35, 0xca,
        0xee, 0x78, 0x05, 0x6b, 0x51, 0xe1, 0x59, 0xa3, 0xf2, 0x71, 0x56, 0x11,
        0x6a, 0x89, 0x94, 0x65, 0x8c, 0xbb, 0x77, 0x3c, 0x7b, 0x28, 0xab, 0xd2,
        0x31, 0xde, 0xc4, 0x5f, 0xcc, 0xcf, 0x76, 0x2c, 0xb8, 0xd8, 0x2e, 0x36,
        0xdb, 0x69, 0xb3, 0x14, 0x95, 0xbe, 0x62, 0xa1, 0x3b, 0x16, 0x66, 0xe9,
        0x5c, 0x6c, 0x6d, 0xad, 0x37, 0x61, 0x4b, 0xb9, 0xe3, 0xba, 0xf1, 0xa0,
        0x85, 0x83, 0xda, 0x47, 0xc5, 0xb0, 0x33, 0xfa, 0x96, 0x6f, 0x6e, 0xc2,
        0xf6, 0x50, 0xff, 0x5d, 0xa9, 0x8e, 0x17, 0x1b, 0x97, 0x7d, 0xec, 0x58,
        0xf7, 0x1f, 0xfb, 0x7c, 0x09, 0x0d, 0x7a, 0x67, 0x45, 0x87, 0xdc, 0xe8,
        0x4f, 0x1d, 0x4e, 0x04, 0xeb, 0xf8, 0xf3, 0x3e, 0x3d, 0xbd, 0x8a, 0x88,
        0xdd, 0xcd, 0x0b, 0x13, 0x98, 0x02, 0x93, 0x80, 0x90, 0xd0, 0x24, 0x34,
        0xcb, 0xed, 0xf4, 0xce, 0x99, 0x10, 0x44, 0x40, 0x92, 0x3a, 0x01, 0x26,
        0x12, 0x1a, 0x48, 0x68, 0xf5, 0x81, 0x8b, 0xc7, 0xd6, 0x20, 0x0a, 0x08,
        0x00, 0x4c, 0xd7, 0x74
]
#константы в hex виде
kC = [
        0x6EA276726C487AB85D27BD10DD849401,
        0xDC87ECE4D890F4B3BA4EB92079CBEB02,
        0xB2259A96B4D88E0BE7690430A44F7F03,
        0x7BCD1B0B73E32BA5B79CB140F2551504,
        0x156F6D791FAB511DEABB0C502FD18105,
        0xA74AF7EFAB73DF160DD208608B9EFE06,
        0xC9E8819DC73BA5AE50F5B570561A6A07,
        0xF6593616E6055689ADFBA18027AA2A08,
        0x98FB40648A4D2C31F0DC1C90FA2EBE09,
        0x2ADEDAF23E95A23A17B518A05E61C10A,
        0x447CAC8052DDD8824A92A5B083E5550B,
        0x8D942D1D95E67D2C1A6710C0D5FF3F0C,
        0xE3365B6FF9AE07944740ADD0087BAB0D,
        0x5113C1F94D76899FA029A9E0AC34D40E,
        0x3FB1B78B213EF327FD0E14F071B0400F,
        0x2FB26C2C0F0AACD1993581C34E975410,
        0x41101A5E6342D669C4123CD39313C011,
        0xF33580C8D79A5862237B38E3375CBF12,
        0x9D97F6BABBD222DA7E5C85F3EAD82B13,
        0x547F77277CE987742EA93083BCC24114,
        0x3ADD015510A1FDCC738E8D936146D515,
        0x88F89BC3A47973C794E789A3C509AA16,
        0xE65AEDB1C831097FC9C034B3188D3E17,
        0xD9EB5A3AE90FFA5834CE2043693D7E18,
        0xB7492C48854780E069E99D53B4B9EA19,
        0x056CB6DE319F0EEB8E80996310F6951A,
        0x6BCEC0AC5DD77453D3A72473CD72011B,
        0xA22641319AECD1FD835291039B686B1C,
        0xCC843743F6A4AB45DE752C1346ECFF1D,
        0x7EA1ADD5427C254E391C2823E2A3801E,
        0x1003DBA72E345FF6643B95333F27141F,
        0x5EA7D8581E149B61F16AC1459CEDA820,
]
it_key = []
#константы для преобразования l
kB = [ 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1 ]
#____________________________________________________________________
#склейка массива в hex строку
def arr_hex(a):
    result = ''
    for i in a:
        result +=i
    return result
#____________________________________________________________________
#перевод в бинарный вид на вход число
def cat (a):
    a = bin(a)[2:10]
    if len(a)<8:
        return ('0'*(8-len(a))+a)
    return a
#____________________________________________________________________
#
def cath (a):
    result = str(hex(a//16))[2:3] + str(hex(a%16))[2:3]
    return result
#____________________________________________________________________
# разность полиномов
def razn_m(a,b):
    for int in b:
        if int in a:
            a.remove(int)
        else :
            a.append(int)
    return sorted(a,reverse=True)
#____________________________________________________________________
# умножение в поле 
def umn(a,b):
    a = int(a,2)*256
    b = int(b,2)
    return cat(table.multTable[a+b])
#____________________________________________________________________
#разбиение строки в массив из 16 слов по 8 бит
def d_block(a,b):
    if b==0:
        if len(a)<32:
            a = '0'*(32-len(a)) + a
        result = []
        for i in range(0,len(a),2):
            result.append(cat(int(a[i:i+2],16)))
    else:
        result = ''
        for i in a:
            result += cath(int(i,2))
    return result
#____________________________________________________________________
#преобразование l на вход блок(128 бит) поделенный по 8 бит {в битовом виде}
def low_l(c):
    result = []
    for i in range(16):
        result.append(int(str(umn(c[i],cat(kB[i]))),2))
    b =0
    for k in result:
        b ^=k
    return cat(b)
#____________________________________________________________________
#преобразование R на вход блок(128 бит) {в битовом виде}
def pr_R (c):
    result = []
    result.append(low_l(c))
    for i in range(len(c)-1):
    	result.append(c[i])
    return result
#____________________________________________________________________
#преобразование L на вход блок(128 бит) {в битовом виде}
def pr_L(c):
    for i in range(16):
        c = pr_R(c)
    return c
#____________________________________________________________________
#нелинейное преобразование S на вход блок {в битовом виде}
def pr_S(c):
    result = []
    for a in c:
        a = a
        result.append(cat(kPi[int(a,2)]))
    return result
#____________________________________________________________________

#развертывание ключей на вход строка 256 бит = 32 байта
def key_raz(key):
    key_list = []
    key_list.append(key[0:128])
    key_list.append(key[128:256])
    return key
#____________________________________________________________________
#функция F[k](a1,a0) = (LSX[k](a1) ^ a0 , a1); на вход константа, и лист из двух ключей
def pr_F(c,a):
    result = [0,0]
    result[1] = a[0]
    temp = a[0]^c
    SX = []
    for i in range(16):
        x = temp % 256
        SX.append(cath(kPi[x]))
        temp = temp//256
    pr_sx = d_block(arr_hex(SX[::-1]),0)
    pr_lsx = d_block(pr_L(pr_sx),1)
    result[0] = int(pr_lsx,16)^a[1]
    return result
#____________________________________________________________________
#функция получения итерационных ключей
def iter_key(keys2,j):
    result = []
    for i in range(8):
            keys2 = pr_F(kC[8*j + i],keys2)
    result.append(keys2[0])
    result.append(keys2[1])
    return result
#____________________________________________________________________
#развертка ключей
def key_reamer(key):
    result = []
    a = key // pow(16,32)
    b = key % pow(16,32)
    ind = 0
    result.append(a)
    result.append(b)
    for j in range(4):
        keys2 = [result[2*j],result[2*j+1]]
        keys2 = iter_key(keys2,j)
        result.append(keys2[0])
        result.append(keys2[1])
    return result
#____________________________________________________________________
#преобразование LSX для шифрования
def pr_LSX(c,a):
    temp = a^c
    SX = []
    for i in range(16):
        x = temp % 256
        SX.append(cath(kPi[x]))
        temp = temp//256
    pr_sx = d_block(arr_hex(SX[::-1]),0)
    pr_lsx = d_block(pr_L(pr_sx),1)
    return int(pr_lsx,16)
#____________________________________________________________________
#шифрование блока данных на вход открытый текст в hex и ключи шифрования
def alg_cipher(op_t,it_key):
    for i in range(9):
        op_t = pr_LSX(it_key[i],op_t)
    op_t = it_key[len(it_key)-1]^op_t
    return op_t
#____________________________________________________________________
#формирование блоков из исходного файла на вход файл на выход лист 
def get_blocks(file,flag):
    c = 0
    strb = []
    s = ''
    for char in file: 
        c += 1
        s += cath(char)
        if c == 16:
            strb.append(int(s,16))
            s = ''
            c = 0
    if flag==0:
        if len(s)<32:
            s += '10'
            s += '00'*(16-len(s)//2)
            strb.append(int(s,16))
        else:
            strb.append(int('1'+'0'*31,16))
    return strb
#____________________________________________________________________
#зашифрование файла
def file_cipher(a,it_key):
    result = []
    k = 0
    for i in a:
        k += 1
        print(k,'/',len(a))
        result.append(alg_cipher(i,it_key))
    return result
#____________________________________________________________________
#запись шифртекста файла
def write_cipher(file,a):
    for text in a:
        file.write(bytes.fromhex(adhex(text)))            
    return file
#____________________________________________________________________
#дополнение hex'а
def adhex(a):
    a = hex(a)[2:]
    if len(a)<32:
        a = '0'*(32-len(a)) + a
    return a
#____________________________________________________________________
#обратное преобразование R на вход строка массив по байтам в двоичном виде
def obr_pr_R(a):
    result = []
    low = a[1:]
    low.append(a[0])
    temp = low_l(low)
    result = a[1:]
    result.append(temp)
    return result
#____________________________________________________________________
#обратное преобразование L на вход строка hex
def obr_pr_L(a):
    result = d_block(a,0)
    for i in range(16):
        result = obr_pr_R(result)
    result = d_block(result,1)
    return result
#____________________________________________________________________
#обратное преобразование S на вход d_block по 8 бит
def obr_pr_S(a):
    a = d_block(a,0)
    result = []
    for i in a:
        result.append(cat(kRevPi[int(i,2)]))
    result = d_block(result,1)
    return result
#____________________________________________________________________
#обратное преобразование SLX
def obr_SLX(k,text):
    result = k^text
    result = adhex(result)
    result = obr_pr_L(result)
    result = obr_pr_S(result)
    return int(result,16)
#____________________________________________________________________
#обратное преобразование блоки данных в hex'е 
def decode_cipher(text,it_key):
    result = []
    ite = 9
    k = 0
    for block in text:
        k += 1
        print(k,'/',len(text))
        for it in range(9,0,-1):
            block = obr_SLX(it_key[it],block)
        block = block^it_key[0]
        result.append(block)
    return result
#____________________________________________________________________
#удаление дополнения на вход все блоки 

def del_addition(dec):
    dec = [adhex(i) for i in dec]
    mask = '10'
    i = len(dec)-1
    while dec[i][32-len(mask):] != mask and len(mask)<= len(dec[i]):
        mask = mask + '00'
    dec[i] = dec[i][:32-len(mask)]
    return dec        
#____________________________________________________________________
#запись расшифрованного файла
def write_decode(file,dec):
    for block in dec:
        file.write(bytes.fromhex(block))
    return file
#____________________________________________________________________
#полное шифрование
def cipher_kuzn(fin,fout,fkey):
    fkey = open(fkey,'r')
    fkey = fkey.read()
    fkey = int(fkey,16)
    it_key = key_reamer(fkey)
    fin = open(fin,"rb")
    op_t = get_blocks(fin.read(),0)
    fout = open(fout,"wb")    
    out = file_cipher(op_t,it_key)
    fout = write_cipher(fout,out)
    fout.close()
    fin.close()    
    print("Success encode!!!")
#____________________________________________________________________
#полное расшифрование
def decipher_kuzn(fin,fout,fkey):
    fkey = open(fkey,'r')
    fkey = fkey.read()
    fkey = int(fkey,16)
    it_key = key_reamer(fkey)    
    fin = open(fin,"rb")
    dec = get_blocks(fin.read(),1)
    fout = open(fout,'wb')
    dec = decode_cipher(dec,it_key)
    dec = del_addition(dec)
    fout = write_decode(fout,dec)
    fout.close()
    fin.close()
    print("Success decode!!!")    
#____________________________________________________________________

print("Введите:\nФайл обработки | Файл вывода | Файл ключа | режим (encode/decode)")
fin,fout,fkey,mode = map(str,input().split())

if mode=='encode':
    cipher_kuzn(fin,fout,fkey)
elif mode=='decode':
    decipher_kuzn(fin,fout,fkey)


#24242 out key.txt decode
