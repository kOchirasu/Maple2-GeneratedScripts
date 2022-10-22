""" trigger/02000253_bf/ground.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[701], visible=False) # 벨라 음성
        set_effect(triggerIds=[702], visible=False) # 벨라 음성
        set_mesh(triggerIds=[107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151], visible=True)

    def on_tick(self) -> state.State:
        if count_users(boxId=906, boxId=1):
            return 벨라소환()


class 벨라소환(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        create_monster(spawnIds=[1001])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라이동()


class 벨라이동(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        # <action name="이펙트를설정한다" arg1="701" arg2="1"/>
        set_conversation(type=1, spawnId=1001, script='$02000253_BF__GROUND__0$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라이동2()


class 벨라이동2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        # <action name="이펙트를설정한다" arg1="702" arg2="1"/>
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1')
        set_conversation(type=1, spawnId=1001, script='$02000253_BF__GROUND__1$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라소멸()


class 벨라소멸(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=140)
        destroy_monster(spawnIds=[1001])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 지진()


class 지진(state.State):
    pass


