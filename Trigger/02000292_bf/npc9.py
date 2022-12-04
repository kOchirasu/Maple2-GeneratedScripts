""" trigger/02000292_bf/npc9.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000628], state=1)
        self.destroy_monster(spawnIds=[1108])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000628], stateValue=0):
            return NPC대사(self.ctx)


class NPC대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000628], state=2)
        self.create_monster(spawnIds=[1108])
        self.set_conversation(type=1, spawnId=1108, script='$02000292_BF__NPC9__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1108, script='$02000292_BF__NPC9__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1108])


initial_state = 시작대기중
