""" trigger/02000500_bf/barricade.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1099]):
            return 초대기3(self.ctx)


class 초대기3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카운트(self.ctx)


class 카운트(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526], visible=True, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1099]):
            return 차단해제(self.ctx)


class 차단해제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526], visible=False, arg3=0, delay=200, scale=2)


initial_state = 대기
