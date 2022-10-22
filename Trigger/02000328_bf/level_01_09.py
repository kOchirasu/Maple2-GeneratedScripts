""" trigger/02000328_bf/level_01_09.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5109], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10009" arg2="1" />
        set_mesh(triggerIds=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919,31920,31921,31922], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41901], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10006]):
            set_mesh(triggerIds=[31901,31902,31903,31904,31905,31906,31907,31908,31909,31910,31911,31912,31913,31914,31915,31916,31917,31918,31919,31920,31921,31922], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41901], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


