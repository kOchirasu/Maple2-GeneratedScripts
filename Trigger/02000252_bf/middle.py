""" trigger/02000252_bf/middle.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8201], visible=False)
        set_effect(triggerIds=[8202], visible=False)
        set_effect(triggerIds=[8203], visible=False)
        set_effect(triggerIds=[8204], visible=False)
        set_effect(triggerIds=[8205], visible=False)
        set_effect(triggerIds=[8206], visible=False)
        set_effect(triggerIds=[8207], visible=False)
        set_effect(triggerIds=[8208], visible=False)
        set_effect(triggerIds=[8209], visible=False)
        set_effect(triggerIds=[8210], visible=False)
        set_effect(triggerIds=[8211], visible=False)
        set_effect(triggerIds=[8212], visible=False)
        set_effect(triggerIds=[8213], visible=False)
        set_effect(triggerIds=[8214], visible=False)
        set_effect(triggerIds=[8215], visible=False)
        set_effect(triggerIds=[8216], visible=False)
        set_effect(triggerIds=[8217], visible=False)
        set_effect(triggerIds=[8218], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=902, boxId=1):
            return 바닥삭제()


class 바닥삭제(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=5)
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142], visible=False, arg3=0, arg4=100)
        create_monster(spawnIds=[1075], arg2=False)
        create_monster(spawnIds=[1076], arg2=False)
        create_monster(spawnIds=[1077], arg2=False)
        create_monster(spawnIds=[1078], arg2=False)
        create_monster(spawnIds=[1079], arg2=False)
        create_monster(spawnIds=[1080], arg2=False)
        create_monster(spawnIds=[1081], arg2=False)
        create_monster(spawnIds=[1082], arg2=False)
        create_monster(spawnIds=[1083], arg2=False)
        create_monster(spawnIds=[1084], arg2=False)
        create_monster(spawnIds=[1085], arg2=False)
        create_monster(spawnIds=[1086], arg2=False)
        create_monster(spawnIds=[1087], arg2=False)
        create_monster(spawnIds=[1088], arg2=False)
        create_monster(spawnIds=[1089], arg2=False)
        create_monster(spawnIds=[1090], arg2=False)
        create_monster(spawnIds=[1091], arg2=False)
        create_monster(spawnIds=[1092], arg2=False)
        create_monster(spawnIds=[1093], arg2=False)
        create_monster(spawnIds=[1094], arg2=False)
        set_effect(triggerIds=[8201], visible=True)
        set_effect(triggerIds=[8202], visible=True)
        set_effect(triggerIds=[8203], visible=True)
        set_effect(triggerIds=[8204], visible=True)
        set_effect(triggerIds=[8205], visible=True)
        set_effect(triggerIds=[8206], visible=True)
        set_effect(triggerIds=[8207], visible=True)
        set_effect(triggerIds=[8208], visible=True)
        set_effect(triggerIds=[8209], visible=True)
        set_effect(triggerIds=[8210], visible=True)
        set_effect(triggerIds=[8211], visible=True)
        set_effect(triggerIds=[8212], visible=True)
        set_effect(triggerIds=[8213], visible=True)
        set_effect(triggerIds=[8214], visible=True)
        set_effect(triggerIds=[8215], visible=True)
        set_effect(triggerIds=[8216], visible=True)
        set_effect(triggerIds=[8217], visible=True)
        set_effect(triggerIds=[8218], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 스킬01()


class 스킬01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[8201], visible=False)
        set_effect(triggerIds=[8202], visible=False)
        set_effect(triggerIds=[8203], visible=False)
        set_effect(triggerIds=[8204], visible=False)
        set_effect(triggerIds=[8205], visible=False)
        set_effect(triggerIds=[8206], visible=False)
        set_effect(triggerIds=[8207], visible=False)
        set_effect(triggerIds=[8208], visible=False)
        set_effect(triggerIds=[8209], visible=False)
        set_effect(triggerIds=[8210], visible=False)
        set_effect(triggerIds=[8211], visible=False)
        set_effect(triggerIds=[8212], visible=False)
        set_effect(triggerIds=[8213], visible=False)
        set_effect(triggerIds=[8214], visible=False)
        set_effect(triggerIds=[8215], visible=False)
        set_effect(triggerIds=[8216], visible=False)
        set_effect(triggerIds=[8217], visible=False)
        set_effect(triggerIds=[8218], visible=False)
        set_skill(triggerIds=[1301], isEnable=True)
        set_skill(triggerIds=[1302], isEnable=True)
        set_skill(triggerIds=[1303], isEnable=True)
        set_skill(triggerIds=[1304], isEnable=True)
        set_skill(triggerIds=[1305], isEnable=True)
        set_skill(triggerIds=[1306], isEnable=True)
        set_skill(triggerIds=[1307], isEnable=True)
        set_skill(triggerIds=[1308], isEnable=True)
        set_skill(triggerIds=[1309], isEnable=True)
        set_skill(triggerIds=[1310], isEnable=True)
        set_skill(triggerIds=[1311], isEnable=True)
        set_skill(triggerIds=[1312], isEnable=True)
        set_skill(triggerIds=[1313], isEnable=True)
        set_skill(triggerIds=[1314], isEnable=True)
        set_skill(triggerIds=[1315], isEnable=True)
        set_skill(triggerIds=[1316], isEnable=True)
        set_skill(triggerIds=[1317], isEnable=True)
        set_skill(triggerIds=[1318], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬02대기()


class 스킬02대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1301], isEnable=False)
        set_skill(triggerIds=[1302], isEnable=False)
        set_skill(triggerIds=[1303], isEnable=False)
        set_skill(triggerIds=[1304], isEnable=False)
        set_skill(triggerIds=[1305], isEnable=False)
        set_skill(triggerIds=[1306], isEnable=False)
        set_skill(triggerIds=[1307], isEnable=False)
        set_skill(triggerIds=[1308], isEnable=False)
        set_skill(triggerIds=[1309], isEnable=False)
        set_skill(triggerIds=[1310], isEnable=False)
        set_skill(triggerIds=[1311], isEnable=False)
        set_skill(triggerIds=[1312], isEnable=False)
        set_skill(triggerIds=[1313], isEnable=False)
        set_skill(triggerIds=[1314], isEnable=False)
        set_skill(triggerIds=[1315], isEnable=False)
        set_skill(triggerIds=[1316], isEnable=False)
        set_skill(triggerIds=[1317], isEnable=False)
        set_skill(triggerIds=[1318], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬02()


class 스킬02(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1307], isEnable=True)
        set_skill(triggerIds=[1308], isEnable=True)
        set_skill(triggerIds=[1309], isEnable=True)
        set_skill(triggerIds=[1310], isEnable=True)
        set_skill(triggerIds=[1311], isEnable=True)
        set_skill(triggerIds=[1312], isEnable=True)
        set_skill(triggerIds=[1313], isEnable=True)
        set_skill(triggerIds=[1314], isEnable=True)
        set_skill(triggerIds=[1315], isEnable=True)
        set_skill(triggerIds=[1316], isEnable=True)
        set_skill(triggerIds=[1317], isEnable=True)
        set_skill(triggerIds=[1318], isEnable=True)
        set_skill(triggerIds=[1319], isEnable=True)
        set_skill(triggerIds=[1320], isEnable=True)
        set_skill(triggerIds=[1321], isEnable=True)
        set_skill(triggerIds=[1322], isEnable=True)
        set_skill(triggerIds=[1323], isEnable=True)
        set_skill(triggerIds=[1324], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬03대기()


class 스킬03대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1307], isEnable=False)
        set_skill(triggerIds=[1308], isEnable=False)
        set_skill(triggerIds=[1309], isEnable=False)
        set_skill(triggerIds=[1310], isEnable=False)
        set_skill(triggerIds=[1311], isEnable=False)
        set_skill(triggerIds=[1312], isEnable=False)
        set_skill(triggerIds=[1313], isEnable=False)
        set_skill(triggerIds=[1314], isEnable=False)
        set_skill(triggerIds=[1315], isEnable=False)
        set_skill(triggerIds=[1316], isEnable=False)
        set_skill(triggerIds=[1317], isEnable=False)
        set_skill(triggerIds=[1318], isEnable=False)
        set_skill(triggerIds=[1319], isEnable=False)
        set_skill(triggerIds=[1320], isEnable=False)
        set_skill(triggerIds=[1321], isEnable=False)
        set_skill(triggerIds=[1322], isEnable=False)
        set_skill(triggerIds=[1323], isEnable=False)
        set_skill(triggerIds=[1324], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬03()


class 스킬03(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1313], isEnable=True)
        set_skill(triggerIds=[1314], isEnable=True)
        set_skill(triggerIds=[1315], isEnable=True)
        set_skill(triggerIds=[1316], isEnable=True)
        set_skill(triggerIds=[1317], isEnable=True)
        set_skill(triggerIds=[1318], isEnable=True)
        set_skill(triggerIds=[1319], isEnable=True)
        set_skill(triggerIds=[1320], isEnable=True)
        set_skill(triggerIds=[1321], isEnable=True)
        set_skill(triggerIds=[1322], isEnable=True)
        set_skill(triggerIds=[1323], isEnable=True)
        set_skill(triggerIds=[1324], isEnable=True)
        set_skill(triggerIds=[1325], isEnable=True)
        set_skill(triggerIds=[1326], isEnable=True)
        set_skill(triggerIds=[1327], isEnable=True)
        set_skill(triggerIds=[1328], isEnable=True)
        set_skill(triggerIds=[1328], isEnable=True)
        set_skill(triggerIds=[1330], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬04대기()


class 스킬04대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1313], isEnable=False)
        set_skill(triggerIds=[1314], isEnable=False)
        set_skill(triggerIds=[1315], isEnable=False)
        set_skill(triggerIds=[1316], isEnable=False)
        set_skill(triggerIds=[1317], isEnable=False)
        set_skill(triggerIds=[1318], isEnable=False)
        set_skill(triggerIds=[1319], isEnable=False)
        set_skill(triggerIds=[1320], isEnable=False)
        set_skill(triggerIds=[1321], isEnable=False)
        set_skill(triggerIds=[1322], isEnable=False)
        set_skill(triggerIds=[1323], isEnable=False)
        set_skill(triggerIds=[1324], isEnable=False)
        set_skill(triggerIds=[1325], isEnable=False)
        set_skill(triggerIds=[1326], isEnable=False)
        set_skill(triggerIds=[1327], isEnable=False)
        set_skill(triggerIds=[1328], isEnable=False)
        set_skill(triggerIds=[1328], isEnable=False)
        set_skill(triggerIds=[1330], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬04()


class 스킬04(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1319], isEnable=True)
        set_skill(triggerIds=[1320], isEnable=True)
        set_skill(triggerIds=[1321], isEnable=True)
        set_skill(triggerIds=[1322], isEnable=True)
        set_skill(triggerIds=[1323], isEnable=True)
        set_skill(triggerIds=[1324], isEnable=True)
        set_skill(triggerIds=[1325], isEnable=True)
        set_skill(triggerIds=[1326], isEnable=True)
        set_skill(triggerIds=[1327], isEnable=True)
        set_skill(triggerIds=[1328], isEnable=True)
        set_skill(triggerIds=[1328], isEnable=True)
        set_skill(triggerIds=[1330], isEnable=True)
        set_skill(triggerIds=[1331], isEnable=True)
        set_skill(triggerIds=[1332], isEnable=True)
        set_skill(triggerIds=[1333], isEnable=True)
        set_skill(triggerIds=[1334], isEnable=True)
        set_skill(triggerIds=[1335], isEnable=True)
        set_skill(triggerIds=[1336], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬05대기()


class 스킬05대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1319], isEnable=False)
        set_skill(triggerIds=[1320], isEnable=False)
        set_skill(triggerIds=[1321], isEnable=False)
        set_skill(triggerIds=[1322], isEnable=False)
        set_skill(triggerIds=[1323], isEnable=False)
        set_skill(triggerIds=[1324], isEnable=False)
        set_skill(triggerIds=[1325], isEnable=False)
        set_skill(triggerIds=[1326], isEnable=False)
        set_skill(triggerIds=[1327], isEnable=False)
        set_skill(triggerIds=[1328], isEnable=False)
        set_skill(triggerIds=[1328], isEnable=False)
        set_skill(triggerIds=[1330], isEnable=False)
        set_skill(triggerIds=[1331], isEnable=False)
        set_skill(triggerIds=[1332], isEnable=False)
        set_skill(triggerIds=[1333], isEnable=False)
        set_skill(triggerIds=[1334], isEnable=False)
        set_skill(triggerIds=[1335], isEnable=False)
        set_skill(triggerIds=[1336], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬05()


class 스킬05(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1325], isEnable=True)
        set_skill(triggerIds=[1326], isEnable=True)
        set_skill(triggerIds=[1327], isEnable=True)
        set_skill(triggerIds=[1328], isEnable=True)
        set_skill(triggerIds=[1328], isEnable=True)
        set_skill(triggerIds=[1330], isEnable=True)
        set_skill(triggerIds=[1331], isEnable=True)
        set_skill(triggerIds=[1332], isEnable=True)
        set_skill(triggerIds=[1333], isEnable=True)
        set_skill(triggerIds=[1334], isEnable=True)
        set_skill(triggerIds=[1335], isEnable=True)
        set_skill(triggerIds=[1336], isEnable=True)
        set_skill(triggerIds=[1337], isEnable=True)
        set_skill(triggerIds=[1338], isEnable=True)
        set_skill(triggerIds=[1339], isEnable=True)
        set_skill(triggerIds=[1340], isEnable=True)
        set_skill(triggerIds=[1341], isEnable=True)
        set_skill(triggerIds=[1342], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬06대기()


class 스킬06대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1325], isEnable=False)
        set_skill(triggerIds=[1326], isEnable=False)
        set_skill(triggerIds=[1327], isEnable=False)
        set_skill(triggerIds=[1328], isEnable=False)
        set_skill(triggerIds=[1328], isEnable=False)
        set_skill(triggerIds=[1330], isEnable=False)
        set_skill(triggerIds=[1331], isEnable=False)
        set_skill(triggerIds=[1332], isEnable=False)
        set_skill(triggerIds=[1333], isEnable=False)
        set_skill(triggerIds=[1334], isEnable=False)
        set_skill(triggerIds=[1335], isEnable=False)
        set_skill(triggerIds=[1336], isEnable=False)
        set_skill(triggerIds=[1337], isEnable=False)
        set_skill(triggerIds=[1338], isEnable=False)
        set_skill(triggerIds=[1339], isEnable=False)
        set_skill(triggerIds=[1340], isEnable=False)
        set_skill(triggerIds=[1341], isEnable=False)
        set_skill(triggerIds=[1342], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬06()


class 스킬06(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1331], isEnable=True)
        set_skill(triggerIds=[1332], isEnable=True)
        set_skill(triggerIds=[1333], isEnable=True)
        set_skill(triggerIds=[1334], isEnable=True)
        set_skill(triggerIds=[1335], isEnable=True)
        set_skill(triggerIds=[1336], isEnable=True)
        set_skill(triggerIds=[1337], isEnable=True)
        set_skill(triggerIds=[1338], isEnable=True)
        set_skill(triggerIds=[1339], isEnable=True)
        set_skill(triggerIds=[1340], isEnable=True)
        set_skill(triggerIds=[1341], isEnable=True)
        set_skill(triggerIds=[1342], isEnable=True)
        set_skill(triggerIds=[1343], isEnable=True)
        set_skill(triggerIds=[1344], isEnable=True)
        set_skill(triggerIds=[1345], isEnable=True)
        set_skill(triggerIds=[1346], isEnable=True)
        set_skill(triggerIds=[1347], isEnable=True)
        set_skill(triggerIds=[1348], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬07대기()


class 스킬07대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1331], isEnable=False)
        set_skill(triggerIds=[1332], isEnable=False)
        set_skill(triggerIds=[1333], isEnable=False)
        set_skill(triggerIds=[1334], isEnable=False)
        set_skill(triggerIds=[1335], isEnable=False)
        set_skill(triggerIds=[1336], isEnable=False)
        set_skill(triggerIds=[1337], isEnable=False)
        set_skill(triggerIds=[1338], isEnable=False)
        set_skill(triggerIds=[1339], isEnable=False)
        set_skill(triggerIds=[1340], isEnable=False)
        set_skill(triggerIds=[1341], isEnable=False)
        set_skill(triggerIds=[1342], isEnable=False)
        set_skill(triggerIds=[1343], isEnable=False)
        set_skill(triggerIds=[1344], isEnable=False)
        set_skill(triggerIds=[1345], isEnable=False)
        set_skill(triggerIds=[1346], isEnable=False)
        set_skill(triggerIds=[1347], isEnable=False)
        set_skill(triggerIds=[1348], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬07()


class 스킬07(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1337], isEnable=True)
        set_skill(triggerIds=[1338], isEnable=True)
        set_skill(triggerIds=[1339], isEnable=True)
        set_skill(triggerIds=[1340], isEnable=True)
        set_skill(triggerIds=[1341], isEnable=True)
        set_skill(triggerIds=[1342], isEnable=True)
        set_skill(triggerIds=[1343], isEnable=True)
        set_skill(triggerIds=[1344], isEnable=True)
        set_skill(triggerIds=[1345], isEnable=True)
        set_skill(triggerIds=[1346], isEnable=True)
        set_skill(triggerIds=[1347], isEnable=True)
        set_skill(triggerIds=[1348], isEnable=True)
        set_skill(triggerIds=[1349], isEnable=True)
        set_skill(triggerIds=[1350], isEnable=True)
        set_skill(triggerIds=[1351], isEnable=True)
        set_skill(triggerIds=[1352], isEnable=True)
        set_skill(triggerIds=[1353], isEnable=True)
        set_skill(triggerIds=[1354], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬08대기()


class 스킬08대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1337], isEnable=False)
        set_skill(triggerIds=[1338], isEnable=False)
        set_skill(triggerIds=[1339], isEnable=False)
        set_skill(triggerIds=[1340], isEnable=False)
        set_skill(triggerIds=[1341], isEnable=False)
        set_skill(triggerIds=[1342], isEnable=False)
        set_skill(triggerIds=[1343], isEnable=False)
        set_skill(triggerIds=[1344], isEnable=False)
        set_skill(triggerIds=[1345], isEnable=False)
        set_skill(triggerIds=[1346], isEnable=False)
        set_skill(triggerIds=[1347], isEnable=False)
        set_skill(triggerIds=[1348], isEnable=False)
        set_skill(triggerIds=[1349], isEnable=False)
        set_skill(triggerIds=[1350], isEnable=False)
        set_skill(triggerIds=[1351], isEnable=False)
        set_skill(triggerIds=[1352], isEnable=False)
        set_skill(triggerIds=[1353], isEnable=False)
        set_skill(triggerIds=[1354], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬08()


class 스킬08(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1343], isEnable=True)
        set_skill(triggerIds=[1344], isEnable=True)
        set_skill(triggerIds=[1345], isEnable=True)
        set_skill(triggerIds=[1346], isEnable=True)
        set_skill(triggerIds=[1347], isEnable=True)
        set_skill(triggerIds=[1348], isEnable=True)
        set_skill(triggerIds=[1349], isEnable=True)
        set_skill(triggerIds=[1350], isEnable=True)
        set_skill(triggerIds=[1351], isEnable=True)
        set_skill(triggerIds=[1352], isEnable=True)
        set_skill(triggerIds=[1353], isEnable=True)
        set_skill(triggerIds=[1354], isEnable=True)
        set_skill(triggerIds=[1355], isEnable=True)
        set_skill(triggerIds=[1356], isEnable=True)
        set_skill(triggerIds=[1357], isEnable=True)
        set_skill(triggerIds=[1358], isEnable=True)
        set_skill(triggerIds=[1359], isEnable=True)
        set_skill(triggerIds=[1360], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬09대기()


class 스킬09대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1343], isEnable=False)
        set_skill(triggerIds=[1344], isEnable=False)
        set_skill(triggerIds=[1345], isEnable=False)
        set_skill(triggerIds=[1346], isEnable=False)
        set_skill(triggerIds=[1347], isEnable=False)
        set_skill(triggerIds=[1348], isEnable=False)
        set_skill(triggerIds=[1349], isEnable=False)
        set_skill(triggerIds=[1350], isEnable=False)
        set_skill(triggerIds=[1351], isEnable=False)
        set_skill(triggerIds=[1352], isEnable=False)
        set_skill(triggerIds=[1353], isEnable=False)
        set_skill(triggerIds=[1354], isEnable=False)
        set_skill(triggerIds=[1355], isEnable=False)
        set_skill(triggerIds=[1356], isEnable=False)
        set_skill(triggerIds=[1357], isEnable=False)
        set_skill(triggerIds=[1358], isEnable=False)
        set_skill(triggerIds=[1359], isEnable=False)
        set_skill(triggerIds=[1360], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬09()


class 스킬09(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1349], isEnable=True)
        set_skill(triggerIds=[1350], isEnable=True)
        set_skill(triggerIds=[1351], isEnable=True)
        set_skill(triggerIds=[1352], isEnable=True)
        set_skill(triggerIds=[1353], isEnable=True)
        set_skill(triggerIds=[1354], isEnable=True)
        set_skill(triggerIds=[1355], isEnable=True)
        set_skill(triggerIds=[1356], isEnable=True)
        set_skill(triggerIds=[1357], isEnable=True)
        set_skill(triggerIds=[1358], isEnable=True)
        set_skill(triggerIds=[1359], isEnable=True)
        set_skill(triggerIds=[1360], isEnable=True)
        set_skill(triggerIds=[1361], isEnable=True)
        set_skill(triggerIds=[1362], isEnable=True)
        set_skill(triggerIds=[1363], isEnable=True)
        set_skill(triggerIds=[1364], isEnable=True)
        set_skill(triggerIds=[1365], isEnable=True)
        set_skill(triggerIds=[1366], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬10대기()


class 스킬10대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1349], isEnable=False)
        set_skill(triggerIds=[1350], isEnable=False)
        set_skill(triggerIds=[1351], isEnable=False)
        set_skill(triggerIds=[1352], isEnable=False)
        set_skill(triggerIds=[1353], isEnable=False)
        set_skill(triggerIds=[1354], isEnable=False)
        set_skill(triggerIds=[1355], isEnable=False)
        set_skill(triggerIds=[1356], isEnable=False)
        set_skill(triggerIds=[1357], isEnable=False)
        set_skill(triggerIds=[1358], isEnable=False)
        set_skill(triggerIds=[1359], isEnable=False)
        set_skill(triggerIds=[1360], isEnable=False)
        set_skill(triggerIds=[1361], isEnable=False)
        set_skill(triggerIds=[1362], isEnable=False)
        set_skill(triggerIds=[1363], isEnable=False)
        set_skill(triggerIds=[1364], isEnable=False)
        set_skill(triggerIds=[1365], isEnable=False)
        set_skill(triggerIds=[1366], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬10()


class 스킬10(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1355], isEnable=True)
        set_skill(triggerIds=[1356], isEnable=True)
        set_skill(triggerIds=[1357], isEnable=True)
        set_skill(triggerIds=[1358], isEnable=True)
        set_skill(triggerIds=[1359], isEnable=True)
        set_skill(triggerIds=[1360], isEnable=True)
        set_skill(triggerIds=[1361], isEnable=True)
        set_skill(triggerIds=[1362], isEnable=True)
        set_skill(triggerIds=[1363], isEnable=True)
        set_skill(triggerIds=[1364], isEnable=True)
        set_skill(triggerIds=[1365], isEnable=True)
        set_skill(triggerIds=[1366], isEnable=True)
        set_skill(triggerIds=[1367], isEnable=True)
        set_skill(triggerIds=[1368], isEnable=True)
        set_skill(triggerIds=[1369], isEnable=True)
        set_skill(triggerIds=[1370], isEnable=True)
        set_skill(triggerIds=[1371], isEnable=True)
        set_skill(triggerIds=[1372], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬11대기()


class 스킬11대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1355], isEnable=False)
        set_skill(triggerIds=[1356], isEnable=False)
        set_skill(triggerIds=[1357], isEnable=False)
        set_skill(triggerIds=[1358], isEnable=False)
        set_skill(triggerIds=[1359], isEnable=False)
        set_skill(triggerIds=[1360], isEnable=False)
        set_skill(triggerIds=[1361], isEnable=False)
        set_skill(triggerIds=[1362], isEnable=False)
        set_skill(triggerIds=[1363], isEnable=False)
        set_skill(triggerIds=[1364], isEnable=False)
        set_skill(triggerIds=[1365], isEnable=False)
        set_skill(triggerIds=[1366], isEnable=False)
        set_skill(triggerIds=[1367], isEnable=False)
        set_skill(triggerIds=[1368], isEnable=False)
        set_skill(triggerIds=[1369], isEnable=False)
        set_skill(triggerIds=[1370], isEnable=False)
        set_skill(triggerIds=[1371], isEnable=False)
        set_skill(triggerIds=[1372], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬11()


class 스킬11(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1361], isEnable=True)
        set_skill(triggerIds=[1362], isEnable=True)
        set_skill(triggerIds=[1363], isEnable=True)
        set_skill(triggerIds=[1364], isEnable=True)
        set_skill(triggerIds=[1365], isEnable=True)
        set_skill(triggerIds=[1366], isEnable=True)
        set_skill(triggerIds=[1367], isEnable=True)
        set_skill(triggerIds=[1368], isEnable=True)
        set_skill(triggerIds=[1369], isEnable=True)
        set_skill(triggerIds=[1370], isEnable=True)
        set_skill(triggerIds=[1371], isEnable=True)
        set_skill(triggerIds=[1372], isEnable=True)
        set_skill(triggerIds=[1373], isEnable=True)
        set_skill(triggerIds=[1374], isEnable=True)
        set_skill(triggerIds=[1375], isEnable=True)
        set_skill(triggerIds=[1376], isEnable=True)
        set_skill(triggerIds=[1377], isEnable=True)
        set_skill(triggerIds=[1378], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬12대기()


class 스킬12대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1361], isEnable=False)
        set_skill(triggerIds=[1362], isEnable=False)
        set_skill(triggerIds=[1363], isEnable=False)
        set_skill(triggerIds=[1364], isEnable=False)
        set_skill(triggerIds=[1365], isEnable=False)
        set_skill(triggerIds=[1366], isEnable=False)
        set_skill(triggerIds=[1367], isEnable=False)
        set_skill(triggerIds=[1368], isEnable=False)
        set_skill(triggerIds=[1369], isEnable=False)
        set_skill(triggerIds=[1370], isEnable=False)
        set_skill(triggerIds=[1371], isEnable=False)
        set_skill(triggerIds=[1372], isEnable=False)
        set_skill(triggerIds=[1373], isEnable=False)
        set_skill(triggerIds=[1374], isEnable=False)
        set_skill(triggerIds=[1375], isEnable=False)
        set_skill(triggerIds=[1376], isEnable=False)
        set_skill(triggerIds=[1377], isEnable=False)
        set_skill(triggerIds=[1378], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬12()


class 스킬12(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1367], isEnable=True)
        set_skill(triggerIds=[1368], isEnable=True)
        set_skill(triggerIds=[1369], isEnable=True)
        set_skill(triggerIds=[1370], isEnable=True)
        set_skill(triggerIds=[1371], isEnable=True)
        set_skill(triggerIds=[1372], isEnable=True)
        set_skill(triggerIds=[1373], isEnable=True)
        set_skill(triggerIds=[1374], isEnable=True)
        set_skill(triggerIds=[1375], isEnable=True)
        set_skill(triggerIds=[1376], isEnable=True)
        set_skill(triggerIds=[1377], isEnable=True)
        set_skill(triggerIds=[1378], isEnable=True)
        set_skill(triggerIds=[1379], isEnable=True)
        set_skill(triggerIds=[1380], isEnable=True)
        set_skill(triggerIds=[1381], isEnable=True)
        set_skill(triggerIds=[1382], isEnable=True)
        set_skill(triggerIds=[1383], isEnable=True)
        set_skill(triggerIds=[1384], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬13대기()


class 스킬13대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1367], isEnable=False)
        set_skill(triggerIds=[1368], isEnable=False)
        set_skill(triggerIds=[1369], isEnable=False)
        set_skill(triggerIds=[1370], isEnable=False)
        set_skill(triggerIds=[1371], isEnable=False)
        set_skill(triggerIds=[1372], isEnable=False)
        set_skill(triggerIds=[1373], isEnable=False)
        set_skill(triggerIds=[1374], isEnable=False)
        set_skill(triggerIds=[1375], isEnable=False)
        set_skill(triggerIds=[1376], isEnable=False)
        set_skill(triggerIds=[1377], isEnable=False)
        set_skill(triggerIds=[1378], isEnable=False)
        set_skill(triggerIds=[1379], isEnable=False)
        set_skill(triggerIds=[1380], isEnable=False)
        set_skill(triggerIds=[1381], isEnable=False)
        set_skill(triggerIds=[1382], isEnable=False)
        set_skill(triggerIds=[1383], isEnable=False)
        set_skill(triggerIds=[1384], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬13()


class 스킬13(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1373], isEnable=True)
        set_skill(triggerIds=[1374], isEnable=True)
        set_skill(triggerIds=[1375], isEnable=True)
        set_skill(triggerIds=[1376], isEnable=True)
        set_skill(triggerIds=[1377], isEnable=True)
        set_skill(triggerIds=[1378], isEnable=True)
        set_skill(triggerIds=[1379], isEnable=True)
        set_skill(triggerIds=[1380], isEnable=True)
        set_skill(triggerIds=[1381], isEnable=True)
        set_skill(triggerIds=[1382], isEnable=True)
        set_skill(triggerIds=[1383], isEnable=True)
        set_skill(triggerIds=[1384], isEnable=True)
        set_skill(triggerIds=[1385], isEnable=True)
        set_skill(triggerIds=[1386], isEnable=True)
        set_skill(triggerIds=[1387], isEnable=True)
        set_skill(triggerIds=[1388], isEnable=True)
        set_skill(triggerIds=[1389], isEnable=True)
        set_skill(triggerIds=[1390], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬14대기()


class 스킬14대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1373], isEnable=False)
        set_skill(triggerIds=[1374], isEnable=False)
        set_skill(triggerIds=[1375], isEnable=False)
        set_skill(triggerIds=[1376], isEnable=False)
        set_skill(triggerIds=[1377], isEnable=False)
        set_skill(triggerIds=[1378], isEnable=False)
        set_skill(triggerIds=[1379], isEnable=False)
        set_skill(triggerIds=[1380], isEnable=False)
        set_skill(triggerIds=[1381], isEnable=False)
        set_skill(triggerIds=[1382], isEnable=False)
        set_skill(triggerIds=[1383], isEnable=False)
        set_skill(triggerIds=[1384], isEnable=False)
        set_skill(triggerIds=[1385], isEnable=False)
        set_skill(triggerIds=[1386], isEnable=False)
        set_skill(triggerIds=[1387], isEnable=False)
        set_skill(triggerIds=[1388], isEnable=False)
        set_skill(triggerIds=[1389], isEnable=False)
        set_skill(triggerIds=[1390], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬14()


class 스킬14(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1379], isEnable=True)
        set_skill(triggerIds=[1380], isEnable=True)
        set_skill(triggerIds=[1381], isEnable=True)
        set_skill(triggerIds=[1382], isEnable=True)
        set_skill(triggerIds=[1383], isEnable=True)
        set_skill(triggerIds=[1384], isEnable=True)
        set_skill(triggerIds=[1385], isEnable=True)
        set_skill(triggerIds=[1386], isEnable=True)
        set_skill(triggerIds=[1387], isEnable=True)
        set_skill(triggerIds=[1388], isEnable=True)
        set_skill(triggerIds=[1389], isEnable=True)
        set_skill(triggerIds=[1390], isEnable=True)
        set_skill(triggerIds=[1391], isEnable=True)
        set_skill(triggerIds=[1392], isEnable=True)
        set_skill(triggerIds=[1393], isEnable=True)
        set_skill(triggerIds=[1394], isEnable=True)
        set_skill(triggerIds=[1395], isEnable=True)
        set_skill(triggerIds=[1396], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬15대기()


class 스킬15대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1379], isEnable=False)
        set_skill(triggerIds=[1380], isEnable=False)
        set_skill(triggerIds=[1381], isEnable=False)
        set_skill(triggerIds=[1382], isEnable=False)
        set_skill(triggerIds=[1383], isEnable=False)
        set_skill(triggerIds=[1384], isEnable=False)
        set_skill(triggerIds=[1385], isEnable=False)
        set_skill(triggerIds=[1386], isEnable=False)
        set_skill(triggerIds=[1387], isEnable=False)
        set_skill(triggerIds=[1388], isEnable=False)
        set_skill(triggerIds=[1389], isEnable=False)
        set_skill(triggerIds=[1390], isEnable=False)
        set_skill(triggerIds=[1391], isEnable=False)
        set_skill(triggerIds=[1392], isEnable=False)
        set_skill(triggerIds=[1393], isEnable=False)
        set_skill(triggerIds=[1394], isEnable=False)
        set_skill(triggerIds=[1395], isEnable=False)
        set_skill(triggerIds=[1396], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬15()


class 스킬15(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1385], isEnable=True)
        set_skill(triggerIds=[1386], isEnable=True)
        set_skill(triggerIds=[1387], isEnable=True)
        set_skill(triggerIds=[1388], isEnable=True)
        set_skill(triggerIds=[1389], isEnable=True)
        set_skill(triggerIds=[1390], isEnable=True)
        set_skill(triggerIds=[1391], isEnable=True)
        set_skill(triggerIds=[1392], isEnable=True)
        set_skill(triggerIds=[1393], isEnable=True)
        set_skill(triggerIds=[1394], isEnable=True)
        set_skill(triggerIds=[1395], isEnable=True)
        set_skill(triggerIds=[1396], isEnable=True)
        set_skill(triggerIds=[1397], isEnable=True)
        set_skill(triggerIds=[1398], isEnable=True)
        set_skill(triggerIds=[1399], isEnable=True)
        set_skill(triggerIds=[1400], isEnable=True)
        set_skill(triggerIds=[1401], isEnable=True)
        set_skill(triggerIds=[1402], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬16대기()


class 스킬16대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1385], isEnable=False)
        set_skill(triggerIds=[1386], isEnable=False)
        set_skill(triggerIds=[1387], isEnable=False)
        set_skill(triggerIds=[1388], isEnable=False)
        set_skill(triggerIds=[1389], isEnable=False)
        set_skill(triggerIds=[1390], isEnable=False)
        set_skill(triggerIds=[1391], isEnable=False)
        set_skill(triggerIds=[1392], isEnable=False)
        set_skill(triggerIds=[1393], isEnable=False)
        set_skill(triggerIds=[1394], isEnable=False)
        set_skill(triggerIds=[1395], isEnable=False)
        set_skill(triggerIds=[1396], isEnable=False)
        set_skill(triggerIds=[1397], isEnable=False)
        set_skill(triggerIds=[1398], isEnable=False)
        set_skill(triggerIds=[1399], isEnable=False)
        set_skill(triggerIds=[1400], isEnable=False)
        set_skill(triggerIds=[1401], isEnable=False)
        set_skill(triggerIds=[1402], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬16()


class 스킬16(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1391], isEnable=True)
        set_skill(triggerIds=[1392], isEnable=True)
        set_skill(triggerIds=[1393], isEnable=True)
        set_skill(triggerIds=[1394], isEnable=True)
        set_skill(triggerIds=[1395], isEnable=True)
        set_skill(triggerIds=[1396], isEnable=True)
        set_skill(triggerIds=[1397], isEnable=True)
        set_skill(triggerIds=[1398], isEnable=True)
        set_skill(triggerIds=[1399], isEnable=True)
        set_skill(triggerIds=[1400], isEnable=True)
        set_skill(triggerIds=[1401], isEnable=True)
        set_skill(triggerIds=[1402], isEnable=True)
        set_skill(triggerIds=[1403], isEnable=True)
        set_skill(triggerIds=[1404], isEnable=True)
        set_skill(triggerIds=[1405], isEnable=True)
        set_skill(triggerIds=[1406], isEnable=True)
        set_skill(triggerIds=[1407], isEnable=True)
        set_skill(triggerIds=[1408], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬17대기()


class 스킬17대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1391], isEnable=False)
        set_skill(triggerIds=[1392], isEnable=False)
        set_skill(triggerIds=[1393], isEnable=False)
        set_skill(triggerIds=[1394], isEnable=False)
        set_skill(triggerIds=[1395], isEnable=False)
        set_skill(triggerIds=[1396], isEnable=False)
        set_skill(triggerIds=[1397], isEnable=False)
        set_skill(triggerIds=[1398], isEnable=False)
        set_skill(triggerIds=[1399], isEnable=False)
        set_skill(triggerIds=[1400], isEnable=False)
        set_skill(triggerIds=[1401], isEnable=False)
        set_skill(triggerIds=[1402], isEnable=False)
        set_skill(triggerIds=[1403], isEnable=False)
        set_skill(triggerIds=[1404], isEnable=False)
        set_skill(triggerIds=[1405], isEnable=False)
        set_skill(triggerIds=[1406], isEnable=False)
        set_skill(triggerIds=[1407], isEnable=False)
        set_skill(triggerIds=[1408], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬17()


class 스킬17(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1391], isEnable=True)
        set_skill(triggerIds=[1392], isEnable=True)
        set_skill(triggerIds=[1393], isEnable=True)
        set_skill(triggerIds=[1394], isEnable=True)
        set_skill(triggerIds=[1395], isEnable=True)
        set_skill(triggerIds=[1396], isEnable=True)
        set_skill(triggerIds=[1397], isEnable=True)
        set_skill(triggerIds=[1398], isEnable=True)
        set_skill(triggerIds=[1399], isEnable=True)
        set_skill(triggerIds=[1400], isEnable=True)
        set_skill(triggerIds=[1401], isEnable=True)
        set_skill(triggerIds=[1402], isEnable=True)
        set_skill(triggerIds=[1403], isEnable=True)
        set_skill(triggerIds=[1404], isEnable=True)
        set_skill(triggerIds=[1405], isEnable=True)
        set_skill(triggerIds=[1406], isEnable=True)
        set_skill(triggerIds=[1407], isEnable=True)
        set_skill(triggerIds=[1408], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬18대기()


class 스킬18대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1391], isEnable=False)
        set_skill(triggerIds=[1392], isEnable=False)
        set_skill(triggerIds=[1393], isEnable=False)
        set_skill(triggerIds=[1394], isEnable=False)
        set_skill(triggerIds=[1395], isEnable=False)
        set_skill(triggerIds=[1396], isEnable=False)
        set_skill(triggerIds=[1397], isEnable=False)
        set_skill(triggerIds=[1398], isEnable=False)
        set_skill(triggerIds=[1399], isEnable=False)
        set_skill(triggerIds=[1400], isEnable=False)
        set_skill(triggerIds=[1401], isEnable=False)
        set_skill(triggerIds=[1402], isEnable=False)
        set_skill(triggerIds=[1403], isEnable=False)
        set_skill(triggerIds=[1404], isEnable=False)
        set_skill(triggerIds=[1405], isEnable=False)
        set_skill(triggerIds=[1406], isEnable=False)
        set_skill(triggerIds=[1407], isEnable=False)
        set_skill(triggerIds=[1408], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬18()


class 스킬18(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1397], isEnable=True)
        set_skill(triggerIds=[1398], isEnable=True)
        set_skill(triggerIds=[1399], isEnable=True)
        set_skill(triggerIds=[1400], isEnable=True)
        set_skill(triggerIds=[1401], isEnable=True)
        set_skill(triggerIds=[1402], isEnable=True)
        set_skill(triggerIds=[1403], isEnable=True)
        set_skill(triggerIds=[1404], isEnable=True)
        set_skill(triggerIds=[1405], isEnable=True)
        set_skill(triggerIds=[1406], isEnable=True)
        set_skill(triggerIds=[1407], isEnable=True)
        set_skill(triggerIds=[1408], isEnable=True)
        set_skill(triggerIds=[1409], isEnable=True)
        set_skill(triggerIds=[1410], isEnable=True)
        set_skill(triggerIds=[1411], isEnable=True)
        set_skill(triggerIds=[1412], isEnable=True)
        set_skill(triggerIds=[1413], isEnable=True)
        set_skill(triggerIds=[1414], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬19대기()


class 스킬19대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1397], isEnable=False)
        set_skill(triggerIds=[1398], isEnable=False)
        set_skill(triggerIds=[1399], isEnable=False)
        set_skill(triggerIds=[1400], isEnable=False)
        set_skill(triggerIds=[1401], isEnable=False)
        set_skill(triggerIds=[1402], isEnable=False)
        set_skill(triggerIds=[1403], isEnable=False)
        set_skill(triggerIds=[1404], isEnable=False)
        set_skill(triggerIds=[1405], isEnable=False)
        set_skill(triggerIds=[1406], isEnable=False)
        set_skill(triggerIds=[1407], isEnable=False)
        set_skill(triggerIds=[1408], isEnable=False)
        set_skill(triggerIds=[1409], isEnable=False)
        set_skill(triggerIds=[1410], isEnable=False)
        set_skill(triggerIds=[1411], isEnable=False)
        set_skill(triggerIds=[1412], isEnable=False)
        set_skill(triggerIds=[1413], isEnable=False)
        set_skill(triggerIds=[1414], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬19()


class 스킬19(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1403], isEnable=True)
        set_skill(triggerIds=[1404], isEnable=True)
        set_skill(triggerIds=[1405], isEnable=True)
        set_skill(triggerIds=[1406], isEnable=True)
        set_skill(triggerIds=[1407], isEnable=True)
        set_skill(triggerIds=[1408], isEnable=True)
        set_skill(triggerIds=[1409], isEnable=True)
        set_skill(triggerIds=[1410], isEnable=True)
        set_skill(triggerIds=[1411], isEnable=True)
        set_skill(triggerIds=[1412], isEnable=True)
        set_skill(triggerIds=[1413], isEnable=True)
        set_skill(triggerIds=[1414], isEnable=True)
        set_skill(triggerIds=[1409], isEnable=True)
        set_skill(triggerIds=[1410], isEnable=True)
        set_skill(triggerIds=[1411], isEnable=True)
        set_skill(triggerIds=[1412], isEnable=True)
        set_skill(triggerIds=[1413], isEnable=True)
        set_skill(triggerIds=[1414], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬20대기()


class 스킬20대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1403], isEnable=False)
        set_skill(triggerIds=[1404], isEnable=False)
        set_skill(triggerIds=[1405], isEnable=False)
        set_skill(triggerIds=[1406], isEnable=False)
        set_skill(triggerIds=[1407], isEnable=False)
        set_skill(triggerIds=[1408], isEnable=False)
        set_skill(triggerIds=[1409], isEnable=False)
        set_skill(triggerIds=[1410], isEnable=False)
        set_skill(triggerIds=[1411], isEnable=False)
        set_skill(triggerIds=[1412], isEnable=False)
        set_skill(triggerIds=[1413], isEnable=False)
        set_skill(triggerIds=[1414], isEnable=False)
        set_skill(triggerIds=[1415], isEnable=False)
        set_skill(triggerIds=[1416], isEnable=False)
        set_skill(triggerIds=[1417], isEnable=False)
        set_skill(triggerIds=[1418], isEnable=False)
        set_skill(triggerIds=[1419], isEnable=False)
        set_skill(triggerIds=[1420], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬20()


class 스킬20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1409], isEnable=True)
        set_skill(triggerIds=[1410], isEnable=True)
        set_skill(triggerIds=[1411], isEnable=True)
        set_skill(triggerIds=[1412], isEnable=True)
        set_skill(triggerIds=[1413], isEnable=True)
        set_skill(triggerIds=[1414], isEnable=True)
        set_skill(triggerIds=[1415], isEnable=True)
        set_skill(triggerIds=[1416], isEnable=True)
        set_skill(triggerIds=[1417], isEnable=True)
        set_skill(triggerIds=[1418], isEnable=True)
        set_skill(triggerIds=[1419], isEnable=True)
        set_skill(triggerIds=[1420], isEnable=True)
        set_skill(triggerIds=[1421], isEnable=True)
        set_skill(triggerIds=[1422], isEnable=True)
        set_skill(triggerIds=[1423], isEnable=True)
        set_skill(triggerIds=[1424], isEnable=True)
        set_skill(triggerIds=[1425], isEnable=True)
        set_skill(triggerIds=[1426], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬21대기()


class 스킬21대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1409], isEnable=False)
        set_skill(triggerIds=[1410], isEnable=False)
        set_skill(triggerIds=[1411], isEnable=False)
        set_skill(triggerIds=[1412], isEnable=False)
        set_skill(triggerIds=[1413], isEnable=False)
        set_skill(triggerIds=[1414], isEnable=False)
        set_skill(triggerIds=[1415], isEnable=False)
        set_skill(triggerIds=[1416], isEnable=False)
        set_skill(triggerIds=[1417], isEnable=False)
        set_skill(triggerIds=[1418], isEnable=False)
        set_skill(triggerIds=[1419], isEnable=False)
        set_skill(triggerIds=[1420], isEnable=False)
        set_skill(triggerIds=[1421], isEnable=False)
        set_skill(triggerIds=[1422], isEnable=False)
        set_skill(triggerIds=[1423], isEnable=False)
        set_skill(triggerIds=[1424], isEnable=False)
        set_skill(triggerIds=[1425], isEnable=False)
        set_skill(triggerIds=[1426], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬21()


class 스킬21(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1415], isEnable=True)
        set_skill(triggerIds=[1416], isEnable=True)
        set_skill(triggerIds=[1417], isEnable=True)
        set_skill(triggerIds=[1418], isEnable=True)
        set_skill(triggerIds=[1419], isEnable=True)
        set_skill(triggerIds=[1420], isEnable=True)
        set_skill(triggerIds=[1421], isEnable=True)
        set_skill(triggerIds=[1422], isEnable=True)
        set_skill(triggerIds=[1423], isEnable=True)
        set_skill(triggerIds=[1424], isEnable=True)
        set_skill(triggerIds=[1425], isEnable=True)
        set_skill(triggerIds=[1426], isEnable=True)
        set_skill(triggerIds=[1427], isEnable=True)
        set_skill(triggerIds=[1428], isEnable=True)
        set_skill(triggerIds=[1429], isEnable=True)
        set_skill(triggerIds=[1430], isEnable=True)
        set_skill(triggerIds=[1431], isEnable=True)
        set_skill(triggerIds=[1432], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬22대기()


class 스킬22대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1415], isEnable=False)
        set_skill(triggerIds=[1416], isEnable=False)
        set_skill(triggerIds=[1417], isEnable=False)
        set_skill(triggerIds=[1418], isEnable=False)
        set_skill(triggerIds=[1419], isEnable=False)
        set_skill(triggerIds=[1420], isEnable=False)
        set_skill(triggerIds=[1421], isEnable=False)
        set_skill(triggerIds=[1422], isEnable=False)
        set_skill(triggerIds=[1423], isEnable=False)
        set_skill(triggerIds=[1424], isEnable=False)
        set_skill(triggerIds=[1425], isEnable=False)
        set_skill(triggerIds=[1426], isEnable=False)
        set_skill(triggerIds=[1427], isEnable=False)
        set_skill(triggerIds=[1428], isEnable=False)
        set_skill(triggerIds=[1429], isEnable=False)
        set_skill(triggerIds=[1430], isEnable=False)
        set_skill(triggerIds=[1431], isEnable=False)
        set_skill(triggerIds=[1432], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬22()


class 스킬22(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1421], isEnable=True)
        set_skill(triggerIds=[1422], isEnable=True)
        set_skill(triggerIds=[1423], isEnable=True)
        set_skill(triggerIds=[1424], isEnable=True)
        set_skill(triggerIds=[1425], isEnable=True)
        set_skill(triggerIds=[1426], isEnable=True)
        set_skill(triggerIds=[1427], isEnable=True)
        set_skill(triggerIds=[1428], isEnable=True)
        set_skill(triggerIds=[1429], isEnable=True)
        set_skill(triggerIds=[1430], isEnable=True)
        set_skill(triggerIds=[1431], isEnable=True)
        set_skill(triggerIds=[1432], isEnable=True)
        set_skill(triggerIds=[1433], isEnable=True)
        set_skill(triggerIds=[1434], isEnable=True)
        set_skill(triggerIds=[1435], isEnable=True)
        set_skill(triggerIds=[1436], isEnable=True)
        set_skill(triggerIds=[1437], isEnable=True)
        set_skill(triggerIds=[1438], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬23대기()


class 스킬23대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1421], isEnable=False)
        set_skill(triggerIds=[1422], isEnable=False)
        set_skill(triggerIds=[1423], isEnable=False)
        set_skill(triggerIds=[1424], isEnable=False)
        set_skill(triggerIds=[1425], isEnable=False)
        set_skill(triggerIds=[1426], isEnable=False)
        set_skill(triggerIds=[1427], isEnable=False)
        set_skill(triggerIds=[1428], isEnable=False)
        set_skill(triggerIds=[1429], isEnable=False)
        set_skill(triggerIds=[1430], isEnable=False)
        set_skill(triggerIds=[1431], isEnable=False)
        set_skill(triggerIds=[1432], isEnable=False)
        set_skill(triggerIds=[1433], isEnable=False)
        set_skill(triggerIds=[1434], isEnable=False)
        set_skill(triggerIds=[1435], isEnable=False)
        set_skill(triggerIds=[1436], isEnable=False)
        set_skill(triggerIds=[1437], isEnable=False)
        set_skill(triggerIds=[1438], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬23()


class 스킬23(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1427], isEnable=True)
        set_skill(triggerIds=[1428], isEnable=True)
        set_skill(triggerIds=[1429], isEnable=True)
        set_skill(triggerIds=[1430], isEnable=True)
        set_skill(triggerIds=[1431], isEnable=True)
        set_skill(triggerIds=[1432], isEnable=True)
        set_skill(triggerIds=[1433], isEnable=True)
        set_skill(triggerIds=[1434], isEnable=True)
        set_skill(triggerIds=[1435], isEnable=True)
        set_skill(triggerIds=[1436], isEnable=True)
        set_skill(triggerIds=[1437], isEnable=True)
        set_skill(triggerIds=[1438], isEnable=True)
        set_skill(triggerIds=[1439], isEnable=True)
        set_skill(triggerIds=[1440], isEnable=True)
        set_skill(triggerIds=[1441], isEnable=True)
        set_skill(triggerIds=[1442], isEnable=True)
        set_skill(triggerIds=[1443], isEnable=True)
        set_skill(triggerIds=[1444], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬24대기()


class 스킬24대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1427], isEnable=False)
        set_skill(triggerIds=[1428], isEnable=False)
        set_skill(triggerIds=[1429], isEnable=False)
        set_skill(triggerIds=[1430], isEnable=False)
        set_skill(triggerIds=[1431], isEnable=False)
        set_skill(triggerIds=[1432], isEnable=False)
        set_skill(triggerIds=[1433], isEnable=False)
        set_skill(triggerIds=[1434], isEnable=False)
        set_skill(triggerIds=[1435], isEnable=False)
        set_skill(triggerIds=[1436], isEnable=False)
        set_skill(triggerIds=[1437], isEnable=False)
        set_skill(triggerIds=[1438], isEnable=False)
        set_skill(triggerIds=[1439], isEnable=False)
        set_skill(triggerIds=[1440], isEnable=False)
        set_skill(triggerIds=[1441], isEnable=False)
        set_skill(triggerIds=[1442], isEnable=False)
        set_skill(triggerIds=[1443], isEnable=False)
        set_skill(triggerIds=[1444], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬24()


class 스킬24(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1433], isEnable=True)
        set_skill(triggerIds=[1434], isEnable=True)
        set_skill(triggerIds=[1435], isEnable=True)
        set_skill(triggerIds=[1436], isEnable=True)
        set_skill(triggerIds=[1437], isEnable=True)
        set_skill(triggerIds=[1438], isEnable=True)
        set_skill(triggerIds=[1439], isEnable=True)
        set_skill(triggerIds=[1440], isEnable=True)
        set_skill(triggerIds=[1441], isEnable=True)
        set_skill(triggerIds=[1442], isEnable=True)
        set_skill(triggerIds=[1443], isEnable=True)
        set_skill(triggerIds=[1444], isEnable=True)
        set_skill(triggerIds=[1445], isEnable=True)
        set_skill(triggerIds=[1446], isEnable=True)
        set_skill(triggerIds=[1447], isEnable=True)
        set_skill(triggerIds=[1448], isEnable=True)
        set_skill(triggerIds=[1449], isEnable=True)
        set_skill(triggerIds=[1450], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬25대기()


class 스킬25대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1433], isEnable=False)
        set_skill(triggerIds=[1434], isEnable=False)
        set_skill(triggerIds=[1435], isEnable=False)
        set_skill(triggerIds=[1436], isEnable=False)
        set_skill(triggerIds=[1437], isEnable=False)
        set_skill(triggerIds=[1438], isEnable=False)
        set_skill(triggerIds=[1439], isEnable=False)
        set_skill(triggerIds=[1440], isEnable=False)
        set_skill(triggerIds=[1441], isEnable=False)
        set_skill(triggerIds=[1442], isEnable=False)
        set_skill(triggerIds=[1443], isEnable=False)
        set_skill(triggerIds=[1444], isEnable=False)
        set_skill(triggerIds=[1445], isEnable=False)
        set_skill(triggerIds=[1446], isEnable=False)
        set_skill(triggerIds=[1447], isEnable=False)
        set_skill(triggerIds=[1448], isEnable=False)
        set_skill(triggerIds=[1449], isEnable=False)
        set_skill(triggerIds=[1450], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬25()


class 스킬25(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1439], isEnable=True)
        set_skill(triggerIds=[1440], isEnable=True)
        set_skill(triggerIds=[1441], isEnable=True)
        set_skill(triggerIds=[1442], isEnable=True)
        set_skill(triggerIds=[1443], isEnable=True)
        set_skill(triggerIds=[1444], isEnable=True)
        set_skill(triggerIds=[1445], isEnable=True)
        set_skill(triggerIds=[1446], isEnable=True)
        set_skill(triggerIds=[1447], isEnable=True)
        set_skill(triggerIds=[1448], isEnable=True)
        set_skill(triggerIds=[1449], isEnable=True)
        set_skill(triggerIds=[1450], isEnable=True)
        set_skill(triggerIds=[1451], isEnable=True)
        set_skill(triggerIds=[1452], isEnable=True)
        set_skill(triggerIds=[1453], isEnable=True)
        set_skill(triggerIds=[1454], isEnable=True)
        set_skill(triggerIds=[1455], isEnable=True)
        set_skill(triggerIds=[1456], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬26대기()


class 스킬26대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1439], isEnable=False)
        set_skill(triggerIds=[1440], isEnable=False)
        set_skill(triggerIds=[1441], isEnable=False)
        set_skill(triggerIds=[1442], isEnable=False)
        set_skill(triggerIds=[1443], isEnable=False)
        set_skill(triggerIds=[1444], isEnable=False)
        set_skill(triggerIds=[1445], isEnable=False)
        set_skill(triggerIds=[1446], isEnable=False)
        set_skill(triggerIds=[1447], isEnable=False)
        set_skill(triggerIds=[1448], isEnable=False)
        set_skill(triggerIds=[1449], isEnable=False)
        set_skill(triggerIds=[1450], isEnable=False)
        set_skill(triggerIds=[1451], isEnable=False)
        set_skill(triggerIds=[1452], isEnable=False)
        set_skill(triggerIds=[1453], isEnable=False)
        set_skill(triggerIds=[1454], isEnable=False)
        set_skill(triggerIds=[1455], isEnable=False)
        set_skill(triggerIds=[1456], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬26()


class 스킬26(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1445], isEnable=True)
        set_skill(triggerIds=[1446], isEnable=True)
        set_skill(triggerIds=[1447], isEnable=True)
        set_skill(triggerIds=[1448], isEnable=True)
        set_skill(triggerIds=[1449], isEnable=True)
        set_skill(triggerIds=[1450], isEnable=True)
        set_skill(triggerIds=[1451], isEnable=True)
        set_skill(triggerIds=[1452], isEnable=True)
        set_skill(triggerIds=[1453], isEnable=True)
        set_skill(triggerIds=[1454], isEnable=True)
        set_skill(triggerIds=[1455], isEnable=True)
        set_skill(triggerIds=[1456], isEnable=True)
        set_skill(triggerIds=[1457], isEnable=True)
        set_skill(triggerIds=[1458], isEnable=True)
        set_skill(triggerIds=[1459], isEnable=True)
        set_skill(triggerIds=[1460], isEnable=True)
        set_skill(triggerIds=[1461], isEnable=True)
        set_skill(triggerIds=[1462], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬27대기()


class 스킬27대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1445], isEnable=False)
        set_skill(triggerIds=[1446], isEnable=False)
        set_skill(triggerIds=[1447], isEnable=False)
        set_skill(triggerIds=[1448], isEnable=False)
        set_skill(triggerIds=[1449], isEnable=False)
        set_skill(triggerIds=[1450], isEnable=False)
        set_skill(triggerIds=[1451], isEnable=False)
        set_skill(triggerIds=[1452], isEnable=False)
        set_skill(triggerIds=[1453], isEnable=False)
        set_skill(triggerIds=[1454], isEnable=False)
        set_skill(triggerIds=[1455], isEnable=False)
        set_skill(triggerIds=[1456], isEnable=False)
        set_skill(triggerIds=[1457], isEnable=False)
        set_skill(triggerIds=[1458], isEnable=False)
        set_skill(triggerIds=[1459], isEnable=False)
        set_skill(triggerIds=[1460], isEnable=False)
        set_skill(triggerIds=[1461], isEnable=False)
        set_skill(triggerIds=[1462], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬27()


class 스킬27(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1451], isEnable=True)
        set_skill(triggerIds=[1452], isEnable=True)
        set_skill(triggerIds=[1453], isEnable=True)
        set_skill(triggerIds=[1454], isEnable=True)
        set_skill(triggerIds=[1455], isEnable=True)
        set_skill(triggerIds=[1456], isEnable=True)
        set_skill(triggerIds=[1457], isEnable=True)
        set_skill(triggerIds=[1458], isEnable=True)
        set_skill(triggerIds=[1459], isEnable=True)
        set_skill(triggerIds=[1460], isEnable=True)
        set_skill(triggerIds=[1461], isEnable=True)
        set_skill(triggerIds=[1462], isEnable=True)
        set_skill(triggerIds=[1463], isEnable=True)
        set_skill(triggerIds=[1464], isEnable=True)
        set_skill(triggerIds=[1465], isEnable=True)
        set_skill(triggerIds=[1466], isEnable=True)
        set_skill(triggerIds=[1467], isEnable=True)
        set_skill(triggerIds=[1468], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬28대기()


class 스킬28대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1451], isEnable=False)
        set_skill(triggerIds=[1452], isEnable=False)
        set_skill(triggerIds=[1453], isEnable=False)
        set_skill(triggerIds=[1454], isEnable=False)
        set_skill(triggerIds=[1455], isEnable=False)
        set_skill(triggerIds=[1456], isEnable=False)
        set_skill(triggerIds=[1457], isEnable=False)
        set_skill(triggerIds=[1458], isEnable=False)
        set_skill(triggerIds=[1459], isEnable=False)
        set_skill(triggerIds=[1460], isEnable=False)
        set_skill(triggerIds=[1461], isEnable=False)
        set_skill(triggerIds=[1462], isEnable=False)
        set_skill(triggerIds=[1463], isEnable=False)
        set_skill(triggerIds=[1464], isEnable=False)
        set_skill(triggerIds=[1465], isEnable=False)
        set_skill(triggerIds=[1466], isEnable=False)
        set_skill(triggerIds=[1467], isEnable=False)
        set_skill(triggerIds=[1468], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬28()


class 스킬28(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1457], isEnable=True)
        set_skill(triggerIds=[1458], isEnable=True)
        set_skill(triggerIds=[1459], isEnable=True)
        set_skill(triggerIds=[1460], isEnable=True)
        set_skill(triggerIds=[1461], isEnable=True)
        set_skill(triggerIds=[1462], isEnable=True)
        set_skill(triggerIds=[1463], isEnable=True)
        set_skill(triggerIds=[1464], isEnable=True)
        set_skill(triggerIds=[1465], isEnable=True)
        set_skill(triggerIds=[1466], isEnable=True)
        set_skill(triggerIds=[1467], isEnable=True)
        set_skill(triggerIds=[1468], isEnable=True)
        set_skill(triggerIds=[1469], isEnable=True)
        set_skill(triggerIds=[1470], isEnable=True)
        set_skill(triggerIds=[1471], isEnable=True)
        set_skill(triggerIds=[1472], isEnable=True)
        set_skill(triggerIds=[1473], isEnable=True)
        set_skill(triggerIds=[1474], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬29대기()


class 스킬29대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1457], isEnable=False)
        set_skill(triggerIds=[1458], isEnable=False)
        set_skill(triggerIds=[1459], isEnable=False)
        set_skill(triggerIds=[1460], isEnable=False)
        set_skill(triggerIds=[1461], isEnable=False)
        set_skill(triggerIds=[1462], isEnable=False)
        set_skill(triggerIds=[1463], isEnable=False)
        set_skill(triggerIds=[1464], isEnable=False)
        set_skill(triggerIds=[1465], isEnable=False)
        set_skill(triggerIds=[1466], isEnable=False)
        set_skill(triggerIds=[1467], isEnable=False)
        set_skill(triggerIds=[1468], isEnable=False)
        set_skill(triggerIds=[1469], isEnable=False)
        set_skill(triggerIds=[1470], isEnable=False)
        set_skill(triggerIds=[1471], isEnable=False)
        set_skill(triggerIds=[1472], isEnable=False)
        set_skill(triggerIds=[1473], isEnable=False)
        set_skill(triggerIds=[1474], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬29()


class 스킬29(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1463], isEnable=True)
        set_skill(triggerIds=[1464], isEnable=True)
        set_skill(triggerIds=[1465], isEnable=True)
        set_skill(triggerIds=[1466], isEnable=True)
        set_skill(triggerIds=[1467], isEnable=True)
        set_skill(triggerIds=[1468], isEnable=True)
        set_skill(triggerIds=[1469], isEnable=True)
        set_skill(triggerIds=[1470], isEnable=True)
        set_skill(triggerIds=[1471], isEnable=True)
        set_skill(triggerIds=[1472], isEnable=True)
        set_skill(triggerIds=[1473], isEnable=True)
        set_skill(triggerIds=[1474], isEnable=True)
        set_skill(triggerIds=[1475], isEnable=True)
        set_skill(triggerIds=[1476], isEnable=True)
        set_skill(triggerIds=[1477], isEnable=True)
        set_skill(triggerIds=[1478], isEnable=True)
        set_skill(triggerIds=[1479], isEnable=True)
        set_skill(triggerIds=[1480], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬30대기()


class 스킬30대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1463], isEnable=False)
        set_skill(triggerIds=[1464], isEnable=False)
        set_skill(triggerIds=[1465], isEnable=False)
        set_skill(triggerIds=[1466], isEnable=False)
        set_skill(triggerIds=[1467], isEnable=False)
        set_skill(triggerIds=[1468], isEnable=False)
        set_skill(triggerIds=[1469], isEnable=False)
        set_skill(triggerIds=[1470], isEnable=False)
        set_skill(triggerIds=[1471], isEnable=False)
        set_skill(triggerIds=[1472], isEnable=False)
        set_skill(triggerIds=[1473], isEnable=False)
        set_skill(triggerIds=[1475], isEnable=False)
        set_skill(triggerIds=[1474], isEnable=False)
        set_skill(triggerIds=[1476], isEnable=False)
        set_skill(triggerIds=[1477], isEnable=False)
        set_skill(triggerIds=[1478], isEnable=False)
        set_skill(triggerIds=[1479], isEnable=False)
        set_skill(triggerIds=[1480], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬30()


class 스킬30(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1469], isEnable=True)
        set_skill(triggerIds=[1470], isEnable=True)
        set_skill(triggerIds=[1471], isEnable=True)
        set_skill(triggerIds=[1472], isEnable=True)
        set_skill(triggerIds=[1473], isEnable=True)
        set_skill(triggerIds=[1474], isEnable=True)
        set_skill(triggerIds=[1475], isEnable=True)
        set_skill(triggerIds=[1476], isEnable=True)
        set_skill(triggerIds=[1477], isEnable=True)
        set_skill(triggerIds=[1478], isEnable=True)
        set_skill(triggerIds=[1479], isEnable=True)
        set_skill(triggerIds=[1480], isEnable=True)
        set_skill(triggerIds=[1481], isEnable=True)
        set_skill(triggerIds=[1482], isEnable=True)
        set_skill(triggerIds=[1483], isEnable=True)
        set_skill(triggerIds=[1484], isEnable=True)
        set_skill(triggerIds=[1485], isEnable=True)
        set_skill(triggerIds=[1486], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬31대기()


class 스킬31대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1469], isEnable=False)
        set_skill(triggerIds=[1470], isEnable=False)
        set_skill(triggerIds=[1471], isEnable=False)
        set_skill(triggerIds=[1472], isEnable=False)
        set_skill(triggerIds=[1473], isEnable=False)
        set_skill(triggerIds=[1474], isEnable=False)
        set_skill(triggerIds=[1475], isEnable=False)
        set_skill(triggerIds=[1476], isEnable=False)
        set_skill(triggerIds=[1477], isEnable=False)
        set_skill(triggerIds=[1478], isEnable=False)
        set_skill(triggerIds=[1479], isEnable=False)
        set_skill(triggerIds=[1480], isEnable=False)
        set_skill(triggerIds=[1481], isEnable=False)
        set_skill(triggerIds=[1482], isEnable=False)
        set_skill(triggerIds=[1483], isEnable=False)
        set_skill(triggerIds=[1484], isEnable=False)
        set_skill(triggerIds=[1485], isEnable=False)
        set_skill(triggerIds=[1486], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬31()


class 스킬31(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1475], isEnable=True)
        set_skill(triggerIds=[1476], isEnable=True)
        set_skill(triggerIds=[1477], isEnable=True)
        set_skill(triggerIds=[1478], isEnable=True)
        set_skill(triggerIds=[1479], isEnable=True)
        set_skill(triggerIds=[1480], isEnable=True)
        set_skill(triggerIds=[1481], isEnable=True)
        set_skill(triggerIds=[1482], isEnable=True)
        set_skill(triggerIds=[1483], isEnable=True)
        set_skill(triggerIds=[1484], isEnable=True)
        set_skill(triggerIds=[1485], isEnable=True)
        set_skill(triggerIds=[1486], isEnable=True)
        set_skill(triggerIds=[1487], isEnable=True)
        set_skill(triggerIds=[1488], isEnable=True)
        set_skill(triggerIds=[1489], isEnable=True)
        set_skill(triggerIds=[1490], isEnable=True)
        set_skill(triggerIds=[1491], isEnable=True)
        set_skill(triggerIds=[1492], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬32대기()


class 스킬32대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1475], isEnable=False)
        set_skill(triggerIds=[1476], isEnable=False)
        set_skill(triggerIds=[1477], isEnable=False)
        set_skill(triggerIds=[1478], isEnable=False)
        set_skill(triggerIds=[1479], isEnable=False)
        set_skill(triggerIds=[1480], isEnable=False)
        set_skill(triggerIds=[1481], isEnable=False)
        set_skill(triggerIds=[1482], isEnable=False)
        set_skill(triggerIds=[1483], isEnable=False)
        set_skill(triggerIds=[1484], isEnable=False)
        set_skill(triggerIds=[1485], isEnable=False)
        set_skill(triggerIds=[1486], isEnable=False)
        set_skill(triggerIds=[1487], isEnable=False)
        set_skill(triggerIds=[1488], isEnable=False)
        set_skill(triggerIds=[1489], isEnable=False)
        set_skill(triggerIds=[1490], isEnable=False)
        set_skill(triggerIds=[1491], isEnable=False)
        set_skill(triggerIds=[1492], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬32()


class 스킬32(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1481], isEnable=True)
        set_skill(triggerIds=[1482], isEnable=True)
        set_skill(triggerIds=[1483], isEnable=True)
        set_skill(triggerIds=[1484], isEnable=True)
        set_skill(triggerIds=[1485], isEnable=True)
        set_skill(triggerIds=[1486], isEnable=True)
        set_skill(triggerIds=[1487], isEnable=True)
        set_skill(triggerIds=[1488], isEnable=True)
        set_skill(triggerIds=[1489], isEnable=True)
        set_skill(triggerIds=[1490], isEnable=True)
        set_skill(triggerIds=[1491], isEnable=True)
        set_skill(triggerIds=[1492], isEnable=True)
        set_skill(triggerIds=[1493], isEnable=True)
        set_skill(triggerIds=[1494], isEnable=True)
        set_skill(triggerIds=[1495], isEnable=True)
        set_skill(triggerIds=[1496], isEnable=True)
        set_skill(triggerIds=[1497], isEnable=True)
        set_skill(triggerIds=[1498], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬33대기()


class 스킬33대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1481], isEnable=False)
        set_skill(triggerIds=[1482], isEnable=False)
        set_skill(triggerIds=[1483], isEnable=False)
        set_skill(triggerIds=[1484], isEnable=False)
        set_skill(triggerIds=[1485], isEnable=False)
        set_skill(triggerIds=[1486], isEnable=False)
        set_skill(triggerIds=[1487], isEnable=False)
        set_skill(triggerIds=[1488], isEnable=False)
        set_skill(triggerIds=[1489], isEnable=False)
        set_skill(triggerIds=[1490], isEnable=False)
        set_skill(triggerIds=[1491], isEnable=False)
        set_skill(triggerIds=[1492], isEnable=False)
        set_skill(triggerIds=[1493], isEnable=False)
        set_skill(triggerIds=[1494], isEnable=False)
        set_skill(triggerIds=[1495], isEnable=False)
        set_skill(triggerIds=[1496], isEnable=False)
        set_skill(triggerIds=[1497], isEnable=False)
        set_skill(triggerIds=[1498], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬33()


class 스킬33(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[1487], isEnable=True)
        set_skill(triggerIds=[1488], isEnable=True)
        set_skill(triggerIds=[1489], isEnable=True)
        set_skill(triggerIds=[1490], isEnable=True)
        set_skill(triggerIds=[1491], isEnable=True)
        set_skill(triggerIds=[1492], isEnable=True)
        set_skill(triggerIds=[1493], isEnable=True)
        set_skill(triggerIds=[1494], isEnable=True)
        set_skill(triggerIds=[1495], isEnable=True)
        set_skill(triggerIds=[1496], isEnable=True)
        set_skill(triggerIds=[1497], isEnable=True)
        set_skill(triggerIds=[1498], isEnable=True)
        set_skill(triggerIds=[1499], isEnable=True)
        set_skill(triggerIds=[1500], isEnable=True)
        set_skill(triggerIds=[1501], isEnable=True)
        set_skill(triggerIds=[1502], isEnable=True)
        set_skill(triggerIds=[1503], isEnable=True)
        set_skill(triggerIds=[1504], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬34대기()


class 스킬34대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1487], isEnable=False)
        set_skill(triggerIds=[1488], isEnable=False)
        set_skill(triggerIds=[1489], isEnable=False)
        set_skill(triggerIds=[1490], isEnable=False)
        set_skill(triggerIds=[1491], isEnable=False)
        set_skill(triggerIds=[1492], isEnable=False)
        set_skill(triggerIds=[1493], isEnable=False)
        set_skill(triggerIds=[1494], isEnable=False)
        set_skill(triggerIds=[1495], isEnable=False)
        set_skill(triggerIds=[1496], isEnable=False)
        set_skill(triggerIds=[1497], isEnable=False)
        set_skill(triggerIds=[1498], isEnable=False)
        set_skill(triggerIds=[1499], isEnable=False)
        set_skill(triggerIds=[1500], isEnable=False)
        set_skill(triggerIds=[1501], isEnable=False)
        set_skill(triggerIds=[1502], isEnable=False)
        set_skill(triggerIds=[1503], isEnable=False)
        set_skill(triggerIds=[1504], isEnable=False)


