/* Write your PL/SQL query statement below */
WITH zombie AS (
	SELECT A.session_id
	,A.user_id
	,MIN(event_timestamp) AS session_start
	,MAX(event_timestamp) AS session_end
	,COUNT(CASE WHEN A.event_type='scroll' THEN 1 END) AS scroll_count
	,COUNT(CASE WHEN A.event_type='click' THEN 1 END) AS click_count
	,COUNT(CASE WHEN A.event_type='purchase' THEN 1 END) AS purchase_count
	FROM app_events A GROUP BY A.session_id, A.user_id
), zombie_session AS (
	SELECT Z.*, (Z.session_end-Z.session_start)*24*60 AS duration FROM zombie Z    
)
SELECT Z.session_id,Z.user_id,Z.duration AS session_duration_minutes, Z.scroll_count 
FROM zombie_session Z
WHERE duration>30 AND scroll_count>4 AND (click_count*1.00/scroll_count)<0.20 AND purchase_count<=0
ORDER BY scroll_count DESC, session_id ASC;