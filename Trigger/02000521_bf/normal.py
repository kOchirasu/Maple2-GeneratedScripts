""" trigger/02000521_bf/normal.xml """
import trigger_api


class roomCheck2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.create_monster(spawnIds=[101,102,103,104,105], animationEffect=False)
        self.set_mesh(triggerIds=[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917], visible=False) # 1층 피직
        self.set_mesh(triggerIds=[1800,1801,1802,1803,1804,1805,1806,1807,1808,1809], visible=False) # 3층 피직
        # 1, 2, 3층 사다리 안보이기 처리
        self.set_ladder(triggerIds=[1101], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1102], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1103], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1104], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1105], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1106], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1107], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1108], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1109], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1110], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1111], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1112], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1113], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1114], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1115], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1116], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1117], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1118], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1201], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1202], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1203], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1204], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1205], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1206], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1207], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1208], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1209], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1210], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1211], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1212], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1213], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1214], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1215], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1216], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1217], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1218], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1301], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1302], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1303], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1304], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1305], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1306], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1307], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1308], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1309], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1310], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1311], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1312], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1313], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1314], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1315], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1316], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1317], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1318], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1401], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1402], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1403], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1404], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1405], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1406], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1407], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1408], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1409], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1410], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1411], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1412], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1413], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1414], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1415], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1416], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1417], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1418], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1501], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1502], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1503], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1504], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1505], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1506], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1507], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1508], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1509], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1510], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1511], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1512], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1513], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1514], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1515], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1516], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1517], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1518], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1601], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1602], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1603], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1604], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1605], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1606], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1607], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1608], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1609], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1610], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1611], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1612], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1613], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1614], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1615], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1616], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1617], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[1618], visible=False, animationEffect=False, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105]):
            return step_02(self.ctx)


class step_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917], visible=True) # 1층 피직
        # 1, 2, 3층 사다리 보이기 처리
        self.set_ladder(triggerIds=[1101], visible=True, animationEffect=True, animationDelay=1)
        self.set_ladder(triggerIds=[1102], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1103], visible=True, animationEffect=True, animationDelay=3)
        self.set_ladder(triggerIds=[1104], visible=True, animationEffect=True, animationDelay=4)
        self.set_ladder(triggerIds=[1105], visible=True, animationEffect=True, animationDelay=5)
        self.set_ladder(triggerIds=[1106], visible=True, animationEffect=True, animationDelay=6)
        self.set_ladder(triggerIds=[1107], visible=True, animationEffect=True, animationDelay=7)
        self.set_ladder(triggerIds=[1108], visible=True, animationEffect=True, animationDelay=8)
        self.set_ladder(triggerIds=[1109], visible=True, animationEffect=True, animationDelay=9)
        self.set_ladder(triggerIds=[1110], visible=True, animationEffect=True, animationDelay=10)
        self.set_ladder(triggerIds=[1111], visible=True, animationEffect=True, animationDelay=11)
        self.set_ladder(triggerIds=[1112], visible=True, animationEffect=True, animationDelay=12)
        self.set_ladder(triggerIds=[1113], visible=True, animationEffect=True, animationDelay=13)
        self.set_ladder(triggerIds=[1114], visible=True, animationEffect=True, animationDelay=14)
        self.set_ladder(triggerIds=[1115], visible=True, animationEffect=True, animationDelay=15)
        self.set_ladder(triggerIds=[1116], visible=True, animationEffect=True, animationDelay=16)
        self.set_ladder(triggerIds=[1117], visible=True, animationEffect=True, animationDelay=17)
        self.set_ladder(triggerIds=[1118], visible=True, animationEffect=True, animationDelay=18)
        self.set_ladder(triggerIds=[1201], visible=True, animationEffect=True, animationDelay=1)
        self.set_ladder(triggerIds=[1202], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1203], visible=True, animationEffect=True, animationDelay=3)
        self.set_ladder(triggerIds=[1204], visible=True, animationEffect=True, animationDelay=4)
        self.set_ladder(triggerIds=[1205], visible=True, animationEffect=True, animationDelay=5)
        self.set_ladder(triggerIds=[1206], visible=True, animationEffect=True, animationDelay=6)
        self.set_ladder(triggerIds=[1207], visible=True, animationEffect=True, animationDelay=7)
        self.set_ladder(triggerIds=[1208], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1209], visible=True, animationEffect=True, animationDelay=8)
        self.set_ladder(triggerIds=[1210], visible=True, animationEffect=True, animationDelay=9)
        self.set_ladder(triggerIds=[1211], visible=True, animationEffect=True, animationDelay=10)
        self.set_ladder(triggerIds=[1212], visible=True, animationEffect=True, animationDelay=11)
        self.set_ladder(triggerIds=[1213], visible=True, animationEffect=True, animationDelay=12)
        self.set_ladder(triggerIds=[1214], visible=True, animationEffect=True, animationDelay=13)
        self.set_ladder(triggerIds=[1215], visible=True, animationEffect=True, animationDelay=14)
        self.set_ladder(triggerIds=[1216], visible=True, animationEffect=True, animationDelay=15)
        self.set_ladder(triggerIds=[1217], visible=True, animationEffect=True, animationDelay=16)
        self.set_ladder(triggerIds=[1218], visible=True, animationEffect=True, animationDelay=17)
        self.set_ladder(triggerIds=[1301], visible=True, animationEffect=True, animationDelay=1)
        self.set_ladder(triggerIds=[1302], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1303], visible=True, animationEffect=True, animationDelay=3)
        self.set_ladder(triggerIds=[1304], visible=True, animationEffect=True, animationDelay=4)
        self.set_ladder(triggerIds=[1305], visible=True, animationEffect=True, animationDelay=5)
        self.set_ladder(triggerIds=[1306], visible=True, animationEffect=True, animationDelay=6)
        self.set_ladder(triggerIds=[1307], visible=True, animationEffect=True, animationDelay=7)
        self.set_ladder(triggerIds=[1308], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1309], visible=True, animationEffect=True, animationDelay=8)
        self.set_ladder(triggerIds=[1310], visible=True, animationEffect=True, animationDelay=9)
        self.set_ladder(triggerIds=[1311], visible=True, animationEffect=True, animationDelay=10)
        self.set_ladder(triggerIds=[1312], visible=True, animationEffect=True, animationDelay=11)
        self.set_ladder(triggerIds=[1313], visible=True, animationEffect=True, animationDelay=12)
        self.set_ladder(triggerIds=[1314], visible=True, animationEffect=True, animationDelay=13)
        self.set_ladder(triggerIds=[1315], visible=True, animationEffect=True, animationDelay=14)
        self.set_ladder(triggerIds=[1316], visible=True, animationEffect=True, animationDelay=15)
        self.set_ladder(triggerIds=[1317], visible=True, animationEffect=True, animationDelay=16)
        self.set_ladder(triggerIds=[1318], visible=True, animationEffect=True, animationDelay=17)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702]):
            return step_03(self.ctx)


class step_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.create_monster(spawnIds=[201,202,203], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203]):
            return step_04(self.ctx)


class step_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.set_ladder(triggerIds=[1401], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1402], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1403], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1404], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1405], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1406], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1407], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1408], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1409], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1410], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1411], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1412], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1413], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1414], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1415], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1416], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1417], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1418], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1501], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1502], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1503], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1504], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1505], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1506], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1507], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1508], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1509], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1510], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1511], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1512], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1513], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1514], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1515], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1516], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1517], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1518], visible=True, animationEffect=True, animationDelay=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703]):
            return step_05(self.ctx)


class step_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터 스폰
        self.create_monster(spawnIds=[301,302,303], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[301,302,303]):
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
        self.set_mesh(triggerIds=[1800,1801,1802,1803,1804,1805,1806,1807,1808,1809], visible=True) # 3층 피직
        self.set_ladder(triggerIds=[1601], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1602], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1603], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1604], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1605], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1606], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1607], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1608], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1609], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1610], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1611], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1612], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1613], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1614], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1615], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1616], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1617], visible=True, animationEffect=True, animationDelay=2)
        self.set_ladder(triggerIds=[1618], visible=True, animationEffect=True, animationDelay=2)


initial_state = roomCheck2
