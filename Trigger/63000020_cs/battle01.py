""" trigger/63000020_cs/battle01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 미션 완료 사운드 이펙트
        create_monster(spawnIds=[101,201,301,401,501], arg2=False)
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_skill(triggerIds=[7000], isEnable=False) # PCKnockBack
        set_effect(triggerIds=[7001], visible=False) # VibrateDizzy
        set_effect(triggerIds=[6000], visible=False) # RingBellStart
        set_effect(triggerIds=[6001], visible=False) # RingBellFinish
        set_effect(triggerIds=[7100], visible=False) # Voice VasaraChen 00001349
        set_effect(triggerIds=[7101], visible=False) # Voice VasaraChen 00001350
        set_effect(triggerIds=[7102], visible=False) # Voice VasaraChen 00001351
        set_effect(triggerIds=[7103], visible=False) # Voice VasaraChen 00001374
        set_effect(triggerIds=[7200], visible=False) # Voice Speenchi 03000902
        set_effect(triggerIds=[7201], visible=False) # Voice Speenchi 03000903
        set_effect(triggerIds=[7202], visible=False) # Voice Speenchi 03000904
        set_effect(triggerIds=[7203], visible=False) # Voice Speenchi 03000905
        set_effect(triggerIds=[7204], visible=False) # Voice Speenchi 03000906
        set_effect(triggerIds=[7205], visible=False) # Voice Speenchi 03000907
        set_effect(triggerIds=[7206], visible=False) # Voice Speenchi 03000908
        set_effect(triggerIds=[7207], visible=False) # Voice Speenchi 03000909
        set_effect(triggerIds=[7208], visible=False) # Voice Speenchi 03000910
        set_effect(triggerIds=[7209], visible=False) # Voice Speenchi 03000911
        set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        set_effect(triggerIds=[7211], visible=False) # Voice Speenchi 03000913

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=70000093, level=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=500, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround01()


class LookAround01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround02()


class LookAround02(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return LookAround03()


class LookAround03(state.State):
    def on_enter(self):
        select_camera(triggerId=511, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LookAround04()


class LookAround04(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return TalkKay03()


class TalkKay03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=13000)
        set_effect(triggerIds=[7205], visible=True) # Voice Speenchi 03000907
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__0$', arg4=7) # Voice 03000907
        set_skip(state=TalkKay04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return TalkKay04()


class TalkKay04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7205], visible=False) # Voice Speenchi 03000907
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TalkKay10()


class TalkKay10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__1$', arg4=8) # Voice 03000908
        set_effect(triggerIds=[7206], visible=True) # Voice Speenchi 03000908
        set_skip(state=TalkKay11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return TalkKay11()


class TalkKay11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        set_effect(triggerIds=[7206], visible=False) # Voice Speenchi 03000908
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstChampoin01()


class FirstChampoin01(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FirstChampoin02()


class FirstChampoin02(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)
        create_monster(spawnIds=[901], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FirstChampoin03()


class FirstChampoin03(state.State):
    def on_enter(self):
        move_npc(spawnId=901, patrolName='MS2PatrolData_900')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__2$', arg4=4) # Voice 03000909
        set_effect(triggerIds=[7207], visible=True) # Voice Speenchi 03000909

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FirstChampoin04()


class FirstChampoin04(state.State):
    def on_enter(self):
        move_npc(spawnId=901, patrolName='MS2PatrolData_901')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FirstChampoin05()


class FirstChampoin05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7207], visible=False) # Voice Speenchi 03000909
        remove_cinematic_talk()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstChampoin06()


class FirstChampoin06(state.State):
    def on_enter(self):
        move_user(mapId=63000020, portalId=2)
        destroy_monster(spawnIds=[901])
        create_monster(spawnIds=[911], arg2=False)
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstBattle01()


class FirstBattle01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__3$', arg4=5) # Voice 03000912
        set_effect(triggerIds=[7210], visible=True) # Voice Speenchi 03000912
        set_skip(state=FirstBattle02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return FirstBattle02()


class FirstBattle02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=700, enable=False)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstBattle03()


class FirstBattle03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10025010, textId=10025010) # 가이드 : 폭주기관차 실바 쓰러트리기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[911]):
            return Delay01()


class Delay01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # RingBellFinish
        set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        hide_guide_summary(entityId=10025010)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondChampoin01()


class SecondChampoin01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[600,601], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SecondChampoin02()


class SecondChampoin02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[902], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SecondChampoin03()


class SecondChampoin03(state.State):
    def on_enter(self):
        move_npc(spawnId=902, patrolName='MS2PatrolData_900')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__4$', arg4=4) # Voice 03000910
        set_effect(triggerIds=[7208], visible=True) # Voice Speenchi 03000910

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondChampoin04()


class SecondChampoin04(state.State):
    def on_enter(self):
        move_npc(spawnId=902, patrolName='MS2PatrolData_901')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SecondChampoin05()


class SecondChampoin05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7208], visible=False) # Voice Speenchi 03000910
        remove_cinematic_talk()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondChampoin06()


class SecondChampoin06(state.State):
    def on_enter(self):
        move_user(mapId=63000020, portalId=2)
        destroy_monster(spawnIds=[902])
        create_monster(spawnIds=[912], arg2=False)
        select_camera(triggerId=700, enable=True)
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondBattle01()


class SecondBattle01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__5$', arg4=5) # Voice 03000912
        set_effect(triggerIds=[7210], visible=True) # Voice Speenchi 03000912
        set_skip(state=SecondBattle02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondBattle02()


class SecondBattle02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=700, enable=False)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondBattle03()


class SecondBattle03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10025020, textId=10025020) # 가이드 : 불멸의 피닉스 쓰러트리기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[912]):
            return Delay02()


class Delay02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # RingBellFinish
        set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        hide_guide_summary(entityId=10025020)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdChampoin01()


class ThirdChampoin01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[600,601], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ThirdChampoin02()


class ThirdChampoin02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[903], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ThirdChampoin03()


class ThirdChampoin03(state.State):
    def on_enter(self):
        move_npc(spawnId=903, patrolName='MS2PatrolData_900')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__6$', arg4=5) # Voice 03000911
        set_effect(triggerIds=[7209], visible=True) # Voice Speenchi 03000911

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdChampoin04()


class ThirdChampoin04(state.State):
    def on_enter(self):
        move_npc(spawnId=903, patrolName='MS2PatrolData_901')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ThirdChampoin05()


class ThirdChampoin05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7209], visible=False) # Voice Speenchi 03000911
        remove_cinematic_talk()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdChampoin06()


class ThirdChampoin06(state.State):
    def on_enter(self):
        move_user(mapId=63000020, portalId=2)
        destroy_monster(spawnIds=[903])
        create_monster(spawnIds=[913], arg2=False)
        select_camera(triggerId=700, enable=True)
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdBattle01()


class ThirdBattle01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_effect(triggerIds=[7210], visible=True) # Voice Speenchi 03000912
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__7$', arg4=5) # Voice 03000912
        set_skip(state=ThirdBattle02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdBattle02()


class ThirdBattle02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=700, enable=False)
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdBattle03()


class ThirdBattle03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10025030, textId=10025030) # 가이드 : 롤링 더글라스 쓰러트리기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[913]):
            return Delay03()


class Delay03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True) # RingBellFinish
        set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        hide_guide_summary(entityId=10025030)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TalkKay20()


class TalkKay20(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=503, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TalkKay21()


class TalkKay21(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        select_camera(triggerId=502, enable=True)
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__8$', arg4=9) # Voice 03000913
        set_effect(triggerIds=[7211], visible=True) # Voice Speenchi 03000913
        set_skip(state=TalkKay22)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return TalkKay22()


class TalkKay22(state.State):
    def on_enter(self):
        move_user(mapId=63000020, portalId=6)
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[7211], visible=False) # Voice Speenchi 03000913

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCFeelDizzy01()


#  PC 현기증 Blur 
class PCFeelDizzy01(state.State):
    def on_enter(self):
        select_camera(triggerId=703, enable=True)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PCFeelDizzy02()


class PCFeelDizzy02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$63000020_CS__BATTLE01__9$', arg4=4, arg5=0)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_A','Emotion_Disappoint_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4200):
            return PCFeelDizzy03()


class PCFeelDizzy03(state.State):
    def on_enter(self):
        select_camera(triggerId=705, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return PCFeelDizzy04()


class PCFeelDizzy04(state.State):
    def on_enter(self):
        select_camera(triggerId=704, enable=True)
        set_effect(triggerIds=[7001], visible=True) # VibrateDizzy
        add_buff(boxIds=[9900], skillId=70000094, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PCFeelOkay01()


class PCFeelOkay01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False) # VibrateDizzy
        add_buff(boxIds=[9900], skillId=70000096, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PCFeelOkay02()


class PCFeelOkay02(state.State):
    def on_enter(self):
        select_camera(triggerId=703, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCFeelOkay03()


class PCFeelOkay03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$63000020_CS__BATTLE01__10$', arg4=4, arg5=0)
        set_pc_emotion_sequence(sequenceNames=['Bore_C'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PCFeelOkay04()


class PCFeelOkay04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # RingBellStart
        select_camera(triggerId=504, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkKay23()


class TalkKay23(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__11$', arg4=9) # Voice 03000902
        set_effect(triggerIds=[7200], visible=True) # Voice Speenchi 03000902
        set_skip(state=TalkKay24)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return TalkKay24()


class TalkKay24(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        move_user(mapId=63000020, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkKay25()


class TalkKay25(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7200], visible=False) # Voice Speenchi 03000902
        select_camera(triggerId=710, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkKay26()


class TalkKay26(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__12$', arg4=14) # Voice 03000903
        set_effect(triggerIds=[7201], visible=True) # Voice Speenchi 03000903
        set_skip(state=TalkKay27)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return TalkKay27()


class TalkKay27(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[7201], visible=False) # Voice Speenchi 03000903

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkKay28()


class TalkKay28(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=502, enable=True)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__13$', arg4=10) # Voice 03000904
        set_effect(triggerIds=[7202], visible=True) # Voice Speenchi 03000904
        set_skip(state=TalkKay29)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return TalkKay29()


class TalkKay29(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7202], visible=False) # Voice Speenchi 03000904
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return LastChampoin01()


class LastChampoin01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LastChampoin02()


class LastChampoin02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[900], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LastChampoin03()


class LastChampoin03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        move_npc(spawnId=900, patrolName='MS2PatrolData_902')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__14$', arg4=11) # Voice 03000905
        set_effect(triggerIds=[7203], visible=True) # Voice Speenchi 03000905

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LastChampoin04()


class LastChampoin04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=900, sequenceName='Bore_A')
        set_skip(state=LastChampoin05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return LastChampoin05()


class LastChampoin05(state.State):
    def on_enter(self):
        move_npc(spawnId=900, patrolName='MS2PatrolData_901')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LastChampoin06()


class LastChampoin06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7203], visible=False) # Voice Speenchi 03000905
        remove_cinematic_talk()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LastChampoin07()


class LastChampoin07(state.State):
    def on_enter(self):
        move_user(mapId=63000020, portalId=2)
        destroy_monster(spawnIds=[900])
        create_monster(spawnIds=[924], arg2=False)
        select_camera(triggerId=700, enable=True)
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LastBattle01()


class LastBattle01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__15$', arg4=7) # Voice 03000906
        set_effect(triggerIds=[7204], visible=True) # Voice Speenchi 03000906
        set_skip(state=LastBattle02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LastBattle02()


#   조정 필요 
class LastBattle02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7204], visible=False) # Voice Speenchi 03000906
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=701, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LastBattle03()


class LastBattle03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$63000020_CS__BATTLE01__16$', arg4=3, arg5=0)
        set_pc_emotion_sequence(sequenceNames=['Striker_Bore_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return LastBattle04()


class LastBattle04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[924])
        create_monster(spawnIds=[910], arg2=False)
        select_camera(triggerId=702, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkChen10()


class TalkChen10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__17$', arg4=4) # Voice 00001349
        set_effect(triggerIds=[7100], visible=True) # Voice VasaraChen 00001349

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TalkChen11()


class TalkChen11(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7100], visible=False) # Voice VasaraChen 00001349
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return BattleStart01()


class BattleStart01(state.State):
    def on_enter(self):
        select_camera(triggerId=702, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BattleStart02()


class BattleStart02(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        show_guide_summary(entityId=10025040, textId=10025040) # 가이드 : 바사라 첸 쓰러트리기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return CameraAct01()


class CameraAct01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraAct02()


class CameraAct02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10025040)
        move_user(mapId=63000020, portalId=4)
        destroy_monster(spawnIds=[910])
        create_monster(spawnIds=[920], arg2=False)
        select_camera(triggerId=800, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCAttack01()


class PCAttack01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_pc_emotion_sequence(sequenceNames=['Knuckle_Attack_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return PCAttack02()


class PCAttack02(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Striker_Event_01'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return KnockBack01()


class KnockBack01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=920, sequenceName='Attack_01_H')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return KnockBack02()


class KnockBack02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=True)
        select_camera(triggerId=801, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return KnockBack03()


class KnockBack03(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Push_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return BlurAct01()


#  PC 1인칭 시점 Blur 연출 
class BlurAct01(state.State):
    def on_enter(self):
        select_camera(triggerId=802, enable=True) # FirstPerspective
        add_buff(boxIds=[9900], skillId=70000094, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BlurAct02()


class BlurAct02(state.State):
    def on_enter(self):
        select_camera(triggerId=803, enable=True) # FirstPerspective
        set_effect(triggerIds=[7001], visible=True) # VibrateDizzy

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BlurAct03()


class BlurAct03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BlurAct04()


class BlurAct04(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=70000095, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return BlurAct05()


class BlurAct05(state.State):
    def on_enter(self):
        select_camera(triggerId=805, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1200):
            return BlurAct06()


class BlurAct06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return BlurAct07()


class BlurAct07(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=24000)
        set_effect(triggerIds=[7001], visible=False) # VibrateDizzy
        add_buff(boxIds=[9900], skillId=70000096, level=1)
        select_camera(triggerId=806, enable=True)
        destroy_monster(spawnIds=[920])
        create_monster(spawnIds=[922], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return BlurAct08()


class BlurAct08(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=922, patrolName='MS2PatrolData_920')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkChen01()


class TalkChen01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__18$', arg4=5) # Voice 00001350
        set_effect(triggerIds=[7101], visible=True) # Voice VasaraChen 00001350
        set_skip(state=TalkChen02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TalkChen02()


class TalkChen02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7101], visible=False) # Voice VasaraChen 00001350
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TalkChen03()


class TalkChen03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__19$', arg4=4) # Voice 00001374  Think
        set_effect(triggerIds=[7103], visible=True) # Voice VasaraChen 00001374
        set_skip(state=TalkChen04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TalkChen04()


class TalkChen04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7103], visible=False) # Voice VasaraChen 00001374
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TalkChen05()


class TalkChen05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__20$', arg4=4) # Voice 00001351
        set_effect(triggerIds=[7102], visible=True) # Voice VasaraChen 00001351
        set_skip(state=TalkChen06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TalkChen06()


class TalkChen06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[922])
        create_monster(spawnIds=[923], arg2=False)
        set_effect(triggerIds=[7102], visible=False) # Voice VasaraChen 00001351
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LastAttack00()


class LastAttack00(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=923, sequenceName='Attack_02_G', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LastAttack01()


#  Skill Effect Attack 연출 
class LastAttack01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_buff(boxIds=[9900], skillId=70000095, level=1)
        select_camera(triggerId=807, enable=True) # FirstPerspective Hit

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return LastAttack02()


class LastAttack02(state.State):
    def on_enter(self):
        select_camera(triggerId=808, enable=True) # FirstPerspective Hit

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return LastAttack03()


class LastAttack03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=923, sequenceName='Attack_03_G')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return PCFainted01()


class PCFainted01(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=70000096, level=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCFainted02()


class PCFainted02(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=70000095, level=1)
        select_camera(triggerId=804, enable=True) # FirstPerspective Down

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCFainted03()


class PCFainted03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A') # WeiHong

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PlayerDown01()


class PlayerDown01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PlayerDown02()


class PlayerDown02(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=70000096, level=1)
        move_user(mapId=63000020, portalId=5)
        destroy_monster(spawnIds=[923])
        create_monster(spawnIds=[921], arg2=False)
        select_camera(triggerId=810, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PlayerDown03()


class PlayerDown03(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=16000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PlayerDown04()


class PlayerDown04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        set_effect(triggerIds=[6001], visible=True) # RingBellFinish

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PlayerDown05()


class PlayerDown05(state.State):
    def on_enter(self):
        select_camera(triggerId=811, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PlayerDown06()


class PlayerDown06(state.State):
    def on_enter(self):
        select_camera(triggerId=812, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return PlayerDown07()

    def on_exit(self):
        destroy_monster(spawnIds=[921])


class PlayerDown07(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=812, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MoveToNextMap01()


class MoveToNextMap01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=63000021, portalId=1, boxId=9900)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    pass


