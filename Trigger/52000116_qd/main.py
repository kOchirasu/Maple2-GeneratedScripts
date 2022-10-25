""" trigger/52000116_qd/main.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100001], questStates=[1]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100001], questStates=[2]):
            return fadeout(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100001], questStates=[3]):
            return fadeout(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003163, illustId='Nelf_normal', msg='$52000116_QD__MAIN__0$', duration=4000, align='Right') # 11003163: 넬프
        self.set_scene_skip(state=fadeout, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return jordyspawn(self.ctx)


class jordyspawn(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000116, portalId=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')
        self.create_monster(spawnIds=[102], animationEffect=True) # 102:조디
        self.select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return jordyhelp(self.ctx)


class jordyhelp(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')
        self.set_conversation(type=2, spawnId=11001838, script='$52000116_QD__MAIN__1$', arg4=1, arg5=0) # 조디 계단 올라가며 하는 대사
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return wowspawn(self.ctx)


class wowspawn(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=True) # 103:연출용 강아지
        self.set_conversation(type=1, spawnId=102, script='$52000116_QD__MAIN__2$', arg4=2, arg5=0) # 조디 뒤로 돌아서 하는 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return camera(self.ctx)


class camera(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return wow(self.ctx)


class wow(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Attack_01_A')
        self.set_conversation(type=2, spawnId=11003179, script='$52000116_QD__MAIN__3$', arg4=2, arg5=0) # 강아지 짖는 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return save(self.ctx)


class save(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Sit_Down_A', duration=400000)
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return battleready(self.ctx)


class battleready(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=True, animationDelay=500) # 멍멍이 몬스터

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return battle(self.ctx)


class battle(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawnId=104, sequenceName='Attack_Idle_A', duration=10000)
        self.reset_camera(interpolationTime=0.5)
        self.move_user_path(patrolName='MS2PatrolData_3003')
        self.set_conversation(type=1, spawnId=102, script='$52000116_QD__MAIN__4$', arg4=2, arg5=0) # 조디 말풍선
        self.set_conversation(type=1, spawnId=101, script='$52000116_QD__MAIN__5$', arg4=2, arg5=0) # 넬프 말풍선
        self.set_conversation(type=1, spawnId=102, script='$52000116_QD__MAIN__6$', arg4=2, arg5=3) # 조디 말풍선

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return camera_A(self.ctx)


class camera_A(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3005')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Motion(self.ctx)


class Motion(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return lol(self.ctx)


class lol(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Damg_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return run(self.ctx)


class run(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_3004')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return fadeout(self.ctx)


class fadeout(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102,103,104])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[105], animationEffect=True) # 조디

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadein(self.ctx)


class fadein(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000116, portalId=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return thank(self.ctx)


class thank(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        self.select_camera_path(pathIds=[4002], returnView=False) # 조디 얼굴로 클로즈업
        self.add_cinematic_talk(npcId=11003164, msg='$52000116_QD__MAIN__7$', duration=2000)
        self.set_scene_skip(state=end, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return endready(self.ctx)


class endready(common.Trigger):
    def on_enter(self):
        self.show_caption(scale=2.3, type='NameCaption', title='$52000116_QD__MAIN__8$', desc='$52000116_QD__MAIN__9$', align='centerLeft', offsetRateX=-0.15, duration=4000)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=2001, type='trigger', achieve='jordy')
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
