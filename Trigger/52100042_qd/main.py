""" trigger/52100042_qd/main.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001], visible=False)
        set_mesh(triggerIds=[6002], visible=False)
        set_mesh(triggerIds=[6003], visible=False)
        set_mesh(triggerIds=[6004], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return roomCheck()


class roomCheck(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return levelcheck()
        if not is_dungeon_room():
            return quest_raid()


class levelcheck(state.State):
    def on_tick(self) -> state.State:
        if dungeon_level(level=2):
            return raid()
        if dungeon_level(level=3):
            return chaos_raid()


class raid(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ExitPortal', value=1):
            return end()


class chaos_raid(state.State):
    def on_enter(self):
        create_monster(spawnIds=[402], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ExitPortal', value=1):
            return end()


class quest_raid(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917], visible=True) # 1층 피직
        set_ladder(triggerIds=[1101], visible=True, animationEffect=True, animationDelay=1)
        set_ladder(triggerIds=[1102], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1103], visible=True, animationEffect=True, animationDelay=3)
        set_ladder(triggerIds=[1104], visible=True, animationEffect=True, animationDelay=4)
        set_ladder(triggerIds=[1105], visible=True, animationEffect=True, animationDelay=5)
        set_ladder(triggerIds=[1106], visible=True, animationEffect=True, animationDelay=6)
        set_ladder(triggerIds=[1107], visible=True, animationEffect=True, animationDelay=7)
        set_ladder(triggerIds=[1108], visible=True, animationEffect=True, animationDelay=8)
        set_ladder(triggerIds=[1109], visible=True, animationEffect=True, animationDelay=9)
        set_ladder(triggerIds=[1110], visible=True, animationEffect=True, animationDelay=10)
        set_ladder(triggerIds=[1111], visible=True, animationEffect=True, animationDelay=11)
        set_ladder(triggerIds=[1112], visible=True, animationEffect=True, animationDelay=12)
        set_ladder(triggerIds=[1113], visible=True, animationEffect=True, animationDelay=13)
        set_ladder(triggerIds=[1114], visible=True, animationEffect=True, animationDelay=14)
        set_ladder(triggerIds=[1115], visible=True, animationEffect=True, animationDelay=15)
        set_ladder(triggerIds=[1116], visible=True, animationEffect=True, animationDelay=16)
        set_ladder(triggerIds=[1117], visible=True, animationEffect=True, animationDelay=17)
        set_ladder(triggerIds=[1118], visible=True, animationEffect=True, animationDelay=18)
        set_ladder(triggerIds=[1201], visible=True, animationEffect=True, animationDelay=1)
        set_ladder(triggerIds=[1202], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1203], visible=True, animationEffect=True, animationDelay=3)
        set_ladder(triggerIds=[1204], visible=True, animationEffect=True, animationDelay=4)
        set_ladder(triggerIds=[1205], visible=True, animationEffect=True, animationDelay=5)
        set_ladder(triggerIds=[1206], visible=True, animationEffect=True, animationDelay=6)
        set_ladder(triggerIds=[1207], visible=True, animationEffect=True, animationDelay=7)
        set_ladder(triggerIds=[1208], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1209], visible=True, animationEffect=True, animationDelay=8)
        set_ladder(triggerIds=[1210], visible=True, animationEffect=True, animationDelay=9)
        set_ladder(triggerIds=[1211], visible=True, animationEffect=True, animationDelay=10)
        set_ladder(triggerIds=[1212], visible=True, animationEffect=True, animationDelay=11)
        set_ladder(triggerIds=[1213], visible=True, animationEffect=True, animationDelay=12)
        set_ladder(triggerIds=[1214], visible=True, animationEffect=True, animationDelay=13)
        set_ladder(triggerIds=[1215], visible=True, animationEffect=True, animationDelay=14)
        set_ladder(triggerIds=[1216], visible=True, animationEffect=True, animationDelay=15)
        set_ladder(triggerIds=[1217], visible=True, animationEffect=True, animationDelay=16)
        set_ladder(triggerIds=[1218], visible=True, animationEffect=True, animationDelay=17)
        set_ladder(triggerIds=[1301], visible=True, animationEffect=True, animationDelay=1)
        set_ladder(triggerIds=[1302], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1303], visible=True, animationEffect=True, animationDelay=3)
        set_ladder(triggerIds=[1304], visible=True, animationEffect=True, animationDelay=4)
        set_ladder(triggerIds=[1305], visible=True, animationEffect=True, animationDelay=5)
        set_ladder(triggerIds=[1306], visible=True, animationEffect=True, animationDelay=6)
        set_ladder(triggerIds=[1307], visible=True, animationEffect=True, animationDelay=7)
        set_ladder(triggerIds=[1308], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1309], visible=True, animationEffect=True, animationDelay=8)
        set_ladder(triggerIds=[1310], visible=True, animationEffect=True, animationDelay=9)
        set_ladder(triggerIds=[1311], visible=True, animationEffect=True, animationDelay=10)
        set_ladder(triggerIds=[1312], visible=True, animationEffect=True, animationDelay=11)
        set_ladder(triggerIds=[1313], visible=True, animationEffect=True, animationDelay=12)
        set_ladder(triggerIds=[1314], visible=True, animationEffect=True, animationDelay=13)
        set_ladder(triggerIds=[1315], visible=True, animationEffect=True, animationDelay=14)
        set_ladder(triggerIds=[1316], visible=True, animationEffect=True, animationDelay=15)
        set_ladder(triggerIds=[1317], visible=True, animationEffect=True, animationDelay=16)
        set_ladder(triggerIds=[1318], visible=True, animationEffect=True, animationDelay=17)
        set_ladder(triggerIds=[1401], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1402], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1403], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1404], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1405], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1406], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1407], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1408], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1409], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1410], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1411], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1412], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1413], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1414], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1415], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1416], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1417], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1418], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1501], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1502], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1503], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1504], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1505], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1506], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1507], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1508], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1509], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1510], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1511], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1512], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1513], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1514], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1515], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1516], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1517], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1518], visible=True, animationEffect=True, animationDelay=2)
        set_mesh(triggerIds=[1800,1801,1802,1803,1804,1805,1806,1807,1808,1809], visible=True) # 3층 피직
        set_ladder(triggerIds=[1601], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1602], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1603], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1604], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1605], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1606], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1607], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1608], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1609], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1610], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1611], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1612], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1613], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1614], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1615], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1616], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1617], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[1618], visible=True, animationEffect=True, animationDelay=2)
        create_monster(spawnIds=[501,502,503,504,505,506,507,508,509,511], arg2=False)
        create_monster(spawnIds=[403], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ExitPortal', value=1):
            return quest_end()
        if user_detected(boxIds=[720]):
            return npcSpawn()


class npcSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[510], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ExitPortal', value=1):
            return quest_end()


class end(state.State):
    def on_enter(self):
        dungeon_clear()
        set_achievement(triggerId=90000, type='trigger', achieve='Madracan03')
        set_achievement(triggerId=90000, type='trigger', achieve='Madracan_Q03')


class quest_end(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=510, script='$52100042_QD__MAIN__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=510, script='$52100042_QD__MAIN__1$', arg4=2, arg5=2)
        set_achievement(triggerId=90000, type='trigger', achieve='Madracan_Q03')
        # <action name="포탈을설정한다" arg1="4" arg2="1" arg3="1" arg4="1"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestEnd_warp()


class QuestEnd_warp(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestEnd_warp_End()

    def on_exit(self):
        move_user(mapId=52100043, portalId=0)


class QuestEnd_warp_End(state.State):
    pass


