""" trigger/52000119_qd/main.xml """
import trigger_api


# 골든타워 8층 : 60100030
# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
# 오프닝 연출
class intro(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920], animationEffect=True) # 기본 배치 몬스터
        self.create_monster(spawnIds=[921,922,923,924,925,926,927,928,929], animationEffect=True) # 기본 배치 몬스터
        self.create_monster(spawnIds=[104,105], animationEffect=True) # 104:랄프
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100030], questStates=[1]):
            return fadeout_01(self.ctx)


class fadeout_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[104,105]) # 104: 랄프
        self.create_monster(spawnIds=[101,102,103], animationEffect=True) # 101:랄프 / 102:조디 / 103: 브로커 랄프의 수하
        self.select_camera_path(pathIds=[4010,4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return fadein_01(self.ctx)


class fadein_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Sit_Down_A', duration=900000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return eventscene_01(self.ctx)


class eventscene_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003169, illustId='Jordy_normal', msg='$52000119_QD__MAIN__0$', duration=3000, align='Left')
        self.set_scene_skip(state=fadeout_02, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return eventscene_02(self.ctx)


class eventscene_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        self.set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__1$', arg4=3, arg5=0) # 브로커 랄프
        self.set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__2$', arg4=3, arg5=3) # 브로커 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return eventscene_03(self.ctx)


class eventscene_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4003], returnView=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk')
        self.set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__3$', arg4=3, arg5=0) # 브로커 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return eventscene_04(self.ctx)


class eventscene_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Damg_B')
        self.set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__4$', arg4=3, arg5=0) # 코쿤

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return eventscene_05(self.ctx)


class eventscene_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        self.set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__5$', arg4=3, arg5=0) # 브로커 랄프
        self.set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__6$', arg4=3, arg5=3) # 브로커 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return eventscene_06(self.ctx)


class eventscene_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_A')
        self.set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__7$', arg4=3, arg5=0) # 코쿤
        self.set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__8$', arg4=3, arg5=3) # 코쿤
        self.set_conversation(type=1, spawnId=102, script='$52000119_QD__MAIN__9$', arg4=2, arg5=4) # 코쿤
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return fadeout_02(self.ctx)


class fadeout_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return reset(self.ctx)


class reset(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return eventscene_end(self.ctx)


class eventscene_end(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=3)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN__10$', arg3='1000', arg4='0')
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return hintmsg(self.ctx)


class hintmsg(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.set_conversation(type=2, spawnId=0, script='$52000119_QD__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return play(self.ctx)


class play(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2002]):
            return fadeout_03(self.ctx)


class fadeout_03(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        self.destroy_monster(spawnIds=[101,102,103]) # 101:랄프 / 102:조디 / 103: 브로커 랄프의 수하
        self.create_monster(spawnIds=[104,105,106], animationEffect=True) # 104:랄프 / 105:조디 / 106: 브로커 랄프의 수하
        self.move_user(mapId=52000119, portalId=6002)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return fadein_03(self.ctx)


class fadein_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='MS2PatrolData_3003')
        self.add_balloon_talk(spawnId=0, msg='$52000119_QD__MAIN__12$', duration=2000, delayTick=0)
        self.set_scene_skip(state=fadeout_04, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return bossscene_01(self.ctx)


# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
class bossscene_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=True)
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Sit_Down_A', duration=150000)
        self.set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__13$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return bossscene_02(self.ctx)


class bossscene_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        self.set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__14$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return bossscene_03(self.ctx)


class bossscene_03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4011], returnView=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__15$', arg4=3, arg5=0) # 랄프
        self.set_conversation(type=1, spawnId=105, script='$52000119_QD__MAIN__16$', arg4=3, arg5=1) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return bossscene_04(self.ctx)


class bossscene_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4013,4014,4015], returnView=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        self.set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__17$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return bossscene_05(self.ctx)


class bossscene_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        self.face_emotion(spawnId=0, emotionName='Object_React_A')
        self.set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__18$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return bossscene_06(self.ctx)


class bossscene_06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3004')
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Attack_01_C')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_3001')
        self.face_emotion(spawnId=0, emotionName='Object_React_A')
        self.set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__19$', arg4=3, arg5=0) # 코쿤

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return bossscene_07(self.ctx)


class bossscene_07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Bore_A')
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=4000)
        self.face_emotion(spawnId=0, emotionName='Object_React_A')
        self.set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__20$', arg4=3, arg5=0) # 코쿤
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return fadeout_04(self.ctx)


class fadeout_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=False)
        self.set_sound(triggerId=7002, enable=True)
        self.destroy_monster(spawnIds=[106]) # 106: 코쿤
        self.create_monster(spawnIds=[997], animationEffect=True) # 999: 코쿤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadein_04(self.ctx)


class fadein_04(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.add_balloon_talk(spawnId=997, msg='$52000119_QD__MAIN__21$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return bossmsg(self.ctx)


class bossmsg(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN__22$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[997]):
            return wait(self.ctx)


class wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7002, enable=False)
        self.add_balloon_talk(spawnId=104, msg='$52000119_QD__MAIN__23$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return fadeout_05(self.ctx)


class fadeout_05(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[997]) # 106: 코쿤
        self.set_achievement(type='trigger', achieve='jordysave')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = intro
