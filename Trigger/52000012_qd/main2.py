""" trigger/52000012_qd/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_actor(triggerId=10001, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=10002, visible=True, initialSequence='Closed')
        self.set_mesh(triggerIds=[10011], visible=True)
        self.set_mesh(triggerIds=[10012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002610], questStates=[2]):
            return 문열림1(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[10002610], questStates=[3]):
            return 문열림1(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[2000], animationEffect=False)
        self.destroy_monster(spawnIds=[5000])
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])


class 문열림1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='19', seconds=1)
        self.set_actor(triggerId=10001, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[10011], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='19'):
            return 문열림2(self.ctx)


class 문열림2(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=10002, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[10012], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[10002611], questStates=[2]):
            return 포털생성(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[10002611], questStates=[3]):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9001]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
