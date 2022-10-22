""" trigger/02000471_bf/warp.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Warp', value=1):
            return warp_1st()


class warp_1st(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return warp_1()
        if random_condition(rate=17):
            return warp_2()
        if random_condition(rate=16):
            return warp_3()
        if random_condition(rate=17):
            return warp_4()
        if random_condition(rate=16):
            return warp_5()
        if random_condition(rate=17):
            return warp_6()


class warp_1(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=11, triggerId=720, count=1)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if user_value(key='Warp', value=2):
            return warp_2nd()


class warp_2(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=12, triggerId=720, count=1)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if user_value(key='Warp', value=2):
            return warp_2nd()


class warp_3(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=13, triggerId=720, count=1)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if user_value(key='Warp', value=2):
            return warp_2nd()


class warp_4(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=14, triggerId=720, count=1)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if user_value(key='Warp', value=2):
            return warp_2nd()


class warp_5(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=15, triggerId=720, count=1)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if user_value(key='Warp', value=2):
            return warp_2nd()


class warp_6(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=16, triggerId=720, count=1)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if user_value(key='Warp', value=2):
            return warp_2nd()


class warp_2nd(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return warp2_1()
        if random_condition(rate=17):
            return warp2_2()
        if random_condition(rate=16):
            return warp2_3()
        if random_condition(rate=17):
            return warp2_4()
        if random_condition(rate=16):
            return warp2_5()
        if random_condition(rate=17):
            return warp2_6()


class warp2_1(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=11, triggerId=720, count=2)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_2(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=12, triggerId=720, count=2)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_3(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=13, triggerId=720, count=2)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_4(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=14, triggerId=720, count=2)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_5(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=15, triggerId=720, count=2)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_6(state.State):
    def on_enter(self):
        move_random_user(mapId=2000471, portalId=16, triggerId=720, count=2)
        set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


