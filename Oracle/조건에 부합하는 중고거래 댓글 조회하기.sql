/*
문제 설명 
다음은 중고거래 게시판 정보를 담은 USED_GOODS_BOARD 테이블과
중고거래 게시판 첨부파일 정보를 담은 USED_GOODS_REPLY 테이블입니다.
USED_GOODS_BOARD 테이블은 다음과 같으며
BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS,
VIEWS은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.
*/

SELECT 
    b.TITLE, 
    b.BOARD_ID, 
    r.REPLY_ID, 
    r.WRITER_ID, 
    r.CONTENTS, 
    TO_CHAR(r.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE
FROM 
    USED_GOODS_BOARD b
JOIN 
    USED_GOODS_REPLY r 
ON 
    b.BOARD_ID = r.BOARD_ID
WHERE 
    TO_CHAR(b.CREATED_DATE, 'YYYY-MM') = '2022-10'
ORDER BY 
    r.CREATED_DATE ASC, 
    b.TITLE ASC;
