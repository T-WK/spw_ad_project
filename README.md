# Text RPG

## 1. GUI

    - 메인 GUI (미정)

        - TEXT RPG 텍스트를 누르면 게임 실행

    - 플레이 GUI

        - 텍스트 이미지를 통한 애니메이션
        - 플레이어의 동작 버튼
        - 행동 결과 텍스트


## 2. 플레이어 직업과 스탯

    |직업|체력|공격력|주문력|치명타|방어력|마법방어력|회피|
    |----|----|-----|------|------|------|---------|----|
    |전사|중|하|상|상|하|하|하|상|
    |궁수|상|중|하|하|하|중|상|중|
    |마법사|하|상|하|하|상|중|하|중|
    |도적|상|하|하|하|중|상|상|하|


## 3. 몬스터 종류와 스탯 (조정중)

    - 고블린

        |종류|체력|공격력|주문력|회피|
        |----|----|-----|------|----|
        |도벽 고블린|하|하|하|상|
        |훈련병 고블린|하|하|하|하|
        |정예 고블린|중|중|하|하|
        |흉폭한 고블린|중|상|중|하|
        |오우거 왕|상|상|상|상|
    

    - 슬라임

        |종류|체력|공격력|주문력|회피|
        |----|----|-----|------|----|
        |노랑 슬라임|하|하|하|상|
        |초록 슬라임|하|하|하|하|
        |빨강 슬라임|중|상|중|하|
        |변형된 슬라임|하|상|상|중|
        |킹 슬라임|상|상|상|상|


    - 골렘

        |종류|체력|공격력|주문력|회피|
        |----|----|-----|------|----|
        |흙 골렘|하|하|하|하|
        |돌 골렘|중|하|하|하|
        |철 골렘|상|중|하|중|
        |다이아 골렘|상|중|하|중|
        |고대 골렘|상|상|상|상|
    

    - 늑대

        |종류|체력|공격력|주문력|회피|
        |----|----|-----|------|----|
        |늑대|중|상|하|상|
        |시바|중|중|중|중|
        |치와와|하|하|상|상|
        |도베르만|중|상|하|상|
        |케르베로스|상|상|상|상|
    

    - 최종보스

        - 전공책

## 4. 턴제 구조

    - 플레이어의 턴

        - 공격시
            - 플레이어가 공격력 만큼의 데미지를 준다.
        
        - 방어시
            - 플레이어가 일정 확률(회피 확률)로 몹의 공격을 피하고 받은 피해의 절반만큼의 데미지로 반격한다.
        
        - 스킬 사용시
            - 스킬 종류에 따라 행동 한다.
        
        - 도망가기
            - 다음 몬스터로 넘어간다.
        
        - 던전 나가기
            - 던전을 나간다.
                - 던전에서 획득한 경험치와 골드의 반을 잃는다 (레벨 다운x).


        - 몬스터의 행동

            - 플레이어의 공격을 일정확률로 회피하면 데미지의 절반을 받는다.
            - 데미지를 받는다.
            - 몬스터가 죽는다.
                - 겸험치와 배추또는 양배추를 떨어뜨리고 죽는다.
    
    - 몬스터의 턴

        - 공격시
            - 몬스터가 공격력 만큼의 데미지를 준다.
        
        - 스킬 사용시
            - 스킬 종류에 다라 행동 한다.
        
        - 도망가기
            - 일정확률로 도망간다.
                - 레벨 격차가 높을 수록 도망가는 확률이 높아진다.
            

        - 플레이어의 상태

            - 데미지를 받는다.
            - 플레이어가 방어를 하고있었으면 일정 확률(회피 확률)로 몹의 공격을 피하고 받은 피해의 절반만큼의 데미지로 반격한다.
            - 플레이어가 죽느다.
                - 던전에서 획득한 경험치와 골드의 반을 잃는다 (레벨 다운x).