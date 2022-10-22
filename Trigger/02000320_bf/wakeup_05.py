""" trigger/02000320_bf/wakeup_05.xml """
from common import *
import state


class 자는중(state.State):
    def on_enter(self):
        set_actor(triggerId=5001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5002, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5003, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if true():
            return 도둑듬()


class 도둑듬(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000318], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000318], arg2=0):
            return 깨어남1()


class 깨어남1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=8)
        set_actor(triggerId=5001, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=5002, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=5004, visible=False, initialSequence='Bore_A')
        set_actor(triggerId=5005, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=5006, visible=False, initialSequence='Stun_A')
        create_monster(spawnIds=[50004], arg2=True)
        set_conversation(type=1, spawnId=50004, script='$02000320_BF__WAKEUP_05__0$', arg4=2, arg5=0)
        create_monster(spawnIds=[50005], arg2=True)
        set_conversation(type=1, spawnId=50005, script='$02000320_BF__WAKEUP_05__1$', arg4=2, arg5=1)
        create_monster(spawnIds=[50006], arg2=True)
        set_conversation(type=1, spawnId=50006, script='$02000320_BF__WAKEUP_05__2$', arg4=2, arg5=2)
        create_monster(spawnIds=[50001])
        create_monster(spawnIds=[50002])
        create_monster(spawnIds=[50003])
        set_conversation(type=1, spawnId=50003, script='$02000320_BF__WAKEUP_05__3$', arg4=2, arg5=3)
        set_conversation(type=1, spawnId=50001, script='$02000320_BF__WAKEUP_05__4$', arg4=2, arg5=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 깨어남2()


class 깨어남2(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=4)
        set_conversation(type=1, spawnId=50002, script='$02000320_BF__WAKEUP_05__5$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=50001, script='$02000320_BF__WAKEUP_05__6$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=50003, script='$02000320_BF__WAKEUP_05__7$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 깨어남3()


class 깨어남3(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=1)
        set_actor(triggerId=5001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 깨어남4()


class 깨어남4(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[50004,50005,50006]):
            return 다시잠듬()
        if not monster_in_combat(boxIds=[50004,50005,50006]):
            return 다시자러감()


class 다시자러감(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=50004)
        remove_balloon_talk(spawnId=50005)
        remove_balloon_talk(spawnId=50006)
        remove_balloon_talk(spawnId=50001)
        remove_balloon_talk(spawnId=50002)
        remove_balloon_talk(spawnId=50003)
        set_timer(timerId='14', seconds=4)
        set_conversation(type=1, spawnId=50004, script='$02000320_BF__WAKEUP_05__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=50005, script='$02000320_BF__WAKEUP_05__9$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=50006, script='$02000320_BF__WAKEUP_05__10$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 다시잠듬()


class 다시잠듬(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[50001,50002,50003,50004,50005,50006])
        set_timer(timerId='15', seconds=7)
        set_actor(triggerId=5004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=5006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 도둑듬()


