""" trigger/52000137_qd/act01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=False)
        destroy_monster(spawnIds=[101,102,103,104,105,201,202,203,301,900,910,920])
        set_effect(triggerIds=[5100], visible=False) # AsimovShield
        set_effect(triggerIds=[5101], visible=False) # RuneShieldThunder
        set_effect(triggerIds=[5200], visible=False) # ShieldExplosion
        set_effect(triggerIds=[5300], visible=False) # Vibrate
        set_effect(triggerIds=[5400], visible=False) # DarkStrom01
        set_effect(triggerIds=[5401], visible=False) # DarkStrom02
        set_effect(triggerIds=[5500], visible=False) # DarkAura01
        set_effect(triggerIds=[5501], visible=False) # DarkAura02
        set_effect(triggerIds=[5600], visible=True) # DarkCloud
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_user_value(key='PatosTired', value=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return LodingDelay01()
        if quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[2]):
            return Quit02()


class LodingDelay01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,201,910,920], arg2=True)
        set_effect(triggerIds=[5100], visible=True) # AsimovShield
        set_effect(triggerIds=[5101], visible=True) # RuneShieldThunder
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return SetMaskEffect01()


class SetMaskEffect01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SetMaskEffect02()


class SetMaskEffect02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ImprisonDarkAnos01()


class ImprisonDarkAnos01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ImprisonDarkAnos02()


class ImprisonDarkAnos02(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AsimovTalk01()


class AsimovTalk01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__0$', duration=5000, align='center', illustId='0') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=DarkAnosTalk01CSkip, arg2='nextState')
        set_skip(state=AsimovTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return AsimovTalk01Skip()


class AsimovTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ZoominAnos01()


class ZoominAnos01(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return AnosTruning01()


class AnosTruning01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5500], visible=True) # DarkAura01

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AnosTruning02()


class AnosTruning02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return AnosTalk01()


class AnosTalk01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003289, msg='$52000137_QD__ACT01__1$', duration=4000, align='center', illustId='0') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_skip(state=AnosTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return AnosTalk01Skip()


class AnosTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CameraChange00()


class CameraChange00(state.State):
    def on_enter(self):
        select_camera(triggerId=603, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange01()


class CameraChange01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCTalk01()


class PCTalk01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__2$', duration=4000, align='center', illustId='0')
        set_skip(state=PCTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCTalk01Skip()


class PCTalk01Skip(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return AsimovTalk02()


class AsimovTalk02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__3$', duration=4000, align='center', illustId='Asimov_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)
        set_skip(state=AsimovTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return AsimovTalk02Skip()


class AsimovTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return AsimovTalk03()


class AsimovTalk03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__4$', duration=5000, align='center', illustId='Asimov_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_skip(state=AsimovTalk03Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return AsimovTalk03Skip()


class AsimovTalk03Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CameraChange02()


class CameraChange02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraChange03()


class CameraChange03(state.State):
    def on_enter(self):
        select_camera(triggerId=604, enable=True) # PC 어깨에 걸고

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCTalk02()


class PCTalk02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__5$', duration=5000, align='center', illustId='0')
        set_skip(state=PCTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PCTalk02Skip()


class PCTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CameraChange04()


class CameraChange04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[104], arg2=False)
        select_camera(triggerId=605, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DarkAnosTalk01()


class DarkAnosTalk01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Attack_Idle_A,Attack_Idle_A') # 1533
        add_cinematic_talk(npcId=11003285, msg='$52000137_QD__ACT01__6$', duration=3000, align='center', illustId='Patos_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_skip(state=DarkAnosTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3100):
            return DarkAnosTalk01Skip()


class DarkAnosTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return DarkAnosAttackAsimov01()


class DarkAnosAttackAsimov01(state.State):
    def on_enter(self):
        select_camera(triggerId=610, enable=True)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Attack_01_A,Attack_Idle_A') # 3200

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return DarkAnosAttackAsimov02()


class DarkAnosAttackAsimov02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5200], visible=True) # ShieldExplosion
        destroy_monster(spawnIds=[201,910,920])
        create_monster(spawnIds=[202], arg2=False)
        set_effect(triggerIds=[5501], visible=True) # DarkAura02

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return DarkAnosAttackAsimov03()


class DarkAnosAttackAsimov03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5500], visible=False) # DarkAura01
        set_effect(triggerIds=[5101], visible=False) # RuneShieldThunder
        set_effect(triggerIds=[5100], visible=False) # AsimovShield

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraChange05()


class CameraChange05(state.State):
    def on_enter(self):
        select_camera(triggerId=611, enable=True)
        move_user_path(patrolName='MS2PatrolData_1003')
        add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__7$', duration=2000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraChange06()


class CameraChange06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_effect(triggerIds=[5501], visible=False) # DarkAura02

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange07()


class CameraChange07(state.State):
    def on_enter(self):
        select_camera(triggerId=612, enable=True) # PC 어깨에 걸고
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return AsimovTalk04()


class AsimovTalk04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003283, msg='$52000137_QD__ACT01__8$', duration=5000, align='center', illustId='Asimov_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_skip(state=AsimovTalk04Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return AsimovTalk04Skip()


class AsimovTalk04Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_npc_emotion_sequence(spawnId=202, sequenceName='Event_02_A,Down_Idle_A,Down_Idle_A,Down_Idle_A,Down_Idle_A') # 임시 - 기절하는 동작 제작되면 타이밍 맞추기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return AsimovFaint01()


class AsimovFaint01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AsimovFaint02()


class AsimovFaint02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[203], arg2=False)
        select_camera(triggerId=613, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AsimovFaint03()


class AsimovFaint03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DarkAnosApproach01()


class DarkAnosApproach01(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_104')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return DarkAnosApproach02()


class DarkAnosApproach02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return DarkAnosTalk02()


class DarkAnosTalk02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003285, msg='$52000137_QD__ACT01__9$', duration=5000, align='center', illustId='Patos_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_skip(state=DarkAnosTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DarkAnosTalk02Skip()


class DarkAnosTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PCTalk03()


class PCTalk03(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__10$', duration=5000, align='center', illustId='0')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PCTalk03Skip()


class PCTalk03Skip(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Idle_A'])
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return DarkAnosTalk03()


class DarkAnosTalk03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003285, msg='$52000137_QD__ACT01__11$', duration=4000, align='center', illustId='Patos_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return DarkAnosTalk03Skip()


class DarkAnosTalk01CSkip(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[201,910,920])
        create_monster(spawnIds=[202], arg2=False)
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[203], arg2=False)
        set_effect(triggerIds=[5500], visible=False) # DarkAura01
        set_effect(triggerIds=[5501], visible=False) # DarkAura02
        set_effect(triggerIds=[5100], visible=False) # AsimovShield
        set_effect(triggerIds=[5101], visible=False) # RuneShieldThunder
        set_effect(triggerIds=[5200], visible=False) # ShieldExplosion
        set_pc_emotion_sequence(sequenceNames=['Attack_Idle_A'])
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return DarkAnosTalk03Skip()


class DarkAnosTalk03Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DarkAnosBattle01()


class DarkAnosBattle01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DarkAnosBattle02()


class DarkAnosBattle02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[104])
        create_monster(spawnIds=[900], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='PatosTired', value=1):
            return DarkAnosDown01()
        if monster_dead(boxIds=[900]):
            return DarkAnosDown01()


class DarkAnosDown01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PositionArrange01()


class PositionArrange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[900])
        create_monster(spawnIds=[105], arg2=False)
        move_user(mapId=52000137, portalId=10, boxId=9900)
        select_camera(triggerId=620, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PositionArrange02()


class PositionArrange02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCBalloonTalk01()


class PCBalloonTalk01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2000')
        add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__12$', duration=2000, delayTick=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCBalloonTalk02()


class PCBalloonTalk02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__13$', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCBalloonTalk03()


class PCBalloonTalk03(state.State):
    def on_enter(self):
        select_camera(triggerId=621, enable=True)
        move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return KanduraApp01()


class KanduraApp01(state.State):
    def on_enter(self):
        select_camera(triggerId=622, enable=True)
        create_monster(spawnIds=[301], arg2=False)
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return KanduraApp02()


class KanduraApp02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$52000137_QD__ACT01__14$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KanduraApp03()


class KanduraApp03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KanduraAttack01()


class KanduraAttack01(state.State):
    def on_enter(self):
        select_camera(triggerId=623, enable=True)
        set_npc_emotion_sequence(spawnId=301, sequenceName='Event_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return KanduraAttack02()


class KanduraAttack02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraChange10()


class CameraChange10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange11()


class CameraChange11(state.State):
    def on_enter(self):
        select_camera(triggerId=630, enable=True) # PC 등뒤에서
        set_pc_emotion_loop(sequenceName='Push_A', duration=30000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraChange12()


class CameraChange12(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return KanduraTalk01()


class KanduraTalk01(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='MS2PatrolData_302')
        add_cinematic_talk(npcId=11003287, msg='$52000137_QD__ACT01__15$', duration=4000, align='center', illustId='Kandura_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_scene_skip(state=ShowCaption04Skip, arg2='exit')
        set_skip(state=KanduraTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraTalk01Skip()


class KanduraTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PCTalk04()


class PCTalk04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000137_QD__ACT01__16$', duration=4000, align='center', illustId='0')
        set_skip(state=PCTalk04Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCTalk04Skip()


class PCTalk04Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return KanduraMoveToDarkAnos01()


class KanduraMoveToDarkAnos01(state.State):
    def on_enter(self):
        select_camera(triggerId=631, enable=True)
        move_npc(spawnId=301, patrolName='MS2PatrolData_303')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return KanduraTalk02()


class KanduraTalk02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003287, msg='$52000137_QD__ACT01__17$', duration=4000, align='center', illustId='Kandura_normal') # align = 일러스트 위치 : (left/ center/ right) 3가지 지원 (생략 시 center)
        set_skip(state=KanduraTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return KanduraTalk02Skip()


class KanduraTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return KanduraReadyToDisapp01()


#  칸두라가 흑화된 아노스를 데리고 함께 사라지는 연출 
class KanduraReadyToDisapp01(state.State):
    def on_enter(self):
        select_camera(triggerId=632, enable=True)
        set_npc_emotion_sequence(spawnId=301, sequenceName='Event_02_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return KanduraReadyToDisapp02()


class KanduraReadyToDisapp02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=True) # Vibrate
        set_effect(triggerIds=[5400], visible=True) # DarkStrom01

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return KanduraReadyToDisapp03()


class KanduraReadyToDisapp03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=False) # DarkStrom01
        set_effect(triggerIds=[5401], visible=True) # DarkStrom02
        destroy_monster(spawnIds=[105,301])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return KanduraReadyToDisapp04()


class KanduraReadyToDisapp04(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ShowCaption01()


#  설명문 출력 
class ShowCaption01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ShowCaption02()


class ShowCaption02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000137_QD__ACT01__18$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return ShowCaption02Skip()


class ShowCaption02Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption03()


class ShowCaption03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000137_QD__ACT01__19$')
        set_skip(state=ShowCaption03Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return ShowCaption03Skip()


class ShowCaption03Skip(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption04()


class ShowCaption04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000137_QD__ACT01__20$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return ShowCaption04Skip()


class ShowCaption04Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='AsimovRetire')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        reset_camera(interpolationTime=1)
        move_user(mapId=2000035, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


