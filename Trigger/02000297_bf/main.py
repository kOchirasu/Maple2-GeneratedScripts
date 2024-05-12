""" trigger/02000297_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[6100])
        self.destroy_monster(spawn_ids=[6200])
        self.set_agent(trigger_ids=[101], visible=False)
        self.set_agent(trigger_ids=[102], visible=False)
        self.set_agent(trigger_ids=[103], visible=False)
        self.set_agent(trigger_ids=[104], visible=False)
        self.set_agent(trigger_ids=[105], visible=False)
        self.set_agent(trigger_ids=[106], visible=False)
        self.set_agent(trigger_ids=[121], visible=False)
        self.set_agent(trigger_ids=[122], visible=False)
        self.set_agent(trigger_ids=[123], visible=False)
        self.set_agent(trigger_ids=[124], visible=False)
        self.set_agent(trigger_ids=[125], visible=False)
        self.set_agent(trigger_ids=[126], visible=False)
        self.set_agent(trigger_ids=[127], visible=False)
        self.set_agent(trigger_ids=[128], visible=False)
        self.set_user_value(key='BattleStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleStart') >= 1:
            return LoadingDelay02(self.ctx)


class LoadingDelay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02000297_BF__MAIN__0$', arg3='5000', arg4='0')
        self.set_agent(trigger_ids=[101], visible=True)
        self.set_agent(trigger_ids=[102], visible=True)
        self.set_agent(trigger_ids=[103], visible=True)
        self.set_agent(trigger_ids=[104], visible=True)
        self.set_agent(trigger_ids=[105], visible=True)
        self.set_agent(trigger_ids=[106], visible=True)
        self.set_agent(trigger_ids=[121], visible=True)
        self.set_agent(trigger_ids=[122], visible=True)
        self.set_agent(trigger_ids=[123], visible=True)
        self.set_agent(trigger_ids=[124], visible=True)
        self.set_agent(trigger_ids=[125], visible=True)
        self.set_agent(trigger_ids=[126], visible=True)
        self.set_agent(trigger_ids=[127], visible=True)
        self.set_agent(trigger_ids=[128], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BossBattle02(self.ctx)


class BossBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[6100])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[6200]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = 대기
