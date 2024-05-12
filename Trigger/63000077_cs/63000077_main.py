""" trigger/63000077_cs/63000077_main.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_actor(triggerId=3001, visible=False, initialSequence='0', arg4=False, arg5=False) # 아빠끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000379], questStates=[3]):
            # 크리스마스 스토리 퀘스트 모두 함께 파티를까지 10종 전체 완료시 일퀘 수행 상태로 만들기
            return 일반사냥(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000378], questStates=[2]):
            return 일반사냥(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000378], questStates=[1]):
            return 수락_01_30000378(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[3]):
            return 완료_01_30000377(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[2]):
            return 화난보보스_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[1]):
            return 잠시대기_01(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 일반사냥(self.ctx)


class 수락_01_30000378(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 수락_02_30000378(self.ctx)


class 수락_02_30000378(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[106,108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에블린일기_01(self.ctx)


class 완료_01_30000377(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 완료_02_30000377(self.ctx)


class 완료_02_30000377(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[106,108], animationEffect=False)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라우스대화_05(self.ctx)


class 잠시대기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_actor(triggerId=3001, visible=True, initialSequence='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 잠시대기_02(self.ctx)


class 잠시대기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 보보스의오해_01(self.ctx)


class 보보스의오해_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=화난보보스_01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스의오해_02(self.ctx)


class 보보스의오해_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 보보스의오해_03(self.ctx)


class 보보스의오해_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 미안해… 소원… 들어줘야 하니까.\n내가 루돌프 되면 꼭 내려줄게.
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__0$', duration=3500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보보스의오해_04(self.ctx)


class 보보스의오해_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보보스의오해_05(self.ctx)


class 보보스의오해_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=102, msg='$63000077_CS__63000077_MAIN__1$', duration=2000) # 으아…오…옷…어…오우

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보보스의오해_06(self.ctx)


class 보보스의오해_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8004, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 보보스의오해_07(self.ctx)


class 보보스의오해_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])
        self.add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__2$', duration=2800, align='right') # 이봐, 무슨 짓이야! 당장 그만둬!
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보보스의오해_08(self.ctx)


class 보보스의오해_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8005, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스의오해_09(self.ctx)


class 보보스의오해_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 응…? 나…는 소원 들어주고 있어.\n$npcName:11004356$의 크리스마스 소원.
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__3$', duration=3500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보보스의오해_10(self.ctx)


class 보보스의오해_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8006, enable=True)
        self.face_emotion(spawnId=0, emotionName='Angry')
        self.move_user_path(patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스의오해_11(self.ctx)


class 보보스의오해_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004356$의 소원은 그런 게 아냐!\n$npcName:11004368$$pp:는,은$ $npcName:11004356$의 소중한 가족이라고! 당장 내려줘!
        self.add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__4$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 보보스의오해_12(self.ctx)


class 보보스의오해_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8005, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스의오해_13(self.ctx)


class 보보스의오해_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__5$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보보스의오해_14(self.ctx)


class 보보스의오해_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004356$ 아빠, 여기 있어야 된다.\n$npcName:11004373$$pp:는,은$ 착한 일을 하는 거다.
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__6$', duration=3500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보보스의오해_15(self.ctx)


class 보보스의오해_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8006, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스의오해_16(self.ctx)


class 보보스의오해_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        self.add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__7$', duration=2500, align='right') # 정말 말이 안 통하는 녀석이잖아.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보보스의오해_17(self.ctx)


class 보보스의오해_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=0, emotionName='Trigger_panic')
        self.add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__8$', duration=2500, align='right') # 도대체 무슨 소릴 하는 거야?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보보스의오해_18(self.ctx)

    def on_exit(self) -> None:
        self.face_emotion(spawnId=0)


class 보보스의오해_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8005, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스의오해_19(self.ctx)


class 보보스의오해_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004373$, 착한 일 하고 산타 할아버지한테 인정 받을 거다.
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__9$', duration=2500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보보스의오해_20(self.ctx)


class 보보스의오해_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 루돌프 돼서, 행복해지고…\n$npcName:11004356$이랑도 같이 놀 거야.
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__10$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 보보스의오해_21(self.ctx)


class 보보스의오해_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보보스의오해_22(self.ctx)


class 보보스의오해_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__11$', duration=2000, align='right') # 날 방해하면…

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 보보스의오해_23(self.ctx)


class 보보스의오해_23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # &lt;font size='40'&gt;때릴 거다!&lt;/font&gt;
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__12$', duration=2000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 화난보보스_01(self.ctx)


class 화난보보스_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 화난보보스_02(self.ctx)


class 화난보보스_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[101,102])
        self.create_monster(spawnIds=[220], animationEffect=False)
        self.create_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 화난보보스_03(self.ctx)


class 화난보보스_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[2]):
            return 패배한보보스_01(self.ctx)


class 일반사냥(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=3001, visible=False, initialSequence='0', arg4=False, arg5=False) # 아빠액터끄기
        self.destroy_monster(spawnIds=[101,102])
        self.create_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], animationEffect=False) # 보보스제외, 일반몹만 소환

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 패배한보보스_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 패배한보보스_02(self.ctx)


class 패배한보보스_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,220])
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=106, sequenceName='Cry_A', duration=35000)
        self.set_actor(triggerId=3001, visible=False, initialSequence='Talk_A')
        self.move_user(mapId=63000077, portalId=4)
        self.select_camera(triggerId=8008, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 패배한보보스_03(self.ctx)


class 패배한보보스_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_scene_skip(state=클라우스대화_03, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라우스대화_01(self.ctx)


class 클라우스대화_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__13$', duration=2500, align='left') # 도와주셔서 감사합니다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 클라우스대화_02(self.ctx)


class 클라우스대화_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__14$', duration=2500, align='left') # 그런데 누구……?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 클라우스대화_03(self.ctx)


class 클라우스대화_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 클라우스대화_04(self.ctx)


class 클라우스대화_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[107])
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라우스대화_05(self.ctx)


class 클라우스대화_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000378], questStates=[1]):
            return 에블린일기_01(self.ctx)


class 에블린일기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 에블린일기_02(self.ctx)


class 에블린일기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # &lt;FONT color='#ffd200'&gt;누군가의 일기장 52페이지&lt;/FONT&gt;\n아빠 미워. 그깟 꽃이 뭐라고 나를 그렇게 혼낸 거야? \n화단 하나 관리 못 했다고 세상이 뒤집히는 것도 아닌데.\n꽃이 나보다 소중하면, 내 눈에 띄지 말고 쭉 정원에서 살아! $npcName:11004368$씨!
        self.set_cinematic_ui(type=9, script='$63000077_CS__63000077_MAIN__15$')
        self.move_user(mapId=63000077, portalId=4)
        self.select_camera(triggerId=8008, enable=True)
        self.set_scene_skip(state=업적_01, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 에블린일기_03(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=2)


class 에블린일기_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다시만난가족_01(self.ctx)


class 다시만난가족_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 제가 $npcName:11004356$의 마음을 아프게 한 것도 사실이고,\n제 딸 $npcName:11004356$의 마음을 달래주려는 순진한 $npcName:11004373$의 부탁이니…
        self.add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__16$', duration=3500, illustId='June_normal', align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다시만난가족_02(self.ctx)


class 다시만난가족_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 잠깐 나무 위에 올라가 있는 것도 나쁘지 않겠다 싶었답니다
        self.add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__17$', duration=3000, illustId='June_normal', align='left')
        self.create_monster(spawnIds=[103,104,105], animationEffect=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 다시만난가족_03(self.ctx)

    def on_exit(self) -> None:
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_2006')


class 다시만난가족_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__18$', duration=2000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 다시만난가족_04(self.ctx)


class 다시만난가족_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8009], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다시만난가족_05(self.ctx)


class 다시만난가족_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 그건 그냥 투정이었어.\n내 소원은 그런 게 아니란 말이에요!
        self.add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__19$', duration=3500, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다시만난가족_06(self.ctx)


class 다시만난가족_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8012, enable=True)
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__20$', duration=2000, align='left') # 으응???

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 다시만난가족_07(self.ctx)


class 다시만난가족_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 다시만난가족_08(self.ctx)


class 다시만난가족_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004356$…소원 아니야?\n내가 잘못한거야…?
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__21$', duration=3500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 다시만난가족_09(self.ctx)


class 다시만난가족_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8011, enable=True)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_2008')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 다시만난가족_10(self.ctx)


class 다시만난가족_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 보…?\n그날 밤 내 얘길 듣고 간 게 역시 너였구나.
        self.add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__22$', duration=3500, illustId='Evelyn_glad', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다시만난가족_11(self.ctx)


class 다시만난가족_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다시만난가족_12(self.ctx)


class 다시만난가족_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 미안…미안해…!\n소원을 들어주고… 행복하게 해주고 싶었는데…!
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__23$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 다시만난가족_13(self.ctx)


class 다시만난가족_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004373$$pp:가,이$… 너무 미안해…!
        self.add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__24$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 다시만난가족_14(self.ctx)


class 다시만난가족_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=8011, enable=True)
        # 아니야, 털북숭이. 미안해 할 필요 없어.\n$npcName:11004356$의 소원은 따로 있으니까
        self.add_cinematic_talk(npcId=11004361, msg='$63000077_CS__63000077_MAIN__25$', duration=4000, illustId='Aiden_smile', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 다시만난가족_15(self.ctx)


class 다시만난가족_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 그래. 진짜 소원을 말하면, 그걸 들어주렴.
        self.add_cinematic_talk(npcId=11004365, msg='$63000077_CS__63000077_MAIN__26$', duration=3500, illustId='Mia_happy', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다시만난가족_16(self.ctx)


class 다시만난가족_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__27$', duration=2000, illustId='Evelyn_normal', align='right') # ……

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다시만난가족_17(self.ctx)


class 다시만난가족_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 미안해요, 모두.\n내가 부린 투정 때문에… 모두 너무 고생했어요.
        self.add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__28$', duration=3500, illustId='Evelyn_sad', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다시만난가족_18(self.ctx)


class 다시만난가족_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 그래서, 우리 $npcName:11004356$의 진짜 크리스마스 소원은 뭐지?
        self.add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__29$', duration=3000, illustId='June_smile', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 다시만난가족_19(self.ctx)


class 다시만난가족_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 우리 가족 모두 함께 모여서…\n행복한 크리스마스 파티를 하는 거예요
        self.add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__30$', duration=3500, illustId='Evelyn_glad', align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다시만난가족_20(self.ctx)


class 다시만난가족_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8013], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 업적_01(self.ctx)


class 업적_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 업적_02(self.ctx)


class 업적_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=701, type='trigger', achieve='ChristmasWish')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000075, portalId=10)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # Missing State: State
        self.set_scene_skip()


initial_state = 준비
