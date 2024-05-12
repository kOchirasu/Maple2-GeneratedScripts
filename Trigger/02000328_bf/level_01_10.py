""" trigger/02000328_bf/level_01_10.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(triggerIds=[5110], isVisible=False)
        # self.create_monster(spawnIds=[10010], animationEffect=True)
        self.set_mesh(triggerIds=[32001,32002,32003,32004,32005,32006,32007,32008,32009,32010,32011,32012,32013,32014,32015,32016,32017,32018,32019,32020,32021,32022], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[42001], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10006]):
            # self.set_cube(triggerIds=[5110], isVisible=True)
            self.set_mesh(triggerIds=[32001,32002,32003,32004,32005,32006,32007,32008,32009,32010,32011,32012,32013,32014,32015,32016,32017,32018,32019,32020,32021,32022], visible=True, arg3=0, delay=200, scale=2)
            self.set_mesh(triggerIds=[42001], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
