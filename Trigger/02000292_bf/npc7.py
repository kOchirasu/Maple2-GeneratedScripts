""" trigger/02000292_bf/npc7.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000626], state=1)
        self.destroy_monster(spawnIds=[1106])

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000626], stateValue=0):
            return NPC대사(self.ctx)


class NPC대사(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000626], state=2)
        self.create_monster(spawnIds=[1106])
        self.set_conversation(type=1, spawnId=1106, script='$02000292_BF__NPC7__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NPC이동(self.ctx)


class NPC이동(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1106, script='$02000292_BF__NPC7__1$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1106])


initial_state = 시작대기중
