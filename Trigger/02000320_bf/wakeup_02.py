""" trigger/02000320_bf/wakeup_02.xml """
from common import *
import state


class 자는중(state.State):
    def on_enter(self):
        set_actor(triggerId=2001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=2002, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=2003, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=2004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=2005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=2006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if true():
            return 도둑듬()


class 도둑듬(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000282], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000282], arg2=0):
            return 깨어남1()


class 깨어남1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=8)
        set_actor(triggerId=2001, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=2002, visible=True, initialSequence='Bore_A')
        set_actor(triggerId=2004, visible=False, initialSequence='Bore_A')
        set_actor(triggerId=2005, visible=False, initialSequence='Stun_A')
        set_actor(triggerId=2006, visible=False, initialSequence='Stun_A')
        create_monster(spawnIds=[20004], arg2=True)
        set_conversation(type=1, spawnId=20004, script='$02000320_BF__WAKEUP_02__0$', arg4=2, arg5=0)
        create_monster(spawnIds=[20005], arg2=True)
        set_conversation(type=1, spawnId=20005, script='$02000320_BF__WAKEUP_02__1$', arg4=2, arg5=1)
        create_monster(spawnIds=[20006], arg2=True)
        set_conversation(type=1, spawnId=20006, script='$02000320_BF__WAKEUP_02__2$', arg4=2, arg5=2)
        create_monster(spawnIds=[20001])
        create_monster(spawnIds=[20002])
        create_monster(spawnIds=[20003])
        set_conversation(type=1, spawnId=20003, script='$02000320_BF__WAKEUP_02__3$', arg4=2, arg5=3)
        set_conversation(type=1, spawnId=20001, script='$02000320_BF__WAKEUP_02__4$', arg4=2, arg5=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 깨어남2()


class 깨어남2(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=4)
        set_conversation(type=1, spawnId=20002, script='$02000320_BF__WAKEUP_02__5$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=20001, script='$02000320_BF__WAKEUP_02__6$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=20003, script='$02000320_BF__WAKEUP_02__7$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 깨어남3()


class 깨어남3(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=1)
        set_actor(triggerId=2001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=2002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 깨어남4()


class 깨어남4(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[20004,20005,20006]):
            return 다시잠듬()
        if not monster_in_combat(boxIds=[20004,20005,20006]):
            return 다시자러감()


class 다시자러감(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=20004)
        remove_balloon_talk(spawnId=20005)
        remove_balloon_talk(spawnId=20006)
        remove_balloon_talk(spawnId=20001)
        remove_balloon_talk(spawnId=20002)
        remove_balloon_talk(spawnId=20003)
        set_timer(timerId='14', seconds=4)
        set_conversation(type=1, spawnId=20004, script='$02000320_BF__WAKEUP_02__8$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=20005, script='$02000320_BF__WAKEUP_02__9$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=20006, script='$02000320_BF__WAKEUP_02__10$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 다시잠듬()


class 다시잠듬(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[20001,20002,20003,20004,20005,20006])
        set_timer(timerId='15', seconds=7)
        set_actor(triggerId=2004, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=2005, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=22006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 도둑듬()


