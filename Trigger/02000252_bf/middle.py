""" trigger/02000252_bf/middle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8201], visible=False)
        self.set_effect(trigger_ids=[8202], visible=False)
        self.set_effect(trigger_ids=[8203], visible=False)
        self.set_effect(trigger_ids=[8204], visible=False)
        self.set_effect(trigger_ids=[8205], visible=False)
        self.set_effect(trigger_ids=[8206], visible=False)
        self.set_effect(trigger_ids=[8207], visible=False)
        self.set_effect(trigger_ids=[8208], visible=False)
        self.set_effect(trigger_ids=[8209], visible=False)
        self.set_effect(trigger_ids=[8210], visible=False)
        self.set_effect(trigger_ids=[8211], visible=False)
        self.set_effect(trigger_ids=[8212], visible=False)
        self.set_effect(trigger_ids=[8213], visible=False)
        self.set_effect(trigger_ids=[8214], visible=False)
        self.set_effect(trigger_ids=[8215], visible=False)
        self.set_effect(trigger_ids=[8216], visible=False)
        self.set_effect(trigger_ids=[8217], visible=False)
        self.set_effect(trigger_ids=[8218], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=902, min_users='1'):
            return 바닥삭제(self.ctx)


class 바닥삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=5)
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142], visible=False, start_delay=0, interval=100)
        self.spawn_monster(spawn_ids=[1075], auto_target=False)
        self.spawn_monster(spawn_ids=[1076], auto_target=False)
        self.spawn_monster(spawn_ids=[1077], auto_target=False)
        self.spawn_monster(spawn_ids=[1078], auto_target=False)
        self.spawn_monster(spawn_ids=[1079], auto_target=False)
        self.spawn_monster(spawn_ids=[1080], auto_target=False)
        self.spawn_monster(spawn_ids=[1081], auto_target=False)
        self.spawn_monster(spawn_ids=[1082], auto_target=False)
        self.spawn_monster(spawn_ids=[1083], auto_target=False)
        self.spawn_monster(spawn_ids=[1084], auto_target=False)
        self.spawn_monster(spawn_ids=[1085], auto_target=False)
        self.spawn_monster(spawn_ids=[1086], auto_target=False)
        self.spawn_monster(spawn_ids=[1087], auto_target=False)
        self.spawn_monster(spawn_ids=[1088], auto_target=False)
        self.spawn_monster(spawn_ids=[1089], auto_target=False)
        self.spawn_monster(spawn_ids=[1090], auto_target=False)
        self.spawn_monster(spawn_ids=[1091], auto_target=False)
        self.spawn_monster(spawn_ids=[1092], auto_target=False)
        self.spawn_monster(spawn_ids=[1093], auto_target=False)
        self.spawn_monster(spawn_ids=[1094], auto_target=False)
        self.set_effect(trigger_ids=[8201], visible=True)
        self.set_effect(trigger_ids=[8202], visible=True)
        self.set_effect(trigger_ids=[8203], visible=True)
        self.set_effect(trigger_ids=[8204], visible=True)
        self.set_effect(trigger_ids=[8205], visible=True)
        self.set_effect(trigger_ids=[8206], visible=True)
        self.set_effect(trigger_ids=[8207], visible=True)
        self.set_effect(trigger_ids=[8208], visible=True)
        self.set_effect(trigger_ids=[8209], visible=True)
        self.set_effect(trigger_ids=[8210], visible=True)
        self.set_effect(trigger_ids=[8211], visible=True)
        self.set_effect(trigger_ids=[8212], visible=True)
        self.set_effect(trigger_ids=[8213], visible=True)
        self.set_effect(trigger_ids=[8214], visible=True)
        self.set_effect(trigger_ids=[8215], visible=True)
        self.set_effect(trigger_ids=[8216], visible=True)
        self.set_effect(trigger_ids=[8217], visible=True)
        self.set_effect(trigger_ids=[8218], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 스킬01(self.ctx)


class 스킬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[8201], visible=False)
        self.set_effect(trigger_ids=[8202], visible=False)
        self.set_effect(trigger_ids=[8203], visible=False)
        self.set_effect(trigger_ids=[8204], visible=False)
        self.set_effect(trigger_ids=[8205], visible=False)
        self.set_effect(trigger_ids=[8206], visible=False)
        self.set_effect(trigger_ids=[8207], visible=False)
        self.set_effect(trigger_ids=[8208], visible=False)
        self.set_effect(trigger_ids=[8209], visible=False)
        self.set_effect(trigger_ids=[8210], visible=False)
        self.set_effect(trigger_ids=[8211], visible=False)
        self.set_effect(trigger_ids=[8212], visible=False)
        self.set_effect(trigger_ids=[8213], visible=False)
        self.set_effect(trigger_ids=[8214], visible=False)
        self.set_effect(trigger_ids=[8215], visible=False)
        self.set_effect(trigger_ids=[8216], visible=False)
        self.set_effect(trigger_ids=[8217], visible=False)
        self.set_effect(trigger_ids=[8218], visible=False)
        self.set_skill(trigger_ids=[1301], enable=True)
        self.set_skill(trigger_ids=[1302], enable=True)
        self.set_skill(trigger_ids=[1303], enable=True)
        self.set_skill(trigger_ids=[1304], enable=True)
        self.set_skill(trigger_ids=[1305], enable=True)
        self.set_skill(trigger_ids=[1306], enable=True)
        self.set_skill(trigger_ids=[1307], enable=True)
        self.set_skill(trigger_ids=[1308], enable=True)
        self.set_skill(trigger_ids=[1309], enable=True)
        self.set_skill(trigger_ids=[1310], enable=True)
        self.set_skill(trigger_ids=[1311], enable=True)
        self.set_skill(trigger_ids=[1312], enable=True)
        self.set_skill(trigger_ids=[1313], enable=True)
        self.set_skill(trigger_ids=[1314], enable=True)
        self.set_skill(trigger_ids=[1315], enable=True)
        self.set_skill(trigger_ids=[1316], enable=True)
        self.set_skill(trigger_ids=[1317], enable=True)
        self.set_skill(trigger_ids=[1318], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬02대기(self.ctx)


class 스킬02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1301], enable=False)
        self.set_skill(trigger_ids=[1302], enable=False)
        self.set_skill(trigger_ids=[1303], enable=False)
        self.set_skill(trigger_ids=[1304], enable=False)
        self.set_skill(trigger_ids=[1305], enable=False)
        self.set_skill(trigger_ids=[1306], enable=False)
        self.set_skill(trigger_ids=[1307], enable=False)
        self.set_skill(trigger_ids=[1308], enable=False)
        self.set_skill(trigger_ids=[1309], enable=False)
        self.set_skill(trigger_ids=[1310], enable=False)
        self.set_skill(trigger_ids=[1311], enable=False)
        self.set_skill(trigger_ids=[1312], enable=False)
        self.set_skill(trigger_ids=[1313], enable=False)
        self.set_skill(trigger_ids=[1314], enable=False)
        self.set_skill(trigger_ids=[1315], enable=False)
        self.set_skill(trigger_ids=[1316], enable=False)
        self.set_skill(trigger_ids=[1317], enable=False)
        self.set_skill(trigger_ids=[1318], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬02(self.ctx)


class 스킬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1307], enable=True)
        self.set_skill(trigger_ids=[1308], enable=True)
        self.set_skill(trigger_ids=[1309], enable=True)
        self.set_skill(trigger_ids=[1310], enable=True)
        self.set_skill(trigger_ids=[1311], enable=True)
        self.set_skill(trigger_ids=[1312], enable=True)
        self.set_skill(trigger_ids=[1313], enable=True)
        self.set_skill(trigger_ids=[1314], enable=True)
        self.set_skill(trigger_ids=[1315], enable=True)
        self.set_skill(trigger_ids=[1316], enable=True)
        self.set_skill(trigger_ids=[1317], enable=True)
        self.set_skill(trigger_ids=[1318], enable=True)
        self.set_skill(trigger_ids=[1319], enable=True)
        self.set_skill(trigger_ids=[1320], enable=True)
        self.set_skill(trigger_ids=[1321], enable=True)
        self.set_skill(trigger_ids=[1322], enable=True)
        self.set_skill(trigger_ids=[1323], enable=True)
        self.set_skill(trigger_ids=[1324], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬03대기(self.ctx)


class 스킬03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1307], enable=False)
        self.set_skill(trigger_ids=[1308], enable=False)
        self.set_skill(trigger_ids=[1309], enable=False)
        self.set_skill(trigger_ids=[1310], enable=False)
        self.set_skill(trigger_ids=[1311], enable=False)
        self.set_skill(trigger_ids=[1312], enable=False)
        self.set_skill(trigger_ids=[1313], enable=False)
        self.set_skill(trigger_ids=[1314], enable=False)
        self.set_skill(trigger_ids=[1315], enable=False)
        self.set_skill(trigger_ids=[1316], enable=False)
        self.set_skill(trigger_ids=[1317], enable=False)
        self.set_skill(trigger_ids=[1318], enable=False)
        self.set_skill(trigger_ids=[1319], enable=False)
        self.set_skill(trigger_ids=[1320], enable=False)
        self.set_skill(trigger_ids=[1321], enable=False)
        self.set_skill(trigger_ids=[1322], enable=False)
        self.set_skill(trigger_ids=[1323], enable=False)
        self.set_skill(trigger_ids=[1324], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬03(self.ctx)


class 스킬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1313], enable=True)
        self.set_skill(trigger_ids=[1314], enable=True)
        self.set_skill(trigger_ids=[1315], enable=True)
        self.set_skill(trigger_ids=[1316], enable=True)
        self.set_skill(trigger_ids=[1317], enable=True)
        self.set_skill(trigger_ids=[1318], enable=True)
        self.set_skill(trigger_ids=[1319], enable=True)
        self.set_skill(trigger_ids=[1320], enable=True)
        self.set_skill(trigger_ids=[1321], enable=True)
        self.set_skill(trigger_ids=[1322], enable=True)
        self.set_skill(trigger_ids=[1323], enable=True)
        self.set_skill(trigger_ids=[1324], enable=True)
        self.set_skill(trigger_ids=[1325], enable=True)
        self.set_skill(trigger_ids=[1326], enable=True)
        self.set_skill(trigger_ids=[1327], enable=True)
        self.set_skill(trigger_ids=[1328], enable=True)
        self.set_skill(trigger_ids=[1328], enable=True)
        self.set_skill(trigger_ids=[1330], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬04대기(self.ctx)


class 스킬04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1313], enable=False)
        self.set_skill(trigger_ids=[1314], enable=False)
        self.set_skill(trigger_ids=[1315], enable=False)
        self.set_skill(trigger_ids=[1316], enable=False)
        self.set_skill(trigger_ids=[1317], enable=False)
        self.set_skill(trigger_ids=[1318], enable=False)
        self.set_skill(trigger_ids=[1319], enable=False)
        self.set_skill(trigger_ids=[1320], enable=False)
        self.set_skill(trigger_ids=[1321], enable=False)
        self.set_skill(trigger_ids=[1322], enable=False)
        self.set_skill(trigger_ids=[1323], enable=False)
        self.set_skill(trigger_ids=[1324], enable=False)
        self.set_skill(trigger_ids=[1325], enable=False)
        self.set_skill(trigger_ids=[1326], enable=False)
        self.set_skill(trigger_ids=[1327], enable=False)
        self.set_skill(trigger_ids=[1328], enable=False)
        self.set_skill(trigger_ids=[1328], enable=False)
        self.set_skill(trigger_ids=[1330], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬04(self.ctx)


class 스킬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1319], enable=True)
        self.set_skill(trigger_ids=[1320], enable=True)
        self.set_skill(trigger_ids=[1321], enable=True)
        self.set_skill(trigger_ids=[1322], enable=True)
        self.set_skill(trigger_ids=[1323], enable=True)
        self.set_skill(trigger_ids=[1324], enable=True)
        self.set_skill(trigger_ids=[1325], enable=True)
        self.set_skill(trigger_ids=[1326], enable=True)
        self.set_skill(trigger_ids=[1327], enable=True)
        self.set_skill(trigger_ids=[1328], enable=True)
        self.set_skill(trigger_ids=[1328], enable=True)
        self.set_skill(trigger_ids=[1330], enable=True)
        self.set_skill(trigger_ids=[1331], enable=True)
        self.set_skill(trigger_ids=[1332], enable=True)
        self.set_skill(trigger_ids=[1333], enable=True)
        self.set_skill(trigger_ids=[1334], enable=True)
        self.set_skill(trigger_ids=[1335], enable=True)
        self.set_skill(trigger_ids=[1336], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬05대기(self.ctx)


class 스킬05대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1319], enable=False)
        self.set_skill(trigger_ids=[1320], enable=False)
        self.set_skill(trigger_ids=[1321], enable=False)
        self.set_skill(trigger_ids=[1322], enable=False)
        self.set_skill(trigger_ids=[1323], enable=False)
        self.set_skill(trigger_ids=[1324], enable=False)
        self.set_skill(trigger_ids=[1325], enable=False)
        self.set_skill(trigger_ids=[1326], enable=False)
        self.set_skill(trigger_ids=[1327], enable=False)
        self.set_skill(trigger_ids=[1328], enable=False)
        self.set_skill(trigger_ids=[1328], enable=False)
        self.set_skill(trigger_ids=[1330], enable=False)
        self.set_skill(trigger_ids=[1331], enable=False)
        self.set_skill(trigger_ids=[1332], enable=False)
        self.set_skill(trigger_ids=[1333], enable=False)
        self.set_skill(trigger_ids=[1334], enable=False)
        self.set_skill(trigger_ids=[1335], enable=False)
        self.set_skill(trigger_ids=[1336], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬05(self.ctx)


class 스킬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1325], enable=True)
        self.set_skill(trigger_ids=[1326], enable=True)
        self.set_skill(trigger_ids=[1327], enable=True)
        self.set_skill(trigger_ids=[1328], enable=True)
        self.set_skill(trigger_ids=[1328], enable=True)
        self.set_skill(trigger_ids=[1330], enable=True)
        self.set_skill(trigger_ids=[1331], enable=True)
        self.set_skill(trigger_ids=[1332], enable=True)
        self.set_skill(trigger_ids=[1333], enable=True)
        self.set_skill(trigger_ids=[1334], enable=True)
        self.set_skill(trigger_ids=[1335], enable=True)
        self.set_skill(trigger_ids=[1336], enable=True)
        self.set_skill(trigger_ids=[1337], enable=True)
        self.set_skill(trigger_ids=[1338], enable=True)
        self.set_skill(trigger_ids=[1339], enable=True)
        self.set_skill(trigger_ids=[1340], enable=True)
        self.set_skill(trigger_ids=[1341], enable=True)
        self.set_skill(trigger_ids=[1342], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬06대기(self.ctx)


class 스킬06대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1325], enable=False)
        self.set_skill(trigger_ids=[1326], enable=False)
        self.set_skill(trigger_ids=[1327], enable=False)
        self.set_skill(trigger_ids=[1328], enable=False)
        self.set_skill(trigger_ids=[1328], enable=False)
        self.set_skill(trigger_ids=[1330], enable=False)
        self.set_skill(trigger_ids=[1331], enable=False)
        self.set_skill(trigger_ids=[1332], enable=False)
        self.set_skill(trigger_ids=[1333], enable=False)
        self.set_skill(trigger_ids=[1334], enable=False)
        self.set_skill(trigger_ids=[1335], enable=False)
        self.set_skill(trigger_ids=[1336], enable=False)
        self.set_skill(trigger_ids=[1337], enable=False)
        self.set_skill(trigger_ids=[1338], enable=False)
        self.set_skill(trigger_ids=[1339], enable=False)
        self.set_skill(trigger_ids=[1340], enable=False)
        self.set_skill(trigger_ids=[1341], enable=False)
        self.set_skill(trigger_ids=[1342], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬06(self.ctx)


class 스킬06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1331], enable=True)
        self.set_skill(trigger_ids=[1332], enable=True)
        self.set_skill(trigger_ids=[1333], enable=True)
        self.set_skill(trigger_ids=[1334], enable=True)
        self.set_skill(trigger_ids=[1335], enable=True)
        self.set_skill(trigger_ids=[1336], enable=True)
        self.set_skill(trigger_ids=[1337], enable=True)
        self.set_skill(trigger_ids=[1338], enable=True)
        self.set_skill(trigger_ids=[1339], enable=True)
        self.set_skill(trigger_ids=[1340], enable=True)
        self.set_skill(trigger_ids=[1341], enable=True)
        self.set_skill(trigger_ids=[1342], enable=True)
        self.set_skill(trigger_ids=[1343], enable=True)
        self.set_skill(trigger_ids=[1344], enable=True)
        self.set_skill(trigger_ids=[1345], enable=True)
        self.set_skill(trigger_ids=[1346], enable=True)
        self.set_skill(trigger_ids=[1347], enable=True)
        self.set_skill(trigger_ids=[1348], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬07대기(self.ctx)


class 스킬07대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1331], enable=False)
        self.set_skill(trigger_ids=[1332], enable=False)
        self.set_skill(trigger_ids=[1333], enable=False)
        self.set_skill(trigger_ids=[1334], enable=False)
        self.set_skill(trigger_ids=[1335], enable=False)
        self.set_skill(trigger_ids=[1336], enable=False)
        self.set_skill(trigger_ids=[1337], enable=False)
        self.set_skill(trigger_ids=[1338], enable=False)
        self.set_skill(trigger_ids=[1339], enable=False)
        self.set_skill(trigger_ids=[1340], enable=False)
        self.set_skill(trigger_ids=[1341], enable=False)
        self.set_skill(trigger_ids=[1342], enable=False)
        self.set_skill(trigger_ids=[1343], enable=False)
        self.set_skill(trigger_ids=[1344], enable=False)
        self.set_skill(trigger_ids=[1345], enable=False)
        self.set_skill(trigger_ids=[1346], enable=False)
        self.set_skill(trigger_ids=[1347], enable=False)
        self.set_skill(trigger_ids=[1348], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬07(self.ctx)


class 스킬07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1337], enable=True)
        self.set_skill(trigger_ids=[1338], enable=True)
        self.set_skill(trigger_ids=[1339], enable=True)
        self.set_skill(trigger_ids=[1340], enable=True)
        self.set_skill(trigger_ids=[1341], enable=True)
        self.set_skill(trigger_ids=[1342], enable=True)
        self.set_skill(trigger_ids=[1343], enable=True)
        self.set_skill(trigger_ids=[1344], enable=True)
        self.set_skill(trigger_ids=[1345], enable=True)
        self.set_skill(trigger_ids=[1346], enable=True)
        self.set_skill(trigger_ids=[1347], enable=True)
        self.set_skill(trigger_ids=[1348], enable=True)
        self.set_skill(trigger_ids=[1349], enable=True)
        self.set_skill(trigger_ids=[1350], enable=True)
        self.set_skill(trigger_ids=[1351], enable=True)
        self.set_skill(trigger_ids=[1352], enable=True)
        self.set_skill(trigger_ids=[1353], enable=True)
        self.set_skill(trigger_ids=[1354], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬08대기(self.ctx)


class 스킬08대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1337], enable=False)
        self.set_skill(trigger_ids=[1338], enable=False)
        self.set_skill(trigger_ids=[1339], enable=False)
        self.set_skill(trigger_ids=[1340], enable=False)
        self.set_skill(trigger_ids=[1341], enable=False)
        self.set_skill(trigger_ids=[1342], enable=False)
        self.set_skill(trigger_ids=[1343], enable=False)
        self.set_skill(trigger_ids=[1344], enable=False)
        self.set_skill(trigger_ids=[1345], enable=False)
        self.set_skill(trigger_ids=[1346], enable=False)
        self.set_skill(trigger_ids=[1347], enable=False)
        self.set_skill(trigger_ids=[1348], enable=False)
        self.set_skill(trigger_ids=[1349], enable=False)
        self.set_skill(trigger_ids=[1350], enable=False)
        self.set_skill(trigger_ids=[1351], enable=False)
        self.set_skill(trigger_ids=[1352], enable=False)
        self.set_skill(trigger_ids=[1353], enable=False)
        self.set_skill(trigger_ids=[1354], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬08(self.ctx)


class 스킬08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1343], enable=True)
        self.set_skill(trigger_ids=[1344], enable=True)
        self.set_skill(trigger_ids=[1345], enable=True)
        self.set_skill(trigger_ids=[1346], enable=True)
        self.set_skill(trigger_ids=[1347], enable=True)
        self.set_skill(trigger_ids=[1348], enable=True)
        self.set_skill(trigger_ids=[1349], enable=True)
        self.set_skill(trigger_ids=[1350], enable=True)
        self.set_skill(trigger_ids=[1351], enable=True)
        self.set_skill(trigger_ids=[1352], enable=True)
        self.set_skill(trigger_ids=[1353], enable=True)
        self.set_skill(trigger_ids=[1354], enable=True)
        self.set_skill(trigger_ids=[1355], enable=True)
        self.set_skill(trigger_ids=[1356], enable=True)
        self.set_skill(trigger_ids=[1357], enable=True)
        self.set_skill(trigger_ids=[1358], enable=True)
        self.set_skill(trigger_ids=[1359], enable=True)
        self.set_skill(trigger_ids=[1360], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬09대기(self.ctx)


class 스킬09대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1343], enable=False)
        self.set_skill(trigger_ids=[1344], enable=False)
        self.set_skill(trigger_ids=[1345], enable=False)
        self.set_skill(trigger_ids=[1346], enable=False)
        self.set_skill(trigger_ids=[1347], enable=False)
        self.set_skill(trigger_ids=[1348], enable=False)
        self.set_skill(trigger_ids=[1349], enable=False)
        self.set_skill(trigger_ids=[1350], enable=False)
        self.set_skill(trigger_ids=[1351], enable=False)
        self.set_skill(trigger_ids=[1352], enable=False)
        self.set_skill(trigger_ids=[1353], enable=False)
        self.set_skill(trigger_ids=[1354], enable=False)
        self.set_skill(trigger_ids=[1355], enable=False)
        self.set_skill(trigger_ids=[1356], enable=False)
        self.set_skill(trigger_ids=[1357], enable=False)
        self.set_skill(trigger_ids=[1358], enable=False)
        self.set_skill(trigger_ids=[1359], enable=False)
        self.set_skill(trigger_ids=[1360], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬09(self.ctx)


class 스킬09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1349], enable=True)
        self.set_skill(trigger_ids=[1350], enable=True)
        self.set_skill(trigger_ids=[1351], enable=True)
        self.set_skill(trigger_ids=[1352], enable=True)
        self.set_skill(trigger_ids=[1353], enable=True)
        self.set_skill(trigger_ids=[1354], enable=True)
        self.set_skill(trigger_ids=[1355], enable=True)
        self.set_skill(trigger_ids=[1356], enable=True)
        self.set_skill(trigger_ids=[1357], enable=True)
        self.set_skill(trigger_ids=[1358], enable=True)
        self.set_skill(trigger_ids=[1359], enable=True)
        self.set_skill(trigger_ids=[1360], enable=True)
        self.set_skill(trigger_ids=[1361], enable=True)
        self.set_skill(trigger_ids=[1362], enable=True)
        self.set_skill(trigger_ids=[1363], enable=True)
        self.set_skill(trigger_ids=[1364], enable=True)
        self.set_skill(trigger_ids=[1365], enable=True)
        self.set_skill(trigger_ids=[1366], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬10대기(self.ctx)


class 스킬10대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1349], enable=False)
        self.set_skill(trigger_ids=[1350], enable=False)
        self.set_skill(trigger_ids=[1351], enable=False)
        self.set_skill(trigger_ids=[1352], enable=False)
        self.set_skill(trigger_ids=[1353], enable=False)
        self.set_skill(trigger_ids=[1354], enable=False)
        self.set_skill(trigger_ids=[1355], enable=False)
        self.set_skill(trigger_ids=[1356], enable=False)
        self.set_skill(trigger_ids=[1357], enable=False)
        self.set_skill(trigger_ids=[1358], enable=False)
        self.set_skill(trigger_ids=[1359], enable=False)
        self.set_skill(trigger_ids=[1360], enable=False)
        self.set_skill(trigger_ids=[1361], enable=False)
        self.set_skill(trigger_ids=[1362], enable=False)
        self.set_skill(trigger_ids=[1363], enable=False)
        self.set_skill(trigger_ids=[1364], enable=False)
        self.set_skill(trigger_ids=[1365], enable=False)
        self.set_skill(trigger_ids=[1366], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬10(self.ctx)


class 스킬10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1355], enable=True)
        self.set_skill(trigger_ids=[1356], enable=True)
        self.set_skill(trigger_ids=[1357], enable=True)
        self.set_skill(trigger_ids=[1358], enable=True)
        self.set_skill(trigger_ids=[1359], enable=True)
        self.set_skill(trigger_ids=[1360], enable=True)
        self.set_skill(trigger_ids=[1361], enable=True)
        self.set_skill(trigger_ids=[1362], enable=True)
        self.set_skill(trigger_ids=[1363], enable=True)
        self.set_skill(trigger_ids=[1364], enable=True)
        self.set_skill(trigger_ids=[1365], enable=True)
        self.set_skill(trigger_ids=[1366], enable=True)
        self.set_skill(trigger_ids=[1367], enable=True)
        self.set_skill(trigger_ids=[1368], enable=True)
        self.set_skill(trigger_ids=[1369], enable=True)
        self.set_skill(trigger_ids=[1370], enable=True)
        self.set_skill(trigger_ids=[1371], enable=True)
        self.set_skill(trigger_ids=[1372], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬11대기(self.ctx)


class 스킬11대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1355], enable=False)
        self.set_skill(trigger_ids=[1356], enable=False)
        self.set_skill(trigger_ids=[1357], enable=False)
        self.set_skill(trigger_ids=[1358], enable=False)
        self.set_skill(trigger_ids=[1359], enable=False)
        self.set_skill(trigger_ids=[1360], enable=False)
        self.set_skill(trigger_ids=[1361], enable=False)
        self.set_skill(trigger_ids=[1362], enable=False)
        self.set_skill(trigger_ids=[1363], enable=False)
        self.set_skill(trigger_ids=[1364], enable=False)
        self.set_skill(trigger_ids=[1365], enable=False)
        self.set_skill(trigger_ids=[1366], enable=False)
        self.set_skill(trigger_ids=[1367], enable=False)
        self.set_skill(trigger_ids=[1368], enable=False)
        self.set_skill(trigger_ids=[1369], enable=False)
        self.set_skill(trigger_ids=[1370], enable=False)
        self.set_skill(trigger_ids=[1371], enable=False)
        self.set_skill(trigger_ids=[1372], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬11(self.ctx)


class 스킬11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1361], enable=True)
        self.set_skill(trigger_ids=[1362], enable=True)
        self.set_skill(trigger_ids=[1363], enable=True)
        self.set_skill(trigger_ids=[1364], enable=True)
        self.set_skill(trigger_ids=[1365], enable=True)
        self.set_skill(trigger_ids=[1366], enable=True)
        self.set_skill(trigger_ids=[1367], enable=True)
        self.set_skill(trigger_ids=[1368], enable=True)
        self.set_skill(trigger_ids=[1369], enable=True)
        self.set_skill(trigger_ids=[1370], enable=True)
        self.set_skill(trigger_ids=[1371], enable=True)
        self.set_skill(trigger_ids=[1372], enable=True)
        self.set_skill(trigger_ids=[1373], enable=True)
        self.set_skill(trigger_ids=[1374], enable=True)
        self.set_skill(trigger_ids=[1375], enable=True)
        self.set_skill(trigger_ids=[1376], enable=True)
        self.set_skill(trigger_ids=[1377], enable=True)
        self.set_skill(trigger_ids=[1378], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬12대기(self.ctx)


class 스킬12대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1361], enable=False)
        self.set_skill(trigger_ids=[1362], enable=False)
        self.set_skill(trigger_ids=[1363], enable=False)
        self.set_skill(trigger_ids=[1364], enable=False)
        self.set_skill(trigger_ids=[1365], enable=False)
        self.set_skill(trigger_ids=[1366], enable=False)
        self.set_skill(trigger_ids=[1367], enable=False)
        self.set_skill(trigger_ids=[1368], enable=False)
        self.set_skill(trigger_ids=[1369], enable=False)
        self.set_skill(trigger_ids=[1370], enable=False)
        self.set_skill(trigger_ids=[1371], enable=False)
        self.set_skill(trigger_ids=[1372], enable=False)
        self.set_skill(trigger_ids=[1373], enable=False)
        self.set_skill(trigger_ids=[1374], enable=False)
        self.set_skill(trigger_ids=[1375], enable=False)
        self.set_skill(trigger_ids=[1376], enable=False)
        self.set_skill(trigger_ids=[1377], enable=False)
        self.set_skill(trigger_ids=[1378], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬12(self.ctx)


class 스킬12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1367], enable=True)
        self.set_skill(trigger_ids=[1368], enable=True)
        self.set_skill(trigger_ids=[1369], enable=True)
        self.set_skill(trigger_ids=[1370], enable=True)
        self.set_skill(trigger_ids=[1371], enable=True)
        self.set_skill(trigger_ids=[1372], enable=True)
        self.set_skill(trigger_ids=[1373], enable=True)
        self.set_skill(trigger_ids=[1374], enable=True)
        self.set_skill(trigger_ids=[1375], enable=True)
        self.set_skill(trigger_ids=[1376], enable=True)
        self.set_skill(trigger_ids=[1377], enable=True)
        self.set_skill(trigger_ids=[1378], enable=True)
        self.set_skill(trigger_ids=[1379], enable=True)
        self.set_skill(trigger_ids=[1380], enable=True)
        self.set_skill(trigger_ids=[1381], enable=True)
        self.set_skill(trigger_ids=[1382], enable=True)
        self.set_skill(trigger_ids=[1383], enable=True)
        self.set_skill(trigger_ids=[1384], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬13대기(self.ctx)


class 스킬13대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1367], enable=False)
        self.set_skill(trigger_ids=[1368], enable=False)
        self.set_skill(trigger_ids=[1369], enable=False)
        self.set_skill(trigger_ids=[1370], enable=False)
        self.set_skill(trigger_ids=[1371], enable=False)
        self.set_skill(trigger_ids=[1372], enable=False)
        self.set_skill(trigger_ids=[1373], enable=False)
        self.set_skill(trigger_ids=[1374], enable=False)
        self.set_skill(trigger_ids=[1375], enable=False)
        self.set_skill(trigger_ids=[1376], enable=False)
        self.set_skill(trigger_ids=[1377], enable=False)
        self.set_skill(trigger_ids=[1378], enable=False)
        self.set_skill(trigger_ids=[1379], enable=False)
        self.set_skill(trigger_ids=[1380], enable=False)
        self.set_skill(trigger_ids=[1381], enable=False)
        self.set_skill(trigger_ids=[1382], enable=False)
        self.set_skill(trigger_ids=[1383], enable=False)
        self.set_skill(trigger_ids=[1384], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬13(self.ctx)


class 스킬13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1373], enable=True)
        self.set_skill(trigger_ids=[1374], enable=True)
        self.set_skill(trigger_ids=[1375], enable=True)
        self.set_skill(trigger_ids=[1376], enable=True)
        self.set_skill(trigger_ids=[1377], enable=True)
        self.set_skill(trigger_ids=[1378], enable=True)
        self.set_skill(trigger_ids=[1379], enable=True)
        self.set_skill(trigger_ids=[1380], enable=True)
        self.set_skill(trigger_ids=[1381], enable=True)
        self.set_skill(trigger_ids=[1382], enable=True)
        self.set_skill(trigger_ids=[1383], enable=True)
        self.set_skill(trigger_ids=[1384], enable=True)
        self.set_skill(trigger_ids=[1385], enable=True)
        self.set_skill(trigger_ids=[1386], enable=True)
        self.set_skill(trigger_ids=[1387], enable=True)
        self.set_skill(trigger_ids=[1388], enable=True)
        self.set_skill(trigger_ids=[1389], enable=True)
        self.set_skill(trigger_ids=[1390], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬14대기(self.ctx)


class 스킬14대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1373], enable=False)
        self.set_skill(trigger_ids=[1374], enable=False)
        self.set_skill(trigger_ids=[1375], enable=False)
        self.set_skill(trigger_ids=[1376], enable=False)
        self.set_skill(trigger_ids=[1377], enable=False)
        self.set_skill(trigger_ids=[1378], enable=False)
        self.set_skill(trigger_ids=[1379], enable=False)
        self.set_skill(trigger_ids=[1380], enable=False)
        self.set_skill(trigger_ids=[1381], enable=False)
        self.set_skill(trigger_ids=[1382], enable=False)
        self.set_skill(trigger_ids=[1383], enable=False)
        self.set_skill(trigger_ids=[1384], enable=False)
        self.set_skill(trigger_ids=[1385], enable=False)
        self.set_skill(trigger_ids=[1386], enable=False)
        self.set_skill(trigger_ids=[1387], enable=False)
        self.set_skill(trigger_ids=[1388], enable=False)
        self.set_skill(trigger_ids=[1389], enable=False)
        self.set_skill(trigger_ids=[1390], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬14(self.ctx)


class 스킬14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1379], enable=True)
        self.set_skill(trigger_ids=[1380], enable=True)
        self.set_skill(trigger_ids=[1381], enable=True)
        self.set_skill(trigger_ids=[1382], enable=True)
        self.set_skill(trigger_ids=[1383], enable=True)
        self.set_skill(trigger_ids=[1384], enable=True)
        self.set_skill(trigger_ids=[1385], enable=True)
        self.set_skill(trigger_ids=[1386], enable=True)
        self.set_skill(trigger_ids=[1387], enable=True)
        self.set_skill(trigger_ids=[1388], enable=True)
        self.set_skill(trigger_ids=[1389], enable=True)
        self.set_skill(trigger_ids=[1390], enable=True)
        self.set_skill(trigger_ids=[1391], enable=True)
        self.set_skill(trigger_ids=[1392], enable=True)
        self.set_skill(trigger_ids=[1393], enable=True)
        self.set_skill(trigger_ids=[1394], enable=True)
        self.set_skill(trigger_ids=[1395], enable=True)
        self.set_skill(trigger_ids=[1396], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬15대기(self.ctx)


class 스킬15대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1379], enable=False)
        self.set_skill(trigger_ids=[1380], enable=False)
        self.set_skill(trigger_ids=[1381], enable=False)
        self.set_skill(trigger_ids=[1382], enable=False)
        self.set_skill(trigger_ids=[1383], enable=False)
        self.set_skill(trigger_ids=[1384], enable=False)
        self.set_skill(trigger_ids=[1385], enable=False)
        self.set_skill(trigger_ids=[1386], enable=False)
        self.set_skill(trigger_ids=[1387], enable=False)
        self.set_skill(trigger_ids=[1388], enable=False)
        self.set_skill(trigger_ids=[1389], enable=False)
        self.set_skill(trigger_ids=[1390], enable=False)
        self.set_skill(trigger_ids=[1391], enable=False)
        self.set_skill(trigger_ids=[1392], enable=False)
        self.set_skill(trigger_ids=[1393], enable=False)
        self.set_skill(trigger_ids=[1394], enable=False)
        self.set_skill(trigger_ids=[1395], enable=False)
        self.set_skill(trigger_ids=[1396], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬15(self.ctx)


class 스킬15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1385], enable=True)
        self.set_skill(trigger_ids=[1386], enable=True)
        self.set_skill(trigger_ids=[1387], enable=True)
        self.set_skill(trigger_ids=[1388], enable=True)
        self.set_skill(trigger_ids=[1389], enable=True)
        self.set_skill(trigger_ids=[1390], enable=True)
        self.set_skill(trigger_ids=[1391], enable=True)
        self.set_skill(trigger_ids=[1392], enable=True)
        self.set_skill(trigger_ids=[1393], enable=True)
        self.set_skill(trigger_ids=[1394], enable=True)
        self.set_skill(trigger_ids=[1395], enable=True)
        self.set_skill(trigger_ids=[1396], enable=True)
        self.set_skill(trigger_ids=[1397], enable=True)
        self.set_skill(trigger_ids=[1398], enable=True)
        self.set_skill(trigger_ids=[1399], enable=True)
        self.set_skill(trigger_ids=[1400], enable=True)
        self.set_skill(trigger_ids=[1401], enable=True)
        self.set_skill(trigger_ids=[1402], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬16대기(self.ctx)


class 스킬16대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1385], enable=False)
        self.set_skill(trigger_ids=[1386], enable=False)
        self.set_skill(trigger_ids=[1387], enable=False)
        self.set_skill(trigger_ids=[1388], enable=False)
        self.set_skill(trigger_ids=[1389], enable=False)
        self.set_skill(trigger_ids=[1390], enable=False)
        self.set_skill(trigger_ids=[1391], enable=False)
        self.set_skill(trigger_ids=[1392], enable=False)
        self.set_skill(trigger_ids=[1393], enable=False)
        self.set_skill(trigger_ids=[1394], enable=False)
        self.set_skill(trigger_ids=[1395], enable=False)
        self.set_skill(trigger_ids=[1396], enable=False)
        self.set_skill(trigger_ids=[1397], enable=False)
        self.set_skill(trigger_ids=[1398], enable=False)
        self.set_skill(trigger_ids=[1399], enable=False)
        self.set_skill(trigger_ids=[1400], enable=False)
        self.set_skill(trigger_ids=[1401], enable=False)
        self.set_skill(trigger_ids=[1402], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬16(self.ctx)


class 스킬16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1391], enable=True)
        self.set_skill(trigger_ids=[1392], enable=True)
        self.set_skill(trigger_ids=[1393], enable=True)
        self.set_skill(trigger_ids=[1394], enable=True)
        self.set_skill(trigger_ids=[1395], enable=True)
        self.set_skill(trigger_ids=[1396], enable=True)
        self.set_skill(trigger_ids=[1397], enable=True)
        self.set_skill(trigger_ids=[1398], enable=True)
        self.set_skill(trigger_ids=[1399], enable=True)
        self.set_skill(trigger_ids=[1400], enable=True)
        self.set_skill(trigger_ids=[1401], enable=True)
        self.set_skill(trigger_ids=[1402], enable=True)
        self.set_skill(trigger_ids=[1403], enable=True)
        self.set_skill(trigger_ids=[1404], enable=True)
        self.set_skill(trigger_ids=[1405], enable=True)
        self.set_skill(trigger_ids=[1406], enable=True)
        self.set_skill(trigger_ids=[1407], enable=True)
        self.set_skill(trigger_ids=[1408], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬17대기(self.ctx)


class 스킬17대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1391], enable=False)
        self.set_skill(trigger_ids=[1392], enable=False)
        self.set_skill(trigger_ids=[1393], enable=False)
        self.set_skill(trigger_ids=[1394], enable=False)
        self.set_skill(trigger_ids=[1395], enable=False)
        self.set_skill(trigger_ids=[1396], enable=False)
        self.set_skill(trigger_ids=[1397], enable=False)
        self.set_skill(trigger_ids=[1398], enable=False)
        self.set_skill(trigger_ids=[1399], enable=False)
        self.set_skill(trigger_ids=[1400], enable=False)
        self.set_skill(trigger_ids=[1401], enable=False)
        self.set_skill(trigger_ids=[1402], enable=False)
        self.set_skill(trigger_ids=[1403], enable=False)
        self.set_skill(trigger_ids=[1404], enable=False)
        self.set_skill(trigger_ids=[1405], enable=False)
        self.set_skill(trigger_ids=[1406], enable=False)
        self.set_skill(trigger_ids=[1407], enable=False)
        self.set_skill(trigger_ids=[1408], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬17(self.ctx)


class 스킬17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1391], enable=True)
        self.set_skill(trigger_ids=[1392], enable=True)
        self.set_skill(trigger_ids=[1393], enable=True)
        self.set_skill(trigger_ids=[1394], enable=True)
        self.set_skill(trigger_ids=[1395], enable=True)
        self.set_skill(trigger_ids=[1396], enable=True)
        self.set_skill(trigger_ids=[1397], enable=True)
        self.set_skill(trigger_ids=[1398], enable=True)
        self.set_skill(trigger_ids=[1399], enable=True)
        self.set_skill(trigger_ids=[1400], enable=True)
        self.set_skill(trigger_ids=[1401], enable=True)
        self.set_skill(trigger_ids=[1402], enable=True)
        self.set_skill(trigger_ids=[1403], enable=True)
        self.set_skill(trigger_ids=[1404], enable=True)
        self.set_skill(trigger_ids=[1405], enable=True)
        self.set_skill(trigger_ids=[1406], enable=True)
        self.set_skill(trigger_ids=[1407], enable=True)
        self.set_skill(trigger_ids=[1408], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬18대기(self.ctx)


class 스킬18대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1391], enable=False)
        self.set_skill(trigger_ids=[1392], enable=False)
        self.set_skill(trigger_ids=[1393], enable=False)
        self.set_skill(trigger_ids=[1394], enable=False)
        self.set_skill(trigger_ids=[1395], enable=False)
        self.set_skill(trigger_ids=[1396], enable=False)
        self.set_skill(trigger_ids=[1397], enable=False)
        self.set_skill(trigger_ids=[1398], enable=False)
        self.set_skill(trigger_ids=[1399], enable=False)
        self.set_skill(trigger_ids=[1400], enable=False)
        self.set_skill(trigger_ids=[1401], enable=False)
        self.set_skill(trigger_ids=[1402], enable=False)
        self.set_skill(trigger_ids=[1403], enable=False)
        self.set_skill(trigger_ids=[1404], enable=False)
        self.set_skill(trigger_ids=[1405], enable=False)
        self.set_skill(trigger_ids=[1406], enable=False)
        self.set_skill(trigger_ids=[1407], enable=False)
        self.set_skill(trigger_ids=[1408], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬18(self.ctx)


class 스킬18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1397], enable=True)
        self.set_skill(trigger_ids=[1398], enable=True)
        self.set_skill(trigger_ids=[1399], enable=True)
        self.set_skill(trigger_ids=[1400], enable=True)
        self.set_skill(trigger_ids=[1401], enable=True)
        self.set_skill(trigger_ids=[1402], enable=True)
        self.set_skill(trigger_ids=[1403], enable=True)
        self.set_skill(trigger_ids=[1404], enable=True)
        self.set_skill(trigger_ids=[1405], enable=True)
        self.set_skill(trigger_ids=[1406], enable=True)
        self.set_skill(trigger_ids=[1407], enable=True)
        self.set_skill(trigger_ids=[1408], enable=True)
        self.set_skill(trigger_ids=[1409], enable=True)
        self.set_skill(trigger_ids=[1410], enable=True)
        self.set_skill(trigger_ids=[1411], enable=True)
        self.set_skill(trigger_ids=[1412], enable=True)
        self.set_skill(trigger_ids=[1413], enable=True)
        self.set_skill(trigger_ids=[1414], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬19대기(self.ctx)


class 스킬19대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1397], enable=False)
        self.set_skill(trigger_ids=[1398], enable=False)
        self.set_skill(trigger_ids=[1399], enable=False)
        self.set_skill(trigger_ids=[1400], enable=False)
        self.set_skill(trigger_ids=[1401], enable=False)
        self.set_skill(trigger_ids=[1402], enable=False)
        self.set_skill(trigger_ids=[1403], enable=False)
        self.set_skill(trigger_ids=[1404], enable=False)
        self.set_skill(trigger_ids=[1405], enable=False)
        self.set_skill(trigger_ids=[1406], enable=False)
        self.set_skill(trigger_ids=[1407], enable=False)
        self.set_skill(trigger_ids=[1408], enable=False)
        self.set_skill(trigger_ids=[1409], enable=False)
        self.set_skill(trigger_ids=[1410], enable=False)
        self.set_skill(trigger_ids=[1411], enable=False)
        self.set_skill(trigger_ids=[1412], enable=False)
        self.set_skill(trigger_ids=[1413], enable=False)
        self.set_skill(trigger_ids=[1414], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬19(self.ctx)


class 스킬19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1403], enable=True)
        self.set_skill(trigger_ids=[1404], enable=True)
        self.set_skill(trigger_ids=[1405], enable=True)
        self.set_skill(trigger_ids=[1406], enable=True)
        self.set_skill(trigger_ids=[1407], enable=True)
        self.set_skill(trigger_ids=[1408], enable=True)
        self.set_skill(trigger_ids=[1409], enable=True)
        self.set_skill(trigger_ids=[1410], enable=True)
        self.set_skill(trigger_ids=[1411], enable=True)
        self.set_skill(trigger_ids=[1412], enable=True)
        self.set_skill(trigger_ids=[1413], enable=True)
        self.set_skill(trigger_ids=[1414], enable=True)
        self.set_skill(trigger_ids=[1409], enable=True)
        self.set_skill(trigger_ids=[1410], enable=True)
        self.set_skill(trigger_ids=[1411], enable=True)
        self.set_skill(trigger_ids=[1412], enable=True)
        self.set_skill(trigger_ids=[1413], enable=True)
        self.set_skill(trigger_ids=[1414], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬20대기(self.ctx)


class 스킬20대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1403], enable=False)
        self.set_skill(trigger_ids=[1404], enable=False)
        self.set_skill(trigger_ids=[1405], enable=False)
        self.set_skill(trigger_ids=[1406], enable=False)
        self.set_skill(trigger_ids=[1407], enable=False)
        self.set_skill(trigger_ids=[1408], enable=False)
        self.set_skill(trigger_ids=[1409], enable=False)
        self.set_skill(trigger_ids=[1410], enable=False)
        self.set_skill(trigger_ids=[1411], enable=False)
        self.set_skill(trigger_ids=[1412], enable=False)
        self.set_skill(trigger_ids=[1413], enable=False)
        self.set_skill(trigger_ids=[1414], enable=False)
        self.set_skill(trigger_ids=[1415], enable=False)
        self.set_skill(trigger_ids=[1416], enable=False)
        self.set_skill(trigger_ids=[1417], enable=False)
        self.set_skill(trigger_ids=[1418], enable=False)
        self.set_skill(trigger_ids=[1419], enable=False)
        self.set_skill(trigger_ids=[1420], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬20(self.ctx)


class 스킬20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1409], enable=True)
        self.set_skill(trigger_ids=[1410], enable=True)
        self.set_skill(trigger_ids=[1411], enable=True)
        self.set_skill(trigger_ids=[1412], enable=True)
        self.set_skill(trigger_ids=[1413], enable=True)
        self.set_skill(trigger_ids=[1414], enable=True)
        self.set_skill(trigger_ids=[1415], enable=True)
        self.set_skill(trigger_ids=[1416], enable=True)
        self.set_skill(trigger_ids=[1417], enable=True)
        self.set_skill(trigger_ids=[1418], enable=True)
        self.set_skill(trigger_ids=[1419], enable=True)
        self.set_skill(trigger_ids=[1420], enable=True)
        self.set_skill(trigger_ids=[1421], enable=True)
        self.set_skill(trigger_ids=[1422], enable=True)
        self.set_skill(trigger_ids=[1423], enable=True)
        self.set_skill(trigger_ids=[1424], enable=True)
        self.set_skill(trigger_ids=[1425], enable=True)
        self.set_skill(trigger_ids=[1426], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬21대기(self.ctx)


class 스킬21대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1409], enable=False)
        self.set_skill(trigger_ids=[1410], enable=False)
        self.set_skill(trigger_ids=[1411], enable=False)
        self.set_skill(trigger_ids=[1412], enable=False)
        self.set_skill(trigger_ids=[1413], enable=False)
        self.set_skill(trigger_ids=[1414], enable=False)
        self.set_skill(trigger_ids=[1415], enable=False)
        self.set_skill(trigger_ids=[1416], enable=False)
        self.set_skill(trigger_ids=[1417], enable=False)
        self.set_skill(trigger_ids=[1418], enable=False)
        self.set_skill(trigger_ids=[1419], enable=False)
        self.set_skill(trigger_ids=[1420], enable=False)
        self.set_skill(trigger_ids=[1421], enable=False)
        self.set_skill(trigger_ids=[1422], enable=False)
        self.set_skill(trigger_ids=[1423], enable=False)
        self.set_skill(trigger_ids=[1424], enable=False)
        self.set_skill(trigger_ids=[1425], enable=False)
        self.set_skill(trigger_ids=[1426], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬21(self.ctx)


class 스킬21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1415], enable=True)
        self.set_skill(trigger_ids=[1416], enable=True)
        self.set_skill(trigger_ids=[1417], enable=True)
        self.set_skill(trigger_ids=[1418], enable=True)
        self.set_skill(trigger_ids=[1419], enable=True)
        self.set_skill(trigger_ids=[1420], enable=True)
        self.set_skill(trigger_ids=[1421], enable=True)
        self.set_skill(trigger_ids=[1422], enable=True)
        self.set_skill(trigger_ids=[1423], enable=True)
        self.set_skill(trigger_ids=[1424], enable=True)
        self.set_skill(trigger_ids=[1425], enable=True)
        self.set_skill(trigger_ids=[1426], enable=True)
        self.set_skill(trigger_ids=[1427], enable=True)
        self.set_skill(trigger_ids=[1428], enable=True)
        self.set_skill(trigger_ids=[1429], enable=True)
        self.set_skill(trigger_ids=[1430], enable=True)
        self.set_skill(trigger_ids=[1431], enable=True)
        self.set_skill(trigger_ids=[1432], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬22대기(self.ctx)


class 스킬22대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1415], enable=False)
        self.set_skill(trigger_ids=[1416], enable=False)
        self.set_skill(trigger_ids=[1417], enable=False)
        self.set_skill(trigger_ids=[1418], enable=False)
        self.set_skill(trigger_ids=[1419], enable=False)
        self.set_skill(trigger_ids=[1420], enable=False)
        self.set_skill(trigger_ids=[1421], enable=False)
        self.set_skill(trigger_ids=[1422], enable=False)
        self.set_skill(trigger_ids=[1423], enable=False)
        self.set_skill(trigger_ids=[1424], enable=False)
        self.set_skill(trigger_ids=[1425], enable=False)
        self.set_skill(trigger_ids=[1426], enable=False)
        self.set_skill(trigger_ids=[1427], enable=False)
        self.set_skill(trigger_ids=[1428], enable=False)
        self.set_skill(trigger_ids=[1429], enable=False)
        self.set_skill(trigger_ids=[1430], enable=False)
        self.set_skill(trigger_ids=[1431], enable=False)
        self.set_skill(trigger_ids=[1432], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬22(self.ctx)


class 스킬22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1421], enable=True)
        self.set_skill(trigger_ids=[1422], enable=True)
        self.set_skill(trigger_ids=[1423], enable=True)
        self.set_skill(trigger_ids=[1424], enable=True)
        self.set_skill(trigger_ids=[1425], enable=True)
        self.set_skill(trigger_ids=[1426], enable=True)
        self.set_skill(trigger_ids=[1427], enable=True)
        self.set_skill(trigger_ids=[1428], enable=True)
        self.set_skill(trigger_ids=[1429], enable=True)
        self.set_skill(trigger_ids=[1430], enable=True)
        self.set_skill(trigger_ids=[1431], enable=True)
        self.set_skill(trigger_ids=[1432], enable=True)
        self.set_skill(trigger_ids=[1433], enable=True)
        self.set_skill(trigger_ids=[1434], enable=True)
        self.set_skill(trigger_ids=[1435], enable=True)
        self.set_skill(trigger_ids=[1436], enable=True)
        self.set_skill(trigger_ids=[1437], enable=True)
        self.set_skill(trigger_ids=[1438], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬23대기(self.ctx)


class 스킬23대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1421], enable=False)
        self.set_skill(trigger_ids=[1422], enable=False)
        self.set_skill(trigger_ids=[1423], enable=False)
        self.set_skill(trigger_ids=[1424], enable=False)
        self.set_skill(trigger_ids=[1425], enable=False)
        self.set_skill(trigger_ids=[1426], enable=False)
        self.set_skill(trigger_ids=[1427], enable=False)
        self.set_skill(trigger_ids=[1428], enable=False)
        self.set_skill(trigger_ids=[1429], enable=False)
        self.set_skill(trigger_ids=[1430], enable=False)
        self.set_skill(trigger_ids=[1431], enable=False)
        self.set_skill(trigger_ids=[1432], enable=False)
        self.set_skill(trigger_ids=[1433], enable=False)
        self.set_skill(trigger_ids=[1434], enable=False)
        self.set_skill(trigger_ids=[1435], enable=False)
        self.set_skill(trigger_ids=[1436], enable=False)
        self.set_skill(trigger_ids=[1437], enable=False)
        self.set_skill(trigger_ids=[1438], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬23(self.ctx)


class 스킬23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1427], enable=True)
        self.set_skill(trigger_ids=[1428], enable=True)
        self.set_skill(trigger_ids=[1429], enable=True)
        self.set_skill(trigger_ids=[1430], enable=True)
        self.set_skill(trigger_ids=[1431], enable=True)
        self.set_skill(trigger_ids=[1432], enable=True)
        self.set_skill(trigger_ids=[1433], enable=True)
        self.set_skill(trigger_ids=[1434], enable=True)
        self.set_skill(trigger_ids=[1435], enable=True)
        self.set_skill(trigger_ids=[1436], enable=True)
        self.set_skill(trigger_ids=[1437], enable=True)
        self.set_skill(trigger_ids=[1438], enable=True)
        self.set_skill(trigger_ids=[1439], enable=True)
        self.set_skill(trigger_ids=[1440], enable=True)
        self.set_skill(trigger_ids=[1441], enable=True)
        self.set_skill(trigger_ids=[1442], enable=True)
        self.set_skill(trigger_ids=[1443], enable=True)
        self.set_skill(trigger_ids=[1444], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬24대기(self.ctx)


class 스킬24대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1427], enable=False)
        self.set_skill(trigger_ids=[1428], enable=False)
        self.set_skill(trigger_ids=[1429], enable=False)
        self.set_skill(trigger_ids=[1430], enable=False)
        self.set_skill(trigger_ids=[1431], enable=False)
        self.set_skill(trigger_ids=[1432], enable=False)
        self.set_skill(trigger_ids=[1433], enable=False)
        self.set_skill(trigger_ids=[1434], enable=False)
        self.set_skill(trigger_ids=[1435], enable=False)
        self.set_skill(trigger_ids=[1436], enable=False)
        self.set_skill(trigger_ids=[1437], enable=False)
        self.set_skill(trigger_ids=[1438], enable=False)
        self.set_skill(trigger_ids=[1439], enable=False)
        self.set_skill(trigger_ids=[1440], enable=False)
        self.set_skill(trigger_ids=[1441], enable=False)
        self.set_skill(trigger_ids=[1442], enable=False)
        self.set_skill(trigger_ids=[1443], enable=False)
        self.set_skill(trigger_ids=[1444], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬24(self.ctx)


class 스킬24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1433], enable=True)
        self.set_skill(trigger_ids=[1434], enable=True)
        self.set_skill(trigger_ids=[1435], enable=True)
        self.set_skill(trigger_ids=[1436], enable=True)
        self.set_skill(trigger_ids=[1437], enable=True)
        self.set_skill(trigger_ids=[1438], enable=True)
        self.set_skill(trigger_ids=[1439], enable=True)
        self.set_skill(trigger_ids=[1440], enable=True)
        self.set_skill(trigger_ids=[1441], enable=True)
        self.set_skill(trigger_ids=[1442], enable=True)
        self.set_skill(trigger_ids=[1443], enable=True)
        self.set_skill(trigger_ids=[1444], enable=True)
        self.set_skill(trigger_ids=[1445], enable=True)
        self.set_skill(trigger_ids=[1446], enable=True)
        self.set_skill(trigger_ids=[1447], enable=True)
        self.set_skill(trigger_ids=[1448], enable=True)
        self.set_skill(trigger_ids=[1449], enable=True)
        self.set_skill(trigger_ids=[1450], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬25대기(self.ctx)


class 스킬25대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1433], enable=False)
        self.set_skill(trigger_ids=[1434], enable=False)
        self.set_skill(trigger_ids=[1435], enable=False)
        self.set_skill(trigger_ids=[1436], enable=False)
        self.set_skill(trigger_ids=[1437], enable=False)
        self.set_skill(trigger_ids=[1438], enable=False)
        self.set_skill(trigger_ids=[1439], enable=False)
        self.set_skill(trigger_ids=[1440], enable=False)
        self.set_skill(trigger_ids=[1441], enable=False)
        self.set_skill(trigger_ids=[1442], enable=False)
        self.set_skill(trigger_ids=[1443], enable=False)
        self.set_skill(trigger_ids=[1444], enable=False)
        self.set_skill(trigger_ids=[1445], enable=False)
        self.set_skill(trigger_ids=[1446], enable=False)
        self.set_skill(trigger_ids=[1447], enable=False)
        self.set_skill(trigger_ids=[1448], enable=False)
        self.set_skill(trigger_ids=[1449], enable=False)
        self.set_skill(trigger_ids=[1450], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬25(self.ctx)


class 스킬25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1439], enable=True)
        self.set_skill(trigger_ids=[1440], enable=True)
        self.set_skill(trigger_ids=[1441], enable=True)
        self.set_skill(trigger_ids=[1442], enable=True)
        self.set_skill(trigger_ids=[1443], enable=True)
        self.set_skill(trigger_ids=[1444], enable=True)
        self.set_skill(trigger_ids=[1445], enable=True)
        self.set_skill(trigger_ids=[1446], enable=True)
        self.set_skill(trigger_ids=[1447], enable=True)
        self.set_skill(trigger_ids=[1448], enable=True)
        self.set_skill(trigger_ids=[1449], enable=True)
        self.set_skill(trigger_ids=[1450], enable=True)
        self.set_skill(trigger_ids=[1451], enable=True)
        self.set_skill(trigger_ids=[1452], enable=True)
        self.set_skill(trigger_ids=[1453], enable=True)
        self.set_skill(trigger_ids=[1454], enable=True)
        self.set_skill(trigger_ids=[1455], enable=True)
        self.set_skill(trigger_ids=[1456], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬26대기(self.ctx)


class 스킬26대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1439], enable=False)
        self.set_skill(trigger_ids=[1440], enable=False)
        self.set_skill(trigger_ids=[1441], enable=False)
        self.set_skill(trigger_ids=[1442], enable=False)
        self.set_skill(trigger_ids=[1443], enable=False)
        self.set_skill(trigger_ids=[1444], enable=False)
        self.set_skill(trigger_ids=[1445], enable=False)
        self.set_skill(trigger_ids=[1446], enable=False)
        self.set_skill(trigger_ids=[1447], enable=False)
        self.set_skill(trigger_ids=[1448], enable=False)
        self.set_skill(trigger_ids=[1449], enable=False)
        self.set_skill(trigger_ids=[1450], enable=False)
        self.set_skill(trigger_ids=[1451], enable=False)
        self.set_skill(trigger_ids=[1452], enable=False)
        self.set_skill(trigger_ids=[1453], enable=False)
        self.set_skill(trigger_ids=[1454], enable=False)
        self.set_skill(trigger_ids=[1455], enable=False)
        self.set_skill(trigger_ids=[1456], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬26(self.ctx)


class 스킬26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1445], enable=True)
        self.set_skill(trigger_ids=[1446], enable=True)
        self.set_skill(trigger_ids=[1447], enable=True)
        self.set_skill(trigger_ids=[1448], enable=True)
        self.set_skill(trigger_ids=[1449], enable=True)
        self.set_skill(trigger_ids=[1450], enable=True)
        self.set_skill(trigger_ids=[1451], enable=True)
        self.set_skill(trigger_ids=[1452], enable=True)
        self.set_skill(trigger_ids=[1453], enable=True)
        self.set_skill(trigger_ids=[1454], enable=True)
        self.set_skill(trigger_ids=[1455], enable=True)
        self.set_skill(trigger_ids=[1456], enable=True)
        self.set_skill(trigger_ids=[1457], enable=True)
        self.set_skill(trigger_ids=[1458], enable=True)
        self.set_skill(trigger_ids=[1459], enable=True)
        self.set_skill(trigger_ids=[1460], enable=True)
        self.set_skill(trigger_ids=[1461], enable=True)
        self.set_skill(trigger_ids=[1462], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬27대기(self.ctx)


class 스킬27대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1445], enable=False)
        self.set_skill(trigger_ids=[1446], enable=False)
        self.set_skill(trigger_ids=[1447], enable=False)
        self.set_skill(trigger_ids=[1448], enable=False)
        self.set_skill(trigger_ids=[1449], enable=False)
        self.set_skill(trigger_ids=[1450], enable=False)
        self.set_skill(trigger_ids=[1451], enable=False)
        self.set_skill(trigger_ids=[1452], enable=False)
        self.set_skill(trigger_ids=[1453], enable=False)
        self.set_skill(trigger_ids=[1454], enable=False)
        self.set_skill(trigger_ids=[1455], enable=False)
        self.set_skill(trigger_ids=[1456], enable=False)
        self.set_skill(trigger_ids=[1457], enable=False)
        self.set_skill(trigger_ids=[1458], enable=False)
        self.set_skill(trigger_ids=[1459], enable=False)
        self.set_skill(trigger_ids=[1460], enable=False)
        self.set_skill(trigger_ids=[1461], enable=False)
        self.set_skill(trigger_ids=[1462], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬27(self.ctx)


class 스킬27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1451], enable=True)
        self.set_skill(trigger_ids=[1452], enable=True)
        self.set_skill(trigger_ids=[1453], enable=True)
        self.set_skill(trigger_ids=[1454], enable=True)
        self.set_skill(trigger_ids=[1455], enable=True)
        self.set_skill(trigger_ids=[1456], enable=True)
        self.set_skill(trigger_ids=[1457], enable=True)
        self.set_skill(trigger_ids=[1458], enable=True)
        self.set_skill(trigger_ids=[1459], enable=True)
        self.set_skill(trigger_ids=[1460], enable=True)
        self.set_skill(trigger_ids=[1461], enable=True)
        self.set_skill(trigger_ids=[1462], enable=True)
        self.set_skill(trigger_ids=[1463], enable=True)
        self.set_skill(trigger_ids=[1464], enable=True)
        self.set_skill(trigger_ids=[1465], enable=True)
        self.set_skill(trigger_ids=[1466], enable=True)
        self.set_skill(trigger_ids=[1467], enable=True)
        self.set_skill(trigger_ids=[1468], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬28대기(self.ctx)


class 스킬28대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1451], enable=False)
        self.set_skill(trigger_ids=[1452], enable=False)
        self.set_skill(trigger_ids=[1453], enable=False)
        self.set_skill(trigger_ids=[1454], enable=False)
        self.set_skill(trigger_ids=[1455], enable=False)
        self.set_skill(trigger_ids=[1456], enable=False)
        self.set_skill(trigger_ids=[1457], enable=False)
        self.set_skill(trigger_ids=[1458], enable=False)
        self.set_skill(trigger_ids=[1459], enable=False)
        self.set_skill(trigger_ids=[1460], enable=False)
        self.set_skill(trigger_ids=[1461], enable=False)
        self.set_skill(trigger_ids=[1462], enable=False)
        self.set_skill(trigger_ids=[1463], enable=False)
        self.set_skill(trigger_ids=[1464], enable=False)
        self.set_skill(trigger_ids=[1465], enable=False)
        self.set_skill(trigger_ids=[1466], enable=False)
        self.set_skill(trigger_ids=[1467], enable=False)
        self.set_skill(trigger_ids=[1468], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬28(self.ctx)


class 스킬28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1457], enable=True)
        self.set_skill(trigger_ids=[1458], enable=True)
        self.set_skill(trigger_ids=[1459], enable=True)
        self.set_skill(trigger_ids=[1460], enable=True)
        self.set_skill(trigger_ids=[1461], enable=True)
        self.set_skill(trigger_ids=[1462], enable=True)
        self.set_skill(trigger_ids=[1463], enable=True)
        self.set_skill(trigger_ids=[1464], enable=True)
        self.set_skill(trigger_ids=[1465], enable=True)
        self.set_skill(trigger_ids=[1466], enable=True)
        self.set_skill(trigger_ids=[1467], enable=True)
        self.set_skill(trigger_ids=[1468], enable=True)
        self.set_skill(trigger_ids=[1469], enable=True)
        self.set_skill(trigger_ids=[1470], enable=True)
        self.set_skill(trigger_ids=[1471], enable=True)
        self.set_skill(trigger_ids=[1472], enable=True)
        self.set_skill(trigger_ids=[1473], enable=True)
        self.set_skill(trigger_ids=[1474], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬29대기(self.ctx)


class 스킬29대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1457], enable=False)
        self.set_skill(trigger_ids=[1458], enable=False)
        self.set_skill(trigger_ids=[1459], enable=False)
        self.set_skill(trigger_ids=[1460], enable=False)
        self.set_skill(trigger_ids=[1461], enable=False)
        self.set_skill(trigger_ids=[1462], enable=False)
        self.set_skill(trigger_ids=[1463], enable=False)
        self.set_skill(trigger_ids=[1464], enable=False)
        self.set_skill(trigger_ids=[1465], enable=False)
        self.set_skill(trigger_ids=[1466], enable=False)
        self.set_skill(trigger_ids=[1467], enable=False)
        self.set_skill(trigger_ids=[1468], enable=False)
        self.set_skill(trigger_ids=[1469], enable=False)
        self.set_skill(trigger_ids=[1470], enable=False)
        self.set_skill(trigger_ids=[1471], enable=False)
        self.set_skill(trigger_ids=[1472], enable=False)
        self.set_skill(trigger_ids=[1473], enable=False)
        self.set_skill(trigger_ids=[1474], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬29(self.ctx)


class 스킬29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1463], enable=True)
        self.set_skill(trigger_ids=[1464], enable=True)
        self.set_skill(trigger_ids=[1465], enable=True)
        self.set_skill(trigger_ids=[1466], enable=True)
        self.set_skill(trigger_ids=[1467], enable=True)
        self.set_skill(trigger_ids=[1468], enable=True)
        self.set_skill(trigger_ids=[1469], enable=True)
        self.set_skill(trigger_ids=[1470], enable=True)
        self.set_skill(trigger_ids=[1471], enable=True)
        self.set_skill(trigger_ids=[1472], enable=True)
        self.set_skill(trigger_ids=[1473], enable=True)
        self.set_skill(trigger_ids=[1474], enable=True)
        self.set_skill(trigger_ids=[1475], enable=True)
        self.set_skill(trigger_ids=[1476], enable=True)
        self.set_skill(trigger_ids=[1477], enable=True)
        self.set_skill(trigger_ids=[1478], enable=True)
        self.set_skill(trigger_ids=[1479], enable=True)
        self.set_skill(trigger_ids=[1480], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬30대기(self.ctx)


class 스킬30대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1463], enable=False)
        self.set_skill(trigger_ids=[1464], enable=False)
        self.set_skill(trigger_ids=[1465], enable=False)
        self.set_skill(trigger_ids=[1466], enable=False)
        self.set_skill(trigger_ids=[1467], enable=False)
        self.set_skill(trigger_ids=[1468], enable=False)
        self.set_skill(trigger_ids=[1469], enable=False)
        self.set_skill(trigger_ids=[1470], enable=False)
        self.set_skill(trigger_ids=[1471], enable=False)
        self.set_skill(trigger_ids=[1472], enable=False)
        self.set_skill(trigger_ids=[1473], enable=False)
        self.set_skill(trigger_ids=[1475], enable=False)
        self.set_skill(trigger_ids=[1474], enable=False)
        self.set_skill(trigger_ids=[1476], enable=False)
        self.set_skill(trigger_ids=[1477], enable=False)
        self.set_skill(trigger_ids=[1478], enable=False)
        self.set_skill(trigger_ids=[1479], enable=False)
        self.set_skill(trigger_ids=[1480], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬30(self.ctx)


class 스킬30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1469], enable=True)
        self.set_skill(trigger_ids=[1470], enable=True)
        self.set_skill(trigger_ids=[1471], enable=True)
        self.set_skill(trigger_ids=[1472], enable=True)
        self.set_skill(trigger_ids=[1473], enable=True)
        self.set_skill(trigger_ids=[1474], enable=True)
        self.set_skill(trigger_ids=[1475], enable=True)
        self.set_skill(trigger_ids=[1476], enable=True)
        self.set_skill(trigger_ids=[1477], enable=True)
        self.set_skill(trigger_ids=[1478], enable=True)
        self.set_skill(trigger_ids=[1479], enable=True)
        self.set_skill(trigger_ids=[1480], enable=True)
        self.set_skill(trigger_ids=[1481], enable=True)
        self.set_skill(trigger_ids=[1482], enable=True)
        self.set_skill(trigger_ids=[1483], enable=True)
        self.set_skill(trigger_ids=[1484], enable=True)
        self.set_skill(trigger_ids=[1485], enable=True)
        self.set_skill(trigger_ids=[1486], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬31대기(self.ctx)


class 스킬31대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1469], enable=False)
        self.set_skill(trigger_ids=[1470], enable=False)
        self.set_skill(trigger_ids=[1471], enable=False)
        self.set_skill(trigger_ids=[1472], enable=False)
        self.set_skill(trigger_ids=[1473], enable=False)
        self.set_skill(trigger_ids=[1474], enable=False)
        self.set_skill(trigger_ids=[1475], enable=False)
        self.set_skill(trigger_ids=[1476], enable=False)
        self.set_skill(trigger_ids=[1477], enable=False)
        self.set_skill(trigger_ids=[1478], enable=False)
        self.set_skill(trigger_ids=[1479], enable=False)
        self.set_skill(trigger_ids=[1480], enable=False)
        self.set_skill(trigger_ids=[1481], enable=False)
        self.set_skill(trigger_ids=[1482], enable=False)
        self.set_skill(trigger_ids=[1483], enable=False)
        self.set_skill(trigger_ids=[1484], enable=False)
        self.set_skill(trigger_ids=[1485], enable=False)
        self.set_skill(trigger_ids=[1486], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬31(self.ctx)


class 스킬31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1475], enable=True)
        self.set_skill(trigger_ids=[1476], enable=True)
        self.set_skill(trigger_ids=[1477], enable=True)
        self.set_skill(trigger_ids=[1478], enable=True)
        self.set_skill(trigger_ids=[1479], enable=True)
        self.set_skill(trigger_ids=[1480], enable=True)
        self.set_skill(trigger_ids=[1481], enable=True)
        self.set_skill(trigger_ids=[1482], enable=True)
        self.set_skill(trigger_ids=[1483], enable=True)
        self.set_skill(trigger_ids=[1484], enable=True)
        self.set_skill(trigger_ids=[1485], enable=True)
        self.set_skill(trigger_ids=[1486], enable=True)
        self.set_skill(trigger_ids=[1487], enable=True)
        self.set_skill(trigger_ids=[1488], enable=True)
        self.set_skill(trigger_ids=[1489], enable=True)
        self.set_skill(trigger_ids=[1490], enable=True)
        self.set_skill(trigger_ids=[1491], enable=True)
        self.set_skill(trigger_ids=[1492], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬32대기(self.ctx)


class 스킬32대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1475], enable=False)
        self.set_skill(trigger_ids=[1476], enable=False)
        self.set_skill(trigger_ids=[1477], enable=False)
        self.set_skill(trigger_ids=[1478], enable=False)
        self.set_skill(trigger_ids=[1479], enable=False)
        self.set_skill(trigger_ids=[1480], enable=False)
        self.set_skill(trigger_ids=[1481], enable=False)
        self.set_skill(trigger_ids=[1482], enable=False)
        self.set_skill(trigger_ids=[1483], enable=False)
        self.set_skill(trigger_ids=[1484], enable=False)
        self.set_skill(trigger_ids=[1485], enable=False)
        self.set_skill(trigger_ids=[1486], enable=False)
        self.set_skill(trigger_ids=[1487], enable=False)
        self.set_skill(trigger_ids=[1488], enable=False)
        self.set_skill(trigger_ids=[1489], enable=False)
        self.set_skill(trigger_ids=[1490], enable=False)
        self.set_skill(trigger_ids=[1491], enable=False)
        self.set_skill(trigger_ids=[1492], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬32(self.ctx)


class 스킬32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1481], enable=True)
        self.set_skill(trigger_ids=[1482], enable=True)
        self.set_skill(trigger_ids=[1483], enable=True)
        self.set_skill(trigger_ids=[1484], enable=True)
        self.set_skill(trigger_ids=[1485], enable=True)
        self.set_skill(trigger_ids=[1486], enable=True)
        self.set_skill(trigger_ids=[1487], enable=True)
        self.set_skill(trigger_ids=[1488], enable=True)
        self.set_skill(trigger_ids=[1489], enable=True)
        self.set_skill(trigger_ids=[1490], enable=True)
        self.set_skill(trigger_ids=[1491], enable=True)
        self.set_skill(trigger_ids=[1492], enable=True)
        self.set_skill(trigger_ids=[1493], enable=True)
        self.set_skill(trigger_ids=[1494], enable=True)
        self.set_skill(trigger_ids=[1495], enable=True)
        self.set_skill(trigger_ids=[1496], enable=True)
        self.set_skill(trigger_ids=[1497], enable=True)
        self.set_skill(trigger_ids=[1498], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬33대기(self.ctx)


class 스킬33대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1481], enable=False)
        self.set_skill(trigger_ids=[1482], enable=False)
        self.set_skill(trigger_ids=[1483], enable=False)
        self.set_skill(trigger_ids=[1484], enable=False)
        self.set_skill(trigger_ids=[1485], enable=False)
        self.set_skill(trigger_ids=[1486], enable=False)
        self.set_skill(trigger_ids=[1487], enable=False)
        self.set_skill(trigger_ids=[1488], enable=False)
        self.set_skill(trigger_ids=[1489], enable=False)
        self.set_skill(trigger_ids=[1490], enable=False)
        self.set_skill(trigger_ids=[1491], enable=False)
        self.set_skill(trigger_ids=[1492], enable=False)
        self.set_skill(trigger_ids=[1493], enable=False)
        self.set_skill(trigger_ids=[1494], enable=False)
        self.set_skill(trigger_ids=[1495], enable=False)
        self.set_skill(trigger_ids=[1496], enable=False)
        self.set_skill(trigger_ids=[1497], enable=False)
        self.set_skill(trigger_ids=[1498], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬33(self.ctx)


class 스킬33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[1487], enable=True)
        self.set_skill(trigger_ids=[1488], enable=True)
        self.set_skill(trigger_ids=[1489], enable=True)
        self.set_skill(trigger_ids=[1490], enable=True)
        self.set_skill(trigger_ids=[1491], enable=True)
        self.set_skill(trigger_ids=[1492], enable=True)
        self.set_skill(trigger_ids=[1493], enable=True)
        self.set_skill(trigger_ids=[1494], enable=True)
        self.set_skill(trigger_ids=[1495], enable=True)
        self.set_skill(trigger_ids=[1496], enable=True)
        self.set_skill(trigger_ids=[1497], enable=True)
        self.set_skill(trigger_ids=[1498], enable=True)
        self.set_skill(trigger_ids=[1499], enable=True)
        self.set_skill(trigger_ids=[1500], enable=True)
        self.set_skill(trigger_ids=[1501], enable=True)
        self.set_skill(trigger_ids=[1502], enable=True)
        self.set_skill(trigger_ids=[1503], enable=True)
        self.set_skill(trigger_ids=[1504], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬34대기(self.ctx)


class 스킬34대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[1487], enable=False)
        self.set_skill(trigger_ids=[1488], enable=False)
        self.set_skill(trigger_ids=[1489], enable=False)
        self.set_skill(trigger_ids=[1490], enable=False)
        self.set_skill(trigger_ids=[1491], enable=False)
        self.set_skill(trigger_ids=[1492], enable=False)
        self.set_skill(trigger_ids=[1493], enable=False)
        self.set_skill(trigger_ids=[1494], enable=False)
        self.set_skill(trigger_ids=[1495], enable=False)
        self.set_skill(trigger_ids=[1496], enable=False)
        self.set_skill(trigger_ids=[1497], enable=False)
        self.set_skill(trigger_ids=[1498], enable=False)
        self.set_skill(trigger_ids=[1499], enable=False)
        self.set_skill(trigger_ids=[1500], enable=False)
        self.set_skill(trigger_ids=[1501], enable=False)
        self.set_skill(trigger_ids=[1502], enable=False)
        self.set_skill(trigger_ids=[1503], enable=False)
        self.set_skill(trigger_ids=[1504], enable=False)


initial_state = 대기
