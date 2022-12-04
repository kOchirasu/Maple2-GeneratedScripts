""" trigger/80000013_bonus/mob_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[104]):
            return wait(self.ctx)


class wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[701]):
            return start(self.ctx)
        if self.wait_tick(waitTick=1500):
            return idle(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
