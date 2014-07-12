'''
Created on Jun 24, 2014

@author: w
'''

def main():
    print first_mendel(2.0, 2.0 ,2.0)

def first_mendel(k, m, n):
    total = k + m + n
    prob_k = k/total
    prob_m = m/total
    prob_n = n/total
    
    prob = (prob_k * prob_k) + (prob_k * prob_n) + (prob_k * prob_m * 0.5)  
      
    return prob

def ros_5():
    fin = open('./rosalind_ini6.txt', 'r')
    fout = open('./output.txt', 'w')
    
    contents = fin.read().split()
    dic = {}
    for string in contents:
        if string in dic:
            dic[string] = dic[string] + 1
        else:
            dic[string] = 1
    for key, value in dic.items():
        print key + " " + str(value)
      
    
    fin.close()
    fout.close()
    return 0


if __name__ == '__main__':
    main()