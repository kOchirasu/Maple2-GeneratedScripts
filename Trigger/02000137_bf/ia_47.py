""" trigger/02000137_bf/ia_47.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000047], state=1)
        self.create_monster(spawnIds=[147])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000047], stateValue=0):
            return NPC탈출(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[147])


class NPC탈출(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[148])
        self.set_conversation(type=1, spawnId=148, script='$02000137_BF__IA_47__0$', arg4=2)
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[148])
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
