""" trigger/02000328_bf/level_01_15.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cube(triggerIds=[5115], isVisible=False)
        # self.create_monster(spawnIds=[10015], animationEffect=True)
        self.set_mesh(triggerIds=[32501,32502,32503,32504,32505,32506,32507,32508,32509,32510,32511,32512,32513,32514,32515,32516,32517,32518,32519,32520,32521,32522,32523,32524,32525,32526,32527,32528,32529,32530,32531,32532,32533,32534,32535,32536,32537,32538], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[8100,8101,8102,8103,8104,8105,8106,8107,8108,8109,8110,8111,8112,8113,8114,8115], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[8200,8201,8202,8203,8204,8205,8206,8207,8208,8209,8210,8211,8212,8213,8214,8215], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[10015]):
            self.set_cube(triggerIds=[5115], isVisible=True)
            self.set_mesh(triggerIds=[32501,32502,32503,32504,32505,32506,32507,32508,32509,32510,32511,32512,32513,32514,32515,32516,32517,32518,32519,32520,32521,32522,32523,32524,32525,32526,32527,32528,32529,32530,32531,32532,32533,32534,32535,32536,32537,32538], visible=True, arg3=0, delay=100, scale=1)
            self.set_mesh(triggerIds=[8100,8101,8102,8103,8104,8105,8106,8107,8108,8109,8110,8111,8112,8113,8114,8115], visible=True, arg3=0, delay=100, scale=1)
            self.set_mesh(triggerIds=[8200,8201,8202,8203,8204,8205,8206,8207,8208,8209,8210,8211,8212,8213,8214,8215], visible=False, arg3=500, delay=100, scale=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
