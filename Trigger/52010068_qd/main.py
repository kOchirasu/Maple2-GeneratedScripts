""" trigger/52010068_qd/main.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> state.State:
        if not quest_user_detected(boxIds=[2001], questIds=[20002391], questStates=[3]):
            return 틴차이_준타_스폰01()
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[3]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[2]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[1]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100400], questStates=[3]):
            return Orde_In_Effect()
        """
        <condition name="퀘스트유저를감지하면" arg1="2001" arg2="50100640" arg3="2" > 
                <transition state="챕터10에필로그연출01" />
            </condition>
        """


class 틴차이_준타_스폰01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[3]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[2]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[1]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100400], questStates=[3]):
            return Orde_In_Effect()
        """
        <condition name="퀘스트유저를감지하면" arg1="2001" arg2="50100640" arg3="2" >
                <transition state="챕터10에필로그연출01" /> 
            </condition>
        """


class Orde_In_Effect(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Orde_In()


class Orde_In(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Orde_In_Turn()


class Orde_In_Turn(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        set_effect(triggerIds=[5001], visible=True)
        set_npc_rotation(spawnId=101, rotation=-45)
        add_cinematic_talk(npcId=11004033, illustId='Orde_normal', msg='$52010068_QD__MAIN__0$', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Orde_In_Talk()


class Orde_In_Talk(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='IceSphere_A')
        add_cinematic_talk(npcId=11004033, illustId='Orde_normal', msg='$52010068_QD__MAIN__1$', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Orde_In_Talk_End()


class Orde_In_Talk_End(state.State):
    def on_enter(self):
        reset_camera()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Orde_In_ReTurn()


class Orde_In_ReTurn(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=101, rotation=360)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[3]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[2]):
            return Orde_Out_Effect()
        if quest_user_detected(boxIds=[2001], questIds=[50100420], questStates=[1]):
            return Orde_Out_Effect()


class Orde_Out_Effect(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Wizard_Teleport_A')
        add_balloon_talk(spawnId=101, msg='$52010068_QD__MAIN__2$', duration=2800, delayTick=0)
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Orde_Out()


class Orde_Out(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        set_effect(triggerIds=[5002], visible=False)


class 챕터10에필로그연출01(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 챕터10에필로그연출02()


class 챕터10에필로그연출02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=9, script='큰 희생이 있었지만, 우리는 $npc:11001698$를 상대로 승리를 얻었다.\n메이플월드를 공격한 그들에게 죄값을 치르게 만든것이다.')
        set_skip(state=챕터10에필로그연출02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출02스킵()


class 챕터10에필로그연출02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출03()


class 챕터10에필로그연출03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='비록 $npc:11001698$는 무사히 도망쳤지만, \n그녀 스스로의 의지로 도망친것은 아니었다.')
        set_skip(state=챕터10에필로그연출03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출03스킵()


class 챕터10에필로그연출03스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출05()


class 챕터10에필로그연출05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='오히려 $npc:11001698$는 이번 전투에서 자신의 요새를 잃고 말았다.')
        set_skip(state=챕터10에필로그연출05스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출05스킵()


class 챕터10에필로그연출05스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출05b()


class 챕터10에필로그연출05b(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 챕터10에필로그연출06()


class 챕터10에필로그연출06(state.State):
    def on_enter(self):
        set_sound(triggerId=90000, arg2=True) # 마드리아 고조 브금
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__3$', arg4=6)
        set_onetime_effect(id=2007, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_01_00002007.xml')
        set_skip(state=챕터10에필로그연출06스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 챕터10에필로그연출06스킵()


class 챕터10에필로그연출06스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출07()


class 챕터10에필로그연출07(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__4$', arg4=6)
        set_onetime_effect(id=2008, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_02_00002008.xml')
        set_skip(state=챕터10에필로그연출07스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 챕터10에필로그연출07스킵()


class 챕터10에필로그연출07스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출08()


class 챕터10에필로그연출08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__5$', arg4=9)
        set_onetime_effect(id=2009, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_03_00002009.xml')
        set_skip(state=챕터10에필로그연출08스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 챕터10에필로그연출08스킵()


class 챕터10에필로그연출08스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출09()


class 챕터10에필로그연출09(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__6$', arg4=5)
        set_onetime_effect(id=2009, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_03_00002009.xml')
        set_skip(state=챕터10에필로그연출9스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출9스킵()


class 챕터10에필로그연출9스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출10()


class 챕터10에필로그연출10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__7$', arg4=5)
        set_onetime_effect(id=2010, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_04_00002010.xml')
        set_skip(state=챕터10에필로그연출10스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출10스킵()


class 챕터10에필로그연출10스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출11()


class 챕터10에필로그연출11(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__8$', arg4=5)
        set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        set_skip(state=챕터10에필로그연출11스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출11스킵()


class 챕터10에필로그연출11스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출12()


class 챕터10에필로그연출12(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__9$', arg4=5)
        set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        set_skip(state=챕터10에필로그연출12스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출12스킵()


class 챕터10에필로그연출12스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출13()


class 챕터10에필로그연출13(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__10$', arg4=5)
        set_onetime_effect(id=2011, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_05_00002011.xml')
        set_skip(state=챕터10에필로그연출13스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출13스킵()


class 챕터10에필로그연출13스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출13_b()


class 챕터10에필로그연출13_b(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__11$', arg4=5)
        set_onetime_effect(id=2012, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_06_00002012.xml')
        set_skip(state=챕터10에필로그연출13b스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 챕터10에필로그연출13b스킵()


class 챕터10에필로그연출13b스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출14()


class 챕터10에필로그연출14(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__12$', arg4=5)
        set_onetime_effect(id=2013, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_07_00002013.xml')
        set_skip(state=챕터10에필로그연출14스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출14스킵()


class 챕터10에필로그연출14스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출15()


class 챕터10에필로그연출15(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__13$', arg4=6)
        set_onetime_effect(id=2014, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_08_00002014.xml')
        set_skip(state=챕터10에필로그연출15스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 챕터10에필로그연출15스킵()


class 챕터10에필로그연출15스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출16()


class 챕터10에필로그연출16(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001820, script='$52010068_QD__MAIN__14$', arg4=5)
        set_onetime_effect(id=2015, enable=True, path='BG/Common/Sound/Eff_Madria_Chapter10_End_09_00002015.xml')
        set_skip(state=챕터10에필로그연출16스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 챕터10에필로그연출16스킵()


class 챕터10에필로그연출16스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출17()


class 챕터10에필로그연출17(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 챕터10에필로그연출18()


class 챕터10에필로그연출18(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$npc:11001698$는 그녀의 용을 타고 날아올랐다\n그리고 이 것이 마드라칸 요새의 최후였다.')
        set_skip(state=챕터10에필로그연출18스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출18스킵()


class 챕터10에필로그연출18스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출18b()


class 챕터10에필로그연출18b(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$npc:11001698$는 분명 다시 돌아올 것이다.\n그리고 또다시 서로에게 소중한 존재들을 빼앗을지도 모른다.')
        set_skip(state=챕터10에필로그연출18b스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출18b스킵()


class 챕터10에필로그연출18b스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출19()


class 챕터10에필로그연출19(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='그렇지만, 할 수 있다면 $npc:11001698$와 싸우지 않아도 될 방법을 찾고자 한다.\n복수의 나선은 결국 서로의 모든것을 파괴할것이기 때문이다.')
        set_skip(state=챕터10에필로그연출19스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출19스킵()


class 챕터10에필로그연출19스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출20()


class 챕터10에필로그연출20(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='그리고 나는 어떤 방법으로든 테룬칼리브들이 살아있다고 굳게 믿고 있다.\n그들이 나를 살렸듯 그들 스스로 어떻게 살아날 방법을 찾았을거라 믿고 싶다.')
        set_skip(state=챕터10에필로그연출20스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출20스킵()


class 챕터10에필로그연출20스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 챕터10에필로그연출21()


class 챕터10에필로그연출21(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='하여, 나는 블랙 샤드의 폭심지, \'아이 오브 라펜타\'의 수색과\n라펜샤드의 조사에 최선을 다할 것이라고 다짐했다.')
        set_skip(state=챕터10에필로그연출22)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 챕터10에필로그연출22()


class 챕터10에필로그연출22(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=52010068, portalId=2)


