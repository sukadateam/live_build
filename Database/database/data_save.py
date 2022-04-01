# -*- coding: utf-8 -*-
students=[]
active_users=[True, True, True]
denied_inputs=['', ' ', None]
data_bases=[['logs', True, 'all', 'list'], ['tools', True, 'all', 'column_row', ['name', 'id']]]
row=[['tools', [b'Circular Saw', b'Makita 1', 'TacoBell', b'5007FA', b'TacoBell', b' ', False]], ['tools', [b'Circular Saw', b'Makita 2', '', b'5007FA', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Makita 4', b'21614', b' ', b' ', b' ']], ['tools', [b'Circular Saw', b'Makita 5', '', b'5007FA', b' ', b' ', False]], ['tools', ['', b'Makita 6', b'*0021863', b'5007FA', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Makita 7', b'54079', b'5077B /Wormdrive', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Makita 9', b'*0072770', b'5007FA', b' ', b' ', False]], ['tools', [b'Circular saw', b'Makita ', b'*0001991', b'5007MGA / 7 1/4"', b'12/2021', b' ', False]], ['tools', [b'Circular saw', b'Makita ', b'*00010985', b'5007MGA / 7 1/4"', b'12/2021', b' ', False]], ['tools', [b'Circular saw', b'Makita ', b'*00015836', b'5104 /10 1/14"', b'12/2021', b' ', False]], ['tools', [b'Circular Saw', b'Porter Cable 3', b'065449 A 2013', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Porter Cable 4', b'A 037163', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Porter Cable 8', b'22603', b' ', b' ', b'Broken tool cabinet', False]], ['tools', [b'Circular Saw', b'Dewalt 6', b'17637', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Cordless Dewalt 1', b'43413', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Cordless Dewalt 2', b'799327', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw LH', b'Bosch LH circular saw', b'307000246', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw LH', b'Bosch LH circular saw', b'307000248', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Bosch RH circular saw', b'408046903', b' ', b' ', b' ', False]], ['tools', [b'Circular Saw', b'Bosch RH circular saw', b'505020874', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Bosch 1', b'2911', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Bosch 2', b' ', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Makita 3', b' ', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Dewalt 4', b'408931', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Dewalt 5', b'438543', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Dewalt 6', b'736664', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Dewalt 8 DW130', b'81661', b' ', b' ', b' ', False]], ['tools', [b'Corded Drill', b'Craftsman 6', b'33954', b' ', b' ', b' ', False]], ['tools', [b'Sawzall', b'Dewalt 4', b'83295 9948E', b' ', b' ', b' ', False]], ['tools', [b'Sawzall', b'Milwaukee 1', b'326A301067098', b' ', b' ', b'Broken tool cabinet', False]], ['tools', [b'Sawzall', b'Porter Cable 1', b'209454 A 2002', b' ', b' ', b' ', False]], ['tools', [b'Sawzall', b'Porter Cable 3', b'83284', b' ', b' ', b' ', False]], ['tools', [b'Multi Tool', b'Bosch Oscillating Saw', b'810036457', b'GOP30-40', b'10/2019', b' ', False]], ['tools', [b'Jig Saw', b'Bosch 1', b'***007681', b' ', b' ', b' ', False]], ['tools', [b'Jig Saw', b'Bosch 2', b'unreadable', b' ', b' ', b' ', False]], ['tools', [b'Jig Saw', b'Bosch', b' ', b' ', b' ', b' ', False]], ['tools', [b'Jig Saw', b'Craftsman 3', b'D7178', b' ', b' ', b' ', False]], ['tools', [b'Screw Gun', b'Hitachi 5', b'N30174', b' ', b' ', b' ', False]], ['tools', [b'Screw Gun', b'Hitachi 6', b'471439', b' ', b' ', b' ', False]], ['tools', [b'Screw Gun', b'Makita 7', b'318818', b' ', b' ', b' ', False]], ['tools', [b'Screw Gun', b'Porter Cable 3', b'1799599961', b' ', b' ', b' ', False]], ['tools', [b'Screw Gun', b'Porter Cable 4', b'141927A7905', b' ', b' ', b' ', False]], ['tools', [b'Screw Gun', b'Porter Cable 8', b' ', b' ', b' ', b' ', False]], ['tools', [b'Screw Gun', b'Milwaukee 1', b'792A394470903', b' ', b' ', b' ', False]], ['tools', [b'Rotozip', b'Porter Cable 2', b'195916A0071', b' ', b' ', b' ', False]], ['tools', [b'Rotozip', b'Rotozip 1', b'DK263387', b' ', b' ', b' ', False]], ['tools', [b'Rotozip', b'Rotozip3', b' ', b' ', b' ', b' ', False]], ['tools', [b'Rotozip', b'Porter Cable 3', b'202031A0042', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Bosch', b' ', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Milwaukee', b'A77A507383173', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Makita 1', b'1555947', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Makita 2', b'1197435', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Makita 3', b'140735', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Dewalt 1', b'312729', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Dewalt 2', b'177781', b' ', b' ', b' ', False]], ['tools', [b'Cordless Drill', b'Makita 4', b'1136058', b'XFD10', b'9-2020', b' ', False]], ['tools', [b'Cordless Drill', b'Makita 5', b'1165553', b'XFD10', b'9-2020', b' ', False]], ['tools', [b'Impact Driver', b'Makita 1', b'730721', b' ', b' ', b' ', False]], ['tools', [b'Impact Driver', b'Makita 2', b'1919902', b' ', b' ', b' ', False]], ['tools', [b'Impact Driver', b'Makita 3', b'119404', b' ', b' ', b' ', False]], ['tools', [b'Impact Driver', b'Makita 4', b'2147346', b'XDT11', b'9/1/2020', b' ', False]], ['tools', [b'Impact Driver', b'makita 5', b'2190014', b'XDT11', b'9/1/2020', b' ', False]], ['tools', [b'Nail gun', b'Porter cable 18 g 1/4\xe2\x80\x9d crown stapler', b'30BA31848S', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Porter cable 15g angle finish nailer', b'52411TYI', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Porter cable 15g angle finish nailer 2-1/2"', b'19196234L147', b'DA250C TY2', b'10-24-19', b' ', False]], ['tools', [b'Nail gun', b'Porter cable 15g angle finish nailer 2-1/2"', b'19126003L247', b'DA250C TY2', b'10-24-19', b' ', False]], ['tools', [b'Nail gun', b'Porter cable 18g brad nailer', b'744486136011', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Porter cable 18g brad nailer 2"', b'17113125QBJ', b'BN200C', b'10-24-19', b' ', False]], ['tools', [b'Nail gun', b'Porter cable 18g brad nailer 2"', b'18212306K147', b'BN200C', b'10-24-19', b' ', False]], ['tools', [b'Nail gun', b'Bostitch N80 stick nailer', b'2217 90', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Bostitch siding gun', b'16S355', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Bostitch N89C', b'09250-0082', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Bostitch brad nailer', b'1071660', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Senco roofing nail gun', b' ', b' ', b' ', b' ', False]], ['tools', [b'Nail gun', b'Bostitch 18g Flooring Stapler', b'19089058 J2 47', b'EHF 1838K', b'10-17-19', b' ', False]], ['tools', [b'Electric staple gun', b'Powershot pro T-50', b' ', b' ', b' ', b' ', False]], ['tools', [b'Power plane', b'Makita', b' ', b' ', b' ', b' ', False]], ['tools', [b'Drywall sanding vac', b'Porta Cable', b' ', b' ', b' ', b' ', False]], ['tools', [b'Drywall sanding vac', b'Porta Cable', b' ', b' ', b' ', b' ', False]], ['tools', [b'Collated screw gun', b'Rigid 6790', b'CS1113 50359', b' ', b' ', b' ', False]], ['tools', [b'Belt Sander', b'Porta Cable', b' ', b' ', b' ', b' ', False]], ['tools', ['', '', 'wefwef', '', '', '']], ['tools', ['', '', 'wfwef', '', '', '']], ['tools', ['', '', 'wef', '', '', '']], ['tools', ['BreakTheGame', 'Tesla', 'IDKMYNAME', 'TacosBell', 'Last Next Year', '[delete table][0]"All*"']], ['tools', ['Testing', 'Testing', 'TestingNew', 'yes', '3/10/21', 'Me', False]]]
lists=[]
known_users=['admin', 'teacher', 'awaewkfnawefujfbraoiehwhrohrewhrowiehriowehrowheroihweiorhwoenfjgofhsan iowrnshturwienywvtuirhewiutherugfbhibfhsgbeiugwohtrafnsvfdbgtwiuw4hruhn rubifuwbgwouhruwgbwegsfrgwehfohbfwgerwyteiuhruefwewewegergwtefefgw']
passwords=['admin', 'teacher', 'wugiwb']
permissions=['admin', 'teacher', 'admin']
global_password=True
allowed_types=['column_row', 'list']
allowed_users=['admin', 'student', 'teacher', 'secret']
debug=True
opto_data=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
opto_row=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 85, 0, 0, 0, 0, 0, 0]
opto_lists=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

