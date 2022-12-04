""" trigger/02100001_bf/600_mobspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='RemoveAll', value=0)
        self.destroy_monster(spawnIds=[600,601,602,603,604,701,702,703,704,705])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn(self.ctx)


class MobSpawn(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[600,601,602,603,604,701,702,703,704,705], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RemoveAll', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[600,601,602,603,604,701,702,703,704,705])


initial_state = Wait
