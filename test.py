from werkzeug.security import generate_password_hash,check_password_hash



password_hash=generate_password_hash("nihao")

print(password_hash)

print(check_password_hash(password_hash,"nihao"))