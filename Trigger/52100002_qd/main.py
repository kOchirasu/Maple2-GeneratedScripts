""" trigger/52100002_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[1]):
            return 룸체크(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[2]):
            return 퀘스트완료가능이거나완료1(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[3]):
            return 퀘스트완료가능이거나완료1(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전시작(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002,2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[2001]):
            self.set_effect(triggerIds=[601], visible=True)
            return 사망체크(self.ctx)
        if self.monster_dead(boxIds=[2001,2002]):
            return 사망딜레이(self.ctx)


class 사망체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001,2002]):
            return 사망딜레이(self.ctx)


class 사망딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001,2002]):
            return 암전대기(self.ctx)


class 퀘스트던전시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002,2101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[2101]):
            self.set_effect(triggerIds=[601], visible=True)
            return 퀘스트사망체크(self.ctx)
        if self.monster_dead(boxIds=[2101,2102]):
            return 퀘스트사망딜레이(self.ctx)


class 퀘스트사망체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2101,2102]):
            return 퀘스트사망딜레이(self.ctx)


class 퀘스트사망딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 퀘스트종료체크(self.ctx)


class 퀘스트종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2101,2102]):
            return 암전대기(self.ctx)


class 암전대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 종료연출대기(self.ctx)


class 종료연출대기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)
        self.move_user(mapId=52100002, portalId=2)
        self.destroy_monster(spawnIds=[1001,1002,2001,2002,2101,2102])
        self.create_monster(spawnIds=[1098,1099], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_loop(spawnId=1098, sequenceName='Dead_B', duration=3000000)
        self.set_npc_emotion_loop(spawnId=1099, sequenceName='Dead_B', duration=3000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료연출(self.ctx)


class 종료연출(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=연출종료)
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__MAIN__0$', align='left', duration=4000)
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__1$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return PC대사(self.ctx)


class PC대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$02000392_BF__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사2(self.ctx)


class PC대사2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$02000392_BF__MAIN__10$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 자매교체(self.ctx)


class 자매교체(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1098,1099])
        self.create_monster(spawnIds=[1096,1097], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 자매대화(self.ctx)


class 자매대화(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 자매대화01(self.ctx)


class 자매대화01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__MAIN__3$', align='left', duration=4000)
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__4$', align='right', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 자매대화02(self.ctx)


class 자매대화02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__MAIN__5$', align='left', duration=5000)
        self.set_conversation(type=1, spawnId=1097, script='$02000392_BF__MAIN__6$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 자매대화03(self.ctx)


class 자매대화03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__11$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC대사3(self.ctx)


class PC대사3(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$02000392_BF__MAIN__12$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자매대화04(self.ctx)


class 자매대화04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__7$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자매대화05(self.ctx)


class 자매대화05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__8$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자매대화06(self.ctx)


class 자매대화06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000392_BF__MAIN__9$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.destroy_monster(spawnIds=[1098,1099])
        self.destroy_monster(spawnIds=[1096,1097])
        self.create_monster(spawnIds=[1096,1097], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # action name="카메라를선택한다" arg1="302" arg2="0"/
        self.reset_camera(interpolationTime=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 룸체크2(self.ctx)


class 퀘스트완료가능이거나완료1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1096,1097], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 룸체크2(self.ctx)


class 룸체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전완료(self.ctx)
        if not self.is_dungeon_room():
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            return 종료(self.ctx)


class 던전완료(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_achievement(triggerId=199, type='trigger', achieve='ClearSirenSisters')
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
