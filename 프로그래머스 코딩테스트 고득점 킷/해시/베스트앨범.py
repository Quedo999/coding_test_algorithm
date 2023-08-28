"""
고유번호 : genres의 인덱스
genres[i] : 고유번호가 i인 노래장르
plays[i] : 고유번호 i가 재생된 횟수
장르 종류는 100개 밑
장르에 속한 곡이 하나면 하나의 곡만 선택
가장 많이 재생된 노래를 2개까지
"""
genres=["classic", "pop", "classic", "classic", "pop", "hip"]
plays=[500, 600, 150, 800, 2500, 1000]

def sol(genres, plays):
    answer = []

    # 속한 노래가 많이 재생된 장르별 정렬
    # 장르: 총 재생수 딕셔너리 생성
    setGen = list(set(genres))
    genPlay = {i:0 for i in setGen}
    for i, gen in enumerate(genres):
        genPlay[gen] = genPlay[gen] + plays[i]
    genPlay = sorted(genPlay.items(), key=lambda x:x[1], reverse=True)

    for gen in genPlay:
        gen = gen[0]
        pList = {i:plays[i] for i, genre in enumerate(genres) if genre == gen}
        
        if len(pList) == 1:
            answer.append(list(pList.keys())[0])
            continue
        result = sorted(pList.items(), key=lambda x: x[1], reverse=True)[:2]
        for i in range(2):
            answer.append(result[i][0])

    return answer


print(sol(genres, plays))