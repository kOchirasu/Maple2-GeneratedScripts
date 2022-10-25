""" trigger/02000213_bf/barricade.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1099]):
            return 카운트(self.ctx)


class 카운트(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 차단(self.ctx)


class 차단(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515], visible=True, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1099]):
            return 차단해제(self.ctx)


class 차단해제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515], visible=False, arg3=0, delay=200, scale=2)


initial_state = 대기
