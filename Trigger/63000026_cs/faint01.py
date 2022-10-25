""" trigger/63000026_cs/faint01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=10000, enable=False) # BGM
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5101], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5102], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5103], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5104], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5105], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5106], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5107], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5300], visible=False) # Faint
        self.set_effect(triggerIds=[5400], visible=False) # ShadowApp
        self.set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001681
        self.set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001717
        self.set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001682
        self.set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001683
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8100], visible=False)
        self.set_agent(triggerIds=[8101], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


# 최초 입장
class Enter01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[90000450], questStates=[1]):
            return Enter02(self.ctx)


class Enter02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10033010, textId=10033010) # 가이드 : 다리를 건너 눈썹달 동굴로 들어가기
        self.set_effect(triggerIds=[5100], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5101], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5102], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5103], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5104], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5105], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5106], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5107], visible=True) # 경로 안내

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return OnTheBridge01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10033010)
        self.set_effect(triggerIds=[5100], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5101], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5102], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5103], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5104], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5105], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5106], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5107], visible=False) # 경로 안내


class OnTheBridge01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=500, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return OnTheBridge02(self.ctx)


class OnTheBridge02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000026, portalId=10, boxId=9900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=250):
            return OnTheBridge03(self.ctx)


class OnTheBridge03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=250):
            return OnTheBridge04(self.ctx)


class OnTheBridge04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return TinChaiComeIn01(self.ctx)


class TinChaiComeIn01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)
        self.set_sound(triggerId=10000, enable=True) # BGM

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return TinChaiComeIn02(self.ctx)


class TinChaiComeIn02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$63000026_CS__FAINT01__5$', arg4=2, arg5=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return TinChaiComeIn03(self.ctx)


class TinChaiComeIn03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TinChaiComeIn04(self.ctx)


class TinChaiComeIn04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)
        self.set_scene_skip(state=PCTeleport03, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return TinChaiTalk01(self.ctx)


class TinChaiTalk01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001681
        self.set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__0$', arg4=5) # 틴차이 00001681
        self.set_skip(state=TinChaiTalk02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return TinChaiTalk02(self.ctx)


class TinChaiTalk02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return TinChaiTalk03(self.ctx)


class TinChaiTalk03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001717
        self.set_effect(triggerIds=[5400], visible=True) # ShadowApp
        self.set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__1$', arg4=3) # 틴차이 00001717
        self.create_monster(spawnIds=[900,901,902,903,904,905,910,911,912,913,914,915])
        self.move_npc(spawnId=900, patrolName='MS2PatrolData_900')
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_901')
        self.move_npc(spawnId=902, patrolName='MS2PatrolData_902')
        self.move_npc(spawnId=903, patrolName='MS2PatrolData_903')
        self.move_npc(spawnId=904, patrolName='MS2PatrolData_904')
        self.move_npc(spawnId=905, patrolName='MS2PatrolData_905')
        self.move_npc(spawnId=910, patrolName='MS2PatrolData_910')
        self.move_npc(spawnId=911, patrolName='MS2PatrolData_911')
        self.move_npc(spawnId=912, patrolName='MS2PatrolData_912')
        self.move_npc(spawnId=913, patrolName='MS2PatrolData_913')
        self.move_npc(spawnId=914, patrolName='MS2PatrolData_914')
        self.move_npc(spawnId=915, patrolName='MS2PatrolData_915')
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DarkShadowApp01(self.ctx)


# 연출용 그림자 패트롤
class DarkShadowApp01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DarkShadowApp02(self.ctx)


class DarkShadowApp02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.move_user(mapId=63000026, portalId=20, boxId=9900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return DarkShadowApp03(self.ctx)


class DarkShadowApp03(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToBattle01(self.ctx)


class ReadyToBattle01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001682
        self.set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__2$', arg4=5) # 틴차이 00001682
        self.set_skip(state=ReadyToBattle02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ReadyToBattle02(self.ctx)


class ReadyToBattle02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera_path(pathIds=[700,701], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return ReadyToBattle03(self.ctx)


class ReadyToBattle03(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000026, portalId=30, boxId=9900)
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001717
        self.set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__3$', arg4=3) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToBattle05(self.ctx)


class ReadyToBattle05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=True) # Faint

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToBattle06(self.ctx)


class ReadyToBattle06(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=30000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PCFaint01(self.ctx)


# PC가 털썩 바닥에 쓰러지는 사운드 이펙트
class PCFaint01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=702, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCFaint02(self.ctx)


class PCFaint02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_103')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCFaint03(self.ctx)


class PCFaint03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001683
        self.set_conversation(type=2, spawnId=11001708, script='$63000026_CS__FAINT01__4$', arg4=5) # 틴차이 00001683
        self.destroy_monster(spawnIds=[900,901,902,903,904,905,910,911,912,913,914,915])
        self.create_monster(spawnIds=[920,921,922], animationEffect=False)
        self.set_skip(state=PCFaint04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PCFaint04(self.ctx)


class PCFaint04(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TinChaiGoToFight01(self.ctx)


class TinChaiGoToFight01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=710, enable=True)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_104')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TinChaiGoToFight02(self.ctx)


class TinChaiGoToFight02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return TinChaiGoToFight03(self.ctx)


class TinChaiGoToFight03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PCTeleport01(self.ctx)


class PCTeleport01(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8100], visible=True)
        self.set_agent(triggerIds=[8101], visible=True)
        self.select_camera_path(pathIds=[720,721], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PCTeleport02(self.ctx)


class PCTeleport02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCTeleport03(self.ctx)


class PCTeleport03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=721, enable=False)
        self.move_user(mapId=63000027, portalId=1, boxId=9900)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
