""" trigger/02000471_bf/warp.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp', value=1):
            return warp_1st(self.ctx)


class warp_1st(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=17):
            return warp_1(self.ctx)
        if self.random_condition(rate=17):
            return warp_2(self.ctx)
        if self.random_condition(rate=16):
            return warp_3(self.ctx)
        if self.random_condition(rate=17):
            return warp_4(self.ctx)
        if self.random_condition(rate=16):
            return warp_5(self.ctx)
        if self.random_condition(rate=17):
            return warp_6(self.ctx)


class warp_1(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=11, triggerId=720, count=1)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp', value=2):
            return warp_2nd(self.ctx)


class warp_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=12, triggerId=720, count=1)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp', value=2):
            return warp_2nd(self.ctx)


class warp_3(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=13, triggerId=720, count=1)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp', value=2):
            return warp_2nd(self.ctx)


class warp_4(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=14, triggerId=720, count=1)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp', value=2):
            return warp_2nd(self.ctx)


class warp_5(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=15, triggerId=720, count=1)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp', value=2):
            return warp_2nd(self.ctx)


class warp_6(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=16, triggerId=720, count=1)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Warp', value=2):
            return warp_2nd(self.ctx)


class warp_2nd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=17):
            return warp2_1(self.ctx)
        if self.random_condition(rate=17):
            return warp2_2(self.ctx)
        if self.random_condition(rate=16):
            return warp2_3(self.ctx)
        if self.random_condition(rate=17):
            return warp2_4(self.ctx)
        if self.random_condition(rate=16):
            return warp2_5(self.ctx)
        if self.random_condition(rate=17):
            return warp2_6(self.ctx)


class warp2_1(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=11, triggerId=720, count=2)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_2(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=12, triggerId=720, count=2)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_3(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=13, triggerId=720, count=2)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_4(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=14, triggerId=720, count=2)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_5(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=15, triggerId=720, count=2)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


class warp2_6(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000471, portalId=16, triggerId=720, count=2)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARP__0$', arg3='3000', arg4='0')


initial_state = idle
