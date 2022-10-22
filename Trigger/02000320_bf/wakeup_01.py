""" trigger/02000320_bf/wakeup_01.xml """
from common import *
import state


class 자는중(state.State):
    def on_enter(self):
        set_actor(triggerId=1001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1002, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1003, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if true():
            return 도둑듬()


class 도둑듬(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000281], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000281], arg2=0):
            return 깨어남1()


class 깨어남1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=8)
        set_actor(triggerId=1001, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=1002, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=1004, visible=False, initialSequence='Bore_A')
        set_actor(triggerId=1005, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=1006, visible=False, initialSequence='Stun_A')
        create_monster(spawnIds=[10004], arg2=True)
        set_conversation(type=1, spawnId=10004, script='$02000320_BF__WAKEUP_01__0$', arg4=2, arg5=0)
        create_monster(spawnIds=[10005], arg2=True)
        set_conversation(type=1, spawnId=10005, script='$02000320_BF__WAKEUP_01__1$', arg4=2, arg5=1)
        create_monster(spawnIds=[10006], arg2=True)
        set_conversation(type=1, spawnId=10006, script='$02000320_BF__WAKEUP_01__2$', arg4=2, arg5=2)
        create_monster(spawnIds=[10001])
        create_monster(spawnIds=[10002])
        create_monster(spawnIds=[10003])
        set_conversation(type=1, spawnId=10003, script='$02000320_BF__WAKEUP_01__3$', arg4=2, arg5=3)
        set_conversation(type=1, spawnId=10001, script='$02000320_BF__WAKEUP_01__4$', arg4=2, arg5=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 깨어남2()


class 깨어남2(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=4)
        set_conversation(type=1, spawnId=10002, script='$02000320_BF__WAKEUP_01__5$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=10001, script='$02000320_BF__WAKEUP_01__6$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=10003, script='$02000320_BF__WAKEUP_01__7$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 깨어남3()


class 깨어남3(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=1)
        set_actor(triggerId=1001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 깨어남4()


class 깨어남4(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10004,10005,10006]):
            return 다시잠듬()
        if not monster_in_combat(boxIds=[10004,10005,10006]):
            return 다시자러감()


class 다시자러감(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=10004)
        remove_balloon_talk(spawnId=10005)
        remove_balloon_talk(spawnId=10006)
        remove_balloon_talk(spawnId=10001)
        remove_balloon_talk(spawnId=10002)
        remove_balloon_talk(spawnId=10003)
        set_timer(timerId='14', seconds=4)
        set_conversation(type=1, spawnId=10004, script='$02000320_BF__WAKEUP_01__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=10005, script='$02000320_BF__WAKEUP_01__9$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=10006, script='$02000320_BF__WAKEUP_01__10$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 다시잠듬()


class 다시잠듬(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[10001,10002,10003,10004,10005,10006])
        set_timer(timerId='15', seconds=7)
        set_actor(triggerId=1004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=1006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 도둑듬()


