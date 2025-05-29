def solution(n, k):
    lamb__skewers = 12000 # 양고기는 12000원
    drink = 2000 # 음료수는 2000원
    answer = (lamb__skewers * n) + (drink * k) # 양고기 n인분 + 음료수 k개 계산
    if n // 10 >= 1: # 만약 양고기를 10인분 넘게 먹으면 음료수 1개 가격 차감
        answer -= drink * (n // 10)
    return answer