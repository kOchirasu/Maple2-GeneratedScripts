""" trigger/02000521_bf/normal.xml """
import trigger_api


class roomCheck2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.spawn_monster(spawn_ids=[101,102,103,104,105], auto_target=False)
        self.set_mesh(trigger_ids=[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917], visible=False) # 1층 피직
        self.set_mesh(trigger_ids=[1800,1801,1802,1803,1804,1805,1806,1807,1808,1809], visible=False) # 3층 피직
        # 1, 2, 3층 사다리 안보이기 처리
        self.set_ladder(trigger_ids=[1101], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1102], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1103], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1104], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1105], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1106], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1107], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1108], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1109], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1110], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1111], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1112], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1113], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1114], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1115], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1116], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1117], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1118], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1201], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1202], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1203], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1204], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1205], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1206], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1207], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1208], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1209], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1210], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1211], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1212], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1213], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1214], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1215], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1216], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1217], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1218], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1301], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1302], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1303], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1304], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1305], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1306], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1307], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1308], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1309], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1310], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1311], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1312], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1313], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1314], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1315], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1316], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1317], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1318], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1401], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1402], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1403], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1404], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1405], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1406], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1407], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1408], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1409], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1410], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1411], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1412], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1413], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1414], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1415], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1416], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1417], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1418], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1501], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1502], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1503], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1504], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1505], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1506], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1507], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1508], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1509], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1510], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1511], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1512], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1513], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1514], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1515], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1516], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1517], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1518], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1601], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1602], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1603], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1604], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1605], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1606], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1607], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1608], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1609], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1610], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1611], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1612], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1613], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1614], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1615], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1616], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1617], visible=False, enable=False, fade=0)
        self.set_ladder(trigger_ids=[1618], visible=False, enable=False, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103,104,105]):
            return step_02(self.ctx)


class step_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917], visible=True) # 1층 피직
        # 1, 2, 3층 사다리 보이기 처리
        self.set_ladder(trigger_ids=[1101], visible=True, enable=True, fade=1)
        self.set_ladder(trigger_ids=[1102], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1103], visible=True, enable=True, fade=3)
        self.set_ladder(trigger_ids=[1104], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[1105], visible=True, enable=True, fade=5)
        self.set_ladder(trigger_ids=[1106], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[1107], visible=True, enable=True, fade=7)
        self.set_ladder(trigger_ids=[1108], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[1109], visible=True, enable=True, fade=9)
        self.set_ladder(trigger_ids=[1110], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[1111], visible=True, enable=True, fade=11)
        self.set_ladder(trigger_ids=[1112], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[1113], visible=True, enable=True, fade=13)
        self.set_ladder(trigger_ids=[1114], visible=True, enable=True, fade=14)
        self.set_ladder(trigger_ids=[1115], visible=True, enable=True, fade=15)
        self.set_ladder(trigger_ids=[1116], visible=True, enable=True, fade=16)
        self.set_ladder(trigger_ids=[1117], visible=True, enable=True, fade=17)
        self.set_ladder(trigger_ids=[1118], visible=True, enable=True, fade=18)
        self.set_ladder(trigger_ids=[1201], visible=True, enable=True, fade=1)
        self.set_ladder(trigger_ids=[1202], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1203], visible=True, enable=True, fade=3)
        self.set_ladder(trigger_ids=[1204], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[1205], visible=True, enable=True, fade=5)
        self.set_ladder(trigger_ids=[1206], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[1207], visible=True, enable=True, fade=7)
        self.set_ladder(trigger_ids=[1208], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1209], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[1210], visible=True, enable=True, fade=9)
        self.set_ladder(trigger_ids=[1211], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[1212], visible=True, enable=True, fade=11)
        self.set_ladder(trigger_ids=[1213], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[1214], visible=True, enable=True, fade=13)
        self.set_ladder(trigger_ids=[1215], visible=True, enable=True, fade=14)
        self.set_ladder(trigger_ids=[1216], visible=True, enable=True, fade=15)
        self.set_ladder(trigger_ids=[1217], visible=True, enable=True, fade=16)
        self.set_ladder(trigger_ids=[1218], visible=True, enable=True, fade=17)
        self.set_ladder(trigger_ids=[1301], visible=True, enable=True, fade=1)
        self.set_ladder(trigger_ids=[1302], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1303], visible=True, enable=True, fade=3)
        self.set_ladder(trigger_ids=[1304], visible=True, enable=True, fade=4)
        self.set_ladder(trigger_ids=[1305], visible=True, enable=True, fade=5)
        self.set_ladder(trigger_ids=[1306], visible=True, enable=True, fade=6)
        self.set_ladder(trigger_ids=[1307], visible=True, enable=True, fade=7)
        self.set_ladder(trigger_ids=[1308], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1309], visible=True, enable=True, fade=8)
        self.set_ladder(trigger_ids=[1310], visible=True, enable=True, fade=9)
        self.set_ladder(trigger_ids=[1311], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[1312], visible=True, enable=True, fade=11)
        self.set_ladder(trigger_ids=[1313], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[1314], visible=True, enable=True, fade=13)
        self.set_ladder(trigger_ids=[1315], visible=True, enable=True, fade=14)
        self.set_ladder(trigger_ids=[1316], visible=True, enable=True, fade=15)
        self.set_ladder(trigger_ids=[1317], visible=True, enable=True, fade=16)
        self.set_ladder(trigger_ids=[1318], visible=True, enable=True, fade=17)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return step_03(self.ctx)


class step_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.spawn_monster(spawn_ids=[201,202,203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201,202,203]):
            return step_04(self.ctx)


class step_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.set_ladder(trigger_ids=[1401], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1402], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1403], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1404], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1405], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1406], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1407], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1408], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1409], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1410], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1411], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1412], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1413], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1414], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1415], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1416], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1417], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1418], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1501], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1502], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1503], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1504], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1505], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1506], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1507], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1508], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1509], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1510], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1511], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1512], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1513], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1514], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1515], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1516], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1517], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1518], visible=True, enable=True, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703]):
            return step_05(self.ctx)


class step_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.spawn_monster(spawn_ids=[301,302,303], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[301,302,303]):
            return step_06(self.ctx)


class step_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LadderGoBossRoom', value=1):
            return step_07(self.ctx)


class step_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1800,1801,1802,1803,1804,1805,1806,1807,1808,1809], visible=True) # 3층 피직
        self.set_ladder(trigger_ids=[1601], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1602], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1603], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1604], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1605], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1606], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1607], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1608], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1609], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1610], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1611], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1612], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1613], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1614], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1615], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1616], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1617], visible=True, enable=True, fade=2)
        self.set_ladder(trigger_ids=[1618], visible=True, enable=True, fade=2)


initial_state = roomCheck2
