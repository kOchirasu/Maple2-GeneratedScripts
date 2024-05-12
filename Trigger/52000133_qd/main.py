""" trigger/52000133_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,111,112])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[2]):
            return 예민한아노스(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[1]):
            return 예민한아노스(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001598], questStates=[3]):
            return 예민한아노스(self.ctx)
        """
        if self.quest_user_detected(boxIds=[9000], questIds=[50001598], questStates=[1]):
            return 예민한아노스(self.ctx)
        """
        if self.quest_user_detected(boxIds=[9000], questIds=[50001598], questStates=[2]):
            # 엘리넬 마법학원 : 50001598 퀘스트 진행 중인 상태
            return 예민한아노스_연출준비(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[2]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[1]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[3]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[2]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[1]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[3]):
            return 케이틀린첫만남(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[2]):
            # 엘리넬 마법학원 : 50001582 퀘스트 진행 중인 상태
            return 케이틀린첫만남_연출시작(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[3]):
            return 빈집(self.ctx)


class 케이틀린첫만남(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101])
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 케이틀린첫만남_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.create_monster(spawnIds=[101])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000133, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 전경스케치01(self.ctx)


class 전경스케치01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전경스케치02(self.ctx)


class 전경스케치02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(pathIds=[8001], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__0$', duration=2000, align='left')
        self.set_scene_skip(state=케이틀린첫만남_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전경스케치03(self.ctx)


class 전경스케치03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC01')
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전경스케치04(self.ctx)


class 전경스케치04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.add_cinematic_talk(npcId=11003254, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__1$', duration=3000, align='center')
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전경스케치05(self.ctx)


class 전경스케치05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.add_balloon_talk(spawnId=101, msg='$52000133_QD__MAIN__2$', duration=3000, delayTick=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Bore_A', duration=3000)
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전경스케치06(self.ctx)


class 전경스케치06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC02')
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전경스케치07(self.ctx)


class 전경스케치07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='NameCaption', title='$52000133_QD__MAIN__3$', desc='$52000133_QD__MAIN__4$', align='centerRight', offsetRateX=-0.05, offsetRateY=0.15, duration=10000, scale=2)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=4000)
        # <action name="스킵을설정한다" arg1="케이틀린첫만남_스킵완료" />  전경스킵을 위해 추가한 스킵 설정. 전체 스킵 개발 시 삭제해도 됨
        # Missing State: State
        self.set_scene_skip() # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출종료(self.ctx)


class 케이틀린첫만남_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000133, portalId=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 예민한아노스(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[111,113])
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 예민한아노스_연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[111])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000133, portalId=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 예민한아노스_연출시작(self.ctx)


class 예민한아노스_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8100], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 케이틀린대사01(self.ctx)


class 케이틀린대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8101], returnView=False)
        self.add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__5$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Bore_A', duration=4600)
        self.move_user_path(patrolName='2_MS2PatrolData_PC01')
        self.set_scene_skip(state=예민한아노스_스킵완료, action='nextState') # setsceneskip 2 set
        # setsceneskip 2 set
        # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사01(self.ctx)


"""
class 케이틀린대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC대사01(self.ctx)

"""


class PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8120], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__6$', duration=3000)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=2000)
        self.move_user_path(patrolName='2_MS2PatrolData_PC02')
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린대사02(self.ctx)


"""
class PC대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사02(self.ctx)

"""


class 케이틀린대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__7$', duration=3000, align='right')
        self.move_npc(spawnId=111, patrolName='2_MS2PatrolData_Katelyn01')
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사02(self.ctx)


"""
class 케이틀린대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC대사02(self.ctx)

"""


class PC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(pathIds=[8110], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__8$', duration=3000, align='right')
        self.move_user_path(patrolName='2_MS2PatrolData_PC03')
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=2000)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린대사03(self.ctx)


"""
class PC대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사03(self.ctx)

"""


class 케이틀린대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8110], returnView=False)
        self.create_monster(spawnIds=[112])
        self.add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__9$', duration=4000, align='right')
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=8200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아노스걸어나옴(self.ctx)


"""
class 아노스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스걸어나옴(self.ctx)

"""


class 아노스걸어나옴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8140], returnView=False)
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__10$', duration=3000, align='left')
        self.move_npc(spawnId=112, patrolName='2_MS2PatrolData_Anos01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__11$', duration=3000, align='left')
        self.move_npc(spawnId=111, patrolName='2_MS2PatrolData_Katelyn02')
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Talk_A', duration=3600)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사03(self.ctx)


"""
class 아노스대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC대사03(self.ctx)

"""


class PC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__12$', align='center', duration=3000)
        self.set_pc_emotion_loop(sequenceName='Emotion_Hello_A', duration=2000)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사02(self.ctx)


"""
class PC대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사02(self.ctx)

"""


class 아노스대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__13$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=112, sequenceName='ChatUp_A', duration=7000)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사04(self.ctx)


"""
class 아노스대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC대사04(self.ctx)

"""


class PC대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8131], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000133_QD__MAIN__14$', duration=3000, align='right')
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Surprise_A'])
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사03(self.ctx)


"""
class PC대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사03(self.ctx)

"""


class 아노스대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__15$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Bore_A', duration=8100)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린대사04(self.ctx)


"""
class 아노스대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사04(self.ctx)

"""


class 케이틀린대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8132], returnView=False)
        self.add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__16$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=12000)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사04(self.ctx)


"""
class 케이틀린대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사04(self.ctx)

"""


class 아노스대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__17$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Bore_B', duration=9500)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사05(self.ctx)


"""
class 아노스대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사05(self.ctx)

"""


class 아노스대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8133], returnView=False)
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_normal', msg='$52000133_QD__MAIN__18$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Talk_A', duration=6300)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린대사05(self.ctx)


"""
class 아노스대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사05(self.ctx)

"""


class 케이틀린대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__19$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Bore_B', duration=7900)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린대사06(self.ctx)


"""
class 케이틀린대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 케이틀린대사06(self.ctx)

"""


class 케이틀린대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003258, illustId='Caitlyn_normal', msg='$52000133_QD__MAIN__20$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Talk_A', duration=6800)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사06(self.ctx)


"""
class 케이틀린대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사06(self.ctx)

"""


class 아노스대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8140], returnView=False)
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_serious', msg='$52000133_QD__MAIN__21$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Bore_A', duration=5800)
        # self.set_skip(state=예민한아노스_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사07(self.ctx)


"""
class 아노스대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사07(self.ctx)

"""


class 아노스대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8140], returnView=False)
        self.add_cinematic_talk(npcId=11003259, illustId='Anos_serious', msg='$52000133_QD__MAIN__22$', duration=3000, align='left')
        # Missing State: State
        self.set_scene_skip() # setsceneskip 2 close
        # setsceneskip 2 close
        # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출종료(self.ctx)


class 예민한아노스_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[113])
        self.destroy_monster(spawnIds=[112])
        self.move_user(mapId=52000133, portalId=13)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
