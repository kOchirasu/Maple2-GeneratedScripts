""" trigger/52000086_qd/hp50.xml """
import trigger_api


class 퀘스트체크50100300_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[3]):
            return 던전종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[2]):
            return 던전종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100300], questStates=[1]):
            return 대기(self.ctx)


class 퀘스트체크50100310_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[3]):
            return 던전종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[2]):
            return 던전종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100310], questStates=[1]):
            return 대기(self.ctx)


class 퀘스트체크50100311_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[3]):
            return 던전종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[2]):
            return 던전종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100311], questStates=[1]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.set_portal(portalId=91, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='hp50', value=1):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[1007,1008], animationEffect=False)
        self.move_user(mapId=52000086, portalId=30)
        self.select_camera(triggerId=313, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다등장(self.ctx)


class 에르다등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(triggerId=314, enable=True)
        self.move_npc(spawnId=1008, patrolName='MS2PatrolData_1008A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사01(self.ctx)


class 에르다대사01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__0$', align='right', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 비에른대사01(self.ctx)


class 비에른대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=315, enable=True)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__1$', align='left', duration=3000)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__2$', align='left', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에르다대사02(self.ctx)


class 에르다대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=316, enable=True)
        self.visible_my_pc(isVisible=False) # 캐릭터 숨김
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__3$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 비에른대사02(self.ctx)


class 비에른대사02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__4$', align='left', duration=4000)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__5$', align='left', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 비에른접근(self.ctx)


class 비에른접근(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1006B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사03(self.ctx)


class 에르다대사03(trigger_api.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=True) # 캐릭터 보임
        self.select_camera(triggerId=317, enable=True)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__6$', align='right', duration=4000)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__7$', align='right', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 비에른대사03(self.ctx)


class 비에른대사03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=318, enable=True)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__8$', align='left', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사04(self.ctx)


class 에르다대사04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=317, enable=True)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__9$', align='right', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 비에른대사04(self.ctx)


class 비에른대사04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=312, enable=True)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__10$', align='right', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 비에른대사05(self.ctx)


class 비에른대사05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=318, enable=True)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__11$', align='left', duration=4000)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__12$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 에르다대사05(self.ctx)


class 에르다대사05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=317, enable=True)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__13$', align='right', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사06(self.ctx)


class 에르다대사06(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1008])
        self.set_visible_breakable_object(triggerIds=[4000], visible=True)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__14$', align='left', duration=2000)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__15$', align='right', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 에르다대사07(self.ctx)


class 에르다대사07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=319, enable=True)
        self.create_monster(spawnIds=[1009], animationEffect=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__16$', align='right', duration=3000)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__17$', align='right', duration=5000)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__18$', align='right', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=13000):
            return 에르다이동(self.ctx)


class 에르다이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1009, patrolName='MS2PatrolData_1009A')
        self.select_camera(triggerId=320, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에르다대사08(self.ctx)


class 에르다대사08(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007A')
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__19$', align='right', duration=4000)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__20$', align='right', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.visible_my_pc(isVisible=True) # 캐릭터 숨김
        self.set_ai_extra_data(key='getBack', value=1)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[1007,1008,1009])
        self.create_monster(spawnIds=[2098], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.add_buff(boxIds=[199], skillId=70000115, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 비에른사망대기(self.ctx)


class 비에른사망대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 사망연출대기(self.ctx)


class 사망연출대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 사망연출시작(self.ctx)


class 사망연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000086, portalId=40)
        self.destroy_monster(spawnIds=[2099])
        self.destroy_monster(spawnIds=[2098])
        self.create_monster(spawnIds=[1101,1102], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=1102, sequenceName='Stun_A', duration=1E+12)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 에드다이동02(self.ctx)


class 에드다이동02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=사망연출종료)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera(triggerId=321, enable=True)
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_1101A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사10(self.ctx)


class 에르다대사10(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__21$', align='right', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 비에른대사10(self.ctx)


class 비에른대사10(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=322, enable=True)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__22$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에르다대사11(self.ctx)


class 에르다대사11(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__23$', align='right', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 비에른대사11(self.ctx)


class 비에른대사11(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=323, enable=True)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__24$', align='left', duration=4000)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__25$', align='left', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 비에른대사12(self.ctx)


class 비에른대사12(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__26$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에르다대사12(self.ctx)


class 에르다대사12(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__27$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 비에른대사13(self.ctx)


class 비에른대사13(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=322, enable=True)
        self.set_npc_emotion_loop(spawnId=1102, sequenceName='Idle_A', duration=1E+12)
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__28$', align='left', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 비에른대사14(self.ctx)


class 비에른대사14(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=324, enable=True)
        self.move_npc(spawnId=1102, patrolName='MS2PatrolData_1102A')
        self.add_cinematic_talk(npcId=11003075, illustId='SnowKing_normal', msg='$52000086_QD__HP50__29$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에드다이동03(self.ctx)


class 에드다이동03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=325, enable=True)
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__30$', align='right', duration=3000)
        # <action name="NPC를이동시킨다" arg1="1101" arg2="MS2PatrolData_1101B" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC말풍선대사(self.ctx)


class PC말풍선대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000086_QD__HP50__31$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 에르다대사13(self.ctx)


class 에르다대사13(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__32$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에르다대사13To1(self.ctx)


class 에르다대사13To1(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003074, illustId='SnowQueen_normal', msg='$52000086_QD__HP50__33$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에르다대사14(self.ctx)


class 에르다대사14(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=321, enable=True)
        # <action name="대화를설정한다" arg1="2" arg2="11003074" arg3="미안하지만 지금은… 생각을 좀 정리하고 싶으니 혼자 있게 해 다오. 부탁이다." arg4="4" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에드다마저이동(self.ctx)


class 에드다마저이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # <action name="NPC를이동시킨다" arg1="1101" arg2="MS2PatrolData_1101C" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 사망연출종료(self.ctx)


class 사망연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[1101,1102])
        self.create_monster(spawnIds=[10000,10001,10002])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_achievement(triggerId=199, type='trigger', achieve='snowkingbjorn')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 던전종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=91, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=52000086, portalId=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 던전종료1(self.ctx)


class 던전종료1(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3102], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=4002, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3102], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=4003, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3103], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=4004, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[3104], visible=False, arg3=0, delay=0, scale=0)
        self.set_breakable(triggerIds=[4000], enable=False)
        self.set_visible_breakable_object(triggerIds=[4000], visible=False)
        self.move_user(mapId=52000086, portalId=30)
        self.destroy_monster(spawnIds=[1101,1102])
        self.create_monster(spawnIds=[10000,10001,10002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 퀘스트체크50100300_2
