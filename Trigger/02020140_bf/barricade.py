""" trigger/02020140_bf/barricade.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 칸막이대기시작()


class 칸막이대기시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_mesh(triggerIds=[608], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[609], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 칸막이대기알림()


class 칸막이대기알림(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020140_BF__BARRICADE__0$', arg3='3000')
        dungeon_enable_give_up(isEnable='1')

    def on_tick(self) -> state.State:
        if dungeon_time_out():
            return 던전실패종료()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패종료()
        if wait_tick(waitTick=30000):
            return 칸막이막기()


class 칸막이막기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[605], visible=True)
        set_mesh(triggerIds=[608], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[609], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if dungeon_time_out():
            return 던전실패종료()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패종료()


class 던전실패종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_mesh(triggerIds=[608], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[609], visible=False, arg3=0, arg4=0, arg5=0)


