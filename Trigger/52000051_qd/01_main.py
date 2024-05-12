""" trigger/52000051_qd/01_main.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3500,3501], visible=True, arg3=0, delay=0, scale=0) # Invisible_IronDoor
        self.set_mesh(triggerIds=[3010,3011,3012,3013], visible=True, arg3=0, delay=0, scale=0) # Barrier
        self.set_mesh(triggerIds=[3014], visible=True, arg3=0, delay=0, scale=0) # FrontBarrier
        self.set_mesh(triggerIds=[3030], visible=True, arg3=0, delay=0, scale=0) # GatePortal
        self.set_actor(triggerId=4001, visible=True, initialSequence='Closed') # IronDoor
        self.set_actor(triggerId=4002, visible=True, initialSequence='Closed') # IronDoor
        self.set_actor(triggerId=4000, visible=True, initialSequence='or_fi_struc_stonegate_A01_off') # StoneGate
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # StoneGate 사운드 이펙트
        self.set_effect(triggerIds=[5004], visible=False) # MetalDoorOpen 사운드 이펙트
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_user_value(key='FindLotus', value=0)
        self.set_user_value(key='PuzzleSolved', value=0)
        self.set_user_value(key='PatrolEnd', value=0)
        self.create_monster(spawnIds=[900], animationEffect=False) # 어둠의 토템

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9000, minUsers='1'):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return SetDarkness01(self.ctx)


class SetDarkness01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=600, enable=True)
        self.create_monster(spawnIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826], animationEffect=False) # 연출용 검은 그림자
        # 미혹의 령 일부 제거 954,960,961,965,966,968,969,971,972,973,979
        self.create_monster(spawnIds=[950,951,952,953,955,956,957,958,959,962,963,964,967,970,974,975,976,977,978,980,981,982], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SetDarkness02(self.ctx)


class SetDarkness02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[100,200], animationEffect=False)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcCinematic01(self.ctx)


class NpcCinematic01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001708, script='$52000051_QD__01_MAIN__0$', arg4=5) # 틴차이
        self.set_skip(state=NpcCinematic01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return NpcCinematic01Skip(self.ctx)


class NpcCinematic01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NpcCinematic02(self.ctx)


class NpcCinematic02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001708, script='$52000051_QD__01_MAIN__1$', arg4=5) # 틴차이
        self.set_skip(state=NpcCinematic02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return NpcCinematic02Skip(self.ctx)


class NpcCinematic02Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NpcCinematic03(self.ctx)


class NpcCinematic03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=601, enable=True)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_110')
        self.move_user_path(patrolName='MS2PatrolData_1001')
        self.set_conversation(type=2, spawnId=11001708, script='$52000051_QD__01_MAIN__2$', arg4=3) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcCinematic04(self.ctx)


class NpcCinematic04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_210')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcCinematic05(self.ctx)


class NpcCinematic05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001557, script='$52000051_QD__01_MAIN__3$', arg4=5) # 준타
        self.set_skip(state=NpcCinematic05Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return NpcCinematic05Skip(self.ctx)


class NpcCinematic05Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.select_camera(triggerId=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_user_value(triggerId=9, key='FindLotus', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcMonologue01(self.ctx)


class NpcMonologue01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001022], stateValue=0):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_200')
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_100')
        self.set_conversation(type=1, spawnId=200, script='$52000051_QD__01_MAIN__4$', arg4=2, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return NpcPatrol01(self.ctx)


class NpcPatrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3014], visible=False, arg3=0, delay=0, scale=0) # FrontBarrier
        self.set_user_value(triggerId=10, key='PatrolStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcPatrol02(self.ctx)


class NpcPatrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000051_QD__01_MAIN__5$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PatrolEnd', value=1):
            return NpcPatrol03(self.ctx)
        if self.monster_dead(boxIds=[900]):
            # 토템 제거
            return NpcChange01(self.ctx)


class NpcPatrol03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9400, spawnIds=[202]):
            return NpcPatrol04(self.ctx)
        if self.monster_dead(boxIds=[900]):
            # 토템 제거
            return NpcChange01(self.ctx)


class NpcPatrol04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9400, minUsers='1'):
            return FoundTotem01(self.ctx)
        if self.monster_dead(boxIds=[900]):
            # 토템 제거
            return NpcChange01(self.ctx)


# 20170223 업데이트 던전 개편 단축
class NpcChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,201])
        self.destroy_monster(spawnIds=[102,202])
        self.create_monster(spawnIds=[105,205], animationEffect=False) # 연출용

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return RemoveTotem02(self.ctx)


class NpcChange02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,201])
        self.destroy_monster(spawnIds=[102,202])
        self.destroy_monster(spawnIds=[103,203]) # 전투
        self.create_monster(spawnIds=[105,205], animationEffect=False) # 연출용
        self.remove_balloon_talk(spawnId=203)
        self.remove_balloon_talk(spawnId=103)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return RemoveTotem02(self.ctx)


class FoundTotem01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,201])
        self.destroy_monster(spawnIds=[102,202])
        self.create_monster(spawnIds=[103,203], animationEffect=False) # 전투
        self.set_conversation(type=1, spawnId=203, script='$02000376_BF__01_MAIN__3$', arg4=3, arg5=0) # 준타
        self.set_conversation(type=1, spawnId=103, script='$02000376_BF__01_MAIN__4$', arg4=3, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return RemoveTotem01(self.ctx)
        if self.monster_dead(boxIds=[900]):
            # 토템 제거
            return NpcChange02(self.ctx)


class RemoveTotem01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900]):
            # 토템 제거
            return RemoveTotem02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[101,201])
        self.destroy_monster(spawnIds=[102,202])
        self.destroy_monster(spawnIds=[103,203])
        # 전투
        self.create_monster(spawnIds=[105,205], animationEffect=False)
        self.remove_balloon_talk(spawnId=203)
        self.remove_balloon_talk(spawnId=103)


class RemoveTotem02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[102,202])
        self.move_npc(spawnId=950, patrolName='MS2PatrolData_850')
        self.move_npc(spawnId=951, patrolName='MS2PatrolData_851')
        self.move_npc(spawnId=952, patrolName='MS2PatrolData_852')
        self.move_npc(spawnId=953, patrolName='MS2PatrolData_853')
        # self.move_npc(spawnId=954, patrolName='MS2PatrolData_854')
        self.move_npc(spawnId=955, patrolName='MS2PatrolData_855')
        self.move_npc(spawnId=956, patrolName='MS2PatrolData_856')
        self.move_npc(spawnId=957, patrolName='MS2PatrolData_857')
        self.move_npc(spawnId=958, patrolName='MS2PatrolData_858')
        self.move_npc(spawnId=959, patrolName='MS2PatrolData_859')
        # self.move_npc(spawnId=960, patrolName='MS2PatrolData_860')
        # self.move_npc(spawnId=961, patrolName='MS2PatrolData_861')
        self.move_npc(spawnId=962, patrolName='MS2PatrolData_862')
        self.move_npc(spawnId=963, patrolName='MS2PatrolData_863')
        self.move_npc(spawnId=964, patrolName='MS2PatrolData_864')
        # self.move_npc(spawnId=965, patrolName='MS2PatrolData_865')
        # self.move_npc(spawnId=966, patrolName='MS2PatrolData_866')
        self.move_npc(spawnId=967, patrolName='MS2PatrolData_867')
        # self.move_npc(spawnId=968, patrolName='MS2PatrolData_868')
        # self.move_npc(spawnId=969, patrolName='MS2PatrolData_869')
        self.move_npc(spawnId=970, patrolName='MS2PatrolData_870')
        # self.move_npc(spawnId=971, patrolName='MS2PatrolData_871')
        # self.move_npc(spawnId=972, patrolName='MS2PatrolData_872')
        # self.move_npc(spawnId=973, patrolName='MS2PatrolData_873')
        self.move_npc(spawnId=974, patrolName='MS2PatrolData_874')
        self.move_npc(spawnId=975, patrolName='MS2PatrolData_875')
        self.move_npc(spawnId=976, patrolName='MS2PatrolData_876')
        self.move_npc(spawnId=977, patrolName='MS2PatrolData_877')
        self.move_npc(spawnId=978, patrolName='MS2PatrolData_878')
        # self.move_npc(spawnId=979, patrolName='MS2PatrolData_879')
        self.move_npc(spawnId=980, patrolName='MS2PatrolData_880')
        self.move_npc(spawnId=981, patrolName='MS2PatrolData_881')
        self.move_npc(spawnId=982, patrolName='MS2PatrolData_882')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return RemoveTotem03(self.ctx)


# 미혹의 령 일부 제거 954,960,961,965,966,968,969,971,973,979
class RemoveTotem03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[102,202])
        self.change_monster(removeSpawnId=950, addSpawnId=850)
        self.change_monster(removeSpawnId=951, addSpawnId=851)
        self.change_monster(removeSpawnId=952, addSpawnId=852)
        self.change_monster(removeSpawnId=953, addSpawnId=853)
        # self.change_monster(removeSpawnId=954, addSpawnId=854)
        self.change_monster(removeSpawnId=955, addSpawnId=855)
        self.change_monster(removeSpawnId=956, addSpawnId=856)
        self.change_monster(removeSpawnId=957, addSpawnId=857)
        self.change_monster(removeSpawnId=958, addSpawnId=858)
        self.change_monster(removeSpawnId=959, addSpawnId=859)
        # self.change_monster(removeSpawnId=960, addSpawnId=860)
        # self.change_monster(removeSpawnId=961, addSpawnId=861)
        self.change_monster(removeSpawnId=962, addSpawnId=862)
        self.change_monster(removeSpawnId=963, addSpawnId=863)
        self.change_monster(removeSpawnId=964, addSpawnId=864)
        # self.change_monster(removeSpawnId=965, addSpawnId=865)
        # self.change_monster(removeSpawnId=966, addSpawnId=866)
        self.change_monster(removeSpawnId=967, addSpawnId=867)
        # self.change_monster(removeSpawnId=968, addSpawnId=868)
        self.change_monster(removeSpawnId=969, addSpawnId=869)
        self.change_monster(removeSpawnId=970, addSpawnId=870)
        # self.change_monster(removeSpawnId=971, addSpawnId=871)
        # self.change_monster(removeSpawnId=972, addSpawnId=872)
        # self.change_monster(removeSpawnId=973, addSpawnId=873)
        self.change_monster(removeSpawnId=974, addSpawnId=874)
        self.change_monster(removeSpawnId=975, addSpawnId=875)
        self.change_monster(removeSpawnId=976, addSpawnId=876)
        self.change_monster(removeSpawnId=977, addSpawnId=877)
        self.change_monster(removeSpawnId=978, addSpawnId=878)
        # self.change_monster(removeSpawnId=979, addSpawnId=879)
        self.change_monster(removeSpawnId=980, addSpawnId=880)
        self.change_monster(removeSpawnId=981, addSpawnId=881)
        self.change_monster(removeSpawnId=982, addSpawnId=882)
        self.set_conversation(type=1, spawnId=105, script='$52000051_QD__01_MAIN__8$', arg4=3, arg5=0) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return RemoveTotem04(self.ctx)


class RemoveTotem04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=205, script='$52000051_QD__01_MAIN__9$', arg4=3, arg5=1) # 준타
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_106')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_206')
        self.set_mesh(triggerIds=[3500,3501], visible=False, arg3=0, delay=0, scale=0) # Invisible_IronDoor
        self.set_actor(triggerId=4002, visible=True, initialSequence='Opened') # IronDoor
        self.set_actor(triggerId=4001, visible=True, initialSequence='Opened') # IronDoor
        self.set_effect(triggerIds=[5004], visible=True) # MetalDoorOpen 사운드 이펙트
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return FoundGate01(self.ctx)


class FoundGate01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=205, script='$52000051_QD__01_MAIN__10$', arg4=3, arg5=0) # 준타
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_107')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_207')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9500, spawnIds=[105]):
            return FoundGate02(self.ctx)


class FoundGate02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=105, script='$52000051_QD__01_MAIN__11$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9501, spawnIds=[105]):
            return ShadowApp01(self.ctx)


class ShadowApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=205, script='$52000051_QD__01_MAIN__12$', arg4=2, arg5=0) # 준타
        self.create_monster(spawnIds=[901,903,905], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return ShadowApp02(self.ctx)


class ShadowApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[105,205]) # 전투
        self.create_monster(spawnIds=[106,206], animationEffect=False)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000051_QD__01_MAIN__13$', arg3='3000', arg4='0')
        self.create_monster(spawnIds=[914,916,918], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return ShadowApp03(self.ctx)


class ShadowApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[921,926,928], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ShadowApp04(self.ctx)


class ShadowApp04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907,908,911,912,913,914,915,916,917,918,921,922,923,924,925,926,927,928,931,932,933,934,935,936,937,938]):
            return StartPuzzle01(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[106,206])
        self.create_monster(spawnIds=[104,204], animationEffect=False)
        # 연출용 NPC


class StartPuzzle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=4, key='PuzzleStart', value=1)
        self.set_conversation(type=1, spawnId=104, script='$52000051_QD__01_MAIN__14$', arg4=2, arg5=0) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return StartPuzzle02(self.ctx)


class StartPuzzle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000051_QD__01_MAIN__15$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return EndPuzzle01(self.ctx)


# NPC 말풍선 퍼즐에 대한 멘트 스크립트 모노로그
class EndPuzzle01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PuzzleSolved', value=1):
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True) # StoneGate 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return GateOpen02(self.ctx)


class GateOpen02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_108')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_208')
        self.set_conversation(type=1, spawnId=104, script='$52000051_QD__01_MAIN__16$', arg4=2, arg5=0) # 틴차이
        self.set_conversation(type=1, spawnId=204, script='$52000051_QD__01_MAIN__17$', arg4=2, arg5=2) # 준타
        self.set_actor(triggerId=4000, visible=True, initialSequence='or_fi_struc_stonegate_A01_on') # StoneGate
        self.set_mesh(triggerIds=[3030], visible=False, arg3=0, delay=0, scale=0) # GatePortal
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return GateOpen03(self.ctx)


class GateOpen03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_109')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_209')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[104,204])


initial_state = Wait
