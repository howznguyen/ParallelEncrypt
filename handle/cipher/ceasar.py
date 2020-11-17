self = 'aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`~!@#$%^&*()'


def encrypt(plaintext,n):
    """Encrypt the string and return the ciphertext"""
    result = ''
    for l in plaintext:
        try:
            i = (self.index(l) + n) % len(self)
            result += self[i]
        except ValueError:
            result += l
    return result

def decrypt(ciphertext,n):
    """Decrypt the string and return the plaintext"""
    result = ''
    for l in ciphertext:
        try:
            i = (self.index(l) - n) % len(self)
            result += self[i]
        except ValueError:
            result += l
    return result


