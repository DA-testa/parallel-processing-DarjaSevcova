# python3
#Darja Ševcova 221RDC039 

def parallel_processing(n, m, data):
    output = []
    thr = [(0,i) for i in range(n)]
    for i in range(m):
        minthread = min(thr, key=lambda x: x[1])
        output.append((minthread[0], minthread[1]))
        thr[minthread[0]] = (minthread[0], minthread[1] + data[i])
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    data = list(map(int, input().split()))                     

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1]


if __name__ == "__main__":
    main()
