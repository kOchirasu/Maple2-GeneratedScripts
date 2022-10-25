""" trigger/99999908/main.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[1,1,1])
        self.set_directional_light(diffuseColor=[1,1,1], specularColor=[0,0,0])
        self.set_timer(timerId='240', seconds=240, startDelay=1, interval=1)


class switch(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5500):
            return 시작(self.ctx)


initial_state = 시작
