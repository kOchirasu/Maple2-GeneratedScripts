""" trigger/02000297_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[6100])
        self.destroy_monster(spawnIds=[6200])
        self.set_agent(triggerIds=[101], visible=False)
        self.set_agent(triggerIds=[102], visible=False)
        self.set_agent(triggerIds=[103], visible=False)
        self.set_agent(triggerIds=[104], visible=False)
        self.set_agent(triggerIds=[105], visible=False)
        self.set_agent(triggerIds=[106], visible=False)
        self.set_agent(triggerIds=[121], visible=False)
        self.set_agent(triggerIds=[122], visible=False)
        self.set_agent(triggerIds=[123], visible=False)
        self.set_agent(triggerIds=[124], visible=False)
        self.set_agent(triggerIds=[125], visible=False)
        self.set_agent(triggerIds=[126], visible=False)
        self.set_agent(triggerIds=[127], visible=False)
        self.set_agent(triggerIds=[128], visible=False)
        self.set_user_value(key='BattleStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleStart', value=1):
            return LoadingDelay02(self.ctx)


class LoadingDelay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9000], sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02000297_BF__MAIN__0$', arg3='5000', arg4='0')
        self.set_agent(triggerIds=[101], visible=True)
        self.set_agent(triggerIds=[102], visible=True)
        self.set_agent(triggerIds=[103], visible=True)
        self.set_agent(triggerIds=[104], visible=True)
        self.set_agent(triggerIds=[105], visible=True)
        self.set_agent(triggerIds=[106], visible=True)
        self.set_agent(triggerIds=[121], visible=True)
        self.set_agent(triggerIds=[122], visible=True)
        self.set_agent(triggerIds=[123], visible=True)
        self.set_agent(triggerIds=[124], visible=True)
        self.set_agent(triggerIds=[125], visible=True)
        self.set_agent(triggerIds=[126], visible=True)
        self.set_agent(triggerIds=[127], visible=True)
        self.set_agent(triggerIds=[128], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BossBattle02(self.ctx)


class BossBattle02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[6100])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[6200]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = 대기
