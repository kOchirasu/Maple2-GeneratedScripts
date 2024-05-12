""" trigger/99999946/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(triggerIds=[500,501,502,503,504,505,506,507,508,509], randomCount=10, isVisible=False)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006], animationEffect=False)
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_cube(triggerIds=[500,501,502,503,504,505,506,507,508,509], randomCount=3, isVisible=True)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
