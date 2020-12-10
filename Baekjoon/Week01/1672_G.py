# # # DNA 염기서열

# # def find_final(n,dna):
    
# #     if n==1:
# #         return print(dna)
# #     else:
# #         result=[]
# #         for k in range(2):
# #             if dna[n-1-k]=='A':
# #                 result.append(0)
# #             elif dna[n-1-k]=='G':
# #                 result.append(1)
# #             elif dna[n-1-k]=='C':
# #                 result.append(2)
# #             elif dna[n-1-k]=='T':
# #                 result.append(3)
            
# #         j=result[0]
# #         i=result[1]
# #         return find_final(n-1,dna[:n-2]+sample[i][j])

# # def find_final_2(n,dna):
# #     sample=[['A','C','A','G'],['C','G','T','A'],['A','T','C','G'],['G','A','G','T']]
# #     while True:
# #         result=[]
# #         for k in range(2):
# #             if dna[n-1-k]=='A':
# #                 result.append(0)
# #             elif dna[n-1-k]=='G':
# #                 result.append(1)
# #             elif dna[n-1-k]=='C':
# #                 result.append(2)
# #             elif dna[n-1-k]=='T':
# #                 result.append(3)
# #         j=result[0]
# #         i=result[1]
# #         if n==2:
# #             print(sample[i][j])
# #             break
# #         else:
# #             n=n-1
# #             dna=dna[:n-2]+sample[i][j]

# def find_final(n,dna,last_str):
#     while True:
#         if len(dna)==1:
#             return print('RESULT : ',dna)
#         else:
#             print('-----------')
#             print('N : ',n)
#             print('DNA : ',dna)
#             print('Last : ',last_str)
#             if last_str=="":
#                 an=dna[n-1]
#             else:
#                 an=last_str
#             an_1=dna[n-2]

#             result=[]
#             for i in range(4):
#                 if an==memo[i]:
#                     result.append(i)
#                 if an_1==memo[i]:
#                     result.append(i)
#             last_str=sample[result[1]][result[0]]
#             n=n-1
#             dna=dna[:n-1]
            


# # if __name__ == "__main__":
# #     n = int(input())
# #     dna = input()
# #     sample=[['A','C','A','G'],['C','G','T','A'],['A','T','C','G'],['G','A','G','T']]

# #     def find_final(n,dna,a):
        
# #         if a=="":
# #             an=dna[n-1]
# #             an_1=dna[n-2]

# #         else:
# #             an=a
# #             an_1=dna[n-2]

        
# #         return find_final(n-1,dna[:n-2],sample[i][j])
        
    
# #     find_final(n,dna,"")

# sample=[['A','C','A','G'],['C','G','T','A'],['A','T','C','G'],['G','A','G','T']]
# memo=['A','G','C','T']

# if __name__ == "__main__":
#     n = int(input())
#     dna = input()


#     find_final(n,dna,"")
    
sample=[['A','C','A','G'],['C','G','T','A'],['A','T','C','G'],['G','A','G','T']]
memo=['A','G','C','T']
def find_final(n,dna,last_str):
    while True:
        result=[]
        if len(dna)==1:
            print('last start an:{}, an_1:{}'.format(last_str,dna))
            an=last_str
            an_1=dna
            for i in range(4):
                if an_1==memo[i]:
                    result.append(i)
                if an==memo[i]:
                    result.append(i)
            return print(sample[result[1]][result[0]])
        else:
            print('------------')
            print("N : ",n)
            print("DNA : ",dna)
            print("LAST : ",last_str)
            if last_str=="":
                an=dna[n-1]
            else:
                an=last_str
            an_1=dna[n-2]

            for i in range(4):
                if an_1==memo[i]:
                    result.append(i)
                if an==memo[i]:
                    result.append(i)
                
            last_str=sample[result[1]][result[0]]
            n=n-1
            dna=dna[:n-1]
if __name__ == "__main__":
    n = int(input())
    dna = input()


    find_final(n,dna,"")    