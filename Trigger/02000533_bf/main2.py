""" trigger/02000533_bf/main2.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703], jobCode=0):
            return 서브몬스터1()


class 서브몬스터1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[601,602,607,608,609,610], arg2=False)
        move_npc(spawnId=601, patrolName='MS2PatrolData_5000')
        move_npc(spawnId=602, patrolName='MS2PatrolData_5001')
        set_npc_emotion_loop(spawnId=607, sequenceName='Sit_Down_A', duration=10000000)
        set_npc_emotion_loop(spawnId=608, sequenceName='Sit_Down_A', duration=10000000)
        set_npc_emotion_loop(spawnId=610, sequenceName='Bore_A', duration=10000000)
        add_balloon_talk(spawnId=601, msg='$02000533_BF__MAIN2__0$', duration=3500, delayTick=0)
        add_balloon_talk(spawnId=602, msg='$02000533_BF__MAIN2__1$', duration=3500, delayTick=500)
        add_balloon_talk(spawnId=601, msg='$02000533_BF__MAIN2__2$', duration=3500, delayTick=1500)
        add_balloon_talk(spawnId=607, msg='$02000533_BF__MAIN2__3$', duration=3500, delayTick=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 서브몬스터2()


class 서브몬스터2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601,602,607,608,609,610])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 서브몬스터3()


class 서브몬스터3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[6601,6602,6607,6608,6609,6610], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[6601,6602,6607,6608,6609,6610]):
            return None # Missing State: 


