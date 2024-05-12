""" trigger/02000095_bf/quest_music.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[101], visible=False)
        self.set_interact_object(triggerIds=[10000465], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000465], stateValue=0):
            return NPC대화(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[892])
        self.create_monster(spawnIds=[893])
        self.create_monster(spawnIds=[894])


class NPC대화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=892, script='$02000095_BF__QUEST_MUSIC__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=893, script='$02000095_BF__QUEST_MUSIC__1$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=894, script='$02000095_BF__QUEST_MUSIC__2$', arg4=2, arg5=4)
        self.set_timer(timerId='1', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[101], visible=True)
        self.destroy_monster(spawnIds=[892])
        self.destroy_monster(spawnIds=[893])
        self.destroy_monster(spawnIds=[894])
        self.set_timer(timerId='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
