""" trigger/02000471_bf/warpcheck.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040318, key='InteractClear', value=0)
        set_user_value(triggerId=2040323, key='Warp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Boss', value=1):
            return warp_condition()


class warp_condition(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return end()
        if check_npc_hp(compare='lowerEqual', value=70, spawnId=1999, isRelative=True):
            return warp_1st()


class warp_1st(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002106], state=1)
        set_interact_object(triggerIds=[10002107], state=1)
        set_mesh(triggerIds=[1207,1208], visible=True, arg3=0, arg4=0, arg5=0)
        set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__0$', arg3='5000', arg4='0')
        add_buff(boxIds=[720], skillId=70002061, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return end()
        if wait_tick(waitTick=10000):
            return warp_go()
        if object_interacted(interactIds=[10002106], arg2=0):
            return warp_cancel()
        if object_interacted(interactIds=[10002107], arg2=0):
            return warp_cancel()


class warp_cancel(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002106], state=0)
        set_interact_object(triggerIds=[10002107], state=0)
        set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, arg4=0, arg5=0)
        set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__1$', arg3='5000', arg4='0')
        add_buff(boxIds=[720], skillId=70002062, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return end()
        if check_npc_hp(compare='lowerEqual', value=30, spawnId=1999, isRelative=True):
            return warp_2nd()


class warp_go(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002106], state=0)
        set_interact_object(triggerIds=[10002107], state=0)
        set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, arg4=0, arg5=0)
        set_user_value(triggerId=2040323, key='Warp', value=1)
        add_buff(boxIds=[720], skillId=70002062, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return end()
        if check_npc_hp(compare='lowerEqual', value=30, spawnId=1999, isRelative=True):
            return warp_2nd()


class warp_2nd(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002106], state=1)
        set_interact_object(triggerIds=[10002107], state=1)
        set_mesh(triggerIds=[1207,1208], visible=True, arg3=0, arg4=0, arg5=10)
        set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__0$', arg3='5000', arg4='0')
        add_buff(boxIds=[720], skillId=70002061, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return end()
        if wait_tick(waitTick=10000):
            return warp_go2()
        if object_interacted(interactIds=[10002106], arg2=0):
            return warp2_cancel()
        if object_interacted(interactIds=[10002107], arg2=0):
            return warp2_cancel()


class warp2_cancel(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002106], state=0)
        set_interact_object(triggerIds=[10002107], state=0)
        set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, arg4=0, arg5=0)
        set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__1$', arg3='5000', arg4='0')
        add_buff(boxIds=[720], skillId=70002062, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return end()
        if true():
            return end()


class warp_go2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002106], state=0)
        set_interact_object(triggerIds=[10002107], state=0)
        set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, arg4=0, arg5=0)
        set_user_value(triggerId=2040323, key='Warp', value=2)
        add_buff(boxIds=[720], skillId=70002062, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1999]):
            return end()
        if true():
            return end()


class end(state.State):
    pass


