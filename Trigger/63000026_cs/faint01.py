""" trigger/63000026_cs/faint01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_sound(triggerId=10000, arg2=False) # BGM
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # 경로 안내
        set_effect(triggerIds=[5101], visible=False) # 경로 안내
        set_effect(triggerIds=[5102], visible=False) # 경로 안내
        set_effect(triggerIds=[5103], visible=False) # 경로 안내
        set_effect(triggerIds=[5104], visible=False) # 경로 안내
        set_effect(triggerIds=[5105], visible=False) # 경로 안내
        set_effect(triggerIds=[5106], visible=False) # 경로 안내
        set_effect(triggerIds=[5107], visible=False) # 경로 안내
        set_effect(triggerIds=[5300], visible=False) # Faint
        set_effect(triggerIds=[5400], visible=False) # ShadowApp
        set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001681
        set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001717
        set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001682
        set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001683
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8100], visible=False)
        set_agent(triggerIds=[8101], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


#  최초 입장 
class Enter01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000450], questStates=[1]):
            return Enter02()


class Enter02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10033010, textId=10033010) # 가이드 : 다리를 건너 눈썹달 동굴로 들어가기
        set_effect(triggerIds=[5100], visible=True) # 경로 안내
        set_effect(triggerIds=[5101], visible=True) # 경로 안내
        set_effect(triggerIds=[5102], visible=True) # 경로 안내
        set_effect(triggerIds=[5103], visible=True) # 경로 안내
        set_effect(triggerIds=[5104], visible=True) # 경로 안내
        set_effect(triggerIds=[5105], visible=True) # 경로 안내
        set_effect(triggerIds=[5106], visible=True) # 경로 안내
        set_effect(triggerIds=[5107], visible=True) # 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return OnTheBridge01()

    def on_exit(self):
        hide_guide_summary(entityId=10033010)
        set_effect(triggerIds=[5100], visible=False) # 경로 안내
        set_effect(triggerIds=[5101], visible=False) # 경로 안내
        set_effect(triggerIds=[5102], visible=False) # 경로 안내
        set_effect(triggerIds=[5103], visible=False) # 경로 안내
        set_effect(triggerIds=[5104], visible=False) # 경로 안내
        set_effect(triggerIds=[5105], visible=False) # 경로 안내
        set_effect(triggerIds=[5106], visible=False) # 경로 안내
        set_effect(triggerIds=[5107], visible=False) # 경로 안내


class OnTheBridge01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=500, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return OnTheBridge02()


class OnTheBridge02(state.State):
    def on_enter(self):
        move_user(mapId=63000026, portalId=10, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=250):
            return OnTheBridge03()


class OnTheBridge03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=250):
            return OnTheBridge04()


class OnTheBridge04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return TinChaiComeIn01()


class TinChaiComeIn01(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        set_sound(triggerId=10000, arg2=True) # BGM

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return TinChaiComeIn02()


class TinChaiComeIn02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000026_CS__FAINT01__5$', arg4=2, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return TinChaiComeIn03()


class TinChaiComeIn03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TinChaiComeIn04()


class TinChaiComeIn04(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_scene_skip(state=PCTeleport03, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return TinChaiTalk01()


class TinChaiTalk01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001681
        set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__0$', arg4=5) # 틴차이 00001681
        set_skip(state=TinChaiTalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TinChaiTalk02()


class TinChaiTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TinChaiTalk03()


class TinChaiTalk03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001717
        set_effect(triggerIds=[5400], visible=True) # ShadowApp
        set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__1$', arg4=3) # 틴차이 00001717
        create_monster(spawnIds=[900,901,902,903,904,905,910,911,912,913,914,915])
        move_npc(spawnId=900, patrolName='MS2PatrolData_900')
        move_npc(spawnId=901, patrolName='MS2PatrolData_901')
        move_npc(spawnId=902, patrolName='MS2PatrolData_902')
        move_npc(spawnId=903, patrolName='MS2PatrolData_903')
        move_npc(spawnId=904, patrolName='MS2PatrolData_904')
        move_npc(spawnId=905, patrolName='MS2PatrolData_905')
        move_npc(spawnId=910, patrolName='MS2PatrolData_910')
        move_npc(spawnId=911, patrolName='MS2PatrolData_911')
        move_npc(spawnId=912, patrolName='MS2PatrolData_912')
        move_npc(spawnId=913, patrolName='MS2PatrolData_913')
        move_npc(spawnId=914, patrolName='MS2PatrolData_914')
        move_npc(spawnId=915, patrolName='MS2PatrolData_915')
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DarkShadowApp01()


#  연출용 그림자 패트롤 
class DarkShadowApp01(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DarkShadowApp02()


class DarkShadowApp02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        move_user(mapId=63000026, portalId=20, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return DarkShadowApp03()


class DarkShadowApp03(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToBattle01()


class ReadyToBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001682
        set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__2$', arg4=5) # 틴차이 00001682
        set_skip(state=ReadyToBattle02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReadyToBattle02()


class ReadyToBattle02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera_path(pathIds=[700,701], returnView=False)
        move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return ReadyToBattle03()


class ReadyToBattle03(state.State):
    def on_enter(self):
        move_user(mapId=63000026, portalId=30, boxId=9900)
        set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001717
        set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__3$', arg4=3) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToBattle05()


class ReadyToBattle05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=True) # Faint

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToBattle06()


class ReadyToBattle06(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=30000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCFaint01()


#  PC가 털썩 바닥에 쓰러지는 사운드 이펙트 
class PCFaint01(state.State):
    def on_enter(self):
        select_camera(triggerId=702, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCFaint02()


class PCFaint02(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCFaint03()


class PCFaint03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001683
        set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__4$', arg4=5) # 틴차이 00001683
        destroy_monster(spawnIds=[900,901,902,903,904,905,910,911,912,913,914,915])
        create_monster(spawnIds=[920,921,922], arg2=False)
        set_skip(state=PCFaint04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PCFaint04()


class PCFaint04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TinChaiGoToFight01()


class TinChaiGoToFight01(state.State):
    def on_enter(self):
        select_camera(triggerId=710, enable=True)
        move_npc(spawnId=103, patrolName='MS2PatrolData_104')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TinChaiGoToFight02()


class TinChaiGoToFight02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return TinChaiGoToFight03()


class TinChaiGoToFight03(state.State):
    def on_enter(self):
        set_scene_skip()
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PCTeleport01()


class PCTeleport01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8100], visible=True)
        set_agent(triggerIds=[8101], visible=True)
        select_camera_path(pathIds=[720,721], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PCTeleport02()


class PCTeleport02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCTeleport03()


class PCTeleport03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=721, enable=False)
        move_user(mapId=63000027, portalId=1, boxId=9900)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    pass


