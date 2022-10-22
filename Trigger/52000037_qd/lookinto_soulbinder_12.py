""" trigger/52000037_qd/lookinto_soulbinder_12.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000175], state=0) # Bag

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[60100065], questStates=[2], jobCode=110):
            return 연출01조건()
        if quest_user_detected(boxIds=[9900], questIds=[60100065], questStates=[3], jobCode=110):
            return NPC만배치()
        if wait_tick(waitTick=1000):
            return 종료()


class NPC만배치(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[101], arg2=False) # NelfDummyNPC
        set_interact_object(triggerIds=[10000175], state=1) # Bag

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 연출01조건(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[101], arg2=False) # NelfDummyNPC
        set_interact_object(triggerIds=[10000175], state=1) # Bag

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9300], questIds=[60100065], questStates=[2], jobCode=110):
            return 연출01시작()


class 연출01시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000037, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            move_user_path(patrolName='MS2PatrolData_PC1101A')
            return PC말풍선01()


class PC말풍선01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC말풍선02()


class PC말풍선02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선03()


class PC말풍선03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선04()


class PC말풍선04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PC말풍선05()


class PC말풍선05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__4$', arg4=5, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 강제이동02조건()


class 강제이동02조건(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9301], questIds=[60100065], questStates=[2], jobCode=110):
            return PC말풍선07()


class PC말풍선07(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__5$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동02()


class 강제이동02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC1101B')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9302], questIds=[60100065], questStates=[2], jobCode=110):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 종료()


class 종료(state.State):
    pass


