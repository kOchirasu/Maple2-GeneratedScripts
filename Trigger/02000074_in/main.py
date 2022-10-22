""" trigger/02000074_in/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4000], visible=False)
        destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001592], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[9000], questIds=[50001592], questStates=[2]):
            return 쪽지스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001592], questStates=[1]):
            return 쪽지스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001591], questStates=[3]):
            return 쪽지스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001591], questStates=[2]):
            return 쪽지스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001589], questStates=[2]):
            return 케이틀린스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001589], questStates=[1]):
            return 케이틀린스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001588], questStates=[3]):
            return 케이틀린스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001588], questStates=[2]): # 
            return 케이틀린스폰()


class 케이틀린스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # 연출용 어둠의 세력 몬스터

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return start()


class 쪽지스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        set_mesh(triggerIds=[4000], visible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return start()


class 종료(state.State):
    pass


