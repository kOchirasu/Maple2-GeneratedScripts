""" trigger/02000471_bf/warpcheck.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2040318, key='InteractClear', value=0)
        self.set_user_value(triggerId=2040323, key='Warp', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Boss', value=1):
            return warp_condition(self.ctx)


class warp_condition(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return end(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=70, spawnId=1999, isRelative=True):
            return warp_1st(self.ctx)


class warp_1st(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002106], state=1)
        self.set_interact_object(triggerIds=[10002107], state=1)
        self.set_mesh(triggerIds=[1207,1208], visible=True, arg3=0, delay=0, scale=0)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__0$', arg3='5000', arg4='0')
        self.add_buff(boxIds=[720], skillId=70002061, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return end(self.ctx)
        if self.wait_tick(waitTick=10000):
            return warp_go(self.ctx)
        if self.object_interacted(interactIds=[10002106], stateValue=0):
            return warp_cancel(self.ctx)
        if self.object_interacted(interactIds=[10002107], stateValue=0):
            return warp_cancel(self.ctx)


class warp_cancel(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002106], state=0)
        self.set_interact_object(triggerIds=[10002107], state=0)
        self.set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, delay=0, scale=0)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__1$', arg3='5000', arg4='0')
        self.add_buff(boxIds=[720], skillId=70002062, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return end(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=30, spawnId=1999, isRelative=True):
            return warp_2nd(self.ctx)


class warp_go(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002106], state=0)
        self.set_interact_object(triggerIds=[10002107], state=0)
        self.set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, delay=0, scale=0)
        self.set_user_value(triggerId=2040323, key='Warp', value=1)
        self.add_buff(boxIds=[720], skillId=70002062, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return end(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=30, spawnId=1999, isRelative=True):
            return warp_2nd(self.ctx)


class warp_2nd(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002106], state=1)
        self.set_interact_object(triggerIds=[10002107], state=1)
        self.set_mesh(triggerIds=[1207,1208], visible=True, arg3=0, delay=0, scale=10)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__0$', arg3='5000', arg4='0')
        self.add_buff(boxIds=[720], skillId=70002061, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return end(self.ctx)
        if self.wait_tick(waitTick=10000):
            return warp_go2(self.ctx)
        if self.object_interacted(interactIds=[10002106], stateValue=0):
            return warp2_cancel(self.ctx)
        if self.object_interacted(interactIds=[10002107], stateValue=0):
            return warp2_cancel(self.ctx)


class warp2_cancel(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002106], state=0)
        self.set_interact_object(triggerIds=[10002107], state=0)
        self.set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, delay=0, scale=0)
        self.set_event_ui(type=1, arg2='$02000471_BF__WARPCHECK__1$', arg3='5000', arg4='0')
        self.add_buff(boxIds=[720], skillId=70002062, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return end(self.ctx)
        if self.true():
            return end(self.ctx)


class warp_go2(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002106], state=0)
        self.set_interact_object(triggerIds=[10002107], state=0)
        self.set_mesh(triggerIds=[1207,1208], visible=False, arg3=0, delay=0, scale=0)
        self.set_user_value(triggerId=2040323, key='Warp', value=2)
        self.add_buff(boxIds=[720], skillId=70002062, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1999]):
            return end(self.ctx)
        if self.true():
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
