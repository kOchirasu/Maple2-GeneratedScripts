""" trigger/02000206_bf/barricade.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516], visible=False, arg3=0, delay=0)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=402, spawnIds=[101]):
            return 카운트(self.ctx)


class 카운트(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=50)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 차단(self.ctx)


class 차단(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516], visible=True, arg3=0, delay=200)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 차단해제(self.ctx)
        if not self.user_detected(boxIds=[402]):
            return 대기(self.ctx)


class 차단해제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516], visible=False, arg3=0, delay=200)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[402]):
            return 대기(self.ctx)


initial_state = 대기
