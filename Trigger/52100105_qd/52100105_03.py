""" trigger/52100105_qd/52100105_03.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1000]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[3]):
            return 시작암전1(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[2]):
            return 연출끝(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[1]):
            return 연출끝(self.ctx)


class 시작암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.visible_my_pc(isVisible=False)
        self.set_onetime_effect(id=200, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 컷신1_1(self.ctx)


class 컷신1_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Kritias_EpicCutScene07_01.swf', movieId=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='0'):
            return None # Missing State: 컷신1_2
        if self.wait_tick(waitTick=3000):
            return 몹소환1(self.ctx)


class 몹소환1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[500], animationEffect=False) # 클라디아
        self.create_monster(spawnIds=[1], animationEffect=False) # 의자
        self.create_monster(spawnIds=[400], animationEffect=False)
        self.create_monster(spawnIds=[401], animationEffect=False)
        self.create_monster(spawnIds=[402], animationEffect=False)
        self.create_monster(spawnIds=[403], animationEffect=False)
        self.create_monster(spawnIds=[404], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 인게임준비0(self.ctx)


class 인게임준비0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=200, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사1(self.ctx)


class 투르카대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[500], arg2=False)
        self.set_scene_skip(state=컷신3_1, action='nextState')
        self.select_camera_path(pathIds=[700,701], returnView=False)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', msg='$52100105_QD__52100105_03__0$', duration=6000, align='Right')
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', msg='$52100105_QD__52100105_03__1$', duration=6000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 클라디아생성1(self.ctx)


class 클라디아생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[500], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 클라디아이동1(self.ctx)


class 클라디아이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=500, patrolName='PatrolData_500_1')
        self.select_camera_path(pathIds=[703,704], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라디아대사1(self.ctx)


class 클라디아대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=500, sequenceName='Talk_A', duration=8666)
        self.add_cinematic_talk(npcId=11004392, illustId='cladia_normal', msg='$52100105_QD__52100105_03__2$', duration=5000, align='left')
        self.add_cinematic_talk(npcId=11004392, illustId='cladia_angry', msg='$52100105_QD__52100105_03__3$', duration=5000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카공격지시1(self.ctx)


class 투르카공격지시1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=705, enable=True)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_normal', msg='$52100105_QD__52100105_03__4$', duration=3000, align='Right')
        self.set_npc_emotion_loop(spawnId=400, sequenceName='Bore_A', duration=1333)
        self.set_npc_emotion_loop(spawnId=500, sequenceName='Attack_Idle_A', duration=5333)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 암전1(self.ctx)


class 암전1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.move_npc(spawnId=401, patrolName='PatrolData_401_1')
        self.move_npc(spawnId=402, patrolName='PatrolData_402_1')
        self.move_npc(spawnId=403, patrolName='PatrolData_403_1')
        self.move_npc(spawnId=404, patrolName='PatrolData_404_1')
        self.set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 컷신3_1(self.ctx)


class 컷신3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[401], arg2=False)
        self.destroy_monster(spawnIds=[402], arg2=False)
        self.destroy_monster(spawnIds=[403], arg2=False)
        self.destroy_monster(spawnIds=[404], arg2=False)
        self.destroy_monster(spawnIds=[500], arg2=False)
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Kritias_EpicCutScene07_02.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 클라디아생성2(self.ctx)
        if self.wait_tick(waitTick=12000):
            return 클라디아생성2(self.ctx)


class 클라디아생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[500], animationEffect=False)
        self.move_npc(spawnId=500, patrolName='PatrolData_500_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카도망1(self.ctx)


class 투르카도망1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=연출끝, action='nextState')
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=100, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawnId=500, sequenceName='Attack_Idle_A', duration=5333)
        self.set_npc_emotion_loop(spawnId=400, sequenceName='Damg_A', duration=5333)
        self.select_camera(triggerId=706, enable=True)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_Broken_Hood', msg='$52100105_QD__52100105_03__5$', duration=4000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카도망2(self.ctx)


class 투르카도망2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카도망3(self.ctx)


class 투르카도망3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=400, patrolName='PatrolData_400_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카도망4(self.ctx)


class 투르카도망4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=707, enable=True)
        self.destroy_monster(spawnIds=[500], arg2=False)
        self.add_cinematic_talk(npcId=11004430, illustId='Turka_Broken_Hood', msg='$52100105_QD__52100105_03__6$', duration=5000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 투르카도망5(self.ctx)


class 투르카도망5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출끝(self.ctx)


class 연출끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.destroy_monster(spawnIds=[-1], arg2=False)
        self.set_effect(triggerIds=[600], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.visible_my_pc(isVisible=True)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52100110, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: State


initial_state = Ready
