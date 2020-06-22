import sys

def dynamic_array(n):
    data = []
    for _ in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a,b))
        data.append(None)

if __name__ == "__main__":
    dynamic_array(30)