""" trigger/02000320_bf/wakeup_09.xml """
from common import *
import state


class 자는중(state.State):
    def on_enter(self):
        set_actor(triggerId=9001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9002, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9003, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if true():
            return 도둑듬()


class 도둑듬(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000353], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000353], arg2=0):
            return 깨어남1()


class 깨어남1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=8)
        set_actor(triggerId=9001, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=9002, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=9004, visible=False, initialSequence='Bore_A')
        set_actor(triggerId=9005, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=9006, visible=False, initialSequence='Stun_A')
        create_monster(spawnIds=[90004], arg2=True)
        set_conversation(type=1, spawnId=90004, script='$02000320_BF__WAKEUP_09__0$', arg4=2, arg5=0)
        create_monster(spawnIds=[90005], arg2=True)
        set_conversation(type=1, spawnId=90005, script='$02000320_BF__WAKEUP_09__1$', arg4=2, arg5=1)
        create_monster(spawnIds=[90006], arg2=True)
        set_conversation(type=1, spawnId=90006, script='$02000320_BF__WAKEUP_09__2$', arg4=2, arg5=2)
        create_monster(spawnIds=[90001])
        create_monster(spawnIds=[90002])
        create_monster(spawnIds=[90003])
        set_conversation(type=1, spawnId=90003, script='$02000320_BF__WAKEUP_09__3$', arg4=2, arg5=3)
        set_conversation(type=1, spawnId=90001, script='$02000320_BF__WAKEUP_09__4$', arg4=2, arg5=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 깨어남2()


class 깨어남2(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=4)
        set_conversation(type=1, spawnId=90002, script='$02000320_BF__WAKEUP_09__5$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=90001, script='$02000320_BF__WAKEUP_09__6$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=90003, script='$02000320_BF__WAKEUP_09__7$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 깨어남3()


class 깨어남3(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=1)
        set_actor(triggerId=9001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 깨어남4()


class 깨어남4(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90004,90005,90006]):
            return 다시잠듬()
        if not monster_in_combat(boxIds=[90004,90005,90006]):
            return 다시자러감()


class 다시자러감(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=90004)
        remove_balloon_talk(spawnId=90005)
        remove_balloon_talk(spawnId=90006)
        remove_balloon_talk(spawnId=90001)
        remove_balloon_talk(spawnId=90002)
        remove_balloon_talk(spawnId=90003)
        set_timer(timerId='14', seconds=4)
        set_conversation(type=1, spawnId=90004, script='$02000320_BF__WAKEUP_09__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=90005, script='$02000320_BF__WAKEUP_09__9$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=90006, script='$02000320_BF__WAKEUP_09__10$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 다시잠듬()


class 다시잠듬(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[90001,90002,90003,90004,90005,90006])
        set_timer(timerId='15', seconds=7)
        set_actor(triggerId=9004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=9006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 도둑듬()


