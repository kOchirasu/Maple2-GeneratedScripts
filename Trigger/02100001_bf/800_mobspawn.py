""" trigger/02100001_bf/800_mobspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='RemoveAll', value=0)
        self.destroy_monster(spawnIds=[800])
        self.set_mesh(triggerIds=[3200], visible=False, arg3=0, delay=0, scale=0) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[800], animationEffect=False)
        self.set_mesh(triggerIds=[3200], visible=True, arg3=0, delay=0, scale=0) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[800]):
            return Delay01(self.ctx)
        if self.user_value(key='RemoveAll', value=1):
            return Quit(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3200], visible=False, arg3=0, delay=0, scale=0) # Egg

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=180000):
            return MobSpawn(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[800])


initial_state = Wait
