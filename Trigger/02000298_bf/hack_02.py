""" trigger/02000298_bf/hack_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000370], state=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[116]):
            return 스폰()


class 스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1032], arg2=False)
        set_interact_object(triggerIds=[10000370], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000370], arg2=0):
            return 코드체크()


class 코드체크(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=197, spawnIds=[1279]):
            return 코드_1279()
        if npc_detected(boxId=197, spawnIds=[1238]):
            return 코드_1238()
        if npc_detected(boxId=197, spawnIds=[1358]):
            return 코드_1358()
        if npc_detected(boxId=197, spawnIds=[1489]):
            return 코드_1489()
        if npc_detected(boxId=197, spawnIds=[1567]):
            return 코드_1567()
        if npc_detected(boxId=197, spawnIds=[1679]):
            return 코드_1679()
        if npc_detected(boxId=197, spawnIds=[2389]):
            return 코드_2389()
        if npc_detected(boxId=197, spawnIds=[2347]):
            return 코드_2347()
        if npc_detected(boxId=197, spawnIds=[2478]):
            return 코드_2478()
        if npc_detected(boxId=197, spawnIds=[2456]):
            return 코드_2456()
        if npc_detected(boxId=197, spawnIds=[2569]):
            return 코드_2569()
        if npc_detected(boxId=197, spawnIds=[2678]):
            return 코드_2678()
        if npc_detected(boxId=197, spawnIds=[3458]):
            return 코드_3458()
        if npc_detected(boxId=197, spawnIds=[3589]):
            return 코드_3589()
        if npc_detected(boxId=197, spawnIds=[3679]):
            return 코드_3679()
        if npc_detected(boxId=197, spawnIds=[3789]):
            return 코드_3789()
        if npc_detected(boxId=197, spawnIds=[4567]):
            return 코드_4567()
        if npc_detected(boxId=197, spawnIds=[4578]):
            return 코드_4578()
        if npc_detected(boxId=197, spawnIds=[4689]):
            return 코드_4689()
        if npc_detected(boxId=197, spawnIds=[4789]):
            return 코드_4789()


class 코드_1279(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__0$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_1238(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__1$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_1358(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__2$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_1489(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__3$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_1567(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__4$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_1679(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__5$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_2389(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__6$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_2347(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__7$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_2478(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__8$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_2456(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__9$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_2569(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__10$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_2678(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__11$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_3458(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__12$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_3589(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__13$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_3679(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__14$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_3789(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__15$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_4567(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__16$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_4578(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__17$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_4689(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__18$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 코드_4789(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_event_ui(type=1, arg2='$02000298_BF__HACK_02__19$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


