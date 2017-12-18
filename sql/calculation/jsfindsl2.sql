SELECT SL_TYPE,SL_NAME
FROM fairy_detail n,fairy_skill s
WHERE n.SL_NO=s.SL_NO AND s.SKILL_TYPE=2 AND s.skillFlag='S' AND SL_TYPE=%s ORDER BY s.SL_NO