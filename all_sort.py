


def quicksort(l):
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

#

def merge(l):
    if len(l) > 1:
        m = len(l) // 2
        a = l[:m]
        b = l[m:]
        merge(a)
        merge(b)
        i = j = k = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                l[k] = a[i]
                i += 1
            else:
                l[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            l[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            l[k] = b[j]
            j += 1
            k += 1

#
def find_min(l):
    smallest = l[0]
    smallest_index = 0
    for i in range(1, len(l)):
        if l[i] < smallest:
            smallest_index  = i
            smallest = l[i]
    return smallest_index

#           

def selection_sort(l):
    new_arr = []
    for i in range(len(l)):
        smallest_index = find_min(l)
        #print('smallest_index = ', smallest_index)
        new_arr.append(l.pop(smallest_index))
    return new_arr
#

if __name__ == '__main__':
    l = [7, 1, 6, -3, 9, 0, -4, 2, 8, 9, 10]
    print('l = ', l)
    print('quicksort')
    print('l = ', quicksort(l))
    print()
    
    #
    l = [7, 1, 6, -3, 9, 0, -4, 2, 8, 9, 10]
    print('l = ', l)
    print('merge')
    merge(l)
    print('l = ', l)
    print()

    #
    l = [7, 1, 6, -3, 9, 0, -4, 2, 8, 9, 10]
    print('l = ', l)
    new_l = selection_sort(l)
    print('selection_sort')
    print('l = ', new_l)










