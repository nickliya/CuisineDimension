select
MAX_HP,MAX_GJ,MAX_FY,MAX_MZ,MAX_SB,
case when instr(replace(attr,6,'A'),'A') = 1 then ATTR1_VALUE when instr(replace(attr,6,'A'),'A') = 2 then ATTR2_VALUE else 0 end+SL_BJ+bj*2 zz_bj,
case when instr(replace(attr,7,'A'),'A') = 1 then ATTR1_VALUE when instr(replace(attr,7,'A'),'A') = 2 then ATTR2_VALUE else 0 end+SL_BS+bs*2 zz_bs,
case when substr(skillup,1,1) = 3 then s.SKILL_DESC_3 else s.SKILL_DESC_4 end skill,
ifnull(case when substr(skillup,1,1) = 3 then b.SKILL_DESC_3 else b.SKILL_DESC_4 end,'') block,
ifnull(case when substr(skillup,1,1) = 3 then s.LEVEL_3 else s.LEVEL_4 end,0) skill2,
ifnull(case when substr(skillup,1,1) = 3 then b.LEVEL_3 else b.LEVEL_4 end,0) block2
from
(select case when skill_up = 'B' then 34 when skill_up = 'S' then 43 when skill_up = 'BO' then 44 else 33 end skillup,
attr1||ATTR2 attr,ATTR1_VALUE,ATTR2_VALUE from equip_suit where TZ_NO = %s) t LEFT OUTER JOIN
(select SKILL_DESC_3,SKILL_DESC_4,LEVEL_3,LEVEL_4 from fairy_skill where skillFlag ='S' and SL_NO = %s) s LEFT OUTER JOIN
(select SKILL_DESC_3,SKILL_DESC_4,LEVEL_3,LEVEL_4 from fairy_skill where skillFlag ='B' and SL_NO = %s) b LEFT OUTER JOIN
(select MAX_HP,MAX_GJ,MAX_FY,MAX_MZ,MAX_SB,SL_BJ,SL_BS from fairy_detail d,fairy_detail_max m where d.SL_NO = m.SL_NO and d.SL_NO = %s) LEFT OUTER JOIN
(select %s bj,%s bs)