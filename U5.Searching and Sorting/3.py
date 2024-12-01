import base64
file_to_obf=open('search_algorithms.py','r').read()
encrypted_code = base64.b64encode(file_to_obf.encode("utf-8"))
print(encrypted_code)
print(encrypted_code.decode('utf-8'))
