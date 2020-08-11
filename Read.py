import threading


number_list = []
lock = threading.Lock()

def readfiles(read_file_address,column,split_flag):
    '''Read file base on the column and split flag.
    Give the file address,The column number, and the split flag
    Return the column in a list(str)
    '''
    try:
        with open(read_file_address,'r')as r_file:
            for line1 in r_file:
                targit_number = line1.rstrip().split(split_flag)[column-1]
                lock.acquire()
                global number_list
                number_list.append(targit_number)
                lock.release()
            print(number_list)
            return number_list
    except BaseException as e:
        print(e)

def writefile(write_file_address,write_str):
    with open(write_file_address,'a') as w_file:
        w_file.write(str(write_str)+'\n')

#Heapsort_bigendian
def big_endian(arr, start, end):
    root = start
    child = root * 2 + 1
    while child <= end:
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
            child = root * 2 + 1
        else:
            break

#Heapsort_sort
def heap_sort(arr,write_file_address='./3.txt'):
    w_file= open(write_file_address, 'a')
    first = len(arr) // 2 - 1
    for start in range(first, -1, -1):
        big_endian(arr, start, len(arr) - 1)
    for end in range(len(arr) - 1, -1, -1):
        arr[0], arr[end] = arr[end], arr[0]
        big_endian(arr, 0, end - 1)
        w_file.write(str(arr[end]) + '\n')
    w_file.close()
    return arr

def main():
    try:
        read_file1 = threading.Thread(target=readfiles, args=('./1.txt', 2, ',',))
        read_file2 = threading.Thread(target=readfiles, args=('./2.txt', 3, '?',))
        read_file1.start()
        read_file2.start()
        read_file1.join()
        read_file2.join()
        int_all_number = list(map(int,number_list))#change all type to int
        heap_sort(int_all_number,'./3.txt')
    except BaseException as e:
        print(e)

if __name__ == "__main__":
    main()

