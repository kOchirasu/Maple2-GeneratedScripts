""" trigger/52000051_qd/01_main.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3500,3501], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_IronDoor
        set_mesh(triggerIds=[3010,3011,3012,3013], visible=True, arg3=0, arg4=0, arg5=0) # Barrier
        set_mesh(triggerIds=[3014], visible=True, arg3=0, arg4=0, arg5=0) # FrontBarrier
        set_mesh(triggerIds=[3030], visible=True, arg3=0, arg4=0, arg5=0) # GatePortal
        set_actor(triggerId=4001, visible=True, initialSequence='Closed') # IronDoor
        set_actor(triggerId=4002, visible=True, initialSequence='Closed') # IronDoor
        set_actor(triggerId=4000, visible=True, initialSequence='or_fi_struc_stonegate_A01_off') # StoneGate
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # StoneGate 사운드 이펙트
        set_effect(triggerIds=[5004], visible=False) # MetalDoorOpen 사운드 이펙트
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_user_value(key='FindLotus', value=0)
        set_user_value(key='PuzzleSolved', value=0)
        set_user_value(key='PatrolEnd', value=0)
        create_monster(spawnIds=[900], arg2=False) # 어둠의 토템

    def on_tick(self) -> state.State:
        if count_users(boxId=9000, boxId=1):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SetDarkness01()


class SetDarkness01(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        create_monster(spawnIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826], arg2=False) # 연출용 검은 그림자
        create_monster(spawnIds=[950,951,952,953,955,956,957,958,959,962,963,964,967,970,974,975,976,977,978,980,981,982], arg2=False) # 미혹의 령 일부 제거 954,960,961,965,966,968,969,971,972,973,979

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SetDarkness02()


class SetDarkness02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[100,200], arg2=False)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcCinematic01()


class NpcCinematic01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000051_QD__01_MAIN__0$', arg4=5) # 틴차이
        set_skip(state=NpcCinematic01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NpcCinematic01Skip()


class NpcCinematic01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NpcCinematic02()


class NpcCinematic02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001708, script='$52000051_QD__01_MAIN__1$', arg4=5) # 틴차이
        set_skip(state=NpcCinematic02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NpcCinematic02Skip()


class NpcCinematic02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return NpcCinematic03()


class NpcCinematic03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        move_npc(spawnId=100, patrolName='MS2PatrolData_110')
        move_user_path(patrolName='MS2PatrolData_1001')
        set_conversation(type=2, spawnId=11001708, script='$52000051_QD__01_MAIN__2$', arg4=3) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcCinematic04()


class NpcCinematic04(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_210')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcCinematic05()


class NpcCinematic05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001557, script='$52000051_QD__01_MAIN__3$', arg4=5) # 준타
        set_skip(state=NpcCinematic05Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return NpcCinematic05Skip()


class NpcCinematic05Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=601, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_user_value(triggerId=9, key='FindLotus', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcMonologue01()


class NpcMonologue01(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001022], arg2=0):
            return NpcMonologue02()


class NpcMonologue02(state.State):
    def on_enter(self):
        move_npc(spawnId=200, patrolName='MS2PatrolData_200')
        move_npc(spawnId=100, patrolName='MS2PatrolData_100')
        set_conversation(type=1, spawnId=200, script='$52000051_QD__01_MAIN__4$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcPatrol01()


class NpcPatrol01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3014], visible=False, arg3=0, arg4=0, arg5=0) # FrontBarrier
        set_user_value(triggerId=10, key='PatrolStart', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcPatrol02()


class NpcPatrol02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52000051_QD__01_MAIN__5$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if user_value(key='PatrolEnd', value=1):
            return NpcPatrol03()
        if monster_dead(boxIds=[900]):
            return NpcChange01()


class NpcPatrol03(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9400, spawnIds=[202]):
            return NpcPatrol04()
        if monster_dead(boxIds=[900]):
            return NpcChange01()


class NpcPatrol04(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9400, boxId=1):
            return FoundTotem01()
        if monster_dead(boxIds=[900]):
            return NpcChange01()


#  20170223 업데이트 던전 개편 단축 
class NpcChange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])
        destroy_monster(spawnIds=[102,202])
        create_monster(spawnIds=[105,205], arg2=False) # 연출용

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RemoveTotem02()


class NpcChange02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])
        destroy_monster(spawnIds=[102,202])
        destroy_monster(spawnIds=[103,203]) # 전투
        create_monster(spawnIds=[105,205], arg2=False) # 연출용
        remove_balloon_talk(spawnId=203)
        remove_balloon_talk(spawnId=103)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RemoveTotem02()


class FoundTotem01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])
        destroy_monster(spawnIds=[102,202])
        create_monster(spawnIds=[103,203], arg2=False) # 전투
        set_conversation(type=1, spawnId=203, script='$02000376_BF__01_MAIN__3$', arg4=3, arg5=0) # 준타
        set_conversation(type=1, spawnId=103, script='$02000376_BF__01_MAIN__4$', arg4=3, arg5=2) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return RemoveTotem01()
        if monster_dead(boxIds=[900]):
            return NpcChange02()


class RemoveTotem01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return RemoveTotem02()

    def on_exit(self):
        destroy_monster(spawnIds=[101,201])
        destroy_monster(spawnIds=[102,202])
        destroy_monster(spawnIds=[103,203]) # 전투
        create_monster(spawnIds=[105,205], arg2=False)
        remove_balloon_talk(spawnId=203)
        remove_balloon_talk(spawnId=103)


class RemoveTotem02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102,202])
        move_npc(spawnId=950, patrolName='MS2PatrolData_850')
        move_npc(spawnId=951, patrolName='MS2PatrolData_851')
        move_npc(spawnId=952, patrolName='MS2PatrolData_852')
        move_npc(spawnId=953, patrolName='MS2PatrolData_853') # action name="NPC를이동시킨다" arg1="954" arg2="MS2PatrolData_854" /
        move_npc(spawnId=955, patrolName='MS2PatrolData_855')
        move_npc(spawnId=956, patrolName='MS2PatrolData_856')
        move_npc(spawnId=957, patrolName='MS2PatrolData_857')
        move_npc(spawnId=958, patrolName='MS2PatrolData_858')
        move_npc(spawnId=959, patrolName='MS2PatrolData_859') # action name="NPC를이동시킨다" arg1="960" arg2="MS2PatrolData_860" /
        move_npc(spawnId=962, patrolName='MS2PatrolData_862')
        move_npc(spawnId=963, patrolName='MS2PatrolData_863')
        move_npc(spawnId=964, patrolName='MS2PatrolData_864') # action name="NPC를이동시킨다" arg1="965" arg2="MS2PatrolData_865" /
        move_npc(spawnId=967, patrolName='MS2PatrolData_867') # action name="NPC를이동시킨다" arg1="968" arg2="MS2PatrolData_868" /
        move_npc(spawnId=970, patrolName='MS2PatrolData_870') # action name="NPC를이동시킨다" arg1="971" arg2="MS2PatrolData_871" /
        move_npc(spawnId=974, patrolName='MS2PatrolData_874')
        move_npc(spawnId=975, patrolName='MS2PatrolData_875')
        move_npc(spawnId=976, patrolName='MS2PatrolData_876')
        move_npc(spawnId=977, patrolName='MS2PatrolData_877')
        move_npc(spawnId=978, patrolName='MS2PatrolData_878') # action name="NPC를이동시킨다" arg1="979" arg2="MS2PatrolData_879" /
        move_npc(spawnId=980, patrolName='MS2PatrolData_880')
        move_npc(spawnId=981, patrolName='MS2PatrolData_881')
        move_npc(spawnId=982, patrolName='MS2PatrolData_882')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RemoveTotem03()


#  미혹의 령 일부 제거 954,960,961,965,966,968,969,971,973,979 
class RemoveTotem03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102,202])
        change_monster(removeSpawnId=950, addSpawnId=850)
        change_monster(removeSpawnId=951, addSpawnId=851)
        change_monster(removeSpawnId=952, addSpawnId=852)
        change_monster(removeSpawnId=953, addSpawnId=853) # action name="몬스터를변경한다" arg1="954" arg2="854" /
        change_monster(removeSpawnId=955, addSpawnId=855)
        change_monster(removeSpawnId=956, addSpawnId=856)
        change_monster(removeSpawnId=957, addSpawnId=857)
        change_monster(removeSpawnId=958, addSpawnId=858)
        change_monster(removeSpawnId=959, addSpawnId=859) # action name="몬스터를변경한다" arg1="960" arg2="860" /
        change_monster(removeSpawnId=962, addSpawnId=862)
        change_monster(removeSpawnId=963, addSpawnId=863)
        change_monster(removeSpawnId=964, addSpawnId=864) # action name="몬스터를변경한다" arg1="965" arg2="865" /
        change_monster(removeSpawnId=967, addSpawnId=867) # action name="몬스터를변경한다" arg1="968" arg2="868" /
        change_monster(removeSpawnId=969, addSpawnId=869)
        change_monster(removeSpawnId=970, addSpawnId=870) # action name="몬스터를변경한다" arg1="971" arg2="871" /
        change_monster(removeSpawnId=974, addSpawnId=874)
        change_monster(removeSpawnId=975, addSpawnId=875)
        change_monster(removeSpawnId=976, addSpawnId=876)
        change_monster(removeSpawnId=977, addSpawnId=877)
        change_monster(removeSpawnId=978, addSpawnId=878) # action name="몬스터를변경한다" arg1="979" arg2="879" /
        change_monster(removeSpawnId=980, addSpawnId=880)
        change_monster(removeSpawnId=981, addSpawnId=881)
        change_monster(removeSpawnId=982, addSpawnId=882)
        set_conversation(type=1, spawnId=105, script='$52000051_QD__01_MAIN__8$', arg4=3, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RemoveTotem04()


class RemoveTotem04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=205, script='$52000051_QD__01_MAIN__9$', arg4=3, arg5=1) # 준타
        move_npc(spawnId=105, patrolName='MS2PatrolData_106')
        move_npc(spawnId=205, patrolName='MS2PatrolData_206')
        set_mesh(triggerIds=[3500,3501], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_IronDoor
        set_actor(triggerId=4002, visible=True, initialSequence='Opened') # IronDoor
        set_actor(triggerId=4001, visible=True, initialSequence='Opened') # IronDoor
        set_effect(triggerIds=[5004], visible=True) # MetalDoorOpen 사운드 이펙트
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FoundGate01()


class FoundGate01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=205, script='$52000051_QD__01_MAIN__10$', arg4=3, arg5=0) # 준타
        move_npc(spawnId=105, patrolName='MS2PatrolData_107')
        move_npc(spawnId=205, patrolName='MS2PatrolData_207')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9500, spawnIds=[105]):
            return FoundGate02()


class FoundGate02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=105, script='$52000051_QD__01_MAIN__11$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9501, spawnIds=[105]):
            return ShadowApp01()


class ShadowApp01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=205, script='$52000051_QD__01_MAIN__12$', arg4=2, arg5=0) # 준타
        create_monster(spawnIds=[901,903,905], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ShadowApp02()


class ShadowApp02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105,205]) # 전투
        create_monster(spawnIds=[106,206], arg2=False)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$52000051_QD__01_MAIN__13$', arg3='3000', arg4='0')
        create_monster(spawnIds=[914,916,918], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ShadowApp03()


class ShadowApp03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[921,926,928], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ShadowApp04()


class ShadowApp04(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903,904,905,906,907,908,911,912,913,914,915,916,917,918,921,922,923,924,925,926,927,928,931,932,933,934,935,936,937,938]):
            return StartPuzzle01()

    def on_exit(self):
        destroy_monster(spawnIds=[106,206])
        create_monster(spawnIds=[104,204], arg2=False) # 연출용 NPC


class StartPuzzle01(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='PuzzleStart', value=1)
        set_conversation(type=1, spawnId=104, script='$52000051_QD__01_MAIN__14$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartPuzzle02()


class StartPuzzle02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$52000051_QD__01_MAIN__15$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EndPuzzle01()


#  NPC 말풍선 퍼즐에 대한 멘트 스크립트 모노로그 
class EndPuzzle01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PuzzleSolved', value=1):
            return GateOpen01()


class GateOpen01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # StoneGate 사운드 이펙트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GateOpen02()


class GateOpen02(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_108')
        move_npc(spawnId=204, patrolName='MS2PatrolData_208')
        set_conversation(type=1, spawnId=104, script='$52000051_QD__01_MAIN__16$', arg4=2, arg5=0) # 틴차이
        set_conversation(type=1, spawnId=204, script='$52000051_QD__01_MAIN__17$', arg4=2, arg5=2) # 준타
        set_actor(triggerId=4000, visible=True, initialSequence='or_fi_struc_stonegate_A01_on') # StoneGate
        set_mesh(triggerIds=[3030], visible=False, arg3=0, arg4=0, arg5=0) # GatePortal
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GateOpen03()


class GateOpen03(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_109')
        move_npc(spawnId=204, patrolName='MS2PatrolData_209')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104,204])


