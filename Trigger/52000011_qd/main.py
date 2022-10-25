""" trigger/52000011_qd/main.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041], enable=True)
        self.set_breakable(triggerIds=[7101,7102,7103,7104,7105,7106,7107,7108,7109,7110,7111,7112,7113,7114,7115,7116,7117,7118,7119,7120,7121,7122,7123,7124,7125,7126,7127,7128,7129,7130,7131,7132,7133,7134,7135,7136,7137,7138,7139,7140,7141,7142,7143,7144,7145,7146,7147,7148,7149,7150,7151,7152,7153,7154,7155,7156,7157,7158,7159,7160,7161,7162,7163,7164,7165,7166,7167,7168,7169,7170], enable=True)
        self.set_breakable(triggerIds=[7201,7202,7203,7204,7205,7206,7207,7208,7209,7210,7211,7212,7213,7214,7215,7216,7217,7218,7219,7220,7221,7222,7223,7224,7225,7226,7227,7228,7229,7230,7231,7232,7233,7234,7235,7236,7237,7238,7239,7240,7241,7242,7243,7244,7245,7246,7247,7248,7249,7250,7251,7252,7253,7254,7255,7256,7257,7258,7259,7260,7261,7262,7263,7264,7265,7266,7267,7268,7269,7270], enable=True)
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=202, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=203, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=204, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=205, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=206, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=207, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=208, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[10002594], questStates=[1]):
            return 연출시작딜레이(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 연출시작딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 오스칼01(self.ctx)


class 오스칼01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[302], returnView=True)
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=2, spawnId=11000015, script='$52000011_QD__MAIN__0$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 오스칼02(self.ctx)


class 오스칼02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=2, spawnId=11000015, script='$52000011_QD__MAIN__1$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NPC교체(self.ctx)


class NPC교체(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.destroy_monster(spawnIds=[2001])
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2002]):
            return 몬스터생성01(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 몬스터생성01(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=202, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[1001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1001]):
            return 몬스터생성02(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 몬스터생성02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1002]):
            return 문열림02(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 문열림02(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_breakable(triggerIds=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041], enable=False)
        self.set_actor(triggerId=203, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[2002]):
            return 몬스터생성03(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 몬스터생성03(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=204, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[1003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1003]):
            return 몬스터생성04(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 몬스터생성04(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1004]):
            return 문열림03(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 문열림03(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_breakable(triggerIds=[7101,7102,7103,7104,7105,7106,7107,7108,7109,7110,7111,7112,7113,7114,7115,7116,7117,7118,7119,7120,7121,7122,7123,7124,7125,7126,7127,7128,7129,7130,7131,7132,7133,7134,7135,7136,7137,7138,7139,7140,7141,7142,7143,7144,7145,7146,7147,7148,7149,7150,7151,7152,7153,7154,7155,7156,7157,7158,7159,7160,7161,7162,7163,7164,7165,7166,7167,7168,7169,7170], enable=False)
        self.set_actor(triggerId=205, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[2002]):
            return 몬스터생성05(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 몬스터생성05(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=206, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[1005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1005]):
            return 몬스터생성06(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 몬스터생성06(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1006], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1006]):
            return 문열림04(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 문열림04(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_breakable(triggerIds=[7201,7202,7203,7204,7205,7206,7207,7208,7209,7210,7211,7212,7213,7214,7215,7216,7217,7218,7219,7220,7221,7222,7223,7224,7225,7226,7227,7228,7229,7230,7231,7232,7233,7234,7235,7236,7237,7238,7239,7240,7241,7242,7243,7244,7245,7246,7247,7248,7249,7250,7251,7252,7253,7254,7255,7256,7257,7258,7259,7260,7261,7262,7263,7264,7265,7266,7267,7268,7269,7270], enable=False)
        self.set_actor(triggerId=207, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3004], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=105, spawnIds=[2002]):
            return 문열림05(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 문열림05(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=208, visible=True, initialSequence='Opened')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=106, spawnIds=[2002]):
            return NPC교체2(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class NPC교체2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2003], animationEffect=False)
        self.destroy_monster(spawnIds=[2002])

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[10002595], questStates=[2]):
            return 포털생성(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 포털생성(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='30'):
            self.move_user(mapId=2000309, portalId=2, boxId=199)
            return 종료(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,2001,2002,2003])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 시작(self.ctx)


initial_state = 시작
