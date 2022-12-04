""" trigger/63000020_cs/battle01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 미션 완료 사운드 이펙트
        self.create_monster(spawnIds=[101,201,301,401,501], animationEffect=False)
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_skill(triggerIds=[7000], enable=False) # PCKnockBack
        self.set_effect(triggerIds=[7001], visible=False) # VibrateDizzy
        self.set_effect(triggerIds=[6000], visible=False) # RingBellStart
        self.set_effect(triggerIds=[6001], visible=False) # RingBellFinish
        self.set_effect(triggerIds=[7100], visible=False) # Voice VasaraChen 00001349
        self.set_effect(triggerIds=[7101], visible=False) # Voice VasaraChen 00001350
        self.set_effect(triggerIds=[7102], visible=False) # Voice VasaraChen 00001351
        self.set_effect(triggerIds=[7103], visible=False) # Voice VasaraChen 00001374
        self.set_effect(triggerIds=[7200], visible=False) # Voice Speenchi 03000902
        self.set_effect(triggerIds=[7201], visible=False) # Voice Speenchi 03000903
        self.set_effect(triggerIds=[7202], visible=False) # Voice Speenchi 03000904
        self.set_effect(triggerIds=[7203], visible=False) # Voice Speenchi 03000905
        self.set_effect(triggerIds=[7204], visible=False) # Voice Speenchi 03000906
        self.set_effect(triggerIds=[7205], visible=False) # Voice Speenchi 03000907
        self.set_effect(triggerIds=[7206], visible=False) # Voice Speenchi 03000908
        self.set_effect(triggerIds=[7207], visible=False) # Voice Speenchi 03000909
        self.set_effect(triggerIds=[7208], visible=False) # Voice Speenchi 03000910
        self.set_effect(triggerIds=[7209], visible=False) # Voice Speenchi 03000911
        self.set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        self.set_effect(triggerIds=[7211], visible=False) # Voice Speenchi 03000913

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9900], skillId=70000093, level=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=511, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return LookAround04(self.ctx)


class LookAround04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return TalkKay03(self.ctx)


class TalkKay03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=13000)
        self.set_effect(triggerIds=[7205], visible=True) # Voice Speenchi 03000907
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__0$', arg4=7) # Voice 03000907
        self.set_skip(state=TalkKay04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return TalkKay04(self.ctx)


class TalkKay04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7205], visible=False) # Voice Speenchi 03000907
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TalkKay10(self.ctx)


class TalkKay10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__1$', arg4=8) # Voice 03000908
        self.set_effect(triggerIds=[7206], visible=True) # Voice Speenchi 03000908
        self.set_skip(state=TalkKay11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return TalkKay11(self.ctx)


class TalkKay11(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.set_effect(triggerIds=[7206], visible=False) # Voice Speenchi 03000908
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstChampoin01(self.ctx)


class FirstChampoin01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FirstChampoin02(self.ctx)


class FirstChampoin02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=601, enable=True)
        self.create_monster(spawnIds=[901], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FirstChampoin03(self.ctx)


class FirstChampoin03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_900')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__2$', arg4=4) # Voice 03000909
        self.set_effect(triggerIds=[7207], visible=True) # Voice Speenchi 03000909

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return FirstChampoin04(self.ctx)


class FirstChampoin04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FirstChampoin05(self.ctx)


class FirstChampoin05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7207], visible=False) # Voice Speenchi 03000909
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstChampoin06(self.ctx)


class FirstChampoin06(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000020, portalId=2)
        self.destroy_monster(spawnIds=[901])
        self.create_monster(spawnIds=[911], animationEffect=False)
        self.select_camera(triggerId=700, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstBattle01(self.ctx)


class FirstBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__3$', arg4=5) # Voice 03000912
        self.set_effect(triggerIds=[7210], visible=True) # Voice Speenchi 03000912
        self.set_skip(state=FirstBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return FirstBattle02(self.ctx)


class FirstBattle02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=700, enable=False)
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstBattle03(self.ctx)


class FirstBattle03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10025010, textId=10025010) # 가이드 : 폭주기관차 실바 쓰러트리기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[911]):
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True) # RingBellFinish
        self.set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.hide_guide_summary(entityId=10025010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondChampoin01(self.ctx)


class SecondChampoin01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[600,601], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return SecondChampoin02(self.ctx)


class SecondChampoin02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[902], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return SecondChampoin03(self.ctx)


class SecondChampoin03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=902, patrolName='MS2PatrolData_900')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__4$', arg4=4) # Voice 03000910
        self.set_effect(triggerIds=[7208], visible=True) # Voice Speenchi 03000910

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondChampoin04(self.ctx)


class SecondChampoin04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=902, patrolName='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return SecondChampoin05(self.ctx)


class SecondChampoin05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7208], visible=False) # Voice Speenchi 03000910
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondChampoin06(self.ctx)


class SecondChampoin06(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000020, portalId=2)
        self.destroy_monster(spawnIds=[902])
        self.create_monster(spawnIds=[912], animationEffect=False)
        self.select_camera(triggerId=700, enable=True)
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondBattle01(self.ctx)


class SecondBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__5$', arg4=5) # Voice 03000912
        self.set_effect(triggerIds=[7210], visible=True) # Voice Speenchi 03000912
        self.set_skip(state=SecondBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondBattle02(self.ctx)


class SecondBattle02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=700, enable=False)
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondBattle03(self.ctx)


class SecondBattle03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10025020, textId=10025020) # 가이드 : 불멸의 피닉스 쓰러트리기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[912]):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True) # RingBellFinish
        self.set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.hide_guide_summary(entityId=10025020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ThirdChampoin01(self.ctx)


class ThirdChampoin01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[600,601], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ThirdChampoin02(self.ctx)


class ThirdChampoin02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[903], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ThirdChampoin03(self.ctx)


class ThirdChampoin03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=903, patrolName='MS2PatrolData_900')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__6$', arg4=5) # Voice 03000911
        self.set_effect(triggerIds=[7209], visible=True) # Voice Speenchi 03000911

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdChampoin04(self.ctx)


class ThirdChampoin04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=903, patrolName='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ThirdChampoin05(self.ctx)


class ThirdChampoin05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7209], visible=False) # Voice Speenchi 03000911
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdChampoin06(self.ctx)


class ThirdChampoin06(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000020, portalId=2)
        self.destroy_monster(spawnIds=[903])
        self.create_monster(spawnIds=[913], animationEffect=False)
        self.select_camera(triggerId=700, enable=True)
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdBattle01(self.ctx)


class ThirdBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_effect(triggerIds=[7210], visible=True) # Voice Speenchi 03000912
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__7$', arg4=5) # Voice 03000912
        self.set_skip(state=ThirdBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdBattle02(self.ctx)


class ThirdBattle02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7210], visible=False) # Voice Speenchi 03000912
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=700, enable=False)
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdBattle03(self.ctx)


class ThirdBattle03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10025030, textId=10025030) # 가이드 : 롤링 더글라스 쓰러트리기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[913]):
            return Delay03(self.ctx)


class Delay03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True) # RingBellFinish
        self.set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.hide_guide_summary(entityId=10025030)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return TalkKay20(self.ctx)


class TalkKay20(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=503, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return TalkKay21(self.ctx)


class TalkKay21(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.select_camera(triggerId=502, enable=True)
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__8$', arg4=9) # Voice 03000913
        self.set_effect(triggerIds=[7211], visible=True) # Voice Speenchi 03000913
        self.set_skip(state=TalkKay22)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return TalkKay22(self.ctx)


class TalkKay22(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000020, portalId=6)
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[7211], visible=False) # Voice Speenchi 03000913

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCFeelDizzy01(self.ctx)


# PC 현기증 Blur
class PCFeelDizzy01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=703, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return PCFeelDizzy02(self.ctx)


class PCFeelDizzy02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$63000020_CS__BATTLE01__9$', arg4=4, arg5=0)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_A','Emotion_Disappoint_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4200):
            return PCFeelDizzy03(self.ctx)


class PCFeelDizzy03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=705, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return PCFeelDizzy04(self.ctx)


class PCFeelDizzy04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=704, enable=True)
        self.set_effect(triggerIds=[7001], visible=True) # VibrateDizzy
        self.add_buff(boxIds=[9900], skillId=70000094, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return PCFeelOkay01(self.ctx)


class PCFeelOkay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=False) # VibrateDizzy
        self.add_buff(boxIds=[9900], skillId=70000096, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PCFeelOkay02(self.ctx)


class PCFeelOkay02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=703, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCFeelOkay03(self.ctx)


class PCFeelOkay03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$63000020_CS__BATTLE01__10$', arg4=4, arg5=0)
        self.set_pc_emotion_sequence(sequenceNames=['Bore_C'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PCFeelOkay04(self.ctx)


class PCFeelOkay04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=True) # RingBellStart
        self.select_camera(triggerId=504, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkKay23(self.ctx)


class TalkKay23(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__11$', arg4=9) # Voice 03000902
        self.set_effect(triggerIds=[7200], visible=True) # Voice Speenchi 03000902
        self.set_skip(state=TalkKay24)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return TalkKay24(self.ctx)


class TalkKay24(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.move_user(mapId=63000020, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkKay25(self.ctx)


class TalkKay25(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7200], visible=False) # Voice Speenchi 03000902
        self.select_camera(triggerId=710, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkKay26(self.ctx)


class TalkKay26(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__12$', arg4=14) # Voice 03000903
        self.set_effect(triggerIds=[7201], visible=True) # Voice Speenchi 03000903
        self.set_skip(state=TalkKay27)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=14000):
            return TalkKay27(self.ctx)


class TalkKay27(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[7201], visible=False) # Voice Speenchi 03000903

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkKay28(self.ctx)


class TalkKay28(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=502, enable=True)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__13$', arg4=10) # Voice 03000904
        self.set_effect(triggerIds=[7202], visible=True) # Voice Speenchi 03000904
        self.set_skip(state=TalkKay29)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return TalkKay29(self.ctx)


class TalkKay29(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7202], visible=False) # Voice Speenchi 03000904
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return LastChampoin01(self.ctx)


class LastChampoin01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LastChampoin02(self.ctx)


class LastChampoin02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[900], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return LastChampoin03(self.ctx)


class LastChampoin03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.move_npc(spawnId=900, patrolName='MS2PatrolData_902')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__14$', arg4=11) # Voice 03000905
        self.set_effect(triggerIds=[7203], visible=True) # Voice Speenchi 03000905

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return LastChampoin04(self.ctx)


class LastChampoin04(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=900, sequenceName='Bore_A')
        self.set_skip(state=LastChampoin05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return LastChampoin05(self.ctx)


class LastChampoin05(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=900, patrolName='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return LastChampoin06(self.ctx)


class LastChampoin06(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7203], visible=False) # Voice Speenchi 03000905
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LastChampoin07(self.ctx)


class LastChampoin07(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000020, portalId=2)
        self.destroy_monster(spawnIds=[900])
        self.create_monster(spawnIds=[924], animationEffect=False)
        self.select_camera(triggerId=700, enable=True)
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LastBattle01(self.ctx)


class LastBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11001626, script='$63000020_CS__BATTLE01__15$', arg4=7) # Voice 03000906
        self.set_effect(triggerIds=[7204], visible=True) # Voice Speenchi 03000906
        self.set_skip(state=LastBattle02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return LastBattle02(self.ctx)


# 조정 필요
class LastBattle02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7204], visible=False) # Voice Speenchi 03000906
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=701, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LastBattle03(self.ctx)


class LastBattle03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$63000020_CS__BATTLE01__16$', arg4=3, arg5=0)
        self.set_pc_emotion_sequence(sequenceNames=['Striker_Bore_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return LastBattle04(self.ctx)


class LastBattle04(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[924])
        self.create_monster(spawnIds=[910], animationEffect=False)
        self.select_camera(triggerId=702, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkChen10(self.ctx)


class TalkChen10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__17$', arg4=4) # Voice 00001349
        self.set_effect(triggerIds=[7100], visible=True) # Voice VasaraChen 00001349

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return TalkChen11(self.ctx)


class TalkChen11(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7100], visible=False) # Voice VasaraChen 00001349
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return BattleStart01(self.ctx)


class BattleStart01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=702, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[6000], visible=True) # RingBellStart

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BattleStart02(self.ctx)


class BattleStart02(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.show_guide_summary(entityId=10025040, textId=10025040) # 가이드 : 바사라 첸 쓰러트리기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return CameraAct01(self.ctx)


class CameraAct01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return CameraAct02(self.ctx)


class CameraAct02(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10025040)
        self.move_user(mapId=63000020, portalId=4)
        self.destroy_monster(spawnIds=[910])
        self.create_monster(spawnIds=[920], animationEffect=False)
        self.select_camera(triggerId=800, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCAttack01(self.ctx)


class PCAttack01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_pc_emotion_sequence(sequenceNames=['Knuckle_Attack_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return PCAttack02(self.ctx)


class PCAttack02(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Striker_Event_01'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return KnockBack01(self.ctx)


class KnockBack01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=920, sequenceName='Attack_01_H')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return KnockBack02(self.ctx)


class KnockBack02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7000], enable=True)
        self.select_camera(triggerId=801, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return KnockBack03(self.ctx)


class KnockBack03(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return BlurAct01(self.ctx)


# PC 1인칭 시점 Blur 연출
class BlurAct01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=802, enable=True) # FirstPerspective
        self.add_buff(boxIds=[9900], skillId=70000094, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BlurAct02(self.ctx)


class BlurAct02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=803, enable=True) # FirstPerspective
        self.set_effect(triggerIds=[7001], visible=True) # VibrateDizzy

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BlurAct03(self.ctx)


class BlurAct03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BlurAct04(self.ctx)


class BlurAct04(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9900], skillId=70000095, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return BlurAct05(self.ctx)


class BlurAct05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=805, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return BlurAct06(self.ctx)


class BlurAct06(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return BlurAct07(self.ctx)


class BlurAct07(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=24000)
        self.set_effect(triggerIds=[7001], visible=False) # VibrateDizzy
        self.add_buff(boxIds=[9900], skillId=70000096, level=1)
        self.select_camera(triggerId=806, enable=True)
        self.destroy_monster(spawnIds=[920])
        self.create_monster(spawnIds=[922], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return BlurAct08(self.ctx)


class BlurAct08(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=922, patrolName='MS2PatrolData_920')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkChen01(self.ctx)


class TalkChen01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__18$', arg4=5) # Voice 00001350
        self.set_effect(triggerIds=[7101], visible=True) # Voice VasaraChen 00001350
        self.set_skip(state=TalkChen02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TalkChen02(self.ctx)


class TalkChen02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7101], visible=False) # Voice VasaraChen 00001350
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TalkChen03(self.ctx)


class TalkChen03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__19$', arg4=4) # Voice 00001374  Think
        self.set_effect(triggerIds=[7103], visible=True) # Voice VasaraChen 00001374
        self.set_skip(state=TalkChen04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return TalkChen04(self.ctx)


class TalkChen04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7103], visible=False) # Voice VasaraChen 00001374
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TalkChen05(self.ctx)


class TalkChen05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001547, script='$63000020_CS__BATTLE01__20$', arg4=4) # Voice 00001351
        self.set_effect(triggerIds=[7102], visible=True) # Voice VasaraChen 00001351
        self.set_skip(state=TalkChen06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return TalkChen06(self.ctx)


class TalkChen06(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[922])
        self.create_monster(spawnIds=[923], animationEffect=False)
        self.set_effect(triggerIds=[7102], visible=False) # Voice VasaraChen 00001351
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LastAttack00(self.ctx)


class LastAttack00(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=923, sequenceName='Attack_02_G', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LastAttack01(self.ctx)


# Skill Effect Attack 연출
class LastAttack01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(boxIds=[9900], skillId=70000095, level=1)
        self.select_camera(triggerId=807, enable=True) # FirstPerspective Hit

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LastAttack02(self.ctx)


class LastAttack02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=808, enable=True) # FirstPerspective Hit

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return LastAttack03(self.ctx)


class LastAttack03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=923, sequenceName='Attack_03_G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return PCFainted01(self.ctx)


class PCFainted01(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9900], skillId=70000096, level=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCFainted02(self.ctx)


class PCFainted02(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9900], skillId=70000095, level=1)
        self.select_camera(triggerId=804, enable=True) # FirstPerspective Down

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCFainted03(self.ctx)


class PCFainted03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A') # WeiHong

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PlayerDown01(self.ctx)


class PlayerDown01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PlayerDown02(self.ctx)


class PlayerDown02(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9900], skillId=70000096, level=1)
        self.move_user(mapId=63000020, portalId=5)
        self.destroy_monster(spawnIds=[923])
        self.create_monster(spawnIds=[921], animationEffect=False)
        self.select_camera(triggerId=810, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PlayerDown03(self.ctx)


class PlayerDown03(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=16000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PlayerDown04(self.ctx)


class PlayerDown04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        self.set_effect(triggerIds=[6001], visible=True) # RingBellFinish

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PlayerDown05(self.ctx)


class PlayerDown05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=811, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PlayerDown06(self.ctx)


class PlayerDown06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=812, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PlayerDown07(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[921])


class PlayerDown07(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=812, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MoveToNextMap01(self.ctx)


class MoveToNextMap01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=63000021, portalId=1, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
