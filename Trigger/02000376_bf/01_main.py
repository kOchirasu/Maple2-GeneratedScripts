""" trigger/02000376_bf/01_main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3500,3501], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_IronDoor
        set_mesh(triggerIds=[3010,3011,3012,3013], visible=True, arg3=0, arg4=0, arg5=0) # Barrier
        set_mesh(triggerIds=[3030], visible=True, arg3=0, arg4=0, arg5=0) # GatePortal
        set_mesh(triggerIds=[3506,3507], visible=True, arg3=0, arg4=0, arg5=0) # EnterInvisibleBarrier
        set_mesh(triggerIds=[3502,3503,3504,3505], visible=True, arg3=0, arg4=0, arg5=0) # EnterPillarBarrier
        set_actor(triggerId=4001, visible=True, initialSequence='Closed') # IronDoor
        set_actor(triggerId=4002, visible=True, initialSequence='Closed') # IronDoor
        set_actor(triggerId=4000, visible=True, initialSequence='or_fi_struc_stonegate_A01_off') # StoneGate
        set_actor(triggerId=4003, visible=True, initialSequence='Closed') # EnterIronDoor
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # StoneGate 사운드 이펙트
        set_effect(triggerIds=[5004], visible=False) # MetalDoorOpen 사운드 이펙트
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_user_value(key='PuzzleSolved', value=0)
        set_user_value(key='PatrolEnd', value=0)
        create_monster(spawnIds=[900], arg2=False) # 어둠의 토템

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        create_monster(spawnIds=[100,200], arg2=False)
        create_monster(spawnIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826], arg2=False) # 연출용 검은 그림자
        create_monster(spawnIds=[950,951,952,953,954,955,956,958,959,961,963,964,965,966,969,970,973,974,976,977,978,979,981], arg2=False) # 미혹의 령

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcMonologue01()

state.DungeonStart = DungeonStart


class NpcMonologue01(state.State):
    def on_enter(self):
        set_user_value(triggerId=11, key='DungeonStart', value=1)
        set_actor(triggerId=4003, visible=True, initialSequence='Opened') # EnterIronDoor
        set_mesh(triggerIds=[3506,3507], visible=False, arg3=0, arg4=0, arg5=0) # EnterInvisibleBarrier
        set_conversation(type=1, spawnId=100, script='$02000376_BF__01_MAIN__0$', arg4=3, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NpcMonologue02()


class NpcMonologue02(state.State):
    def on_enter(self):
        set_actor(triggerId=4003, visible=False, initialSequence='Opened') # EnterIronDoor
        set_mesh(triggerIds=[3502,3503,3504,3505], visible=False, arg3=0, arg4=100, arg5=5) # EnterPillarBarrier
        move_npc(spawnId=100, patrolName='MS2PatrolData_100')
        move_npc(spawnId=200, patrolName='MS2PatrolData_200')
        set_conversation(type=1, spawnId=200, script='$02000376_BF__01_MAIN__1$', arg4=4, arg5=0) # 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NpcPatrol01()


class NpcPatrol01(state.State):
    def on_enter(self):
        set_user_value(triggerId=10, key='PatrolStart', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return NpcPatrol02()


class NpcPatrol02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000376_BF__01_MAIN__2$', arg3='5000', arg4='0')

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
        destroy_monster(spawnIds=[101,201])
        destroy_monster(spawnIds=[102,202])
        move_npc(spawnId=950, patrolName='MS2PatrolData_850')
        move_npc(spawnId=951, patrolName='MS2PatrolData_851')
        move_npc(spawnId=952, patrolName='MS2PatrolData_852')
        move_npc(spawnId=953, patrolName='MS2PatrolData_853')
        move_npc(spawnId=954, patrolName='MS2PatrolData_854')
        move_npc(spawnId=955, patrolName='MS2PatrolData_855')
        move_npc(spawnId=956, patrolName='MS2PatrolData_856')
        move_npc(spawnId=958, patrolName='MS2PatrolData_858')
        move_npc(spawnId=959, patrolName='MS2PatrolData_859')
        move_npc(spawnId=961, patrolName='MS2PatrolData_861')
        move_npc(spawnId=963, patrolName='MS2PatrolData_863')
        move_npc(spawnId=964, patrolName='MS2PatrolData_864')
        move_npc(spawnId=965, patrolName='MS2PatrolData_865')
        move_npc(spawnId=966, patrolName='MS2PatrolData_866')
        move_npc(spawnId=969, patrolName='MS2PatrolData_869')
        move_npc(spawnId=970, patrolName='MS2PatrolData_870')
        move_npc(spawnId=973, patrolName='MS2PatrolData_873')
        move_npc(spawnId=974, patrolName='MS2PatrolData_874')
        move_npc(spawnId=976, patrolName='MS2PatrolData_876')
        move_npc(spawnId=977, patrolName='MS2PatrolData_877')
        move_npc(spawnId=978, patrolName='MS2PatrolData_878')
        move_npc(spawnId=979, patrolName='MS2PatrolData_879')
        move_npc(spawnId=981, patrolName='MS2PatrolData_881')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RemoveTotem03()


#  NPC 말풍선 어둠이 걷혔어 
class RemoveTotem03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102,202])
        change_monster(removeSpawnId=950, addSpawnId=850)
        change_monster(removeSpawnId=951, addSpawnId=851)
        change_monster(removeSpawnId=952, addSpawnId=852)
        change_monster(removeSpawnId=953, addSpawnId=853)
        change_monster(removeSpawnId=954, addSpawnId=854)
        change_monster(removeSpawnId=955, addSpawnId=855)
        change_monster(removeSpawnId=956, addSpawnId=856)
        change_monster(removeSpawnId=958, addSpawnId=858)
        change_monster(removeSpawnId=959, addSpawnId=859)
        change_monster(removeSpawnId=961, addSpawnId=861)
        change_monster(removeSpawnId=963, addSpawnId=863)
        change_monster(removeSpawnId=964, addSpawnId=864)
        change_monster(removeSpawnId=965, addSpawnId=865)
        change_monster(removeSpawnId=966, addSpawnId=866)
        change_monster(removeSpawnId=968, addSpawnId=868)
        change_monster(removeSpawnId=969, addSpawnId=869)
        change_monster(removeSpawnId=970, addSpawnId=870)
        change_monster(removeSpawnId=973, addSpawnId=873)
        change_monster(removeSpawnId=974, addSpawnId=874)
        change_monster(removeSpawnId=976, addSpawnId=876)
        change_monster(removeSpawnId=977, addSpawnId=877)
        change_monster(removeSpawnId=978, addSpawnId=878)
        change_monster(removeSpawnId=979, addSpawnId=879)
        change_monster(removeSpawnId=981, addSpawnId=881)
        set_conversation(type=1, spawnId=105, script='$02000376_BF__01_MAIN__5$', arg4=3, arg5=1) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return RemoveTotem04()


class RemoveTotem04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102,202])
        set_conversation(type=1, spawnId=205, script='$02000376_BF__01_MAIN__6$', arg4=3, arg5=2) # 준타
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
        destroy_monster(spawnIds=[102,202])
        set_conversation(type=1, spawnId=205, script='$02000376_BF__01_MAIN__7$', arg4=2, arg5=0) # 준타
        move_npc(spawnId=105, patrolName='MS2PatrolData_107')
        move_npc(spawnId=205, patrolName='MS2PatrolData_207')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9500, spawnIds=[105]):
            return FoundGate02()


class FoundGate02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=105, script='$02000376_BF__01_MAIN__8$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9501, spawnIds=[105]):
            return ShadowApp01()


class ShadowApp01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=205, script='$02000376_BF__01_MAIN__9$', arg4=2, arg5=0) # 준타
        create_monster(spawnIds=[901,902,903,904,905,906,907,908], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ShadowApp02()


class ShadowApp02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[105,205]) # 전투
        create_monster(spawnIds=[106,206], arg2=False)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000376_BF__01_MAIN__10$', arg3='3000', arg4='0')
        create_monster(spawnIds=[911,912,913,914,915,916,917,918], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return ShadowApp03()


class ShadowApp03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[921,922,923,924,925,926,927,928], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ShadowApp04()


class ShadowApp04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[931,932,933,934,935,936,937,938], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901,902,903,904,905,906,907,908,911,912,913,914,915,916,917,918,921,922,923,924,925,926,927,928,931,932,933,934,935,936,937,938]):
            return StartPuzzle01()

    def on_exit(self):
        destroy_monster(spawnIds=[106,206])
        create_monster(spawnIds=[104,204], arg2=False) # 연출용 NPC


class StartPuzzle01(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='PuzzleStart', value=1)
        set_conversation(type=1, spawnId=104, script='$02000376_BF__01_MAIN__11$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return StartPuzzle02()


class StartPuzzle02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000376_BF__01_MAIN__12$', arg3='5000', arg4='0')

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
        set_conversation(type=1, spawnId=104, script='$02000376_BF__01_MAIN__13$', arg4=2, arg5=0) # 틴차이
        set_conversation(type=1, spawnId=204, script='$02000376_BF__01_MAIN__14$', arg4=2, arg5=2) # 준타
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


