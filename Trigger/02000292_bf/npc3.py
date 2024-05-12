""" trigger/02000292_bf/npc3.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000622], state=1)
        self.destroy_monster(spawn_ids=[1100])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000622], state=0):
            return NPC대사(self.ctx)


class NPC대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000622], state=2)
        self.spawn_monster(spawn_ids=[1100])
        self.set_dialogue(type=1, spawn_id=1100, script='$02000292_BF__NPC3__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1100, script='$02000292_BF__NPC3__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1100])


initial_state = 시작대기중
