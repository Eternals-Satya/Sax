def run_sax_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()

    # Konversi syntax jika diperlukan (bisa jadi lebih kompleks nantinya)
    code = code.replace("printx(", "print(")  # Contoh penggantian sintaks

    # Eksekusi file sebagai Python code
    exec(code)
