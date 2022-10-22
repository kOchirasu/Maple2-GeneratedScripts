""" trigger/52000011_qd/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041], enabled=True)
        set_breakable(triggerIds=[7101,7102,7103,7104,7105,7106,7107,7108,7109,7110,7111,7112,7113,7114,7115,7116,7117,7118,7119,7120,7121,7122,7123,7124,7125,7126,7127,7128,7129,7130,7131,7132,7133,7134,7135,7136,7137,7138,7139,7140,7141,7142,7143,7144,7145,7146,7147,7148,7149,7150,7151,7152,7153,7154,7155,7156,7157,7158,7159,7160,7161,7162,7163,7164,7165,7166,7167,7168,7169,7170], enabled=True)
        set_breakable(triggerIds=[7201,7202,7203,7204,7205,7206,7207,7208,7209,7210,7211,7212,7213,7214,7215,7216,7217,7218,7219,7220,7221,7222,7223,7224,7225,7226,7227,7228,7229,7230,7231,7232,7233,7234,7235,7236,7237,7238,7239,7240,7241,7242,7243,7244,7245,7246,7247,7248,7249,7250,7251,7252,7253,7254,7255,7256,7257,7258,7259,7260,7261,7262,7263,7264,7265,7266,7267,7268,7269,7270], enabled=True)
        create_monster(spawnIds=[2001], arg2=False)
        set_actor(triggerId=201, visible=True, initialSequence='Closed')
        set_actor(triggerId=202, visible=True, initialSequence='Closed')
        set_actor(triggerId=203, visible=True, initialSequence='Closed')
        set_actor(triggerId=204, visible=True, initialSequence='Closed')
        set_actor(triggerId=205, visible=True, initialSequence='Closed')
        set_actor(triggerId=206, visible=True, initialSequence='Closed')
        set_actor(triggerId=207, visible=True, initialSequence='Closed')
        set_actor(triggerId=208, visible=True, initialSequence='Closed')
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3004], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_agent(triggerIds=[9005], visible=True)
        set_agent(triggerIds=[9006], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[10002594], questStates=[1]):
            return 연출시작딜레이()
        if not user_detected(boxIds=[199]):
            return 종료()


class 연출시작딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 오스칼01()


class 오스칼01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[302], returnView=True)
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11000015, script='$52000011_QD__MAIN__0$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 오스칼02()


class 오스칼02(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11000015, script='$52000011_QD__MAIN__1$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if true():
            return NPC교체()


class NPC교체(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)
        destroy_monster(spawnIds=[2001])
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[2002]):
            return 몬스터생성01()
        if not user_detected(boxIds=[199]):
            return 종료()


class 몬스터생성01(state.State):
    def on_enter(self):
        set_actor(triggerId=202, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001]):
            return 몬스터생성02()
        if not user_detected(boxIds=[199]):
            return 종료()


class 몬스터생성02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1002]):
            return 문열림02()
        if not user_detected(boxIds=[199]):
            return 종료()


class 문열림02(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_breakable(triggerIds=[7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032,7033,7034,7035,7036,7037,7038,7039,7040,7041], enabled=False)
        set_actor(triggerId=203, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[2002]):
            return 몬스터생성03()
        if not user_detected(boxIds=[199]):
            return 종료()


class 몬스터생성03(state.State):
    def on_enter(self):
        set_actor(triggerId=204, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[1003], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1003]):
            return 몬스터생성04()
        if not user_detected(boxIds=[199]):
            return 종료()


class 몬스터생성04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1004]):
            return 문열림03()
        if not user_detected(boxIds=[199]):
            return 종료()


class 문열림03(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_breakable(triggerIds=[7101,7102,7103,7104,7105,7106,7107,7108,7109,7110,7111,7112,7113,7114,7115,7116,7117,7118,7119,7120,7121,7122,7123,7124,7125,7126,7127,7128,7129,7130,7131,7132,7133,7134,7135,7136,7137,7138,7139,7140,7141,7142,7143,7144,7145,7146,7147,7148,7149,7150,7151,7152,7153,7154,7155,7156,7157,7158,7159,7160,7161,7162,7163,7164,7165,7166,7167,7168,7169,7170], enabled=False)
        set_actor(triggerId=205, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[2002]):
            return 몬스터생성05()
        if not user_detected(boxIds=[199]):
            return 종료()


class 몬스터생성05(state.State):
    def on_enter(self):
        set_actor(triggerId=206, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[1005], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1005]):
            return 몬스터생성06()
        if not user_detected(boxIds=[199]):
            return 종료()


class 몬스터생성06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1006]):
            return 문열림04()
        if not user_detected(boxIds=[199]):
            return 종료()


class 문열림04(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_breakable(triggerIds=[7201,7202,7203,7204,7205,7206,7207,7208,7209,7210,7211,7212,7213,7214,7215,7216,7217,7218,7219,7220,7221,7222,7223,7224,7225,7226,7227,7228,7229,7230,7231,7232,7233,7234,7235,7236,7237,7238,7239,7240,7241,7242,7243,7244,7245,7246,7247,7248,7249,7250,7251,7252,7253,7254,7255,7256,7257,7258,7259,7260,7261,7262,7263,7264,7265,7266,7267,7268,7269,7270], enabled=False)
        set_actor(triggerId=207, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[3004], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=105, spawnIds=[2002]):
            return 문열림05()
        if not user_detected(boxIds=[199]):
            return 종료()


class 문열림05(state.State):
    def on_enter(self):
        set_actor(triggerId=208, visible=True, initialSequence='Opened')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=106, spawnIds=[2002]):
            return NPC교체2()
        if not user_detected(boxIds=[199]):
            return 종료()


class NPC교체2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003], arg2=False)
        destroy_monster(spawnIds=[2002])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[10002595], questStates=[2]):
            return 포털생성()
        if not user_detected(boxIds=[199]):
            return 종료()


class 포털생성(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            move_user(mapId=2000309, portalId=2, boxId=199)
            return 종료()
        if not user_detected(boxIds=[199]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,2001,2002,2003])

    def on_tick(self) -> state.State:
        if true():
            return 시작()


