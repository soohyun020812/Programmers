/*
문제 설명
다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블입니다.
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블은 아래와 같은 구조로 되어있으며,
HISTORY_ID, CAR_ID, START_DATE, END_DATE는
각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서
대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시하는
컬럼(컬럼명: RENT_TYPE)을 추가하여 대여기록을 출력하는 SQL문을 작성해주세요.
결과는 대여 기록 ID를 기준으로 내림차순 정렬해주세요.
*/

SELECT 
    HISTORY_ID,
    CAR_ID,
    START_DATE,
    END_DATE,
    CASE 
        WHEN END_DATE - START_DATE + 1 >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END AS RENT_TYPE
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE 
    START_DATE >= TO_DATE('2022-09-01', 'YYYY-MM-DD')
    AND START_DATE < TO_DATE('2022-10-01', 'YYYY-MM-DD')
ORDER BY 
    HISTORY_ID DESC;
