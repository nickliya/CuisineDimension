SELECT '【'||e_type_sub||'】'||e_bj||'暴', e_BJ, e_BS
FROM equip_info t,equip_suit n WHERE  e_type=3 AND t.E_TZ=n.TZ_NO AND n.TZ_NAME = '%s'