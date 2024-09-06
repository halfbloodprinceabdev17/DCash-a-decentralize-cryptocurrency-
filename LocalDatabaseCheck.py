import hashlib

def get_file_hash(file_path):
    """Calculate and return the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    # Provide the paths and names of the three files you want to compare
    file_info = [
        ("NodeData/ChainData5001.txt", "Node 1"),
        ("NodeData/ChainData5002.txt", "Node 2"),
        ("NodeData/ChainData5003.txt", "Node 3"),
    ]

    hashes = [get_file_hash(file_path) for file_path, _ in file_info]
    majority_hash = max(set(hashes), key=hashes.count)
    majority_count = hashes.count(majority_hash)

    if majority_count >= len(file_info)*(2/3):
        print(f"The majority of files with the same data (count: {majority_count}):")
        for file_path, file_name in file_info:
            if get_file_hash(file_path) == majority_hash:
                pass
                #print(file_name)
            else:
                print(file_name," is Compromised")
    else:
        print("Files are different.")


if __name__ == "__main__":
    main()
