""" trigger/02000535_bf/main2.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[707], jobCode=0):
            return 데코지우고몬스터스폰()


class 데코지우고몬스터스폰(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[5501,5502,5503,5504,5505,5520,5521,5522,5523,5532])
        create_monster(spawnIds=[501,522,532,533,534,535,536,537,538], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[501,522,532,533,534,535,536,537,538]):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5501,5502,5503,5504,5505,5520,5521,5522,5523,5532])
        destroy_monster(spawnIds=[501,522,532,533,534,535,536,537,538])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 끝()


