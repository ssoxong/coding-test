from urllib import parse
import urllib.request
import json

HANDLE = 'ssoxong'

assignment = [
    [1000,10950,1008,10951,10952,10953,15552,11718],
    [25501,2751,15649,15650,11729],
    [17466,1629,11819,11050,11051,1978,15965,16563,2609,25344,17425],
    [2751,11650,10814,1920,2805,15810,2417],
    [21870,10090,1725],
    [2748,1463,1912,11053,2293,2294,12865,9251,12852,14002,9252],
    [10828,9012,17298,1725,10845,10866,2003,11003,14289],
    [11047,25312,11399,1931,14908,2180,1260,11724,2178,1012,14940],
    [2252,28360,14567,15681,1949,10272],
    [1822,20920,2015,2075,2696,1976,1197,20390,28119],
    [1753,11779,16118,11404,11780,23258,11657]
]

additional = [
    [2003,17425,11659,8298,4307,9012,27297,2437,28065],
    [1992,1074,16974,2448,15918,18665,1891,17297,1351,9537,19333],
    [1990,2824,25342,11690,11688,20505,17840],
    [2512,17245,2110,27654,1637,10227],
    [14601,9537,25686,4256,2261,19333,1067],
    [4994,15910,10844,1958,5557,2616,12869,1344,11049,5550,12013,9520,5573,2315,2392],
    [10799,6051,2800,2867,23735,15678,27935,11475,1533],
    [2878,21761,13975,28340,11877,14464,16496,12776,7576,15971,14442,13913,17071],
    [2637,25953,18780,2394,3044,16297,28169],
    [1351,2957,15942,13306,17469,13309,22306,2887,4792],
    [1238,19701,12930,1219,13141,24024,20445,7577,27400,18253]
]

def get_solve_count(handle, problem_list):
    query = 'solved_by:' + handle + ' ('
    for i in range(len(problem_list)):
        query += 'id:' + str(problem_list[i]) + (' | ' if i + 1 < len(problem_list) else ')')
    url = 'https://solved.ac/api/v3/search/problem?query=' + parse.quote(query)
    res = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    return res.get('count')

def get_user_info(handle, problemset, desc):
    weeks = len(problemset)
    res = [get_solve_count(handle, problemset[i]) for i in range(weeks)]
    total = [len(problemset[i]) for i in range(len(problemset))]
    ratio = [res[i] / total[i] * 100 for i in range(len(problemset))]

    print(handle, desc)
    for i in range(weeks):
        print('%d주차: %.2f (%d/%d)' % (i+1, res[i] / total[i] * 100, res[i], total[i]))
    print('전체: %.2f (%d/%d)' % (sum(res) / sum(total) * 100, sum(res), sum(total)))
    print()

get_user_info(HANDLE, assignment, '필수 문제')
get_user_info(HANDLE, additional, '추가 문제')