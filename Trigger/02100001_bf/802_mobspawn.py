""" trigger/02100001_bf/802_mobspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='RemoveAll', value=0)
        self.destroy_monster(spawn_ids=[802])
        self.set_mesh(trigger_ids=[3202], visible=False, start_delay=0, interval=0, fade=0) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[802], auto_target=False)
        self.set_mesh(trigger_ids=[3202], visible=True, start_delay=0, interval=0, fade=0) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[802]):
            return Delay01(self.ctx)
        if self.user_value(key='RemoveAll') >= 1:
            return Quit(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3202], visible=False, start_delay=0, interval=0, fade=0) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=180000):
            # 리스폰 딜레이
            return MobSpawn(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[802])


initial_state = Wait
