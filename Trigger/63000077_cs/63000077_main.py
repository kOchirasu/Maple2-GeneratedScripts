""" trigger/63000077_cs/63000077_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        set_actor(triggerId=3001, visible=False, initialSequence='0', arg4=False, arg5=False) # 아빠끄기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000379], questStates=[3]):
            return 일반사냥()
        if quest_user_detected(boxIds=[701], questIds=[30000378], questStates=[2]):
            return 일반사냥()
        if quest_user_detected(boxIds=[701], questIds=[30000378], questStates=[1]):
            return 수락_01_30000378()
        if quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[3]):
            return 완료_01_30000377()
        if quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[2]):
            return 화난보보스_01()
        if quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[1]):
            return 잠시대기_01()
        if user_detected(boxIds=[701]):
            return 일반사냥()


class 수락_01_30000378(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 수락_02_30000378()


class 수락_02_30000378(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[106,108], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에블린일기_01()


class 완료_01_30000377(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 완료_02_30000377()


class 완료_02_30000377(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[106,108], arg2=False)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라우스대화_05()


class 잠시대기_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_actor(triggerId=3001, visible=True, initialSequence='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 잠시대기_02()


class 잠시대기_02(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 보보스의오해_01()


class 보보스의오해_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=화난보보스_01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스의오해_02()


class 보보스의오해_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 보보스의오해_03()


class 보보스의오해_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__0$', duration=3500, align='right') # 미안해… 소원… 들어줘야 하니까.\n내가 루돌프 되면 꼭 내려줄게.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 보보스의오해_04()


class 보보스의오해_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보보스의오해_05()


class 보보스의오해_05(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='$63000077_CS__63000077_MAIN__1$', duration=2000) # 으아…오…옷…어…오우

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보보스의오해_06()


class 보보스의오해_06(state.State):
    def on_enter(self):
        select_camera(triggerId=8004, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 보보스의오해_07()


class 보보스의오해_07(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])
        add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__2$', duration=2800, align='right') # 이봐, 무슨 짓이야! 당장 그만둬!
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보보스의오해_08()


class 보보스의오해_08(state.State):
    def on_enter(self):
        select_camera(triggerId=8005, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스의오해_09()


class 보보스의오해_09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__3$', duration=3500, align='right') # 응…? 나…는 소원 들어주고 있어.\n$npcName:11004356$의 크리스마스 소원.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 보보스의오해_10()


class 보보스의오해_10(state.State):
    def on_enter(self):
        select_camera(triggerId=8006, enable=True)
        face_emotion(spawnId=0, emotionName='Angry')
        move_user_path(patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스의오해_11()


class 보보스의오해_11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__4$', duration=4000, align='right') # $npcName:11004356$의 소원은 그런 게 아냐!\n$npcName:11004368$$pp:는,은$ $npcName:11004356$의 소중한 가족이라고! 당장 내려줘!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 보보스의오해_12()


class 보보스의오해_12(state.State):
    def on_enter(self):
        select_camera(triggerId=8005, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스의오해_13()


class 보보스의오해_13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__5$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보보스의오해_14()


class 보보스의오해_14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__6$', duration=3500, align='right') # $npcName:11004356$ 아빠, 여기 있어야 된다.\n$npcName:11004373$$pp:는,은$ 착한 일을 하는 거다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 보보스의오해_15()


class 보보스의오해_15(state.State):
    def on_enter(self):
        select_camera(triggerId=8006, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스의오해_16()


class 보보스의오해_16(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__7$', duration=2500, align='right') # 정말 말이 안 통하는 녀석이잖아.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보보스의오해_17()


class 보보스의오해_17(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Trigger_panic')
        add_cinematic_talk(npcId=0, msg='$63000077_CS__63000077_MAIN__8$', duration=2500, align='right') # 도대체 무슨 소릴 하는 거야?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보보스의오해_18()

    def on_exit(self):
        face_emotion(spawnId=0)


class 보보스의오해_18(state.State):
    def on_enter(self):
        select_camera(triggerId=8005, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스의오해_19()


class 보보스의오해_19(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__9$', duration=2500, align='right') # $npcName:11004373$, 착한 일 하고 산타 할아버지한테 인정 받을 거다.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보보스의오해_20()


class 보보스의오해_20(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__10$', duration=3000, align='right') # 루돌프 돼서, 행복해지고…\n$npcName:11004356$이랑도 같이 놀 거야.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 보보스의오해_21()


class 보보스의오해_21(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스의오해_22()


class 보보스의오해_22(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__11$', duration=2000, align='right') # 날 방해하면…

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 보보스의오해_23()


class 보보스의오해_23(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__12$', duration=2000, align='right') # &lt;font size='40'&gt;때릴 거다!&lt;/font&gt;

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 화난보보스_01()


class 화난보보스_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 화난보보스_02()


class 화난보보스_02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[101,102])
        create_monster(spawnIds=[220], arg2=False)
        create_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 화난보보스_03()


class 화난보보스_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000377], questStates=[2]):
            return 패배한보보스_01()


class 일반사냥(state.State):
    def on_enter(self):
        set_actor(triggerId=3001, visible=False, initialSequence='0', arg4=False, arg5=False) # 아빠액터끄기
        destroy_monster(spawnIds=[101,102])
        create_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216], arg2=False) # 보보스제외, 일반몹만 소환

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 패배한보보스_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 패배한보보스_02()


class 패배한보보스_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,220])
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        set_npc_emotion_loop(spawnId=106, sequenceName='Cry_A', duration=35000)
        set_actor(triggerId=3001, visible=False, initialSequence='Talk_A')
        move_user(mapId=63000077, portalId=4)
        select_camera(triggerId=8008, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 패배한보보스_03()


class 패배한보보스_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=클라우스대화_03, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라우스대화_01()


class 클라우스대화_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__13$', duration=2500, align='left') # 도와주셔서 감사합니다!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 클라우스대화_02()


class 클라우스대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__14$', duration=2500, align='left') # 그런데 누구……?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 클라우스대화_03()


class 클라우스대화_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 클라우스대화_04()


class 클라우스대화_04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[107])
        create_monster(spawnIds=[108], arg2=False)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라우스대화_05()


class 클라우스대화_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000378], questStates=[1]):
            return 에블린일기_01()


class 에블린일기_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에블린일기_02()


class 에블린일기_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$63000077_CS__63000077_MAIN__15$') # &lt;FONT color='#ffd200'&gt;누군가의 일기장 52페이지&lt;/FONT&gt;\n아빠 미워. 그깟 꽃이 뭐라고 나를 그렇게 혼낸 거야? \n화단 하나 관리 못 했다고 세상이 뒤집히는 것도 아닌데.\n꽃이 나보다 소중하면, 내 눈에 띄지 말고 쭉 정원에서 살아! $npcName:11004368$씨!
        move_user(mapId=63000077, portalId=4)
        select_camera(triggerId=8008, enable=True)
        set_scene_skip(state=업적_01, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 에블린일기_03()

    def on_exit(self):
        set_cinematic_ui(type=2)


class 에블린일기_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다시만난가족_01()


class 다시만난가족_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__16$', duration=3500, illustId='June_normal', align='left') # 제가 $npcName:11004356$의 마음을 아프게 한 것도 사실이고,\n제 딸 $npcName:11004356$의 마음을 달래주려는 순진한 $npcName:11004373$의 부탁이니…

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 다시만난가족_02()


class 다시만난가족_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__17$', duration=3000, illustId='June_normal', align='left') # 잠깐 나무 위에 올라가 있는 것도 나쁘지 않겠다 싶었답니다
        create_monster(spawnIds=[103,104,105], arg2=False)
        move_npc(spawnId=103, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 다시만난가족_03()

    def on_exit(self):
        move_npc(spawnId=108, patrolName='MS2PatrolData_2006')


class 다시만난가족_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__18$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 다시만난가족_04()


class 다시만난가족_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다시만난가족_05()


class 다시만난가족_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__19$', duration=3500, align='right') # 그건 그냥 투정이었어.\n내 소원은 그런 게 아니란 말이에요!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 다시만난가족_06()


class 다시만난가족_06(state.State):
    def on_enter(self):
        select_camera(triggerId=8012, enable=True)
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__20$', duration=2000, align='left') # 으응???

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 다시만난가족_07()


class 다시만난가족_07(state.State):
    def on_enter(self):
        move_npc(spawnId=106, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 다시만난가족_08()


class 다시만난가족_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__21$', duration=3500, align='left') # $npcName:11004356$…소원 아니야?\n내가 잘못한거야…?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 다시만난가족_09()


class 다시만난가족_09(state.State):
    def on_enter(self):
        select_camera(triggerId=8011, enable=True)
        move_npc(spawnId=103, patrolName='MS2PatrolData_2008')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 다시만난가족_10()


class 다시만난가족_10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__22$', duration=3500, illustId='Evelyn_glad', align='right') # 보…?\n그날 밤 내 얘길 듣고 간 게 역시 너였구나.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다시만난가족_11()


class 다시만난가족_11(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_2004')
        move_npc(spawnId=105, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다시만난가족_12()


class 다시만난가족_12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__23$', duration=4000, align='left') # 미안…미안해…!\n소원을 들어주고… 행복하게 해주고 싶었는데…!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 다시만난가족_13()


class 다시만난가족_13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004373, msg='$63000077_CS__63000077_MAIN__24$', duration=3000, align='left') # $npcName:11004373$$pp:가,이$… 너무 미안해…!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 다시만난가족_14()


class 다시만난가족_14(state.State):
    def on_enter(self):
        select_camera(triggerId=8011, enable=True)
        add_cinematic_talk(npcId=11004361, msg='$63000077_CS__63000077_MAIN__25$', duration=4000, illustId='Aiden_smile', align='right') # 아니야, 털북숭이. 미안해 할 필요 없어.\n$npcName:11004356$의 소원은 따로 있으니까

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 다시만난가족_15()


class 다시만난가족_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004365, msg='$63000077_CS__63000077_MAIN__26$', duration=3500, illustId='Mia_happy', align='right') # 그래. 진짜 소원을 말하면, 그걸 들어주렴.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 다시만난가족_16()


class 다시만난가족_16(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__27$', duration=2000, illustId='Evelyn_normal', align='right') # ……

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다시만난가족_17()


class 다시만난가족_17(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__28$', duration=3500, illustId='Evelyn_sad', align='right') # 미안해요, 모두.\n내가 부린 투정 때문에… 모두 너무 고생했어요.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 다시만난가족_18()


class 다시만난가족_18(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004368, msg='$63000077_CS__63000077_MAIN__29$', duration=3000, illustId='June_smile', align='right') # 그래서, 우리 $npcName:11004356$의 진짜 크리스마스 소원은 뭐지?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 다시만난가족_19()


class 다시만난가족_19(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004356, msg='$63000077_CS__63000077_MAIN__30$', duration=3500, illustId='Evelyn_glad', align='right') # 우리 가족 모두 함께 모여서…\n행복한 크리스마스 파티를 하는 거예요

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 다시만난가족_20()


class 다시만난가족_20(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8013], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 업적_01()


class 업적_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 업적_02()


class 업적_02(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='ChristmasWish')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=63000075, portalId=10)


class 종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_scene_skip()


