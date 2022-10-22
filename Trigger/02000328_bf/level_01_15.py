""" trigger/02000328_bf/level_01_15.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5115], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10015" arg2="1" />
        set_mesh(triggerIds=[32501,32502,32503,32504,32505,32506,32507,32508,32509,32510,32511,32512,32513,32514,32515,32516,32517,32518,32519,32520,32521,32522,32523,32524,32525,32526,32527,32528,32529,32530,32531,32532,32533,32534,32535,32536,32537,32538], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[8100,8101,8102,8103,8104,8105,8106,8107,8108,8109,8110,8111,8112,8113,8114,8115], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[8200,8201,8202,8203,8204,8205,8206,8207,8208,8209,8210,8211,8212,8213,8214,8215], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10015]):
            set_cube(triggerIds=[5115], isVisible=True)
            set_mesh(triggerIds=[32501,32502,32503,32504,32505,32506,32507,32508,32509,32510,32511,32512,32513,32514,32515,32516,32517,32518,32519,32520,32521,32522,32523,32524,32525,32526,32527,32528,32529,32530,32531,32532,32533,32534,32535,32536,32537,32538], visible=True, arg3=0, arg4=100, arg5=1)
            set_mesh(triggerIds=[8100,8101,8102,8103,8104,8105,8106,8107,8108,8109,8110,8111,8112,8113,8114,8115], visible=True, arg3=0, arg4=100, arg5=1)
            set_mesh(triggerIds=[8200,8201,8202,8203,8204,8205,8206,8207,8208,8209,8210,8211,8212,8213,8214,8215], visible=False, arg3=500, arg4=100, arg5=1)
            return 종료()


class 종료(state.State):
    pass


