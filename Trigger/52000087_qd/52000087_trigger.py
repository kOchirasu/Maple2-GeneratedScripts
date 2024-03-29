""" trigger/52000087_qd/52000087_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[22651], questIds=[20002266], questStates=[3]):
            return 용무없는유저는아웃(self.ctx)
        if self.quest_user_detected(boxIds=[22651], questIds=[10002781], questStates=[1]):
            return 카르카르시작(self.ctx)
        if self.quest_user_detected(boxIds=[22651], questIds=[20002265], questStates=[3]):
            return 완료연출01_20002265(self.ctx)


# 카르카르 연출, 메이플연합 회담씬
class 카르카르시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 진행(self.ctx)


class 진행(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에레브_1(self.ctx)


class 에레브_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__0$', arg4=3)
        self.set_skip(state=에레브_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 에레브_1skip(self.ctx)


class 에레브_1skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 에레브_2(self.ctx)


class 에레브_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__1$', arg4=5)
        self.set_skip(state=에레브_2skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브_2skip(self.ctx)


class 에레브_2skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 에레브_3(self.ctx)


class 에레브_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__2$', arg4=5)
        self.set_skip(state=에레브_3skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브_3skip(self.ctx)


class 에레브_3skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 블랙아이_1(self.ctx)


class 블랙아이_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__3$', arg4=3)
        self.set_skip(state=블랙아이_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 블랙아이_1skip(self.ctx)


class 블랙아이_1skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 블랙아이_1a(self.ctx)


class 블랙아이_1a(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__4$', arg4=5)
        self.set_skip(state=블랙아이_1askip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 블랙아이_1askip(self.ctx)


class 블랙아이_1askip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 프레이_1(self.ctx)


class 프레이_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000119, script='$52000087_QD__52000087_TRIGGER__5$', arg4=5)
        self.set_skip(state=프레이_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 프레이_1skip(self.ctx)


class 프레이_1skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 구르는천둥_1(self.ctx)


class 구르는천둥_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001581, script='$52000087_QD__52000087_TRIGGER__6$', arg4=3)
        self.set_skip(state=구르는천둥_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 구르는천둥_1skip(self.ctx)


class 구르는천둥_1skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 알론_1(self.ctx)


class 알론_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__7$', arg4=3)
        self.set_skip(state=알론_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 알론_1skip(self.ctx)


class 알론_1skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오스칼_1(self.ctx)


class 오스칼_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000015, script='$52000087_QD__52000087_TRIGGER__8$', arg4=5)
        self.set_skip(state=오스칼_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 오스칼_1skip(self.ctx)


class 오스칼_1skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 블랙아이_2(self.ctx)


class 블랙아이_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__9$', arg4=5)
        self.set_skip(state=블랙아이_2skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 블랙아이_2skip(self.ctx)


class 블랙아이_2skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 블랙아이_2a(self.ctx)


class 블랙아이_2a(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__10$', arg4=5)
        self.set_skip(state=블랙아이_2askip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 블랙아이_2askip(self.ctx)


class 블랙아이_2askip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 블랙아이_3(self.ctx)


class 블랙아이_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000006, script='$52000087_QD__52000087_TRIGGER__11$', arg4=5)
        self.set_skip(state=블랙아이_3skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 블랙아이_3skip(self.ctx)


class 블랙아이_3skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 알론_2(self.ctx)


class 알론_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__12$', arg4=3)
        self.set_skip(state=알론_2skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 알론_2skip(self.ctx)


class 알론_2skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 에레브_4(self.ctx)


class 에레브_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__13$', arg4=5)
        self.set_skip(state=에레브_4skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브_4skip(self.ctx)


class 에레브_4skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 영상준비(self.ctx)


class 영상준비(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_timer(timerId='21', seconds=2)
        self.select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='21'):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_scene_movie(fileName='lumieragonhistory.swf', movieId=1)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 알론_3(self.ctx)


class 알론_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__14$', arg4=5)
        self.set_skip(state=알론_3skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 알론_3skip(self.ctx)


class 알론_3skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 알론_4(self.ctx)


class 알론_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__15$', arg4=5)
        self.set_skip(state=알론_4skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 알론_4skip(self.ctx)


class 알론_4skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 알론_4a(self.ctx)


class 알론_4a(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__16$', arg4=5)
        self.set_skip(state=알론_4askip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 알론_4askip(self.ctx)


class 알론_4askip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 알론_5(self.ctx)


class 알론_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000076, script='$52000087_QD__52000087_TRIGGER__17$', arg4=5)
        self.set_skip(state=알론_5skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 알론_5skip(self.ctx)


class 알론_5skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 에레브_5(self.ctx)


class 에레브_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__18$', arg4=5)
        self.set_skip(state=에레브_5skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브_5skip(self.ctx)


class 에레브_5skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 에레브_6(self.ctx)


class 에레브_6(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__19$', arg4=5)
        self.set_skip(state=에레브_6skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브_6skip(self.ctx)


class 에레브_6skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 칼_1(self.ctx)


class 칼_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000074, script='$52000087_QD__52000087_TRIGGER__20$', arg4=5)
        self.set_skip(state=칼_1skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 칼_1skip(self.ctx)


class 칼_1skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 에레브_7(self.ctx)


class 에레브_7(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__21$', arg4=5)
        self.set_skip(state=에레브_7skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브_7skip(self.ctx)


class 에레브_7skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 에레브_8(self.ctx)


class 에레브_8(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000075, script='$52000087_QD__52000087_TRIGGER__22$', arg4=5)
        self.set_skip(state=에레브_8skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 에레브_8skip(self.ctx)


class 에레브_8skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=22651, type='trigger', achieve='Lumieragon_History')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


# 챕터10 [20002265 새로운 실마리]완료 시 연출, 오르데가 포탈타고 나타남
class 완료연출01_20002265(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(mapId=52000087, portalId=10)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 완료연출02_20002265(self.ctx)


class 완료연출02_20002265(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[2002,2003,2004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 완료연출03_20002265(self.ctx)


class 완료연출03_20002265(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.create_monster(spawnIds=[1003], animationEffect=False) # 오르데
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_Start') # 오르데 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 완료연출04_20002265(self.ctx)


class 완료연출04_20002265(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=1003, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 완료연출04_b20002265(self.ctx)


class 완료연출04_b20002265(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003087, script='$52000087_QD__52000087_TRIGGER__23$', arg4=3) # 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 완료연출04_c20002265(self.ctx)


class 완료연출04_c20002265(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1003, sequenceName='ChatUp_A')
        self.set_conversation(type=2, spawnId=11003087, script='$52000087_QD__52000087_TRIGGER__24$', arg4=3) # 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 완료연출05_20002265(self.ctx)


class 완료연출05_20002265(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=2)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_Orde') # 오르데 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[22651], questIds=[20002266], questStates=[3]):
            return 완료연출01_20002266(self.ctx)


# 챕터10 [20002265 새로운 실마리]완료 시 연출 종료, 오르데가 포탈타고 나타남
# 챕터10 [20002266 취향입니다, 존중해주시죠]완료 시 연출, 오르데와 PC가 포탈열고 사라짐
class 완료연출01_난입20002266(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1003], animationEffect=False) # 오르데

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 완료연출01_20002266(self.ctx)


class 완료연출01_20002266(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000087, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 완료연출02_20002266(self.ctx)


class 완료연출02_20002266(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[2005,2006], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 완료연출03_20002266(self.ctx)


class 완료연출03_20002266(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003087, script='$52000087_QD__52000087_TRIGGER__25$', arg4=3) # 대사
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_OrdeOut') # 에레브 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 완료연출04_20002266(self.ctx)


class 완료연출04_20002266(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=500, visible=True, enable=True, minimapVisible=True)
        self.set_effect(triggerIds=[601], visible=True)
        self.destroy_monster(spawnIds=[1003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 완료연출05_20002266(self.ctx)


class 완료연출05_20002266(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)


class 용무없는유저는아웃(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[22651], questIds=[20002285], questStates=[3]):
            return 챕터10에필로그연출01(self.ctx)


# 챕터10 에필로그 연출
class 챕터10에필로그연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(mapId=52000087, portalId=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 챕터10에필로그연출02(self.ctx)


class 챕터10에필로그연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__26$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출03(self.ctx)


class 챕터10에필로그연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__27$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출05(self.ctx)


class 챕터10에필로그연출05(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__28$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출05b(self.ctx)


class 챕터10에필로그연출05b(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출06(self.ctx)


class 챕터10에필로그연출06(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=90000, enable=True) # 마드리아 고조 브금
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__29$', arg4=6)
        self.set_onetime_effect(id=2007, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_01_00002007.xml')
        self.set_skip(state=챕터10에필로그연출06스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 챕터10에필로그연출06스킵(self.ctx)


class 챕터10에필로그연출06스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출07(self.ctx)


class 챕터10에필로그연출07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__30$', arg4=6)
        self.set_onetime_effect(id=2008, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_02_00002008.xml')
        self.set_skip(state=챕터10에필로그연출07스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 챕터10에필로그연출07스킵(self.ctx)


class 챕터10에필로그연출07스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출08(self.ctx)


class 챕터10에필로그연출08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__31$', arg4=9)
        self.set_onetime_effect(id=2009, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_03_00002009.xml')
        self.set_skip(state=챕터10에필로그연출08스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 챕터10에필로그연출08스킵(self.ctx)


class 챕터10에필로그연출08스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출09(self.ctx)


class 챕터10에필로그연출09(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__32$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 챕터10에필로그연출10(self.ctx)


class 챕터10에필로그연출10(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__33$', arg4=5)
        self.set_onetime_effect(id=2010, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_04_00002010.xml')
        self.set_skip(state=챕터10에필로그연출10스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 챕터10에필로그연출10스킵(self.ctx)


class 챕터10에필로그연출10스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출11(self.ctx)


class 챕터10에필로그연출11(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__34$', arg4=5)
        self.set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        self.set_skip(state=챕터10에필로그연출11스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 챕터10에필로그연출11스킵(self.ctx)


class 챕터10에필로그연출11스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출12(self.ctx)


class 챕터10에필로그연출12(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__35$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출13(self.ctx)


class 챕터10에필로그연출13(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__36$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출13_b(self.ctx)


class 챕터10에필로그연출13_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__37$', arg4=5)
        self.set_onetime_effect(id=2012, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_06_00002012.xml')
        self.set_skip(state=챕터10에필로그연출13b스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 챕터10에필로그연출13b스킵(self.ctx)


class 챕터10에필로그연출13b스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출14(self.ctx)


class 챕터10에필로그연출14(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__38$', arg4=5)
        self.set_onetime_effect(id=2013, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_07_00002013.xml')
        self.set_skip(state=챕터10에필로그연출14스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출14스킵(self.ctx)


class 챕터10에필로그연출14스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출15(self.ctx)


class 챕터10에필로그연출15(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__39$', arg4=6)
        self.set_onetime_effect(id=2014, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_08_00002014.xml')
        self.set_skip(state=챕터10에필로그연출15스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 챕터10에필로그연출15스킵(self.ctx)


class 챕터10에필로그연출15스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출16(self.ctx)


class 챕터10에필로그연출16(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001820, script='$52000087_QD__52000087_TRIGGER__40$', arg4=5)
        self.set_onetime_effect(id=2015, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_09_00002015.xml')
        self.set_skip(state=챕터10에필로그연출16스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 챕터10에필로그연출16스킵(self.ctx)


class 챕터10에필로그연출16스킵(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 챕터10에필로그연출17(self.ctx)


class 챕터10에필로그연출17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 챕터10에필로그연출18(self.ctx)


class 챕터10에필로그연출18(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__41$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출18b(self.ctx)


class 챕터10에필로그연출18b(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__42$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출19(self.ctx)


class 챕터10에필로그연출19(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__43$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출20(self.ctx)


class 챕터10에필로그연출20(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__44$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출21(self.ctx)


class 챕터10에필로그연출21(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000087_QD__52000087_TRIGGER__45$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 챕터10에필로그연출22(self.ctx)


class 챕터10에필로그연출22(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=2000025, portalId=2)


initial_state = 대기
