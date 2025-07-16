import os, secrets

def secure_delete(path, passes=1):
    if not os.path.isfile(path):
        print(f"Path {path} is not a file.")
        return
    length = os.path.getsize(path)
    with open(path, "r+b") as f:
        for _ in range(passes):
            f.seek(0)
            f.write(secrets.token_bytes(length))
            f.flush()
            os.fsync(f.fileno())
    os.remove(path)
    print(f"Securely deleted {path} with {passes} passes.")

def secure_delete_dir(directory, passes=1):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            secure_delete(os.path.join(root, name), passes)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(directory)
    print(f"Securely deleted directory {directory} with {passes} passes on all files.")