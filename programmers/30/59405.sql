-- 상위 n개 레코드
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1; 
-- 최상위, 중복 허용
-- SELECT NAME FROM ANIMAL_INS WHERE DATETIME=(SELECT MIN(DATETIME) FROM ANIMAL_INS)
