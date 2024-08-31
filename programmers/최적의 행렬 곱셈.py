# def solution(matrix_sizes):
#     answer = 0
#     arr = []
#     ans = 0
    
#     def mul(m, matrix):
#         nonlocal ans
#         if len(matrix)==1:
#             print(ans)
#             arr.append(ans)
#             return

#         for i, mm in enumerate(matrix):
#             print(i, m, mm)
#             if not(m[1]==mm[0] or m[0]==mm[1]): continue
#             print('not')

#             tmp_m = matrix.copy()
#             tmp_m.pop(i)

#             res = 0
#             if m[1]==matrix[0][0]:
#                 res=m[0]*m[1]*matrix[0][1]
#                 return
#             else:
#                 res=m[0]*m[1]*matrix[0][0]
#             print(m, mm, ans, res)
#             ans+=res
#             mul(mm, tmp_m)
#             ans-=res
    
#     for i, m in enumerate(matrix_sizes):
#         print(i, m)
#         tmp_m = matrix_sizes.copy()
#         tmp_m=tmp_m[i+1:]
#         ans = 0
#         mul(m, tmp_m)
        
#     print(min(arr))
#     return min(arr)

# solution([[5,3],[3,10],[10,6]]) # 270