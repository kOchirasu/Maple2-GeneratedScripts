""" trigger/02100009_bf/barricade.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[80000], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if check_user():
            return CheckUser10_GuildRaid()


class CheckUser10_GuildRaid(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True, display=False, arg5=0) # 최대 30초 대기

    def on_tick(self) -> state.State:
        if count_users(boxId=102, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if count_users(boxId=102, boxId=10, operator='Less'):
            return MaxCount10_Wait()


class MaxCount10_Wait(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> state.State:
        if count_users(boxId=102, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if time_expired(timerId='1'):
            return MaxCount10_Start()
        if wait_tick(waitTick=6000):
            return MaxCount10_Wait()


class MaxCount10_Start(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if true():
            return state.DungeonStart()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        select_camera(triggerId=904, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ShowCaption01()

state.DungeonStart = DungeonStart


#  설명문 출력 
class ShowCaption01(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100009_BF__BARRICADE__0$')
        set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return ShowCaption01Skip()


class ShowCaption01Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption02()


class ShowCaption02(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100009_BF__BARRICADE__1$')
        set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return ShowCaption02Skip()


class ShowCaption02Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CloseCaptionSetting()


class CloseCaptionSetting(state.State):
    def on_enter(self):
        close_cinematic()
        select_camera(triggerId=904, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False)
        set_effect(triggerIds=[7002], visible=False)
        set_effect(triggerIds=[7003], visible=False)
        set_effect(triggerIds=[7004], visible=False)
        set_mesh(triggerIds=[8000], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if any_one():
            return 유저감지()


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02100009_BF__BARRICADE__2$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8000], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[7001], visible=True)
        set_effect(triggerIds=[7002], visible=True)
        set_effect(triggerIds=[7003], visible=True)
        set_effect(triggerIds=[7004], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[100000001,100000002]):
            return 차단해제()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8000], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[7001], visible=False)
        set_effect(triggerIds=[7002], visible=False)
        set_effect(triggerIds=[7003], visible=False)
        set_effect(triggerIds=[7004], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 종료(state.State):
    pass


