import os, sys

# Append the parent directory to the Python path library
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import litevectors


def process_test_vectors(fileName: str, positive: bool):
    with open(fileName) as fin:
        while True:
            desc = fin.readline()
            data = fin.readline()
            if not desc:
                break
            try:
                print("Test:", desc.strip())
                litevectors.loadb(bytes.fromhex(data))

                if not positive:
                    print("Unflagged error parsing negative vector")
                    sys.exit(1)

            except Exception as ex:
                if positive:
                    print("Unexpected error parsing positive vector:", ex)
                    sys.exit(1)


if __name__ == '__main__':
    process_test_vectors("litevectors_positive.txt", True)
    process_test_vectors("litevectors_negative.txt", False)
    print()
    print("All Tests Successful")
