""" trigger/02000320_bf/wakeup_08.xml """
from common import *
import state


class 자는중(state.State):
    def on_enter(self):
        set_actor(triggerId=8001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8002, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8003, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if true():
            return 도둑듬()


class 도둑듬(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000352], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000352], arg2=0):
            return 깨어남1()


class 깨어남1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=8)
        set_actor(triggerId=8001, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=8002, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=8004, visible=False, initialSequence='Bore_A')
        set_actor(triggerId=8005, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=8006, visible=False, initialSequence='Stun_A')
        create_monster(spawnIds=[80004], arg2=True)
        set_conversation(type=1, spawnId=80004, script='$02000320_BF__WAKEUP_08__0$', arg4=2, arg5=0)
        create_monster(spawnIds=[80005], arg2=True)
        set_conversation(type=1, spawnId=80005, script='$02000320_BF__WAKEUP_08__1$', arg4=2, arg5=1)
        create_monster(spawnIds=[80006], arg2=True)
        set_conversation(type=1, spawnId=80006, script='$02000320_BF__WAKEUP_08__2$', arg4=2, arg5=2)
        create_monster(spawnIds=[80001])
        create_monster(spawnIds=[80002])
        create_monster(spawnIds=[80003])
        set_conversation(type=1, spawnId=80003, script='$02000320_BF__WAKEUP_08__3$', arg4=2, arg5=3)
        set_conversation(type=1, spawnId=80001, script='$02000320_BF__WAKEUP_08__4$', arg4=2, arg5=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 깨어남2()


class 깨어남2(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=4)
        set_conversation(type=1, spawnId=80002, script='$02000320_BF__WAKEUP_08__5$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=80001, script='$02000320_BF__WAKEUP_08__6$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=80003, script='$02000320_BF__WAKEUP_08__7$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 깨어남3()


class 깨어남3(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=1)
        set_actor(triggerId=8001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 깨어남4()


class 깨어남4(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[80004,80005,80006]):
            return 다시잠듬()
        if not monster_in_combat(boxIds=[80004,80005,80006]):
            return 다시자러감()


class 다시자러감(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=80004)
        remove_balloon_talk(spawnId=80005)
        remove_balloon_talk(spawnId=80006)
        remove_balloon_talk(spawnId=80001)
        remove_balloon_talk(spawnId=80002)
        remove_balloon_talk(spawnId=80003)
        set_timer(timerId='14', seconds=4)
        set_conversation(type=1, spawnId=80004, script='$02000320_BF__WAKEUP_08__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=80005, script='$02000320_BF__WAKEUP_08__9$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=80006, script='$02000320_BF__WAKEUP_08__10$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 다시잠듬()


class 다시잠듬(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[80001,80002,80003,80004,80005,80006])
        set_timer(timerId='15', seconds=7)
        set_actor(triggerId=8004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=8006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 도둑듬()


