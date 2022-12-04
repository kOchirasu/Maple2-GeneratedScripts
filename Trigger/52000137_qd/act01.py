""" trigger/52000137_qd/act01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7000], enable=False)
        self.destroy_monster(spawnIds=[101,102,103,104,105,201,202,203,301,900,910,920])
        self.set_effect(triggerIds=[5100], visible=False) # AsimovShield
        self.set_effect(triggerIds=[5101], visible=False) # RuneShieldThunder
        self.set_effect(triggerIds=[5200], visible=False) # ShieldExplosion
        self.set_effect(triggerIds=[5300], visible=False) # Vibrate
        self.set_effect(triggerIds=[5400], visible=False) # DarkStrom01
        self.set_effect(triggerIds=[5401], visible=False) # DarkStrom02
        self.set_effect(triggerIds=[5500], visible=False) # DarkAura01
        self.set_effect(triggerIds=[5501], visible=False) # DarkAura02
        self.set_effect(triggerIds=[5600], visible=True) # DarkCloud
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_user_value(key='PatosTired', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return LodingDelay01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return Quit02(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,201,910,920], animationEffect=True)
        self.set_effect(triggerIds=[5100], visible=True) # AsimovShield
        self.set_effect(triggerIds=[5101], visible=True) # RuneShieldThunder
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return SetMaskEffect01(self.ctx)


class SetMaskEffect01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SetMaskEffect02(self.ctx)


class SetMaskEffect02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ImprisonDarkAnos01(self.ctx)


class ImprisonDarkAnos01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ImprisonDarkAnos02(self.ctx)


class ImprisonDarkAnos02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return AsimovTalk01(self.ctx)


class AsimovTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__0$', duration=5000, align='center', illustId='0') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_scene_skip(state=DarkAnosTalk01CSkip, action='nextState')
        self.set_skip(state=AsimovTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return AsimovTalk01Skip(self.ctx)


class AsimovTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ZoominAnos01(self.ctx)


class ZoominAnos01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return AnosTruning01(self.ctx)


class AnosTruning01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5500], visible=True) # DarkAura01

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return AnosTruning02(self.ctx)


class AnosTruning02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return AnosTalk01(self.ctx)


class AnosTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003289, msg='$52000137_QD__ACT01__1$', duration=4000, align='center', illustId='0') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_skip(state=AnosTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return AnosTalk01Skip(self.ctx)


class AnosTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return CameraChange00(self.ctx)


class CameraChange00(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=603, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange01(self.ctx)


class CameraChange01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCTalk01(self.ctx)


class PCTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__2$', duration=4000, align='center', illustId='0')
        self.set_skip(state=PCTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCTalk01Skip(self.ctx)


class PCTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return AsimovTalk02(self.ctx)


class AsimovTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__3$', duration=4000, align='center', illustId='Asimov_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.set_skip(state=AsimovTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return AsimovTalk02Skip(self.ctx)


class AsimovTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return AsimovTalk03(self.ctx)


class AsimovTalk03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__4$', duration=5000, align='center', illustId='Asimov_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_skip(state=AsimovTalk03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return AsimovTalk03Skip(self.ctx)


class AsimovTalk03Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return CameraChange02(self.ctx)


class CameraChange02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraChange03(self.ctx)


class CameraChange03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=604, enable=True) # PC 어깨에 걸고

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCTalk02(self.ctx)


class PCTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__5$', duration=5000, align='center', illustId='0')
        self.set_skip(state=PCTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return PCTalk02Skip(self.ctx)


class PCTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return CameraChange04(self.ctx)


class CameraChange04(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.select_camera(triggerId=605, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DarkAnosTalk01(self.ctx)


class DarkAnosTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Attack_Idle_A,Attack_Idle_A') # 1533
        self.add_cinematic_talk(npcId=11003285, msg='$52000137_QD__ACT01__6$', duration=3000, align='center', illustId='Patos_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_skip(state=DarkAnosTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3100):
            return DarkAnosTalk01Skip(self.ctx)


class DarkAnosTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return DarkAnosAttackAsimov01(self.ctx)


class DarkAnosAttackAsimov01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=610, enable=True)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Attack_01_A,Attack_Idle_A') # 3200

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return DarkAnosAttackAsimov02(self.ctx)


class DarkAnosAttackAsimov02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5200], visible=True) # ShieldExplosion
        self.destroy_monster(spawnIds=[201,910,920])
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.set_effect(triggerIds=[5501], visible=True) # DarkAura02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return DarkAnosAttackAsimov03(self.ctx)


class DarkAnosAttackAsimov03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5500], visible=False) # DarkAura01
        self.set_effect(triggerIds=[5101], visible=False) # RuneShieldThunder
        self.set_effect(triggerIds=[5100], visible=False) # AsimovShield

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraChange05(self.ctx)


class CameraChange05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=611, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1003')
        self.add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__7$', duration=2000, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraChange06(self.ctx)


class CameraChange06(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_effect(triggerIds=[5501], visible=False) # DarkAura02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange07(self.ctx)


class CameraChange07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=612, enable=True) # PC 어깨에 걸고
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return AsimovTalk04(self.ctx)


class AsimovTalk04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__8$', duration=5000, align='center', illustId='Asimov_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_skip(state=AsimovTalk04Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return AsimovTalk04Skip(self.ctx)


class AsimovTalk04Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Event_02_A,Down_Idle_A,Down_Idle_A,Down_Idle_A,Down_Idle_A') # 임시 - 기절하는 동작 제작되면 타이밍 맞추기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return AsimovFaint01(self.ctx)


class AsimovFaint01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return AsimovFaint02(self.ctx)


class AsimovFaint02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[203], animationEffect=False)
        self.select_camera(triggerId=613, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return AsimovFaint03(self.ctx)


class AsimovFaint03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DarkAnosApproach01(self.ctx)


class DarkAnosApproach01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return DarkAnosApproach02(self.ctx)


class DarkAnosApproach02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return DarkAnosTalk02(self.ctx)


class DarkAnosTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003285, msg='$52000137_QD__ACT01__9$', duration=5000, align='center', illustId='Patos_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_skip(state=DarkAnosTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return DarkAnosTalk02Skip(self.ctx)


class DarkAnosTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PCTalk03(self.ctx)


class PCTalk03(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__10$', duration=5000, align='center', illustId='0')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return PCTalk03Skip(self.ctx)


class PCTalk03Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return DarkAnosTalk03(self.ctx)


class DarkAnosTalk03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003285, msg='$52000137_QD__ACT01__11$', duration=4000, align='center', illustId='Patos_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return DarkAnosTalk03Skip(self.ctx)


class DarkAnosTalk01CSkip(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[201,910,920])
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[203], animationEffect=False)
        self.set_effect(triggerIds=[5500], visible=False) # DarkAura01
        self.set_effect(triggerIds=[5501], visible=False) # DarkAura02
        self.set_effect(triggerIds=[5100], visible=False) # AsimovShield
        self.set_effect(triggerIds=[5101], visible=False) # RuneShieldThunder
        self.set_effect(triggerIds=[5200], visible=False) # ShieldExplosion
        self.set_pc_emotion_sequence(sequenceNames=['Attack_Idle_A'])
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return DarkAnosTalk03Skip(self.ctx)


class DarkAnosTalk03Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DarkAnosBattle01(self.ctx)


class DarkAnosBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DarkAnosBattle02(self.ctx)


class DarkAnosBattle02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.create_monster(spawnIds=[900], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PatosTired', value=1):
            return DarkAnosDown01(self.ctx)
        if self.monster_dead(boxIds=[900]):
            return DarkAnosDown01(self.ctx)


class DarkAnosDown01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PositionArrange01(self.ctx)


class PositionArrange01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[900])
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.move_user(mapId=52000137, portalId=10, boxId=9900)
        self.select_camera(triggerId=620, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PositionArrange02(self.ctx)


class PositionArrange02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCBalloonTalk01(self.ctx)


class PCBalloonTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2000')
        self.add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__12$', duration=2000, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCBalloonTalk02(self.ctx)


class PCBalloonTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__13$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCBalloonTalk03(self.ctx)


class PCBalloonTalk03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=621, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return KanduraApp01(self.ctx)


class KanduraApp01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=622, enable=True)
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return KanduraApp02(self.ctx)


class KanduraApp02(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__14$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return KanduraApp03(self.ctx)


class KanduraApp03(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return KanduraAttack01(self.ctx)


class KanduraAttack01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=623, enable=True)
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Event_01_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return KanduraAttack02(self.ctx)


class KanduraAttack02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraChange10(self.ctx)


class CameraChange10(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange11(self.ctx)


class CameraChange11(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=630, enable=True) # PC 등뒤에서
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=30000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraChange12(self.ctx)


class CameraChange12(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return KanduraTalk01(self.ctx)


class KanduraTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_302')
        self.add_cinematic_talk(npcId=11003287, msg='$52000137_QD__ACT01__15$', duration=4000, align='center', illustId='Kandura_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_scene_skip(state=ShowCaption04Skip, action='exit')
        self.set_skip(state=KanduraTalk01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraTalk01Skip(self.ctx)


class KanduraTalk01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PCTalk04(self.ctx)


class PCTalk04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__16$', duration=4000, align='center', illustId='0')
        self.set_skip(state=PCTalk04Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCTalk04Skip(self.ctx)


class PCTalk04Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return KanduraMoveToDarkAnos01(self.ctx)


class KanduraMoveToDarkAnos01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=631, enable=True)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_303')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return KanduraTalk02(self.ctx)


class KanduraTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003287, msg='$52000137_QD__ACT01__17$', duration=4000, align='center', illustId='Kandura_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        self.set_skip(state=KanduraTalk02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return KanduraTalk02Skip(self.ctx)


class KanduraTalk02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return KanduraReadyToDisapp01(self.ctx)


# 칸두라가 흑화된 아노스를 데리고 함께 사라지는 연출
class KanduraReadyToDisapp01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=632, enable=True)
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Event_02_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return KanduraReadyToDisapp02(self.ctx)


class KanduraReadyToDisapp02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=True) # Vibrate
        self.set_effect(triggerIds=[5400], visible=True) # DarkStrom01

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return KanduraReadyToDisapp03(self.ctx)


class KanduraReadyToDisapp03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=False) # DarkStrom01
        self.set_effect(triggerIds=[5401], visible=True) # DarkStrom02
        self.destroy_monster(spawnIds=[105,301])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return KanduraReadyToDisapp04(self.ctx)


class KanduraReadyToDisapp04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShowCaption02(self.ctx)


class ShowCaption02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000137_QD__ACT01__18$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ShowCaption03(self.ctx)


class ShowCaption03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000137_QD__ACT01__19$')
        self.set_skip(state=ShowCaption03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return ShowCaption03Skip(self.ctx)


class ShowCaption03Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ShowCaption04(self.ctx)


class ShowCaption04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000137_QD__ACT01__20$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return ShowCaption04Skip(self.ctx)


class ShowCaption04Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9900, type='trigger', achieve='AsimovRetire')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.reset_camera(interpolationTime=1)
        self.move_user(mapId=2000035, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


initial_state = Wait
