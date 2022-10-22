""" trigger/52010004_qd/battle01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[10000], visible=False)
        set_agent(triggerIds=[10001], visible=False)
        set_agent(triggerIds=[10002], visible=False)
        set_agent(triggerIds=[10003], visible=False)
        create_monster(spawnIds=[101], arg2=False) # Quest
        set_mesh(triggerIds=[7000,7001,7002,7003], visible=False, arg3=0, arg4=0, arg5=0) # BattleZone

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[10002800], questStates=[2]):
            return 둔바교체01()


class 둔바교체01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_mesh(triggerIds=[7000,7001,7002,7003], visible=True, arg3=0, arg4=0, arg5=0) # BattleZone
        destroy_monster(spawnIds=[101]) # Quest
        create_monster(spawnIds=[102], arg2=False) # Act

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 둔바연출준비01()


class 둔바연출준비01(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        select_camera(triggerId=601, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 둔바대화01()


class 둔바대화01(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=2)
        set_conversation(type=2, spawnId=11001217, script='$52010004_QD__BATTLE01__0$', arg4=2)
        set_skip(state=둔바대화02대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 둔바대화02대기()


class 둔바대화02대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 둔바대화02()


class 둔바대화02(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=2)
        set_conversation(type=2, spawnId=11001217, script='$52010004_QD__BATTLE01__1$', arg4=2)
        set_skip(state=둔바대화03대기)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 둔바대화03대기()


class 둔바대화03대기(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return 둔바대화03()


class 둔바대화03(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=2)
        set_conversation(type=2, spawnId=11001217, script='$52010004_QD__BATTLE01__2$', arg4=2)
        set_skip(state=둔바연출종료01)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 둔바연출종료01()


class 둔바연출종료01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_timer(timerId='13', seconds=1)
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 전투준비01()


class 전투준비01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=1)
        set_agent(triggerIds=[10000], visible=True)
        set_agent(triggerIds=[10001], visible=True)
        set_agent(triggerIds=[10002], visible=True)
        set_agent(triggerIds=[10003], visible=True)
        destroy_monster(spawnIds=[102]) # Act
        create_monster(spawnIds=[201], arg2=True) # Monster

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 전투중01()


class 전투중01(state.State):
    def on_enter(self):
        move_user(mapId=52010004, portalId=50, boxId=9000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return 둔바교체대기02()


class 둔바교체대기02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[7000,7001,7002,7003], visible=False, arg3=0, arg4=0, arg5=0) # BattleZone
        set_timer(timerId='30', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 둔바교체02()


class 둔바교체02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201]) # Monster
        create_monster(spawnIds=[101], arg2=False) # Quest


