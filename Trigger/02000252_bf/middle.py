""" trigger/02000252_bf/middle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8201], visible=False)
        self.set_effect(triggerIds=[8202], visible=False)
        self.set_effect(triggerIds=[8203], visible=False)
        self.set_effect(triggerIds=[8204], visible=False)
        self.set_effect(triggerIds=[8205], visible=False)
        self.set_effect(triggerIds=[8206], visible=False)
        self.set_effect(triggerIds=[8207], visible=False)
        self.set_effect(triggerIds=[8208], visible=False)
        self.set_effect(triggerIds=[8209], visible=False)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_effect(triggerIds=[8211], visible=False)
        self.set_effect(triggerIds=[8212], visible=False)
        self.set_effect(triggerIds=[8213], visible=False)
        self.set_effect(triggerIds=[8214], visible=False)
        self.set_effect(triggerIds=[8215], visible=False)
        self.set_effect(triggerIds=[8216], visible=False)
        self.set_effect(triggerIds=[8217], visible=False)
        self.set_effect(triggerIds=[8218], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=902, boxId=1):
            return 바닥삭제(self.ctx)


class 바닥삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=5)
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142], visible=False, arg3=0, delay=100)
        self.create_monster(spawnIds=[1075], animationEffect=False)
        self.create_monster(spawnIds=[1076], animationEffect=False)
        self.create_monster(spawnIds=[1077], animationEffect=False)
        self.create_monster(spawnIds=[1078], animationEffect=False)
        self.create_monster(spawnIds=[1079], animationEffect=False)
        self.create_monster(spawnIds=[1080], animationEffect=False)
        self.create_monster(spawnIds=[1081], animationEffect=False)
        self.create_monster(spawnIds=[1082], animationEffect=False)
        self.create_monster(spawnIds=[1083], animationEffect=False)
        self.create_monster(spawnIds=[1084], animationEffect=False)
        self.create_monster(spawnIds=[1085], animationEffect=False)
        self.create_monster(spawnIds=[1086], animationEffect=False)
        self.create_monster(spawnIds=[1087], animationEffect=False)
        self.create_monster(spawnIds=[1088], animationEffect=False)
        self.create_monster(spawnIds=[1089], animationEffect=False)
        self.create_monster(spawnIds=[1090], animationEffect=False)
        self.create_monster(spawnIds=[1091], animationEffect=False)
        self.create_monster(spawnIds=[1092], animationEffect=False)
        self.create_monster(spawnIds=[1093], animationEffect=False)
        self.create_monster(spawnIds=[1094], animationEffect=False)
        self.set_effect(triggerIds=[8201], visible=True)
        self.set_effect(triggerIds=[8202], visible=True)
        self.set_effect(triggerIds=[8203], visible=True)
        self.set_effect(triggerIds=[8204], visible=True)
        self.set_effect(triggerIds=[8205], visible=True)
        self.set_effect(triggerIds=[8206], visible=True)
        self.set_effect(triggerIds=[8207], visible=True)
        self.set_effect(triggerIds=[8208], visible=True)
        self.set_effect(triggerIds=[8209], visible=True)
        self.set_effect(triggerIds=[8210], visible=True)
        self.set_effect(triggerIds=[8211], visible=True)
        self.set_effect(triggerIds=[8212], visible=True)
        self.set_effect(triggerIds=[8213], visible=True)
        self.set_effect(triggerIds=[8214], visible=True)
        self.set_effect(triggerIds=[8215], visible=True)
        self.set_effect(triggerIds=[8216], visible=True)
        self.set_effect(triggerIds=[8217], visible=True)
        self.set_effect(triggerIds=[8218], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 스킬01(self.ctx)


class 스킬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[8201], visible=False)
        self.set_effect(triggerIds=[8202], visible=False)
        self.set_effect(triggerIds=[8203], visible=False)
        self.set_effect(triggerIds=[8204], visible=False)
        self.set_effect(triggerIds=[8205], visible=False)
        self.set_effect(triggerIds=[8206], visible=False)
        self.set_effect(triggerIds=[8207], visible=False)
        self.set_effect(triggerIds=[8208], visible=False)
        self.set_effect(triggerIds=[8209], visible=False)
        self.set_effect(triggerIds=[8210], visible=False)
        self.set_effect(triggerIds=[8211], visible=False)
        self.set_effect(triggerIds=[8212], visible=False)
        self.set_effect(triggerIds=[8213], visible=False)
        self.set_effect(triggerIds=[8214], visible=False)
        self.set_effect(triggerIds=[8215], visible=False)
        self.set_effect(triggerIds=[8216], visible=False)
        self.set_effect(triggerIds=[8217], visible=False)
        self.set_effect(triggerIds=[8218], visible=False)
        self.set_skill(triggerIds=[1301], enable=True)
        self.set_skill(triggerIds=[1302], enable=True)
        self.set_skill(triggerIds=[1303], enable=True)
        self.set_skill(triggerIds=[1304], enable=True)
        self.set_skill(triggerIds=[1305], enable=True)
        self.set_skill(triggerIds=[1306], enable=True)
        self.set_skill(triggerIds=[1307], enable=True)
        self.set_skill(triggerIds=[1308], enable=True)
        self.set_skill(triggerIds=[1309], enable=True)
        self.set_skill(triggerIds=[1310], enable=True)
        self.set_skill(triggerIds=[1311], enable=True)
        self.set_skill(triggerIds=[1312], enable=True)
        self.set_skill(triggerIds=[1313], enable=True)
        self.set_skill(triggerIds=[1314], enable=True)
        self.set_skill(triggerIds=[1315], enable=True)
        self.set_skill(triggerIds=[1316], enable=True)
        self.set_skill(triggerIds=[1317], enable=True)
        self.set_skill(triggerIds=[1318], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬02대기(self.ctx)


class 스킬02대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1301], enable=False)
        self.set_skill(triggerIds=[1302], enable=False)
        self.set_skill(triggerIds=[1303], enable=False)
        self.set_skill(triggerIds=[1304], enable=False)
        self.set_skill(triggerIds=[1305], enable=False)
        self.set_skill(triggerIds=[1306], enable=False)
        self.set_skill(triggerIds=[1307], enable=False)
        self.set_skill(triggerIds=[1308], enable=False)
        self.set_skill(triggerIds=[1309], enable=False)
        self.set_skill(triggerIds=[1310], enable=False)
        self.set_skill(triggerIds=[1311], enable=False)
        self.set_skill(triggerIds=[1312], enable=False)
        self.set_skill(triggerIds=[1313], enable=False)
        self.set_skill(triggerIds=[1314], enable=False)
        self.set_skill(triggerIds=[1315], enable=False)
        self.set_skill(triggerIds=[1316], enable=False)
        self.set_skill(triggerIds=[1317], enable=False)
        self.set_skill(triggerIds=[1318], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬02(self.ctx)


class 스킬02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1307], enable=True)
        self.set_skill(triggerIds=[1308], enable=True)
        self.set_skill(triggerIds=[1309], enable=True)
        self.set_skill(triggerIds=[1310], enable=True)
        self.set_skill(triggerIds=[1311], enable=True)
        self.set_skill(triggerIds=[1312], enable=True)
        self.set_skill(triggerIds=[1313], enable=True)
        self.set_skill(triggerIds=[1314], enable=True)
        self.set_skill(triggerIds=[1315], enable=True)
        self.set_skill(triggerIds=[1316], enable=True)
        self.set_skill(triggerIds=[1317], enable=True)
        self.set_skill(triggerIds=[1318], enable=True)
        self.set_skill(triggerIds=[1319], enable=True)
        self.set_skill(triggerIds=[1320], enable=True)
        self.set_skill(triggerIds=[1321], enable=True)
        self.set_skill(triggerIds=[1322], enable=True)
        self.set_skill(triggerIds=[1323], enable=True)
        self.set_skill(triggerIds=[1324], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬03대기(self.ctx)


class 스킬03대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1307], enable=False)
        self.set_skill(triggerIds=[1308], enable=False)
        self.set_skill(triggerIds=[1309], enable=False)
        self.set_skill(triggerIds=[1310], enable=False)
        self.set_skill(triggerIds=[1311], enable=False)
        self.set_skill(triggerIds=[1312], enable=False)
        self.set_skill(triggerIds=[1313], enable=False)
        self.set_skill(triggerIds=[1314], enable=False)
        self.set_skill(triggerIds=[1315], enable=False)
        self.set_skill(triggerIds=[1316], enable=False)
        self.set_skill(triggerIds=[1317], enable=False)
        self.set_skill(triggerIds=[1318], enable=False)
        self.set_skill(triggerIds=[1319], enable=False)
        self.set_skill(triggerIds=[1320], enable=False)
        self.set_skill(triggerIds=[1321], enable=False)
        self.set_skill(triggerIds=[1322], enable=False)
        self.set_skill(triggerIds=[1323], enable=False)
        self.set_skill(triggerIds=[1324], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬03(self.ctx)


class 스킬03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1313], enable=True)
        self.set_skill(triggerIds=[1314], enable=True)
        self.set_skill(triggerIds=[1315], enable=True)
        self.set_skill(triggerIds=[1316], enable=True)
        self.set_skill(triggerIds=[1317], enable=True)
        self.set_skill(triggerIds=[1318], enable=True)
        self.set_skill(triggerIds=[1319], enable=True)
        self.set_skill(triggerIds=[1320], enable=True)
        self.set_skill(triggerIds=[1321], enable=True)
        self.set_skill(triggerIds=[1322], enable=True)
        self.set_skill(triggerIds=[1323], enable=True)
        self.set_skill(triggerIds=[1324], enable=True)
        self.set_skill(triggerIds=[1325], enable=True)
        self.set_skill(triggerIds=[1326], enable=True)
        self.set_skill(triggerIds=[1327], enable=True)
        self.set_skill(triggerIds=[1328], enable=True)
        self.set_skill(triggerIds=[1328], enable=True)
        self.set_skill(triggerIds=[1330], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬04대기(self.ctx)


class 스킬04대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1313], enable=False)
        self.set_skill(triggerIds=[1314], enable=False)
        self.set_skill(triggerIds=[1315], enable=False)
        self.set_skill(triggerIds=[1316], enable=False)
        self.set_skill(triggerIds=[1317], enable=False)
        self.set_skill(triggerIds=[1318], enable=False)
        self.set_skill(triggerIds=[1319], enable=False)
        self.set_skill(triggerIds=[1320], enable=False)
        self.set_skill(triggerIds=[1321], enable=False)
        self.set_skill(triggerIds=[1322], enable=False)
        self.set_skill(triggerIds=[1323], enable=False)
        self.set_skill(triggerIds=[1324], enable=False)
        self.set_skill(triggerIds=[1325], enable=False)
        self.set_skill(triggerIds=[1326], enable=False)
        self.set_skill(triggerIds=[1327], enable=False)
        self.set_skill(triggerIds=[1328], enable=False)
        self.set_skill(triggerIds=[1328], enable=False)
        self.set_skill(triggerIds=[1330], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬04(self.ctx)


class 스킬04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1319], enable=True)
        self.set_skill(triggerIds=[1320], enable=True)
        self.set_skill(triggerIds=[1321], enable=True)
        self.set_skill(triggerIds=[1322], enable=True)
        self.set_skill(triggerIds=[1323], enable=True)
        self.set_skill(triggerIds=[1324], enable=True)
        self.set_skill(triggerIds=[1325], enable=True)
        self.set_skill(triggerIds=[1326], enable=True)
        self.set_skill(triggerIds=[1327], enable=True)
        self.set_skill(triggerIds=[1328], enable=True)
        self.set_skill(triggerIds=[1328], enable=True)
        self.set_skill(triggerIds=[1330], enable=True)
        self.set_skill(triggerIds=[1331], enable=True)
        self.set_skill(triggerIds=[1332], enable=True)
        self.set_skill(triggerIds=[1333], enable=True)
        self.set_skill(triggerIds=[1334], enable=True)
        self.set_skill(triggerIds=[1335], enable=True)
        self.set_skill(triggerIds=[1336], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬05대기(self.ctx)


class 스킬05대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1319], enable=False)
        self.set_skill(triggerIds=[1320], enable=False)
        self.set_skill(triggerIds=[1321], enable=False)
        self.set_skill(triggerIds=[1322], enable=False)
        self.set_skill(triggerIds=[1323], enable=False)
        self.set_skill(triggerIds=[1324], enable=False)
        self.set_skill(triggerIds=[1325], enable=False)
        self.set_skill(triggerIds=[1326], enable=False)
        self.set_skill(triggerIds=[1327], enable=False)
        self.set_skill(triggerIds=[1328], enable=False)
        self.set_skill(triggerIds=[1328], enable=False)
        self.set_skill(triggerIds=[1330], enable=False)
        self.set_skill(triggerIds=[1331], enable=False)
        self.set_skill(triggerIds=[1332], enable=False)
        self.set_skill(triggerIds=[1333], enable=False)
        self.set_skill(triggerIds=[1334], enable=False)
        self.set_skill(triggerIds=[1335], enable=False)
        self.set_skill(triggerIds=[1336], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬05(self.ctx)


class 스킬05(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1325], enable=True)
        self.set_skill(triggerIds=[1326], enable=True)
        self.set_skill(triggerIds=[1327], enable=True)
        self.set_skill(triggerIds=[1328], enable=True)
        self.set_skill(triggerIds=[1328], enable=True)
        self.set_skill(triggerIds=[1330], enable=True)
        self.set_skill(triggerIds=[1331], enable=True)
        self.set_skill(triggerIds=[1332], enable=True)
        self.set_skill(triggerIds=[1333], enable=True)
        self.set_skill(triggerIds=[1334], enable=True)
        self.set_skill(triggerIds=[1335], enable=True)
        self.set_skill(triggerIds=[1336], enable=True)
        self.set_skill(triggerIds=[1337], enable=True)
        self.set_skill(triggerIds=[1338], enable=True)
        self.set_skill(triggerIds=[1339], enable=True)
        self.set_skill(triggerIds=[1340], enable=True)
        self.set_skill(triggerIds=[1341], enable=True)
        self.set_skill(triggerIds=[1342], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬06대기(self.ctx)


class 스킬06대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1325], enable=False)
        self.set_skill(triggerIds=[1326], enable=False)
        self.set_skill(triggerIds=[1327], enable=False)
        self.set_skill(triggerIds=[1328], enable=False)
        self.set_skill(triggerIds=[1328], enable=False)
        self.set_skill(triggerIds=[1330], enable=False)
        self.set_skill(triggerIds=[1331], enable=False)
        self.set_skill(triggerIds=[1332], enable=False)
        self.set_skill(triggerIds=[1333], enable=False)
        self.set_skill(triggerIds=[1334], enable=False)
        self.set_skill(triggerIds=[1335], enable=False)
        self.set_skill(triggerIds=[1336], enable=False)
        self.set_skill(triggerIds=[1337], enable=False)
        self.set_skill(triggerIds=[1338], enable=False)
        self.set_skill(triggerIds=[1339], enable=False)
        self.set_skill(triggerIds=[1340], enable=False)
        self.set_skill(triggerIds=[1341], enable=False)
        self.set_skill(triggerIds=[1342], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬06(self.ctx)


class 스킬06(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1331], enable=True)
        self.set_skill(triggerIds=[1332], enable=True)
        self.set_skill(triggerIds=[1333], enable=True)
        self.set_skill(triggerIds=[1334], enable=True)
        self.set_skill(triggerIds=[1335], enable=True)
        self.set_skill(triggerIds=[1336], enable=True)
        self.set_skill(triggerIds=[1337], enable=True)
        self.set_skill(triggerIds=[1338], enable=True)
        self.set_skill(triggerIds=[1339], enable=True)
        self.set_skill(triggerIds=[1340], enable=True)
        self.set_skill(triggerIds=[1341], enable=True)
        self.set_skill(triggerIds=[1342], enable=True)
        self.set_skill(triggerIds=[1343], enable=True)
        self.set_skill(triggerIds=[1344], enable=True)
        self.set_skill(triggerIds=[1345], enable=True)
        self.set_skill(triggerIds=[1346], enable=True)
        self.set_skill(triggerIds=[1347], enable=True)
        self.set_skill(triggerIds=[1348], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬07대기(self.ctx)


class 스킬07대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1331], enable=False)
        self.set_skill(triggerIds=[1332], enable=False)
        self.set_skill(triggerIds=[1333], enable=False)
        self.set_skill(triggerIds=[1334], enable=False)
        self.set_skill(triggerIds=[1335], enable=False)
        self.set_skill(triggerIds=[1336], enable=False)
        self.set_skill(triggerIds=[1337], enable=False)
        self.set_skill(triggerIds=[1338], enable=False)
        self.set_skill(triggerIds=[1339], enable=False)
        self.set_skill(triggerIds=[1340], enable=False)
        self.set_skill(triggerIds=[1341], enable=False)
        self.set_skill(triggerIds=[1342], enable=False)
        self.set_skill(triggerIds=[1343], enable=False)
        self.set_skill(triggerIds=[1344], enable=False)
        self.set_skill(triggerIds=[1345], enable=False)
        self.set_skill(triggerIds=[1346], enable=False)
        self.set_skill(triggerIds=[1347], enable=False)
        self.set_skill(triggerIds=[1348], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬07(self.ctx)


class 스킬07(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1337], enable=True)
        self.set_skill(triggerIds=[1338], enable=True)
        self.set_skill(triggerIds=[1339], enable=True)
        self.set_skill(triggerIds=[1340], enable=True)
        self.set_skill(triggerIds=[1341], enable=True)
        self.set_skill(triggerIds=[1342], enable=True)
        self.set_skill(triggerIds=[1343], enable=True)
        self.set_skill(triggerIds=[1344], enable=True)
        self.set_skill(triggerIds=[1345], enable=True)
        self.set_skill(triggerIds=[1346], enable=True)
        self.set_skill(triggerIds=[1347], enable=True)
        self.set_skill(triggerIds=[1348], enable=True)
        self.set_skill(triggerIds=[1349], enable=True)
        self.set_skill(triggerIds=[1350], enable=True)
        self.set_skill(triggerIds=[1351], enable=True)
        self.set_skill(triggerIds=[1352], enable=True)
        self.set_skill(triggerIds=[1353], enable=True)
        self.set_skill(triggerIds=[1354], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬08대기(self.ctx)


class 스킬08대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1337], enable=False)
        self.set_skill(triggerIds=[1338], enable=False)
        self.set_skill(triggerIds=[1339], enable=False)
        self.set_skill(triggerIds=[1340], enable=False)
        self.set_skill(triggerIds=[1341], enable=False)
        self.set_skill(triggerIds=[1342], enable=False)
        self.set_skill(triggerIds=[1343], enable=False)
        self.set_skill(triggerIds=[1344], enable=False)
        self.set_skill(triggerIds=[1345], enable=False)
        self.set_skill(triggerIds=[1346], enable=False)
        self.set_skill(triggerIds=[1347], enable=False)
        self.set_skill(triggerIds=[1348], enable=False)
        self.set_skill(triggerIds=[1349], enable=False)
        self.set_skill(triggerIds=[1350], enable=False)
        self.set_skill(triggerIds=[1351], enable=False)
        self.set_skill(triggerIds=[1352], enable=False)
        self.set_skill(triggerIds=[1353], enable=False)
        self.set_skill(triggerIds=[1354], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬08(self.ctx)


class 스킬08(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1343], enable=True)
        self.set_skill(triggerIds=[1344], enable=True)
        self.set_skill(triggerIds=[1345], enable=True)
        self.set_skill(triggerIds=[1346], enable=True)
        self.set_skill(triggerIds=[1347], enable=True)
        self.set_skill(triggerIds=[1348], enable=True)
        self.set_skill(triggerIds=[1349], enable=True)
        self.set_skill(triggerIds=[1350], enable=True)
        self.set_skill(triggerIds=[1351], enable=True)
        self.set_skill(triggerIds=[1352], enable=True)
        self.set_skill(triggerIds=[1353], enable=True)
        self.set_skill(triggerIds=[1354], enable=True)
        self.set_skill(triggerIds=[1355], enable=True)
        self.set_skill(triggerIds=[1356], enable=True)
        self.set_skill(triggerIds=[1357], enable=True)
        self.set_skill(triggerIds=[1358], enable=True)
        self.set_skill(triggerIds=[1359], enable=True)
        self.set_skill(triggerIds=[1360], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬09대기(self.ctx)


class 스킬09대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1343], enable=False)
        self.set_skill(triggerIds=[1344], enable=False)
        self.set_skill(triggerIds=[1345], enable=False)
        self.set_skill(triggerIds=[1346], enable=False)
        self.set_skill(triggerIds=[1347], enable=False)
        self.set_skill(triggerIds=[1348], enable=False)
        self.set_skill(triggerIds=[1349], enable=False)
        self.set_skill(triggerIds=[1350], enable=False)
        self.set_skill(triggerIds=[1351], enable=False)
        self.set_skill(triggerIds=[1352], enable=False)
        self.set_skill(triggerIds=[1353], enable=False)
        self.set_skill(triggerIds=[1354], enable=False)
        self.set_skill(triggerIds=[1355], enable=False)
        self.set_skill(triggerIds=[1356], enable=False)
        self.set_skill(triggerIds=[1357], enable=False)
        self.set_skill(triggerIds=[1358], enable=False)
        self.set_skill(triggerIds=[1359], enable=False)
        self.set_skill(triggerIds=[1360], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬09(self.ctx)


class 스킬09(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1349], enable=True)
        self.set_skill(triggerIds=[1350], enable=True)
        self.set_skill(triggerIds=[1351], enable=True)
        self.set_skill(triggerIds=[1352], enable=True)
        self.set_skill(triggerIds=[1353], enable=True)
        self.set_skill(triggerIds=[1354], enable=True)
        self.set_skill(triggerIds=[1355], enable=True)
        self.set_skill(triggerIds=[1356], enable=True)
        self.set_skill(triggerIds=[1357], enable=True)
        self.set_skill(triggerIds=[1358], enable=True)
        self.set_skill(triggerIds=[1359], enable=True)
        self.set_skill(triggerIds=[1360], enable=True)
        self.set_skill(triggerIds=[1361], enable=True)
        self.set_skill(triggerIds=[1362], enable=True)
        self.set_skill(triggerIds=[1363], enable=True)
        self.set_skill(triggerIds=[1364], enable=True)
        self.set_skill(triggerIds=[1365], enable=True)
        self.set_skill(triggerIds=[1366], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬10대기(self.ctx)


class 스킬10대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1349], enable=False)
        self.set_skill(triggerIds=[1350], enable=False)
        self.set_skill(triggerIds=[1351], enable=False)
        self.set_skill(triggerIds=[1352], enable=False)
        self.set_skill(triggerIds=[1353], enable=False)
        self.set_skill(triggerIds=[1354], enable=False)
        self.set_skill(triggerIds=[1355], enable=False)
        self.set_skill(triggerIds=[1356], enable=False)
        self.set_skill(triggerIds=[1357], enable=False)
        self.set_skill(triggerIds=[1358], enable=False)
        self.set_skill(triggerIds=[1359], enable=False)
        self.set_skill(triggerIds=[1360], enable=False)
        self.set_skill(triggerIds=[1361], enable=False)
        self.set_skill(triggerIds=[1362], enable=False)
        self.set_skill(triggerIds=[1363], enable=False)
        self.set_skill(triggerIds=[1364], enable=False)
        self.set_skill(triggerIds=[1365], enable=False)
        self.set_skill(triggerIds=[1366], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬10(self.ctx)


class 스킬10(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1355], enable=True)
        self.set_skill(triggerIds=[1356], enable=True)
        self.set_skill(triggerIds=[1357], enable=True)
        self.set_skill(triggerIds=[1358], enable=True)
        self.set_skill(triggerIds=[1359], enable=True)
        self.set_skill(triggerIds=[1360], enable=True)
        self.set_skill(triggerIds=[1361], enable=True)
        self.set_skill(triggerIds=[1362], enable=True)
        self.set_skill(triggerIds=[1363], enable=True)
        self.set_skill(triggerIds=[1364], enable=True)
        self.set_skill(triggerIds=[1365], enable=True)
        self.set_skill(triggerIds=[1366], enable=True)
        self.set_skill(triggerIds=[1367], enable=True)
        self.set_skill(triggerIds=[1368], enable=True)
        self.set_skill(triggerIds=[1369], enable=True)
        self.set_skill(triggerIds=[1370], enable=True)
        self.set_skill(triggerIds=[1371], enable=True)
        self.set_skill(triggerIds=[1372], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬11대기(self.ctx)


class 스킬11대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1355], enable=False)
        self.set_skill(triggerIds=[1356], enable=False)
        self.set_skill(triggerIds=[1357], enable=False)
        self.set_skill(triggerIds=[1358], enable=False)
        self.set_skill(triggerIds=[1359], enable=False)
        self.set_skill(triggerIds=[1360], enable=False)
        self.set_skill(triggerIds=[1361], enable=False)
        self.set_skill(triggerIds=[1362], enable=False)
        self.set_skill(triggerIds=[1363], enable=False)
        self.set_skill(triggerIds=[1364], enable=False)
        self.set_skill(triggerIds=[1365], enable=False)
        self.set_skill(triggerIds=[1366], enable=False)
        self.set_skill(triggerIds=[1367], enable=False)
        self.set_skill(triggerIds=[1368], enable=False)
        self.set_skill(triggerIds=[1369], enable=False)
        self.set_skill(triggerIds=[1370], enable=False)
        self.set_skill(triggerIds=[1371], enable=False)
        self.set_skill(triggerIds=[1372], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬11(self.ctx)


class 스킬11(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1361], enable=True)
        self.set_skill(triggerIds=[1362], enable=True)
        self.set_skill(triggerIds=[1363], enable=True)
        self.set_skill(triggerIds=[1364], enable=True)
        self.set_skill(triggerIds=[1365], enable=True)
        self.set_skill(triggerIds=[1366], enable=True)
        self.set_skill(triggerIds=[1367], enable=True)
        self.set_skill(triggerIds=[1368], enable=True)
        self.set_skill(triggerIds=[1369], enable=True)
        self.set_skill(triggerIds=[1370], enable=True)
        self.set_skill(triggerIds=[1371], enable=True)
        self.set_skill(triggerIds=[1372], enable=True)
        self.set_skill(triggerIds=[1373], enable=True)
        self.set_skill(triggerIds=[1374], enable=True)
        self.set_skill(triggerIds=[1375], enable=True)
        self.set_skill(triggerIds=[1376], enable=True)
        self.set_skill(triggerIds=[1377], enable=True)
        self.set_skill(triggerIds=[1378], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬12대기(self.ctx)


class 스킬12대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1361], enable=False)
        self.set_skill(triggerIds=[1362], enable=False)
        self.set_skill(triggerIds=[1363], enable=False)
        self.set_skill(triggerIds=[1364], enable=False)
        self.set_skill(triggerIds=[1365], enable=False)
        self.set_skill(triggerIds=[1366], enable=False)
        self.set_skill(triggerIds=[1367], enable=False)
        self.set_skill(triggerIds=[1368], enable=False)
        self.set_skill(triggerIds=[1369], enable=False)
        self.set_skill(triggerIds=[1370], enable=False)
        self.set_skill(triggerIds=[1371], enable=False)
        self.set_skill(triggerIds=[1372], enable=False)
        self.set_skill(triggerIds=[1373], enable=False)
        self.set_skill(triggerIds=[1374], enable=False)
        self.set_skill(triggerIds=[1375], enable=False)
        self.set_skill(triggerIds=[1376], enable=False)
        self.set_skill(triggerIds=[1377], enable=False)
        self.set_skill(triggerIds=[1378], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬12(self.ctx)


class 스킬12(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1367], enable=True)
        self.set_skill(triggerIds=[1368], enable=True)
        self.set_skill(triggerIds=[1369], enable=True)
        self.set_skill(triggerIds=[1370], enable=True)
        self.set_skill(triggerIds=[1371], enable=True)
        self.set_skill(triggerIds=[1372], enable=True)
        self.set_skill(triggerIds=[1373], enable=True)
        self.set_skill(triggerIds=[1374], enable=True)
        self.set_skill(triggerIds=[1375], enable=True)
        self.set_skill(triggerIds=[1376], enable=True)
        self.set_skill(triggerIds=[1377], enable=True)
        self.set_skill(triggerIds=[1378], enable=True)
        self.set_skill(triggerIds=[1379], enable=True)
        self.set_skill(triggerIds=[1380], enable=True)
        self.set_skill(triggerIds=[1381], enable=True)
        self.set_skill(triggerIds=[1382], enable=True)
        self.set_skill(triggerIds=[1383], enable=True)
        self.set_skill(triggerIds=[1384], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬13대기(self.ctx)


class 스킬13대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1367], enable=False)
        self.set_skill(triggerIds=[1368], enable=False)
        self.set_skill(triggerIds=[1369], enable=False)
        self.set_skill(triggerIds=[1370], enable=False)
        self.set_skill(triggerIds=[1371], enable=False)
        self.set_skill(triggerIds=[1372], enable=False)
        self.set_skill(triggerIds=[1373], enable=False)
        self.set_skill(triggerIds=[1374], enable=False)
        self.set_skill(triggerIds=[1375], enable=False)
        self.set_skill(triggerIds=[1376], enable=False)
        self.set_skill(triggerIds=[1377], enable=False)
        self.set_skill(triggerIds=[1378], enable=False)
        self.set_skill(triggerIds=[1379], enable=False)
        self.set_skill(triggerIds=[1380], enable=False)
        self.set_skill(triggerIds=[1381], enable=False)
        self.set_skill(triggerIds=[1382], enable=False)
        self.set_skill(triggerIds=[1383], enable=False)
        self.set_skill(triggerIds=[1384], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬13(self.ctx)


class 스킬13(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1373], enable=True)
        self.set_skill(triggerIds=[1374], enable=True)
        self.set_skill(triggerIds=[1375], enable=True)
        self.set_skill(triggerIds=[1376], enable=True)
        self.set_skill(triggerIds=[1377], enable=True)
        self.set_skill(triggerIds=[1378], enable=True)
        self.set_skill(triggerIds=[1379], enable=True)
        self.set_skill(triggerIds=[1380], enable=True)
        self.set_skill(triggerIds=[1381], enable=True)
        self.set_skill(triggerIds=[1382], enable=True)
        self.set_skill(triggerIds=[1383], enable=True)
        self.set_skill(triggerIds=[1384], enable=True)
        self.set_skill(triggerIds=[1385], enable=True)
        self.set_skill(triggerIds=[1386], enable=True)
        self.set_skill(triggerIds=[1387], enable=True)
        self.set_skill(triggerIds=[1388], enable=True)
        self.set_skill(triggerIds=[1389], enable=True)
        self.set_skill(triggerIds=[1390], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬14대기(self.ctx)


class 스킬14대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1373], enable=False)
        self.set_skill(triggerIds=[1374], enable=False)
        self.set_skill(triggerIds=[1375], enable=False)
        self.set_skill(triggerIds=[1376], enable=False)
        self.set_skill(triggerIds=[1377], enable=False)
        self.set_skill(triggerIds=[1378], enable=False)
        self.set_skill(triggerIds=[1379], enable=False)
        self.set_skill(triggerIds=[1380], enable=False)
        self.set_skill(triggerIds=[1381], enable=False)
        self.set_skill(triggerIds=[1382], enable=False)
        self.set_skill(triggerIds=[1383], enable=False)
        self.set_skill(triggerIds=[1384], enable=False)
        self.set_skill(triggerIds=[1385], enable=False)
        self.set_skill(triggerIds=[1386], enable=False)
        self.set_skill(triggerIds=[1387], enable=False)
        self.set_skill(triggerIds=[1388], enable=False)
        self.set_skill(triggerIds=[1389], enable=False)
        self.set_skill(triggerIds=[1390], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬14(self.ctx)


class 스킬14(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1379], enable=True)
        self.set_skill(triggerIds=[1380], enable=True)
        self.set_skill(triggerIds=[1381], enable=True)
        self.set_skill(triggerIds=[1382], enable=True)
        self.set_skill(triggerIds=[1383], enable=True)
        self.set_skill(triggerIds=[1384], enable=True)
        self.set_skill(triggerIds=[1385], enable=True)
        self.set_skill(triggerIds=[1386], enable=True)
        self.set_skill(triggerIds=[1387], enable=True)
        self.set_skill(triggerIds=[1388], enable=True)
        self.set_skill(triggerIds=[1389], enable=True)
        self.set_skill(triggerIds=[1390], enable=True)
        self.set_skill(triggerIds=[1391], enable=True)
        self.set_skill(triggerIds=[1392], enable=True)
        self.set_skill(triggerIds=[1393], enable=True)
        self.set_skill(triggerIds=[1394], enable=True)
        self.set_skill(triggerIds=[1395], enable=True)
        self.set_skill(triggerIds=[1396], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬15대기(self.ctx)


class 스킬15대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1379], enable=False)
        self.set_skill(triggerIds=[1380], enable=False)
        self.set_skill(triggerIds=[1381], enable=False)
        self.set_skill(triggerIds=[1382], enable=False)
        self.set_skill(triggerIds=[1383], enable=False)
        self.set_skill(triggerIds=[1384], enable=False)
        self.set_skill(triggerIds=[1385], enable=False)
        self.set_skill(triggerIds=[1386], enable=False)
        self.set_skill(triggerIds=[1387], enable=False)
        self.set_skill(triggerIds=[1388], enable=False)
        self.set_skill(triggerIds=[1389], enable=False)
        self.set_skill(triggerIds=[1390], enable=False)
        self.set_skill(triggerIds=[1391], enable=False)
        self.set_skill(triggerIds=[1392], enable=False)
        self.set_skill(triggerIds=[1393], enable=False)
        self.set_skill(triggerIds=[1394], enable=False)
        self.set_skill(triggerIds=[1395], enable=False)
        self.set_skill(triggerIds=[1396], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬15(self.ctx)


class 스킬15(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1385], enable=True)
        self.set_skill(triggerIds=[1386], enable=True)
        self.set_skill(triggerIds=[1387], enable=True)
        self.set_skill(triggerIds=[1388], enable=True)
        self.set_skill(triggerIds=[1389], enable=True)
        self.set_skill(triggerIds=[1390], enable=True)
        self.set_skill(triggerIds=[1391], enable=True)
        self.set_skill(triggerIds=[1392], enable=True)
        self.set_skill(triggerIds=[1393], enable=True)
        self.set_skill(triggerIds=[1394], enable=True)
        self.set_skill(triggerIds=[1395], enable=True)
        self.set_skill(triggerIds=[1396], enable=True)
        self.set_skill(triggerIds=[1397], enable=True)
        self.set_skill(triggerIds=[1398], enable=True)
        self.set_skill(triggerIds=[1399], enable=True)
        self.set_skill(triggerIds=[1400], enable=True)
        self.set_skill(triggerIds=[1401], enable=True)
        self.set_skill(triggerIds=[1402], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬16대기(self.ctx)


class 스킬16대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1385], enable=False)
        self.set_skill(triggerIds=[1386], enable=False)
        self.set_skill(triggerIds=[1387], enable=False)
        self.set_skill(triggerIds=[1388], enable=False)
        self.set_skill(triggerIds=[1389], enable=False)
        self.set_skill(triggerIds=[1390], enable=False)
        self.set_skill(triggerIds=[1391], enable=False)
        self.set_skill(triggerIds=[1392], enable=False)
        self.set_skill(triggerIds=[1393], enable=False)
        self.set_skill(triggerIds=[1394], enable=False)
        self.set_skill(triggerIds=[1395], enable=False)
        self.set_skill(triggerIds=[1396], enable=False)
        self.set_skill(triggerIds=[1397], enable=False)
        self.set_skill(triggerIds=[1398], enable=False)
        self.set_skill(triggerIds=[1399], enable=False)
        self.set_skill(triggerIds=[1400], enable=False)
        self.set_skill(triggerIds=[1401], enable=False)
        self.set_skill(triggerIds=[1402], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬16(self.ctx)


class 스킬16(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1391], enable=True)
        self.set_skill(triggerIds=[1392], enable=True)
        self.set_skill(triggerIds=[1393], enable=True)
        self.set_skill(triggerIds=[1394], enable=True)
        self.set_skill(triggerIds=[1395], enable=True)
        self.set_skill(triggerIds=[1396], enable=True)
        self.set_skill(triggerIds=[1397], enable=True)
        self.set_skill(triggerIds=[1398], enable=True)
        self.set_skill(triggerIds=[1399], enable=True)
        self.set_skill(triggerIds=[1400], enable=True)
        self.set_skill(triggerIds=[1401], enable=True)
        self.set_skill(triggerIds=[1402], enable=True)
        self.set_skill(triggerIds=[1403], enable=True)
        self.set_skill(triggerIds=[1404], enable=True)
        self.set_skill(triggerIds=[1405], enable=True)
        self.set_skill(triggerIds=[1406], enable=True)
        self.set_skill(triggerIds=[1407], enable=True)
        self.set_skill(triggerIds=[1408], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬17대기(self.ctx)


class 스킬17대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1391], enable=False)
        self.set_skill(triggerIds=[1392], enable=False)
        self.set_skill(triggerIds=[1393], enable=False)
        self.set_skill(triggerIds=[1394], enable=False)
        self.set_skill(triggerIds=[1395], enable=False)
        self.set_skill(triggerIds=[1396], enable=False)
        self.set_skill(triggerIds=[1397], enable=False)
        self.set_skill(triggerIds=[1398], enable=False)
        self.set_skill(triggerIds=[1399], enable=False)
        self.set_skill(triggerIds=[1400], enable=False)
        self.set_skill(triggerIds=[1401], enable=False)
        self.set_skill(triggerIds=[1402], enable=False)
        self.set_skill(triggerIds=[1403], enable=False)
        self.set_skill(triggerIds=[1404], enable=False)
        self.set_skill(triggerIds=[1405], enable=False)
        self.set_skill(triggerIds=[1406], enable=False)
        self.set_skill(triggerIds=[1407], enable=False)
        self.set_skill(triggerIds=[1408], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬17(self.ctx)


class 스킬17(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1391], enable=True)
        self.set_skill(triggerIds=[1392], enable=True)
        self.set_skill(triggerIds=[1393], enable=True)
        self.set_skill(triggerIds=[1394], enable=True)
        self.set_skill(triggerIds=[1395], enable=True)
        self.set_skill(triggerIds=[1396], enable=True)
        self.set_skill(triggerIds=[1397], enable=True)
        self.set_skill(triggerIds=[1398], enable=True)
        self.set_skill(triggerIds=[1399], enable=True)
        self.set_skill(triggerIds=[1400], enable=True)
        self.set_skill(triggerIds=[1401], enable=True)
        self.set_skill(triggerIds=[1402], enable=True)
        self.set_skill(triggerIds=[1403], enable=True)
        self.set_skill(triggerIds=[1404], enable=True)
        self.set_skill(triggerIds=[1405], enable=True)
        self.set_skill(triggerIds=[1406], enable=True)
        self.set_skill(triggerIds=[1407], enable=True)
        self.set_skill(triggerIds=[1408], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬18대기(self.ctx)


class 스킬18대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1391], enable=False)
        self.set_skill(triggerIds=[1392], enable=False)
        self.set_skill(triggerIds=[1393], enable=False)
        self.set_skill(triggerIds=[1394], enable=False)
        self.set_skill(triggerIds=[1395], enable=False)
        self.set_skill(triggerIds=[1396], enable=False)
        self.set_skill(triggerIds=[1397], enable=False)
        self.set_skill(triggerIds=[1398], enable=False)
        self.set_skill(triggerIds=[1399], enable=False)
        self.set_skill(triggerIds=[1400], enable=False)
        self.set_skill(triggerIds=[1401], enable=False)
        self.set_skill(triggerIds=[1402], enable=False)
        self.set_skill(triggerIds=[1403], enable=False)
        self.set_skill(triggerIds=[1404], enable=False)
        self.set_skill(triggerIds=[1405], enable=False)
        self.set_skill(triggerIds=[1406], enable=False)
        self.set_skill(triggerIds=[1407], enable=False)
        self.set_skill(triggerIds=[1408], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬18(self.ctx)


class 스킬18(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1397], enable=True)
        self.set_skill(triggerIds=[1398], enable=True)
        self.set_skill(triggerIds=[1399], enable=True)
        self.set_skill(triggerIds=[1400], enable=True)
        self.set_skill(triggerIds=[1401], enable=True)
        self.set_skill(triggerIds=[1402], enable=True)
        self.set_skill(triggerIds=[1403], enable=True)
        self.set_skill(triggerIds=[1404], enable=True)
        self.set_skill(triggerIds=[1405], enable=True)
        self.set_skill(triggerIds=[1406], enable=True)
        self.set_skill(triggerIds=[1407], enable=True)
        self.set_skill(triggerIds=[1408], enable=True)
        self.set_skill(triggerIds=[1409], enable=True)
        self.set_skill(triggerIds=[1410], enable=True)
        self.set_skill(triggerIds=[1411], enable=True)
        self.set_skill(triggerIds=[1412], enable=True)
        self.set_skill(triggerIds=[1413], enable=True)
        self.set_skill(triggerIds=[1414], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬19대기(self.ctx)


class 스킬19대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1397], enable=False)
        self.set_skill(triggerIds=[1398], enable=False)
        self.set_skill(triggerIds=[1399], enable=False)
        self.set_skill(triggerIds=[1400], enable=False)
        self.set_skill(triggerIds=[1401], enable=False)
        self.set_skill(triggerIds=[1402], enable=False)
        self.set_skill(triggerIds=[1403], enable=False)
        self.set_skill(triggerIds=[1404], enable=False)
        self.set_skill(triggerIds=[1405], enable=False)
        self.set_skill(triggerIds=[1406], enable=False)
        self.set_skill(triggerIds=[1407], enable=False)
        self.set_skill(triggerIds=[1408], enable=False)
        self.set_skill(triggerIds=[1409], enable=False)
        self.set_skill(triggerIds=[1410], enable=False)
        self.set_skill(triggerIds=[1411], enable=False)
        self.set_skill(triggerIds=[1412], enable=False)
        self.set_skill(triggerIds=[1413], enable=False)
        self.set_skill(triggerIds=[1414], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬19(self.ctx)


class 스킬19(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1403], enable=True)
        self.set_skill(triggerIds=[1404], enable=True)
        self.set_skill(triggerIds=[1405], enable=True)
        self.set_skill(triggerIds=[1406], enable=True)
        self.set_skill(triggerIds=[1407], enable=True)
        self.set_skill(triggerIds=[1408], enable=True)
        self.set_skill(triggerIds=[1409], enable=True)
        self.set_skill(triggerIds=[1410], enable=True)
        self.set_skill(triggerIds=[1411], enable=True)
        self.set_skill(triggerIds=[1412], enable=True)
        self.set_skill(triggerIds=[1413], enable=True)
        self.set_skill(triggerIds=[1414], enable=True)
        self.set_skill(triggerIds=[1409], enable=True)
        self.set_skill(triggerIds=[1410], enable=True)
        self.set_skill(triggerIds=[1411], enable=True)
        self.set_skill(triggerIds=[1412], enable=True)
        self.set_skill(triggerIds=[1413], enable=True)
        self.set_skill(triggerIds=[1414], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬20대기(self.ctx)


class 스킬20대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1403], enable=False)
        self.set_skill(triggerIds=[1404], enable=False)
        self.set_skill(triggerIds=[1405], enable=False)
        self.set_skill(triggerIds=[1406], enable=False)
        self.set_skill(triggerIds=[1407], enable=False)
        self.set_skill(triggerIds=[1408], enable=False)
        self.set_skill(triggerIds=[1409], enable=False)
        self.set_skill(triggerIds=[1410], enable=False)
        self.set_skill(triggerIds=[1411], enable=False)
        self.set_skill(triggerIds=[1412], enable=False)
        self.set_skill(triggerIds=[1413], enable=False)
        self.set_skill(triggerIds=[1414], enable=False)
        self.set_skill(triggerIds=[1415], enable=False)
        self.set_skill(triggerIds=[1416], enable=False)
        self.set_skill(triggerIds=[1417], enable=False)
        self.set_skill(triggerIds=[1418], enable=False)
        self.set_skill(triggerIds=[1419], enable=False)
        self.set_skill(triggerIds=[1420], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬20(self.ctx)


class 스킬20(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1409], enable=True)
        self.set_skill(triggerIds=[1410], enable=True)
        self.set_skill(triggerIds=[1411], enable=True)
        self.set_skill(triggerIds=[1412], enable=True)
        self.set_skill(triggerIds=[1413], enable=True)
        self.set_skill(triggerIds=[1414], enable=True)
        self.set_skill(triggerIds=[1415], enable=True)
        self.set_skill(triggerIds=[1416], enable=True)
        self.set_skill(triggerIds=[1417], enable=True)
        self.set_skill(triggerIds=[1418], enable=True)
        self.set_skill(triggerIds=[1419], enable=True)
        self.set_skill(triggerIds=[1420], enable=True)
        self.set_skill(triggerIds=[1421], enable=True)
        self.set_skill(triggerIds=[1422], enable=True)
        self.set_skill(triggerIds=[1423], enable=True)
        self.set_skill(triggerIds=[1424], enable=True)
        self.set_skill(triggerIds=[1425], enable=True)
        self.set_skill(triggerIds=[1426], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬21대기(self.ctx)


class 스킬21대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1409], enable=False)
        self.set_skill(triggerIds=[1410], enable=False)
        self.set_skill(triggerIds=[1411], enable=False)
        self.set_skill(triggerIds=[1412], enable=False)
        self.set_skill(triggerIds=[1413], enable=False)
        self.set_skill(triggerIds=[1414], enable=False)
        self.set_skill(triggerIds=[1415], enable=False)
        self.set_skill(triggerIds=[1416], enable=False)
        self.set_skill(triggerIds=[1417], enable=False)
        self.set_skill(triggerIds=[1418], enable=False)
        self.set_skill(triggerIds=[1419], enable=False)
        self.set_skill(triggerIds=[1420], enable=False)
        self.set_skill(triggerIds=[1421], enable=False)
        self.set_skill(triggerIds=[1422], enable=False)
        self.set_skill(triggerIds=[1423], enable=False)
        self.set_skill(triggerIds=[1424], enable=False)
        self.set_skill(triggerIds=[1425], enable=False)
        self.set_skill(triggerIds=[1426], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬21(self.ctx)


class 스킬21(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1415], enable=True)
        self.set_skill(triggerIds=[1416], enable=True)
        self.set_skill(triggerIds=[1417], enable=True)
        self.set_skill(triggerIds=[1418], enable=True)
        self.set_skill(triggerIds=[1419], enable=True)
        self.set_skill(triggerIds=[1420], enable=True)
        self.set_skill(triggerIds=[1421], enable=True)
        self.set_skill(triggerIds=[1422], enable=True)
        self.set_skill(triggerIds=[1423], enable=True)
        self.set_skill(triggerIds=[1424], enable=True)
        self.set_skill(triggerIds=[1425], enable=True)
        self.set_skill(triggerIds=[1426], enable=True)
        self.set_skill(triggerIds=[1427], enable=True)
        self.set_skill(triggerIds=[1428], enable=True)
        self.set_skill(triggerIds=[1429], enable=True)
        self.set_skill(triggerIds=[1430], enable=True)
        self.set_skill(triggerIds=[1431], enable=True)
        self.set_skill(triggerIds=[1432], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬22대기(self.ctx)


class 스킬22대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1415], enable=False)
        self.set_skill(triggerIds=[1416], enable=False)
        self.set_skill(triggerIds=[1417], enable=False)
        self.set_skill(triggerIds=[1418], enable=False)
        self.set_skill(triggerIds=[1419], enable=False)
        self.set_skill(triggerIds=[1420], enable=False)
        self.set_skill(triggerIds=[1421], enable=False)
        self.set_skill(triggerIds=[1422], enable=False)
        self.set_skill(triggerIds=[1423], enable=False)
        self.set_skill(triggerIds=[1424], enable=False)
        self.set_skill(triggerIds=[1425], enable=False)
        self.set_skill(triggerIds=[1426], enable=False)
        self.set_skill(triggerIds=[1427], enable=False)
        self.set_skill(triggerIds=[1428], enable=False)
        self.set_skill(triggerIds=[1429], enable=False)
        self.set_skill(triggerIds=[1430], enable=False)
        self.set_skill(triggerIds=[1431], enable=False)
        self.set_skill(triggerIds=[1432], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬22(self.ctx)


class 스킬22(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1421], enable=True)
        self.set_skill(triggerIds=[1422], enable=True)
        self.set_skill(triggerIds=[1423], enable=True)
        self.set_skill(triggerIds=[1424], enable=True)
        self.set_skill(triggerIds=[1425], enable=True)
        self.set_skill(triggerIds=[1426], enable=True)
        self.set_skill(triggerIds=[1427], enable=True)
        self.set_skill(triggerIds=[1428], enable=True)
        self.set_skill(triggerIds=[1429], enable=True)
        self.set_skill(triggerIds=[1430], enable=True)
        self.set_skill(triggerIds=[1431], enable=True)
        self.set_skill(triggerIds=[1432], enable=True)
        self.set_skill(triggerIds=[1433], enable=True)
        self.set_skill(triggerIds=[1434], enable=True)
        self.set_skill(triggerIds=[1435], enable=True)
        self.set_skill(triggerIds=[1436], enable=True)
        self.set_skill(triggerIds=[1437], enable=True)
        self.set_skill(triggerIds=[1438], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬23대기(self.ctx)


class 스킬23대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1421], enable=False)
        self.set_skill(triggerIds=[1422], enable=False)
        self.set_skill(triggerIds=[1423], enable=False)
        self.set_skill(triggerIds=[1424], enable=False)
        self.set_skill(triggerIds=[1425], enable=False)
        self.set_skill(triggerIds=[1426], enable=False)
        self.set_skill(triggerIds=[1427], enable=False)
        self.set_skill(triggerIds=[1428], enable=False)
        self.set_skill(triggerIds=[1429], enable=False)
        self.set_skill(triggerIds=[1430], enable=False)
        self.set_skill(triggerIds=[1431], enable=False)
        self.set_skill(triggerIds=[1432], enable=False)
        self.set_skill(triggerIds=[1433], enable=False)
        self.set_skill(triggerIds=[1434], enable=False)
        self.set_skill(triggerIds=[1435], enable=False)
        self.set_skill(triggerIds=[1436], enable=False)
        self.set_skill(triggerIds=[1437], enable=False)
        self.set_skill(triggerIds=[1438], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬23(self.ctx)


class 스킬23(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1427], enable=True)
        self.set_skill(triggerIds=[1428], enable=True)
        self.set_skill(triggerIds=[1429], enable=True)
        self.set_skill(triggerIds=[1430], enable=True)
        self.set_skill(triggerIds=[1431], enable=True)
        self.set_skill(triggerIds=[1432], enable=True)
        self.set_skill(triggerIds=[1433], enable=True)
        self.set_skill(triggerIds=[1434], enable=True)
        self.set_skill(triggerIds=[1435], enable=True)
        self.set_skill(triggerIds=[1436], enable=True)
        self.set_skill(triggerIds=[1437], enable=True)
        self.set_skill(triggerIds=[1438], enable=True)
        self.set_skill(triggerIds=[1439], enable=True)
        self.set_skill(triggerIds=[1440], enable=True)
        self.set_skill(triggerIds=[1441], enable=True)
        self.set_skill(triggerIds=[1442], enable=True)
        self.set_skill(triggerIds=[1443], enable=True)
        self.set_skill(triggerIds=[1444], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬24대기(self.ctx)


class 스킬24대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1427], enable=False)
        self.set_skill(triggerIds=[1428], enable=False)
        self.set_skill(triggerIds=[1429], enable=False)
        self.set_skill(triggerIds=[1430], enable=False)
        self.set_skill(triggerIds=[1431], enable=False)
        self.set_skill(triggerIds=[1432], enable=False)
        self.set_skill(triggerIds=[1433], enable=False)
        self.set_skill(triggerIds=[1434], enable=False)
        self.set_skill(triggerIds=[1435], enable=False)
        self.set_skill(triggerIds=[1436], enable=False)
        self.set_skill(triggerIds=[1437], enable=False)
        self.set_skill(triggerIds=[1438], enable=False)
        self.set_skill(triggerIds=[1439], enable=False)
        self.set_skill(triggerIds=[1440], enable=False)
        self.set_skill(triggerIds=[1441], enable=False)
        self.set_skill(triggerIds=[1442], enable=False)
        self.set_skill(triggerIds=[1443], enable=False)
        self.set_skill(triggerIds=[1444], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬24(self.ctx)


class 스킬24(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1433], enable=True)
        self.set_skill(triggerIds=[1434], enable=True)
        self.set_skill(triggerIds=[1435], enable=True)
        self.set_skill(triggerIds=[1436], enable=True)
        self.set_skill(triggerIds=[1437], enable=True)
        self.set_skill(triggerIds=[1438], enable=True)
        self.set_skill(triggerIds=[1439], enable=True)
        self.set_skill(triggerIds=[1440], enable=True)
        self.set_skill(triggerIds=[1441], enable=True)
        self.set_skill(triggerIds=[1442], enable=True)
        self.set_skill(triggerIds=[1443], enable=True)
        self.set_skill(triggerIds=[1444], enable=True)
        self.set_skill(triggerIds=[1445], enable=True)
        self.set_skill(triggerIds=[1446], enable=True)
        self.set_skill(triggerIds=[1447], enable=True)
        self.set_skill(triggerIds=[1448], enable=True)
        self.set_skill(triggerIds=[1449], enable=True)
        self.set_skill(triggerIds=[1450], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬25대기(self.ctx)


class 스킬25대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1433], enable=False)
        self.set_skill(triggerIds=[1434], enable=False)
        self.set_skill(triggerIds=[1435], enable=False)
        self.set_skill(triggerIds=[1436], enable=False)
        self.set_skill(triggerIds=[1437], enable=False)
        self.set_skill(triggerIds=[1438], enable=False)
        self.set_skill(triggerIds=[1439], enable=False)
        self.set_skill(triggerIds=[1440], enable=False)
        self.set_skill(triggerIds=[1441], enable=False)
        self.set_skill(triggerIds=[1442], enable=False)
        self.set_skill(triggerIds=[1443], enable=False)
        self.set_skill(triggerIds=[1444], enable=False)
        self.set_skill(triggerIds=[1445], enable=False)
        self.set_skill(triggerIds=[1446], enable=False)
        self.set_skill(triggerIds=[1447], enable=False)
        self.set_skill(triggerIds=[1448], enable=False)
        self.set_skill(triggerIds=[1449], enable=False)
        self.set_skill(triggerIds=[1450], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬25(self.ctx)


class 스킬25(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1439], enable=True)
        self.set_skill(triggerIds=[1440], enable=True)
        self.set_skill(triggerIds=[1441], enable=True)
        self.set_skill(triggerIds=[1442], enable=True)
        self.set_skill(triggerIds=[1443], enable=True)
        self.set_skill(triggerIds=[1444], enable=True)
        self.set_skill(triggerIds=[1445], enable=True)
        self.set_skill(triggerIds=[1446], enable=True)
        self.set_skill(triggerIds=[1447], enable=True)
        self.set_skill(triggerIds=[1448], enable=True)
        self.set_skill(triggerIds=[1449], enable=True)
        self.set_skill(triggerIds=[1450], enable=True)
        self.set_skill(triggerIds=[1451], enable=True)
        self.set_skill(triggerIds=[1452], enable=True)
        self.set_skill(triggerIds=[1453], enable=True)
        self.set_skill(triggerIds=[1454], enable=True)
        self.set_skill(triggerIds=[1455], enable=True)
        self.set_skill(triggerIds=[1456], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬26대기(self.ctx)


class 스킬26대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1439], enable=False)
        self.set_skill(triggerIds=[1440], enable=False)
        self.set_skill(triggerIds=[1441], enable=False)
        self.set_skill(triggerIds=[1442], enable=False)
        self.set_skill(triggerIds=[1443], enable=False)
        self.set_skill(triggerIds=[1444], enable=False)
        self.set_skill(triggerIds=[1445], enable=False)
        self.set_skill(triggerIds=[1446], enable=False)
        self.set_skill(triggerIds=[1447], enable=False)
        self.set_skill(triggerIds=[1448], enable=False)
        self.set_skill(triggerIds=[1449], enable=False)
        self.set_skill(triggerIds=[1450], enable=False)
        self.set_skill(triggerIds=[1451], enable=False)
        self.set_skill(triggerIds=[1452], enable=False)
        self.set_skill(triggerIds=[1453], enable=False)
        self.set_skill(triggerIds=[1454], enable=False)
        self.set_skill(triggerIds=[1455], enable=False)
        self.set_skill(triggerIds=[1456], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬26(self.ctx)


class 스킬26(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1445], enable=True)
        self.set_skill(triggerIds=[1446], enable=True)
        self.set_skill(triggerIds=[1447], enable=True)
        self.set_skill(triggerIds=[1448], enable=True)
        self.set_skill(triggerIds=[1449], enable=True)
        self.set_skill(triggerIds=[1450], enable=True)
        self.set_skill(triggerIds=[1451], enable=True)
        self.set_skill(triggerIds=[1452], enable=True)
        self.set_skill(triggerIds=[1453], enable=True)
        self.set_skill(triggerIds=[1454], enable=True)
        self.set_skill(triggerIds=[1455], enable=True)
        self.set_skill(triggerIds=[1456], enable=True)
        self.set_skill(triggerIds=[1457], enable=True)
        self.set_skill(triggerIds=[1458], enable=True)
        self.set_skill(triggerIds=[1459], enable=True)
        self.set_skill(triggerIds=[1460], enable=True)
        self.set_skill(triggerIds=[1461], enable=True)
        self.set_skill(triggerIds=[1462], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬27대기(self.ctx)


class 스킬27대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1445], enable=False)
        self.set_skill(triggerIds=[1446], enable=False)
        self.set_skill(triggerIds=[1447], enable=False)
        self.set_skill(triggerIds=[1448], enable=False)
        self.set_skill(triggerIds=[1449], enable=False)
        self.set_skill(triggerIds=[1450], enable=False)
        self.set_skill(triggerIds=[1451], enable=False)
        self.set_skill(triggerIds=[1452], enable=False)
        self.set_skill(triggerIds=[1453], enable=False)
        self.set_skill(triggerIds=[1454], enable=False)
        self.set_skill(triggerIds=[1455], enable=False)
        self.set_skill(triggerIds=[1456], enable=False)
        self.set_skill(triggerIds=[1457], enable=False)
        self.set_skill(triggerIds=[1458], enable=False)
        self.set_skill(triggerIds=[1459], enable=False)
        self.set_skill(triggerIds=[1460], enable=False)
        self.set_skill(triggerIds=[1461], enable=False)
        self.set_skill(triggerIds=[1462], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬27(self.ctx)


class 스킬27(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1451], enable=True)
        self.set_skill(triggerIds=[1452], enable=True)
        self.set_skill(triggerIds=[1453], enable=True)
        self.set_skill(triggerIds=[1454], enable=True)
        self.set_skill(triggerIds=[1455], enable=True)
        self.set_skill(triggerIds=[1456], enable=True)
        self.set_skill(triggerIds=[1457], enable=True)
        self.set_skill(triggerIds=[1458], enable=True)
        self.set_skill(triggerIds=[1459], enable=True)
        self.set_skill(triggerIds=[1460], enable=True)
        self.set_skill(triggerIds=[1461], enable=True)
        self.set_skill(triggerIds=[1462], enable=True)
        self.set_skill(triggerIds=[1463], enable=True)
        self.set_skill(triggerIds=[1464], enable=True)
        self.set_skill(triggerIds=[1465], enable=True)
        self.set_skill(triggerIds=[1466], enable=True)
        self.set_skill(triggerIds=[1467], enable=True)
        self.set_skill(triggerIds=[1468], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬28대기(self.ctx)


class 스킬28대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1451], enable=False)
        self.set_skill(triggerIds=[1452], enable=False)
        self.set_skill(triggerIds=[1453], enable=False)
        self.set_skill(triggerIds=[1454], enable=False)
        self.set_skill(triggerIds=[1455], enable=False)
        self.set_skill(triggerIds=[1456], enable=False)
        self.set_skill(triggerIds=[1457], enable=False)
        self.set_skill(triggerIds=[1458], enable=False)
        self.set_skill(triggerIds=[1459], enable=False)
        self.set_skill(triggerIds=[1460], enable=False)
        self.set_skill(triggerIds=[1461], enable=False)
        self.set_skill(triggerIds=[1462], enable=False)
        self.set_skill(triggerIds=[1463], enable=False)
        self.set_skill(triggerIds=[1464], enable=False)
        self.set_skill(triggerIds=[1465], enable=False)
        self.set_skill(triggerIds=[1466], enable=False)
        self.set_skill(triggerIds=[1467], enable=False)
        self.set_skill(triggerIds=[1468], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬28(self.ctx)


class 스킬28(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1457], enable=True)
        self.set_skill(triggerIds=[1458], enable=True)
        self.set_skill(triggerIds=[1459], enable=True)
        self.set_skill(triggerIds=[1460], enable=True)
        self.set_skill(triggerIds=[1461], enable=True)
        self.set_skill(triggerIds=[1462], enable=True)
        self.set_skill(triggerIds=[1463], enable=True)
        self.set_skill(triggerIds=[1464], enable=True)
        self.set_skill(triggerIds=[1465], enable=True)
        self.set_skill(triggerIds=[1466], enable=True)
        self.set_skill(triggerIds=[1467], enable=True)
        self.set_skill(triggerIds=[1468], enable=True)
        self.set_skill(triggerIds=[1469], enable=True)
        self.set_skill(triggerIds=[1470], enable=True)
        self.set_skill(triggerIds=[1471], enable=True)
        self.set_skill(triggerIds=[1472], enable=True)
        self.set_skill(triggerIds=[1473], enable=True)
        self.set_skill(triggerIds=[1474], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬29대기(self.ctx)


class 스킬29대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1457], enable=False)
        self.set_skill(triggerIds=[1458], enable=False)
        self.set_skill(triggerIds=[1459], enable=False)
        self.set_skill(triggerIds=[1460], enable=False)
        self.set_skill(triggerIds=[1461], enable=False)
        self.set_skill(triggerIds=[1462], enable=False)
        self.set_skill(triggerIds=[1463], enable=False)
        self.set_skill(triggerIds=[1464], enable=False)
        self.set_skill(triggerIds=[1465], enable=False)
        self.set_skill(triggerIds=[1466], enable=False)
        self.set_skill(triggerIds=[1467], enable=False)
        self.set_skill(triggerIds=[1468], enable=False)
        self.set_skill(triggerIds=[1469], enable=False)
        self.set_skill(triggerIds=[1470], enable=False)
        self.set_skill(triggerIds=[1471], enable=False)
        self.set_skill(triggerIds=[1472], enable=False)
        self.set_skill(triggerIds=[1473], enable=False)
        self.set_skill(triggerIds=[1474], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬29(self.ctx)


class 스킬29(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1463], enable=True)
        self.set_skill(triggerIds=[1464], enable=True)
        self.set_skill(triggerIds=[1465], enable=True)
        self.set_skill(triggerIds=[1466], enable=True)
        self.set_skill(triggerIds=[1467], enable=True)
        self.set_skill(triggerIds=[1468], enable=True)
        self.set_skill(triggerIds=[1469], enable=True)
        self.set_skill(triggerIds=[1470], enable=True)
        self.set_skill(triggerIds=[1471], enable=True)
        self.set_skill(triggerIds=[1472], enable=True)
        self.set_skill(triggerIds=[1473], enable=True)
        self.set_skill(triggerIds=[1474], enable=True)
        self.set_skill(triggerIds=[1475], enable=True)
        self.set_skill(triggerIds=[1476], enable=True)
        self.set_skill(triggerIds=[1477], enable=True)
        self.set_skill(triggerIds=[1478], enable=True)
        self.set_skill(triggerIds=[1479], enable=True)
        self.set_skill(triggerIds=[1480], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬30대기(self.ctx)


class 스킬30대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1463], enable=False)
        self.set_skill(triggerIds=[1464], enable=False)
        self.set_skill(triggerIds=[1465], enable=False)
        self.set_skill(triggerIds=[1466], enable=False)
        self.set_skill(triggerIds=[1467], enable=False)
        self.set_skill(triggerIds=[1468], enable=False)
        self.set_skill(triggerIds=[1469], enable=False)
        self.set_skill(triggerIds=[1470], enable=False)
        self.set_skill(triggerIds=[1471], enable=False)
        self.set_skill(triggerIds=[1472], enable=False)
        self.set_skill(triggerIds=[1473], enable=False)
        self.set_skill(triggerIds=[1475], enable=False)
        self.set_skill(triggerIds=[1474], enable=False)
        self.set_skill(triggerIds=[1476], enable=False)
        self.set_skill(triggerIds=[1477], enable=False)
        self.set_skill(triggerIds=[1478], enable=False)
        self.set_skill(triggerIds=[1479], enable=False)
        self.set_skill(triggerIds=[1480], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬30(self.ctx)


class 스킬30(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1469], enable=True)
        self.set_skill(triggerIds=[1470], enable=True)
        self.set_skill(triggerIds=[1471], enable=True)
        self.set_skill(triggerIds=[1472], enable=True)
        self.set_skill(triggerIds=[1473], enable=True)
        self.set_skill(triggerIds=[1474], enable=True)
        self.set_skill(triggerIds=[1475], enable=True)
        self.set_skill(triggerIds=[1476], enable=True)
        self.set_skill(triggerIds=[1477], enable=True)
        self.set_skill(triggerIds=[1478], enable=True)
        self.set_skill(triggerIds=[1479], enable=True)
        self.set_skill(triggerIds=[1480], enable=True)
        self.set_skill(triggerIds=[1481], enable=True)
        self.set_skill(triggerIds=[1482], enable=True)
        self.set_skill(triggerIds=[1483], enable=True)
        self.set_skill(triggerIds=[1484], enable=True)
        self.set_skill(triggerIds=[1485], enable=True)
        self.set_skill(triggerIds=[1486], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬31대기(self.ctx)


class 스킬31대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1469], enable=False)
        self.set_skill(triggerIds=[1470], enable=False)
        self.set_skill(triggerIds=[1471], enable=False)
        self.set_skill(triggerIds=[1472], enable=False)
        self.set_skill(triggerIds=[1473], enable=False)
        self.set_skill(triggerIds=[1474], enable=False)
        self.set_skill(triggerIds=[1475], enable=False)
        self.set_skill(triggerIds=[1476], enable=False)
        self.set_skill(triggerIds=[1477], enable=False)
        self.set_skill(triggerIds=[1478], enable=False)
        self.set_skill(triggerIds=[1479], enable=False)
        self.set_skill(triggerIds=[1480], enable=False)
        self.set_skill(triggerIds=[1481], enable=False)
        self.set_skill(triggerIds=[1482], enable=False)
        self.set_skill(triggerIds=[1483], enable=False)
        self.set_skill(triggerIds=[1484], enable=False)
        self.set_skill(triggerIds=[1485], enable=False)
        self.set_skill(triggerIds=[1486], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬31(self.ctx)


class 스킬31(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1475], enable=True)
        self.set_skill(triggerIds=[1476], enable=True)
        self.set_skill(triggerIds=[1477], enable=True)
        self.set_skill(triggerIds=[1478], enable=True)
        self.set_skill(triggerIds=[1479], enable=True)
        self.set_skill(triggerIds=[1480], enable=True)
        self.set_skill(triggerIds=[1481], enable=True)
        self.set_skill(triggerIds=[1482], enable=True)
        self.set_skill(triggerIds=[1483], enable=True)
        self.set_skill(triggerIds=[1484], enable=True)
        self.set_skill(triggerIds=[1485], enable=True)
        self.set_skill(triggerIds=[1486], enable=True)
        self.set_skill(triggerIds=[1487], enable=True)
        self.set_skill(triggerIds=[1488], enable=True)
        self.set_skill(triggerIds=[1489], enable=True)
        self.set_skill(triggerIds=[1490], enable=True)
        self.set_skill(triggerIds=[1491], enable=True)
        self.set_skill(triggerIds=[1492], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬32대기(self.ctx)


class 스킬32대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1475], enable=False)
        self.set_skill(triggerIds=[1476], enable=False)
        self.set_skill(triggerIds=[1477], enable=False)
        self.set_skill(triggerIds=[1478], enable=False)
        self.set_skill(triggerIds=[1479], enable=False)
        self.set_skill(triggerIds=[1480], enable=False)
        self.set_skill(triggerIds=[1481], enable=False)
        self.set_skill(triggerIds=[1482], enable=False)
        self.set_skill(triggerIds=[1483], enable=False)
        self.set_skill(triggerIds=[1484], enable=False)
        self.set_skill(triggerIds=[1485], enable=False)
        self.set_skill(triggerIds=[1486], enable=False)
        self.set_skill(triggerIds=[1487], enable=False)
        self.set_skill(triggerIds=[1488], enable=False)
        self.set_skill(triggerIds=[1489], enable=False)
        self.set_skill(triggerIds=[1490], enable=False)
        self.set_skill(triggerIds=[1491], enable=False)
        self.set_skill(triggerIds=[1492], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬32(self.ctx)


class 스킬32(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1481], enable=True)
        self.set_skill(triggerIds=[1482], enable=True)
        self.set_skill(triggerIds=[1483], enable=True)
        self.set_skill(triggerIds=[1484], enable=True)
        self.set_skill(triggerIds=[1485], enable=True)
        self.set_skill(triggerIds=[1486], enable=True)
        self.set_skill(triggerIds=[1487], enable=True)
        self.set_skill(triggerIds=[1488], enable=True)
        self.set_skill(triggerIds=[1489], enable=True)
        self.set_skill(triggerIds=[1490], enable=True)
        self.set_skill(triggerIds=[1491], enable=True)
        self.set_skill(triggerIds=[1492], enable=True)
        self.set_skill(triggerIds=[1493], enable=True)
        self.set_skill(triggerIds=[1494], enable=True)
        self.set_skill(triggerIds=[1495], enable=True)
        self.set_skill(triggerIds=[1496], enable=True)
        self.set_skill(triggerIds=[1497], enable=True)
        self.set_skill(triggerIds=[1498], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬33대기(self.ctx)


class 스킬33대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1481], enable=False)
        self.set_skill(triggerIds=[1482], enable=False)
        self.set_skill(triggerIds=[1483], enable=False)
        self.set_skill(triggerIds=[1484], enable=False)
        self.set_skill(triggerIds=[1485], enable=False)
        self.set_skill(triggerIds=[1486], enable=False)
        self.set_skill(triggerIds=[1487], enable=False)
        self.set_skill(triggerIds=[1488], enable=False)
        self.set_skill(triggerIds=[1489], enable=False)
        self.set_skill(triggerIds=[1490], enable=False)
        self.set_skill(triggerIds=[1491], enable=False)
        self.set_skill(triggerIds=[1492], enable=False)
        self.set_skill(triggerIds=[1493], enable=False)
        self.set_skill(triggerIds=[1494], enable=False)
        self.set_skill(triggerIds=[1495], enable=False)
        self.set_skill(triggerIds=[1496], enable=False)
        self.set_skill(triggerIds=[1497], enable=False)
        self.set_skill(triggerIds=[1498], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬33(self.ctx)


class 스킬33(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[1487], enable=True)
        self.set_skill(triggerIds=[1488], enable=True)
        self.set_skill(triggerIds=[1489], enable=True)
        self.set_skill(triggerIds=[1490], enable=True)
        self.set_skill(triggerIds=[1491], enable=True)
        self.set_skill(triggerIds=[1492], enable=True)
        self.set_skill(triggerIds=[1493], enable=True)
        self.set_skill(triggerIds=[1494], enable=True)
        self.set_skill(triggerIds=[1495], enable=True)
        self.set_skill(triggerIds=[1496], enable=True)
        self.set_skill(triggerIds=[1497], enable=True)
        self.set_skill(triggerIds=[1498], enable=True)
        self.set_skill(triggerIds=[1499], enable=True)
        self.set_skill(triggerIds=[1500], enable=True)
        self.set_skill(triggerIds=[1501], enable=True)
        self.set_skill(triggerIds=[1502], enable=True)
        self.set_skill(triggerIds=[1503], enable=True)
        self.set_skill(triggerIds=[1504], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 스킬34대기(self.ctx)


class 스킬34대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1487], enable=False)
        self.set_skill(triggerIds=[1488], enable=False)
        self.set_skill(triggerIds=[1489], enable=False)
        self.set_skill(triggerIds=[1490], enable=False)
        self.set_skill(triggerIds=[1491], enable=False)
        self.set_skill(triggerIds=[1492], enable=False)
        self.set_skill(triggerIds=[1493], enable=False)
        self.set_skill(triggerIds=[1494], enable=False)
        self.set_skill(triggerIds=[1495], enable=False)
        self.set_skill(triggerIds=[1496], enable=False)
        self.set_skill(triggerIds=[1497], enable=False)
        self.set_skill(triggerIds=[1498], enable=False)
        self.set_skill(triggerIds=[1499], enable=False)
        self.set_skill(triggerIds=[1500], enable=False)
        self.set_skill(triggerIds=[1501], enable=False)
        self.set_skill(triggerIds=[1502], enable=False)
        self.set_skill(triggerIds=[1503], enable=False)
        self.set_skill(triggerIds=[1504], enable=False)


initial_state = 대기
