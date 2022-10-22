""" trigger/81000002_item/mainprocess_springbeach.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[302]):
            return 이벤트대기중()


class 이벤트대기중(state.State):
    def on_enter(self):
        set_portal(portalId=901, visible=True, enabled=True, minimapVisible=True)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624], visible=False)
        set_mesh(triggerIds=[651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677], visible=True)
        set_mesh(triggerIds=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832], visible=True)
        set_effect(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=180000):
            return 준비멘트1()


class 준비멘트1(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=6)
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_00')
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__0$', arg3='5000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 준비멘트2()


class 준비멘트2(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=4)
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_01')
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__1$', arg3='3000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 경기장입장()


class 경기장입장(state.State):
    def on_tick(self) -> state.State:
        if true():
            move_to_portal(portalId=902, boxId=302)
            return 잠시대기()


class 잠시대기(state.State):
    def on_enter(self):
        set_timer(timerId='13', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 시작멘트1()


class 시작멘트1(state.State):
    def on_enter(self):
        start_mini_game(isShowResultUI=False, boxId=301, round=5, gameName='UserMassive_Springbeach')
        set_mini_game_area_for_hack(boxId=301) # 해킹 보안용 시작 box 설정
        set_timer(timerId='13', seconds=5)
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__2$', arg3='4000')
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_02') # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 시작멘트2()


class 시작멘트2(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=5)
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__3$', arg3='5500')
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_03')

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 시작멘트3()


class 시작멘트3(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_04')
        set_timer(timerId='15', seconds=5)
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__4$', arg3='5500')

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 라운드1()


#  1라운드 
class 라운드1(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=301, round=1)
        set_timer(timerId='16', seconds=4)
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_05')
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__5$', arg3='3000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='16'):
            return 게임시작1()


class 게임시작1(state.State):
    def on_enter(self):
        set_timer(timerId='17', seconds=6)
        set_event_ui(type=0, arg2='1,5')
        show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__6$', stage=1, count=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='17'):
            return 스프링섞기01()


class 스프링섞기01(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=5):
            return 스프링공격01_1()
        if random_condition(rate=5):
            return 스프링공격02_1()
        if random_condition(rate=5):
            return 스프링공격03_1()
        if random_condition(rate=5):
            return 스프링공격04_1()
        if random_condition(rate=5):
            return 스프링공격05_1()
        if random_condition(rate=5):
            return 스프링공격06_1()
        if random_condition(rate=5):
            return 스프링공격07_1()
        if random_condition(rate=5):
            return 스프링공격08_1()
        if random_condition(rate=5):
            return 스프링공격09_1()
        if random_condition(rate=5):
            return 스프링공격10_1()
        if random_condition(rate=4):
            return 스프링공격11_1()
        if random_condition(rate=4):
            return 스프링공격12_1()
        if random_condition(rate=4):
            return 스프링공격13_1()
        if random_condition(rate=4):
            return 스프링공격14_1()
        if random_condition(rate=4):
            return 스프링공격15_1()
        if random_condition(rate=2):
            return 스프링공격16_1()
        if random_condition(rate=2):
            return 스프링공격17_1()
        if random_condition(rate=2):
            return 스프링공격18_1()
        if random_condition(rate=2):
            return 스프링공격19_1()
        if random_condition(rate=2):
            return 스프링공격20_1()
        if random_condition(rate=1):
            return 스프링공격21_1()
        if random_condition(rate=1):
            return 스프링공격22_1()
        if random_condition(rate=1):
            return 스프링공격23_1()
        if random_condition(rate=1):
            return 스프링공격24_1()
        if random_condition(rate=1):
            return 스프링공격25_1()
        if random_condition(rate=1):
            return 스프링공격26_1()
        if random_condition(rate=1):
            return 스프링공격27_1()
        if random_condition(rate=1):
            return 스프링공격28_1()
        if random_condition(rate=1):
            return 스프링공격29_1()
        if random_condition(rate=1):
            return 스프링공격30_1()
        if random_condition(rate=1):
            return 스프링공격31_1()
        if random_condition(rate=1):
            return 스프링공격32_1()
        if random_condition(rate=1):
            return 스프링공격33_1()
        if random_condition(rate=1):
            return 스프링공격34_1()
        if random_condition(rate=1):
            return 스프링공격35_1()
        if random_condition(rate=1):
            return 스프링공격36_1()
        if random_condition(rate=1):
            return 스프링공격37_1()
        if random_condition(rate=1):
            return 스프링공격38_1()
        if random_condition(rate=1):
            return 스프링공격39_1()
        if random_condition(rate=1):
            return 스프링공격40_1()


class 공격중지01(state.State):
    def on_enter(self):
        set_timer(timerId='19', seconds=3)
        set_skill(triggerIds=[201], isEnable=False)
        set_skill(triggerIds=[202], isEnable=False)
        set_skill(triggerIds=[203], isEnable=False)
        set_skill(triggerIds=[204], isEnable=False)
        set_skill(triggerIds=[205], isEnable=False)
        set_skill(triggerIds=[206], isEnable=False)
        set_skill(triggerIds=[207], isEnable=False)
        set_skill(triggerIds=[208], isEnable=False)
        set_skill(triggerIds=[209], isEnable=False)
        set_skill(triggerIds=[210], isEnable=False)
        set_skill(triggerIds=[211], isEnable=False)
        set_skill(triggerIds=[212], isEnable=False)
        set_skill(triggerIds=[213], isEnable=False)
        set_skill(triggerIds=[214], isEnable=False)
        set_skill(triggerIds=[215], isEnable=False)
        set_skill(triggerIds=[216], isEnable=False)
        set_skill(triggerIds=[217], isEnable=False)
        set_skill(triggerIds=[218], isEnable=False)
        set_skill(triggerIds=[219], isEnable=False)
        set_skill(triggerIds=[220], isEnable=False)
        set_skill(triggerIds=[221], isEnable=False)
        set_skill(triggerIds=[222], isEnable=False)
        set_skill(triggerIds=[223], isEnable=False)
        set_skill(triggerIds=[224], isEnable=False)
        set_skill(triggerIds=[225], isEnable=False)
        set_skill(triggerIds=[226], isEnable=False)
        set_skill(triggerIds=[227], isEnable=False)
        set_skill(triggerIds=[228], isEnable=False)
        set_skill(triggerIds=[229], isEnable=False)
        set_skill(triggerIds=[230], isEnable=False)
        set_skill(triggerIds=[231], isEnable=False)
        set_skill(triggerIds=[232], isEnable=False)
        set_skill(triggerIds=[233], isEnable=False)
        set_skill(triggerIds=[234], isEnable=False)
        set_skill(triggerIds=[235], isEnable=False)
        set_skill(triggerIds=[236], isEnable=False)
        set_skill(triggerIds=[237], isEnable=False)
        set_skill(triggerIds=[238], isEnable=False)
        set_skill(triggerIds=[239], isEnable=False)
        set_skill(triggerIds=[240], isEnable=False)
        set_skill(triggerIds=[241], isEnable=False)
        set_skill(triggerIds=[242], isEnable=False)
        set_skill(triggerIds=[243], isEnable=False)
        set_skill(triggerIds=[244], isEnable=False)
        set_skill(triggerIds=[245], isEnable=False)
        set_skill(triggerIds=[246], isEnable=False)
        set_skill(triggerIds=[247], isEnable=False)
        set_skill(triggerIds=[248], isEnable=False)
        set_skill(triggerIds=[249], isEnable=False)
        set_skill(triggerIds=[250], isEnable=False)
        set_skill(triggerIds=[251], isEnable=False)
        set_skill(triggerIds=[252], isEnable=False)
        set_skill(triggerIds=[253], isEnable=False)
        set_skill(triggerIds=[254], isEnable=False)
        set_skill(triggerIds=[255], isEnable=False)
        set_skill(triggerIds=[256], isEnable=False)
        set_skill(triggerIds=[257], isEnable=False)
        set_skill(triggerIds=[258], isEnable=False)
        set_skill(triggerIds=[259], isEnable=False)
        set_skill(triggerIds=[260], isEnable=False)
        set_skill(triggerIds=[261], isEnable=False)
        set_skill(triggerIds=[262], isEnable=False)
        set_skill(triggerIds=[263], isEnable=False)
        set_skill(triggerIds=[264], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='19'):
            return 생존자수색01()
        if not user_detected(boxIds=[301]):
            return 모두탈락()


class 생존자수색01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 한숨돌리기01()


class 한숨돌리기01(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2, gameName='UserMassive_Springbeach')
        set_timer(timerId='20', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 라운드2()


#  2라운드 
class 라운드2(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=301, round=2)
        set_timer(timerId='21', seconds=4)
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_07')
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__7$', arg3='3000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 게임시작2()


class 게임시작2(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=6)
        set_event_ui(type=0, arg2='2,5')
        show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__8$', stage=2, count=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return 스프링섞기02()


class 스프링섞기02(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return 스프링공격01_2()
        if random_condition(rate=2):
            return 스프링공격02_2()
        if random_condition(rate=2):
            return 스프링공격03_2()
        if random_condition(rate=2):
            return 스프링공격04_2()
        if random_condition(rate=2):
            return 스프링공격05_2()
        if random_condition(rate=2):
            return 스프링공격06_2()
        if random_condition(rate=2):
            return 스프링공격07_2()
        if random_condition(rate=2):
            return 스프링공격08_2()
        if random_condition(rate=2):
            return 스프링공격09_2()
        if random_condition(rate=2):
            return 스프링공격10_2()
        if random_condition(rate=3):
            return 스프링공격11_2()
        if random_condition(rate=3):
            return 스프링공격12_2()
        if random_condition(rate=3):
            return 스프링공격13_2()
        if random_condition(rate=3):
            return 스프링공격14_2()
        if random_condition(rate=3):
            return 스프링공격15_2()
        if random_condition(rate=5):
            return 스프링공격16_2()
        if random_condition(rate=5):
            return 스프링공격17_2()
        if random_condition(rate=5):
            return 스프링공격18_2()
        if random_condition(rate=5):
            return 스프링공격19_2()
        if random_condition(rate=5):
            return 스프링공격20_2()
        if random_condition(rate=1):
            return 스프링공격21_2()
        if random_condition(rate=1):
            return 스프링공격22_2()
        if random_condition(rate=1):
            return 스프링공격23_2()
        if random_condition(rate=1):
            return 스프링공격24_2()
        if random_condition(rate=1):
            return 스프링공격25_2()
        if random_condition(rate=5):
            return 스프링공격26_2()
        if random_condition(rate=5):
            return 스프링공격27_2()
        if random_condition(rate=5):
            return 스프링공격28_2()
        if random_condition(rate=5):
            return 스프링공격29_2()
        if random_condition(rate=5):
            return 스프링공격30_2()
        if random_condition(rate=1):
            return 스프링공격31_2()
        if random_condition(rate=1):
            return 스프링공격32_2()
        if random_condition(rate=1):
            return 스프링공격33_2()
        if random_condition(rate=1):
            return 스프링공격34_2()
        if random_condition(rate=1):
            return 스프링공격35_2()
        if random_condition(rate=1):
            return 스프링공격36_2()
        if random_condition(rate=1):
            return 스프링공격37_2()
        if random_condition(rate=1):
            return 스프링공격38_2()
        if random_condition(rate=1):
            return 스프링공격39_2()
        if random_condition(rate=1):
            return 스프링공격40_2()


class 공격중지02(state.State):
    def on_enter(self):
        set_timer(timerId='23', seconds=3)
        set_skill(triggerIds=[201], isEnable=False)
        set_skill(triggerIds=[202], isEnable=False)
        set_skill(triggerIds=[203], isEnable=False)
        set_skill(triggerIds=[204], isEnable=False)
        set_skill(triggerIds=[205], isEnable=False)
        set_skill(triggerIds=[206], isEnable=False)
        set_skill(triggerIds=[207], isEnable=False)
        set_skill(triggerIds=[208], isEnable=False)
        set_skill(triggerIds=[209], isEnable=False)
        set_skill(triggerIds=[210], isEnable=False)
        set_skill(triggerIds=[211], isEnable=False)
        set_skill(triggerIds=[212], isEnable=False)
        set_skill(triggerIds=[213], isEnable=False)
        set_skill(triggerIds=[214], isEnable=False)
        set_skill(triggerIds=[215], isEnable=False)
        set_skill(triggerIds=[216], isEnable=False)
        set_skill(triggerIds=[217], isEnable=False)
        set_skill(triggerIds=[218], isEnable=False)
        set_skill(triggerIds=[219], isEnable=False)
        set_skill(triggerIds=[220], isEnable=False)
        set_skill(triggerIds=[221], isEnable=False)
        set_skill(triggerIds=[222], isEnable=False)
        set_skill(triggerIds=[223], isEnable=False)
        set_skill(triggerIds=[224], isEnable=False)
        set_skill(triggerIds=[225], isEnable=False)
        set_skill(triggerIds=[226], isEnable=False)
        set_skill(triggerIds=[227], isEnable=False)
        set_skill(triggerIds=[228], isEnable=False)
        set_skill(triggerIds=[229], isEnable=False)
        set_skill(triggerIds=[230], isEnable=False)
        set_skill(triggerIds=[231], isEnable=False)
        set_skill(triggerIds=[232], isEnable=False)
        set_skill(triggerIds=[233], isEnable=False)
        set_skill(triggerIds=[234], isEnable=False)
        set_skill(triggerIds=[235], isEnable=False)
        set_skill(triggerIds=[236], isEnable=False)
        set_skill(triggerIds=[237], isEnable=False)
        set_skill(triggerIds=[238], isEnable=False)
        set_skill(triggerIds=[239], isEnable=False)
        set_skill(triggerIds=[240], isEnable=False)
        set_skill(triggerIds=[241], isEnable=False)
        set_skill(triggerIds=[242], isEnable=False)
        set_skill(triggerIds=[243], isEnable=False)
        set_skill(triggerIds=[244], isEnable=False)
        set_skill(triggerIds=[245], isEnable=False)
        set_skill(triggerIds=[246], isEnable=False)
        set_skill(triggerIds=[247], isEnable=False)
        set_skill(triggerIds=[248], isEnable=False)
        set_skill(triggerIds=[249], isEnable=False)
        set_skill(triggerIds=[250], isEnable=False)
        set_skill(triggerIds=[251], isEnable=False)
        set_skill(triggerIds=[252], isEnable=False)
        set_skill(triggerIds=[253], isEnable=False)
        set_skill(triggerIds=[254], isEnable=False)
        set_skill(triggerIds=[255], isEnable=False)
        set_skill(triggerIds=[256], isEnable=False)
        set_skill(triggerIds=[257], isEnable=False)
        set_skill(triggerIds=[258], isEnable=False)
        set_skill(triggerIds=[259], isEnable=False)
        set_skill(triggerIds=[260], isEnable=False)
        set_skill(triggerIds=[261], isEnable=False)
        set_skill(triggerIds=[262], isEnable=False)
        set_skill(triggerIds=[263], isEnable=False)
        set_skill(triggerIds=[264], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='23'):
            return 생존자수색02()
        if not user_detected(boxIds=[301]):
            return 모두탈락()


class 생존자수색02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 한숨돌리기02()


class 한숨돌리기02(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2, gameName='UserMassive_Springbeach')
        set_timer(timerId='24', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='24'):
            return 라운드3()


#  3라운드 
class 라운드3(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=301, round=3)
        set_timer(timerId='25', seconds=4)
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_09')
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__9$', arg3='3000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 게임시작3()


class 게임시작3(state.State):
    def on_enter(self):
        set_timer(timerId='26', seconds=6)
        set_event_ui(type=0, arg2='3,5')
        show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__10$', stage=3, count=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='26'):
            return 스프링섞기03()


class 스프링섞기03(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return 스프링공격01_3()
        if random_condition(rate=1):
            return 스프링공격02_3()
        if random_condition(rate=1):
            return 스프링공격03_3()
        if random_condition(rate=1):
            return 스프링공격04_3()
        if random_condition(rate=1):
            return 스프링공격05_3()
        if random_condition(rate=1):
            return 스프링공격06_3()
        if random_condition(rate=1):
            return 스프링공격07_3()
        if random_condition(rate=1):
            return 스프링공격08_3()
        if random_condition(rate=1):
            return 스프링공격09_3()
        if random_condition(rate=1):
            return 스프링공격10_3()
        if random_condition(rate=1):
            return 스프링공격11_3()
        if random_condition(rate=1):
            return 스프링공격12_3()
        if random_condition(rate=1):
            return 스프링공격13_3()
        if random_condition(rate=1):
            return 스프링공격14_3()
        if random_condition(rate=1):
            return 스프링공격15_3()
        if random_condition(rate=5):
            return 스프링공격16_3()
        if random_condition(rate=5):
            return 스프링공격17_3()
        if random_condition(rate=5):
            return 스프링공격18_3()
        if random_condition(rate=5):
            return 스프링공격19_3()
        if random_condition(rate=5):
            return 스프링공격20_3()
        if random_condition(rate=2):
            return 스프링공격21_3()
        if random_condition(rate=2):
            return 스프링공격22_3()
        if random_condition(rate=2):
            return 스프링공격23_3()
        if random_condition(rate=2):
            return 스프링공격24_3()
        if random_condition(rate=2):
            return 스프링공격25_3()
        if random_condition(rate=5):
            return 스프링공격26_3()
        if random_condition(rate=5):
            return 스프링공격27_3()
        if random_condition(rate=5):
            return 스프링공격28_3()
        if random_condition(rate=5):
            return 스프링공격29_3()
        if random_condition(rate=5):
            return 스프링공격30_3()
        if random_condition(rate=3):
            return 스프링공격31_3()
        if random_condition(rate=3):
            return 스프링공격32_3()
        if random_condition(rate=3):
            return 스프링공격33_3()
        if random_condition(rate=3):
            return 스프링공격34_3()
        if random_condition(rate=3):
            return 스프링공격35_3()
        if random_condition(rate=2):
            return 스프링공격36_3()
        if random_condition(rate=2):
            return 스프링공격37_3()
        if random_condition(rate=2):
            return 스프링공격38_3()
        if random_condition(rate=2):
            return 스프링공격39_3()
        if random_condition(rate=2):
            return 스프링공격40_3()


class 공격중지03(state.State):
    def on_enter(self):
        set_timer(timerId='27', seconds=3)
        set_skill(triggerIds=[201], isEnable=False)
        set_skill(triggerIds=[202], isEnable=False)
        set_skill(triggerIds=[203], isEnable=False)
        set_skill(triggerIds=[204], isEnable=False)
        set_skill(triggerIds=[205], isEnable=False)
        set_skill(triggerIds=[206], isEnable=False)
        set_skill(triggerIds=[207], isEnable=False)
        set_skill(triggerIds=[208], isEnable=False)
        set_skill(triggerIds=[209], isEnable=False)
        set_skill(triggerIds=[210], isEnable=False)
        set_skill(triggerIds=[211], isEnable=False)
        set_skill(triggerIds=[212], isEnable=False)
        set_skill(triggerIds=[213], isEnable=False)
        set_skill(triggerIds=[214], isEnable=False)
        set_skill(triggerIds=[215], isEnable=False)
        set_skill(triggerIds=[216], isEnable=False)
        set_skill(triggerIds=[217], isEnable=False)
        set_skill(triggerIds=[218], isEnable=False)
        set_skill(triggerIds=[219], isEnable=False)
        set_skill(triggerIds=[220], isEnable=False)
        set_skill(triggerIds=[221], isEnable=False)
        set_skill(triggerIds=[222], isEnable=False)
        set_skill(triggerIds=[223], isEnable=False)
        set_skill(triggerIds=[224], isEnable=False)
        set_skill(triggerIds=[225], isEnable=False)
        set_skill(triggerIds=[226], isEnable=False)
        set_skill(triggerIds=[227], isEnable=False)
        set_skill(triggerIds=[228], isEnable=False)
        set_skill(triggerIds=[229], isEnable=False)
        set_skill(triggerIds=[230], isEnable=False)
        set_skill(triggerIds=[231], isEnable=False)
        set_skill(triggerIds=[232], isEnable=False)
        set_skill(triggerIds=[233], isEnable=False)
        set_skill(triggerIds=[234], isEnable=False)
        set_skill(triggerIds=[235], isEnable=False)
        set_skill(triggerIds=[236], isEnable=False)
        set_skill(triggerIds=[237], isEnable=False)
        set_skill(triggerIds=[238], isEnable=False)
        set_skill(triggerIds=[239], isEnable=False)
        set_skill(triggerIds=[240], isEnable=False)
        set_skill(triggerIds=[241], isEnable=False)
        set_skill(triggerIds=[242], isEnable=False)
        set_skill(triggerIds=[243], isEnable=False)
        set_skill(triggerIds=[244], isEnable=False)
        set_skill(triggerIds=[245], isEnable=False)
        set_skill(triggerIds=[246], isEnable=False)
        set_skill(triggerIds=[247], isEnable=False)
        set_skill(triggerIds=[248], isEnable=False)
        set_skill(triggerIds=[249], isEnable=False)
        set_skill(triggerIds=[250], isEnable=False)
        set_skill(triggerIds=[251], isEnable=False)
        set_skill(triggerIds=[252], isEnable=False)
        set_skill(triggerIds=[253], isEnable=False)
        set_skill(triggerIds=[254], isEnable=False)
        set_skill(triggerIds=[255], isEnable=False)
        set_skill(triggerIds=[256], isEnable=False)
        set_skill(triggerIds=[257], isEnable=False)
        set_skill(triggerIds=[258], isEnable=False)
        set_skill(triggerIds=[259], isEnable=False)
        set_skill(triggerIds=[260], isEnable=False)
        set_skill(triggerIds=[261], isEnable=False)
        set_skill(triggerIds=[262], isEnable=False)
        set_skill(triggerIds=[263], isEnable=False)
        set_skill(triggerIds=[264], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='27'):
            return 생존자수색03()
        if not user_detected(boxIds=[301]):
            return 모두탈락()


class 생존자수색03(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 한숨돌리기03()


class 한숨돌리기03(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2, gameName='UserMassive_Springbeach')
        set_timer(timerId='28', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='28'):
            return 라운드4()


#  4라운드 
class 라운드4(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=301, round=4)
        set_timer(timerId='29', seconds=4)
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_11')
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__11$', arg3='3000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='29'):
            return 게임시작4()


class 게임시작4(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=6)
        set_event_ui(type=0, arg2='4,5')
        show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__12$', stage=4, count=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 스프링섞기04()


class 스프링섞기04(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return 스프링공격01_4()
        if random_condition(rate=1):
            return 스프링공격02_4()
        if random_condition(rate=1):
            return 스프링공격03_4()
        if random_condition(rate=1):
            return 스프링공격04_4()
        if random_condition(rate=1):
            return 스프링공격05_4()
        if random_condition(rate=1):
            return 스프링공격06_4()
        if random_condition(rate=1):
            return 스프링공격07_4()
        if random_condition(rate=1):
            return 스프링공격08_4()
        if random_condition(rate=1):
            return 스프링공격09_4()
        if random_condition(rate=1):
            return 스프링공격10_4()
        if random_condition(rate=1):
            return 스프링공격11_4()
        if random_condition(rate=1):
            return 스프링공격12_4()
        if random_condition(rate=1):
            return 스프링공격13_4()
        if random_condition(rate=1):
            return 스프링공격14_4()
        if random_condition(rate=1):
            return 스프링공격15_4()
        if random_condition(rate=3):
            return 스프링공격16_4()
        if random_condition(rate=3):
            return 스프링공격17_4()
        if random_condition(rate=3):
            return 스프링공격18_4()
        if random_condition(rate=3):
            return 스프링공격19_4()
        if random_condition(rate=3):
            return 스프링공격20_4()
        if random_condition(rate=4):
            return 스프링공격21_4()
        if random_condition(rate=4):
            return 스프링공격22_4()
        if random_condition(rate=4):
            return 스프링공격23_4()
        if random_condition(rate=4):
            return 스프링공격24_4()
        if random_condition(rate=3):
            return 스프링공격25_4()
        if random_condition(rate=3):
            return 스프링공격26_4()
        if random_condition(rate=3):
            return 스프링공격27_4()
        if random_condition(rate=3):
            return 스프링공격28_4()
        if random_condition(rate=3):
            return 스프링공격29_4()
        if random_condition(rate=3):
            return 스프링공격30_4()
        if random_condition(rate=4):
            return 스프링공격31_4()
        if random_condition(rate=4):
            return 스프링공격32_4()
        if random_condition(rate=4):
            return 스프링공격33_4()
        if random_condition(rate=4):
            return 스프링공격34_4()
        if random_condition(rate=4):
            return 스프링공격35_4()
        if random_condition(rate=2):
            return 스프링공격36_4()
        if random_condition(rate=3):
            return 스프링공격37_4()
        if random_condition(rate=3):
            return 스프링공격38_4()
        if random_condition(rate=4):
            return 스프링공격39_4()
        if random_condition(rate=4):
            return 스프링공격40_4()


class 공격중지04(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=3)
        set_skill(triggerIds=[201], isEnable=False)
        set_skill(triggerIds=[202], isEnable=False)
        set_skill(triggerIds=[203], isEnable=False)
        set_skill(triggerIds=[204], isEnable=False)
        set_skill(triggerIds=[205], isEnable=False)
        set_skill(triggerIds=[206], isEnable=False)
        set_skill(triggerIds=[207], isEnable=False)
        set_skill(triggerIds=[208], isEnable=False)
        set_skill(triggerIds=[209], isEnable=False)
        set_skill(triggerIds=[210], isEnable=False)
        set_skill(triggerIds=[211], isEnable=False)
        set_skill(triggerIds=[212], isEnable=False)
        set_skill(triggerIds=[213], isEnable=False)
        set_skill(triggerIds=[214], isEnable=False)
        set_skill(triggerIds=[215], isEnable=False)
        set_skill(triggerIds=[216], isEnable=False)
        set_skill(triggerIds=[217], isEnable=False)
        set_skill(triggerIds=[218], isEnable=False)
        set_skill(triggerIds=[219], isEnable=False)
        set_skill(triggerIds=[220], isEnable=False)
        set_skill(triggerIds=[221], isEnable=False)
        set_skill(triggerIds=[222], isEnable=False)
        set_skill(triggerIds=[223], isEnable=False)
        set_skill(triggerIds=[224], isEnable=False)
        set_skill(triggerIds=[225], isEnable=False)
        set_skill(triggerIds=[226], isEnable=False)
        set_skill(triggerIds=[227], isEnable=False)
        set_skill(triggerIds=[228], isEnable=False)
        set_skill(triggerIds=[229], isEnable=False)
        set_skill(triggerIds=[230], isEnable=False)
        set_skill(triggerIds=[231], isEnable=False)
        set_skill(triggerIds=[232], isEnable=False)
        set_skill(triggerIds=[233], isEnable=False)
        set_skill(triggerIds=[234], isEnable=False)
        set_skill(triggerIds=[235], isEnable=False)
        set_skill(triggerIds=[236], isEnable=False)
        set_skill(triggerIds=[237], isEnable=False)
        set_skill(triggerIds=[238], isEnable=False)
        set_skill(triggerIds=[239], isEnable=False)
        set_skill(triggerIds=[240], isEnable=False)
        set_skill(triggerIds=[241], isEnable=False)
        set_skill(triggerIds=[242], isEnable=False)
        set_skill(triggerIds=[243], isEnable=False)
        set_skill(triggerIds=[244], isEnable=False)
        set_skill(triggerIds=[245], isEnable=False)
        set_skill(triggerIds=[246], isEnable=False)
        set_skill(triggerIds=[247], isEnable=False)
        set_skill(triggerIds=[248], isEnable=False)
        set_skill(triggerIds=[249], isEnable=False)
        set_skill(triggerIds=[250], isEnable=False)
        set_skill(triggerIds=[251], isEnable=False)
        set_skill(triggerIds=[252], isEnable=False)
        set_skill(triggerIds=[253], isEnable=False)
        set_skill(triggerIds=[254], isEnable=False)
        set_skill(triggerIds=[255], isEnable=False)
        set_skill(triggerIds=[256], isEnable=False)
        set_skill(triggerIds=[257], isEnable=False)
        set_skill(triggerIds=[258], isEnable=False)
        set_skill(triggerIds=[259], isEnable=False)
        set_skill(triggerIds=[260], isEnable=False)
        set_skill(triggerIds=[261], isEnable=False)
        set_skill(triggerIds=[262], isEnable=False)
        set_skill(triggerIds=[263], isEnable=False)
        set_skill(triggerIds=[264], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 생존자수색04()
        if not user_detected(boxIds=[301]):
            return 모두탈락()


class 생존자수색04(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 한숨돌리기04()


class 한숨돌리기04(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2, gameName='UserMassive_Springbeach')
        set_timer(timerId='32', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='32'):
            return 라운드5()


#  5라운드 
class 라운드5(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=301, round=5)
        set_timer(timerId='33', seconds=4)
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_13')
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__13$', arg3='3000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='33'):
            return 게임시작5()


class 게임시작5(state.State):
    def on_enter(self):
        set_timer(timerId='34', seconds=6)
        set_event_ui(type=0, arg2='5,5')
        show_count_ui(text='$61000007_ME__MAINPROCESS_SPRINGBEACH__14$', stage=5, count=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='34'):
            return 스프링섞기05()


class 스프링섞기05(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return 스프링공격16_5()
        if random_condition(rate=2):
            return 스프링공격17_5()
        if random_condition(rate=2):
            return 스프링공격18_5()
        if random_condition(rate=2):
            return 스프링공격19_5()
        if random_condition(rate=2):
            return 스프링공격20_5()
        if random_condition(rate=6):
            return 스프링공격21_5()
        if random_condition(rate=5):
            return 스프링공격22_5()
        if random_condition(rate=6):
            return 스프링공격23_5()
        if random_condition(rate=6):
            return 스프링공격24_5()
        if random_condition(rate=6):
            return 스프링공격25_5()
        if random_condition(rate=2):
            return 스프링공격26_5()
        if random_condition(rate=2):
            return 스프링공격27_5()
        if random_condition(rate=2):
            return 스프링공격28_5()
        if random_condition(rate=2):
            return 스프링공격29_5()
        if random_condition(rate=2):
            return 스프링공격30_5()
        if random_condition(rate=5):
            return 스프링공격31_5()
        if random_condition(rate=5):
            return 스프링공격32_5()
        if random_condition(rate=5):
            return 스프링공격33_5()
        if random_condition(rate=5):
            return 스프링공격34_5()
        if random_condition(rate=5):
            return 스프링공격35_5()
        if random_condition(rate=4):
            return 스프링공격36_5()
        if random_condition(rate=6):
            return 스프링공격37_5()
        if random_condition(rate=6):
            return 스프링공격38_5()
        if random_condition(rate=5):
            return 스프링공격39_5()
        if random_condition(rate=5):
            return 스프링공격40_5()


class 공격중지05(state.State):
    def on_enter(self):
        set_timer(timerId='35', seconds=3)
        set_skill(triggerIds=[201], isEnable=False)
        set_skill(triggerIds=[202], isEnable=False)
        set_skill(triggerIds=[203], isEnable=False)
        set_skill(triggerIds=[204], isEnable=False)
        set_skill(triggerIds=[205], isEnable=False)
        set_skill(triggerIds=[206], isEnable=False)
        set_skill(triggerIds=[207], isEnable=False)
        set_skill(triggerIds=[208], isEnable=False)
        set_skill(triggerIds=[209], isEnable=False)
        set_skill(triggerIds=[210], isEnable=False)
        set_skill(triggerIds=[211], isEnable=False)
        set_skill(triggerIds=[212], isEnable=False)
        set_skill(triggerIds=[213], isEnable=False)
        set_skill(triggerIds=[214], isEnable=False)
        set_skill(triggerIds=[215], isEnable=False)
        set_skill(triggerIds=[216], isEnable=False)
        set_skill(triggerIds=[217], isEnable=False)
        set_skill(triggerIds=[218], isEnable=False)
        set_skill(triggerIds=[219], isEnable=False)
        set_skill(triggerIds=[220], isEnable=False)
        set_skill(triggerIds=[221], isEnable=False)
        set_skill(triggerIds=[222], isEnable=False)
        set_skill(triggerIds=[223], isEnable=False)
        set_skill(triggerIds=[224], isEnable=False)
        set_skill(triggerIds=[225], isEnable=False)
        set_skill(triggerIds=[226], isEnable=False)
        set_skill(triggerIds=[227], isEnable=False)
        set_skill(triggerIds=[228], isEnable=False)
        set_skill(triggerIds=[229], isEnable=False)
        set_skill(triggerIds=[230], isEnable=False)
        set_skill(triggerIds=[231], isEnable=False)
        set_skill(triggerIds=[232], isEnable=False)
        set_skill(triggerIds=[233], isEnable=False)
        set_skill(triggerIds=[234], isEnable=False)
        set_skill(triggerIds=[235], isEnable=False)
        set_skill(triggerIds=[236], isEnable=False)
        set_skill(triggerIds=[237], isEnable=False)
        set_skill(triggerIds=[238], isEnable=False)
        set_skill(triggerIds=[239], isEnable=False)
        set_skill(triggerIds=[240], isEnable=False)
        set_skill(triggerIds=[241], isEnable=False)
        set_skill(triggerIds=[242], isEnable=False)
        set_skill(triggerIds=[243], isEnable=False)
        set_skill(triggerIds=[244], isEnable=False)
        set_skill(triggerIds=[245], isEnable=False)
        set_skill(triggerIds=[246], isEnable=False)
        set_skill(triggerIds=[247], isEnable=False)
        set_skill(triggerIds=[248], isEnable=False)
        set_skill(triggerIds=[249], isEnable=False)
        set_skill(triggerIds=[250], isEnable=False)
        set_skill(triggerIds=[251], isEnable=False)
        set_skill(triggerIds=[252], isEnable=False)
        set_skill(triggerIds=[253], isEnable=False)
        set_skill(triggerIds=[254], isEnable=False)
        set_skill(triggerIds=[255], isEnable=False)
        set_skill(triggerIds=[256], isEnable=False)
        set_skill(triggerIds=[257], isEnable=False)
        set_skill(triggerIds=[258], isEnable=False)
        set_skill(triggerIds=[259], isEnable=False)
        set_skill(triggerIds=[260], isEnable=False)
        set_skill(triggerIds=[261], isEnable=False)
        set_skill(triggerIds=[262], isEnable=False)
        set_skill(triggerIds=[263], isEnable=False)
        set_skill(triggerIds=[264], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='35'):
            return 생존자수색05()
        if not user_detected(boxIds=[301]):
            return 모두탈락()


class 생존자수색05(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 한숨돌리기05()


class 한숨돌리기05(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2, gameName='UserMassive_Springbeach')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 우승자카메라연출()


class 우승자카메라연출(state.State):
    def on_enter(self):
        mini_game_camera_direction(boxId=301, cameraId=9001)
        play_system_sound_in_box(boxIds=[301], sound='ME_Mainprocess_Springbeach_15')
        set_event_ui(type=3, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__15$', arg3='5000', arg4='301')
        set_event_ui(type=4, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__16$', arg3='5000', arg4='303,304,305,306')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_local_camera(cameraId=9001, enable=False)
            return 보상단계()


class 보상단계(state.State):
    def on_enter(self):
        add_buff(boxIds=[301], skillId=70000132, level=1)
        add_buff(boxIds=[301], skillId=70000019, level=1) # 에레브의 축복
        mini_game_give_reward(winnerBoxId=301, contentType='UserOpenMiniGameExtraReward') # 1일 5회 추가 보너스
        end_mini_game(winnerBoxId=301, gameName='UserMassive_Springbeach')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 다리등장()


#  생존자없음 
class 모두탈락(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, gameName='UserMassive_Springbeach')
        end_mini_game(winnerBoxId=301, gameName='UserMassive_Springbeach')
        set_timer(timerId='40', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='40'):
            return 탈락멘트()


class 탈락멘트(state.State):
    def on_enter(self):
        set_timer(timerId='40', seconds=6)
        set_event_ui(type=5, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__21$', arg3='5000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='40'):
            return 다리등장()


#  마무리 
class 다리등장(state.State):
    def on_enter(self):
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_timer(timerId='41', seconds=10)
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624], visible=True)
        set_mesh(triggerIds=[651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677], visible=False)
        set_mesh(triggerIds=[701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832], visible=False)
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__22$', arg3='10000')
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_22')

    def on_tick(self) -> state.State:
        if time_expired(timerId='41'):
            return 유저이동()


class 유저이동(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')
        play_system_sound_in_box(sound='ME_Mainprocess_Springbeach_23')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=120000):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


#  패턴 목록_라운드1
class 스프링공격01_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_101()


class 게임진행1_101(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격02_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_102()


class 게임진행1_102(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격03_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_103()


class 게임진행1_103(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격04_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_104()


class 게임진행1_104(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격05_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_105()


class 게임진행1_105(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격06_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_106()


class 게임진행1_106(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격07_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_107()


class 게임진행1_107(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격08_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_108()


class 게임진행1_108(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격09_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_109()


class 게임진행1_109(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격10_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_110()


class 게임진행1_110(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격11_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_111()


class 게임진행1_111(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격12_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_112()


class 게임진행1_112(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격13_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_113()


class 게임진행1_113(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격14_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_114()


class 게임진행1_114(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격15_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_115()


class 게임진행1_115(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격16_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_116()


class 게임진행1_116(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격17_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_117()


class 게임진행1_117(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격18_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_118()


class 게임진행1_118(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격19_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_119()


class 게임진행1_119(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격20_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_120()


class 게임진행1_120(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격21_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_121()


class 게임진행1_121(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격22_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_122()


class 게임진행1_122(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격23_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_123()


class 게임진행1_123(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격24_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_124()


class 게임진행1_124(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격25_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_125()


class 게임진행1_125(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격26_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_126()


class 게임진행1_126(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격27_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_127()


class 게임진행1_127(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격28_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_128()


class 게임진행1_128(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격29_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_129()


class 게임진행1_129(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격30_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_130()


class 게임진행1_130(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격31_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_131()


class 게임진행1_131(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격32_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_132()


class 게임진행1_132(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격33_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_133()


class 게임진행1_133(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격34_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_134()


class 게임진행1_134(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격35_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_135()


class 게임진행1_135(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격36_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_136()


class 게임진행1_136(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격37_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_137()


class 게임진행1_137(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격38_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_138()


class 게임진행1_138(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격39_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_139()


class 게임진행1_139(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


class 스프링공격40_1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_140()


class 게임진행1_140(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지01()


#  패턴 목록_라운드2
class 스프링공격01_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_201()


class 게임진행1_201(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격02_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_202()


class 게임진행1_202(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격03_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_203()


class 게임진행1_203(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격04_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_204()


class 게임진행1_204(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=2)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격05_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_205()


class 게임진행1_205(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격06_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_206()


class 게임진행1_206(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격07_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_207()


class 게임진행1_207(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격08_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_208()


class 게임진행1_208(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격09_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_209()


class 게임진행1_209(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격10_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_210()


class 게임진행1_210(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격11_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_211()


class 게임진행1_211(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격12_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_212()


class 게임진행1_212(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격13_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_213()


class 게임진행1_213(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격14_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_214()


class 게임진행1_214(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격15_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_215()


class 게임진행1_215(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격16_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_216()


class 게임진행1_216(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격17_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_217()


class 게임진행1_217(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격18_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_218()


class 게임진행1_218(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격19_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_219()


class 게임진행1_219(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격20_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_220()


class 게임진행1_220(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격21_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_221()


class 게임진행1_221(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격22_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_222()


class 게임진행1_222(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격23_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_223()


class 게임진행1_223(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격24_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_224()


class 게임진행1_224(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격25_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_225()


class 게임진행1_225(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격26_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_226()


class 게임진행1_226(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격27_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_227()


class 게임진행1_227(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격28_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_228()


class 게임진행1_228(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격29_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_229()


class 게임진행1_229(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격30_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_230()


class 게임진행1_230(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격31_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_231()


class 게임진행1_231(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격32_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_232()


class 게임진행1_232(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격33_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_233()


class 게임진행1_233(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격34_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_234()


class 게임진행1_234(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격35_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_235()


class 게임진행1_235(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격36_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_236()


class 게임진행1_236(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격37_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_237()


class 게임진행1_237(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격38_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_238()


class 게임진행1_238(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격39_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_239()


class 게임진행1_239(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


class 스프링공격40_2(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_240()


class 게임진행1_240(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지02()


#  패턴 목록_라운드3
class 스프링공격01_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_301()


class 게임진행1_301(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격02_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_302()


class 게임진행1_302(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격03_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_303()


class 게임진행1_303(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격04_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_304()


class 게임진행1_304(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격05_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_305()


class 게임진행1_305(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격06_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_306()


class 게임진행1_306(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격07_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_307()


class 게임진행1_307(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격08_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_308()


class 게임진행1_308(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격09_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_309()


class 게임진행1_309(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격10_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_310()


class 게임진행1_310(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격11_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_311()


class 게임진행1_311(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격12_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_312()


class 게임진행1_312(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격13_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_313()


class 게임진행1_313(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격14_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_314()


class 게임진행1_314(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격15_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_315()


class 게임진행1_315(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격16_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_316()


class 게임진행1_316(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격17_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_317()


class 게임진행1_317(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격18_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_318()


class 게임진행1_318(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격19_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_319()


class 게임진행1_319(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격20_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_320()


class 게임진행1_320(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격21_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_321()


class 게임진행1_321(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격22_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_322()


class 게임진행1_322(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격23_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_323()


class 게임진행1_323(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격24_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_324()


class 게임진행1_324(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격25_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_325()


class 게임진행1_325(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격26_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_326()


class 게임진행1_326(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격27_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_327()


class 게임진행1_327(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격28_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_328()


class 게임진행1_328(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격29_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_329()


class 게임진행1_329(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격30_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_330()


class 게임진행1_330(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격31_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_331()


class 게임진행1_331(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격32_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_332()


class 게임진행1_332(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격33_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_333()


class 게임진행1_333(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격34_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_334()


class 게임진행1_334(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격35_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_335()


class 게임진행1_335(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격36_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_336()


class 게임진행1_336(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격37_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_337()


class 게임진행1_337(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격38_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_338()


class 게임진행1_338(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격39_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_339()


class 게임진행1_339(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


class 스프링공격40_3(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_340()


class 게임진행1_340(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지03()


#  패턴 목록_라운드4
class 스프링공격01_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_401()


class 게임진행1_401(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격02_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_402()


class 게임진행1_402(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격03_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_403()


class 게임진행1_403(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격04_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_404()


class 게임진행1_404(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격05_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_405()


class 게임진행1_405(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격06_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_406()


class 게임진행1_406(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격07_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_407()


class 게임진행1_407(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격08_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_408()


class 게임진행1_408(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격09_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_409()


class 게임진행1_409(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격10_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_410()


class 게임진행1_410(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격11_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_411()


class 게임진행1_411(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격12_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_412()


class 게임진행1_412(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격13_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_413()


class 게임진행1_413(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격14_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_414()


class 게임진행1_414(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격15_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_415()


class 게임진행1_415(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격16_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_416()


class 게임진행1_416(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격17_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_417()


class 게임진행1_417(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격18_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_418()


class 게임진행1_418(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격19_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_419()


class 게임진행1_419(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격20_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_420()


class 게임진행1_420(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격21_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_421()


class 게임진행1_421(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격22_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_422()


class 게임진행1_422(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격23_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_423()


class 게임진행1_423(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격24_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_424()


class 게임진행1_424(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격25_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_425()


class 게임진행1_425(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격26_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_426()


class 게임진행1_426(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격27_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_427()


class 게임진행1_427(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격28_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_428()


class 게임진행1_428(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격29_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_429()


class 게임진행1_429(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격30_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_430()


class 게임진행1_430(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격31_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_431()


class 게임진행1_431(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격32_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_432()


class 게임진행1_432(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격33_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_433()


class 게임진행1_433(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격34_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_434()


class 게임진행1_434(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격35_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_435()


class 게임진행1_435(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격36_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_436()


class 게임진행1_436(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격37_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_437()


class 게임진행1_437(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격38_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_438()


class 게임진행1_438(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격39_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_439()


class 게임진행1_439(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


class 스프링공격40_4(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_440()


class 게임진행1_440(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지04()


#  패턴 목록_라운드5
class 스프링공격01_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[105,106,107,108,117,118,119,120,129,130,131,132,137,138,139,140,141,142,143,144,145,150,151,152,153,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_501()


class 게임진행1_501(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격02_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,137,138,139,140,150,151,152,153], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_502()


class 게임진행1_502(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격03_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,109,110,111,112,113,114,115,116,121,122,123,124,129,130,131,132,141,142,143,144,145,154,155,156,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_503()


class 게임진행1_503(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격04_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,117,118,119,120,121,127,128,129,133,134,135,137,138,139,147,148,149,150,151,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_504()


class 게임진행1_504(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격05_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[104,105,108,109,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,140,141,145,146,153,154,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_505()


class 게임진행1_505(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격06_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,108,109,110,111,112,113,114,115,116,117,120,121,128,129,131,132,133,142,143,144,145,146,155,156,157,158,159,160,161], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_506()


class 게임진행1_506(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격07_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,111,112,115,116,117,118,119,120,121,122,127,128,129,130,131,132,133,134,137,138,143,148,149,150,151,156,157,158,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_507()


class 게임진행1_507(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격08_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[107,108,109,110,111,112,113,114,115,116,117,118,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,151,152,155,156], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_508()


class 게임진행1_508(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격09_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,115,116,117,118,119,122,124,125,127,130,131,132,133,134,136,137,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_509()


class 게임진행1_509(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격10_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,110,111,112,113,114,115,118,131,134,135,136,137,138,139,142,143,144,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_510()


class 게임진행1_510(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격11_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_511()


class 게임진행1_511(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격12_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,107,108,113,114,115,116,119,120,125,126,127,128,131,132,138,140,142,146,147,148,149,151,153,155,157,158,159,160], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_512()


class 게임진행1_512(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격13_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,105,107,109,111,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,145,147,149,151,153,155,157,159,161,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_513()


class 게임진행1_513(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격14_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,106,108,109,111,114,116,117,119,120,121,122,124,125,127,128,129,130,132,133,135,138,139,142,143,145,146,148,150,153,154,157,159,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_514()


class 게임진행1_514(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격15_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,109,110,111,112,115,116,117,118,119,120,123,124,125,126,127,128,131,132,133,134,137,138,140,141,143,144,145,148,149,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_515()


class 게임진행1_515(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격16_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,140,141,145,146,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_516()


class 게임진행1_516(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격17_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,119,120,121,122,125,126,127,128,129,130,131,132,135,136,138,139,140,142,143,146,147,148,149,151,152,153,155,156,157,158,159,160,161,162], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_517()


class 게임진행1_517(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격18_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,104,105,106,107,109,110,111,113,114,116,117,118,119,121,122,123,125,126,128,129,130,131,133,134,135,138,140,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_518()


class 게임진행1_518(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격19_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,138,139,142,143,144,145,146,147,148,150,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_519()


class 게임진행1_519(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격20_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,105,106,107,108,109,110,111,112,115,116,117,118,119,121,122,123,124,125,126,127,129,130,131,132,133,134,137,138,140,141,143,144,145,146,147,148,149,150,151,153,154,156,157,158,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_520()


class 게임진행1_520(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격21_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,111,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,140,141,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_521()


class 게임진행1_521(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격22_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,111,112,113,114,115,116,118,119,120,121,122,123,125,126,127,128,129,130,131,132,134,135,136,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,155,156,157,158,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_522()


class 게임진행1_522(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격23_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_523()


class 게임진행1_523(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격24_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,127,128,129,130,131,132,133,134,135,136,138,139,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_524()


class 게임진행1_524(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격25_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_525()


class 게임진행1_525(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격26_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,120,122,124,125,127,129,130,132,133,135,136,137,138,139,142,143,144,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_526()


class 게임진행1_526(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격27_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,117,120,121,122,123,124,125,126,127,130,132,133,134,135,136,137,138,139,140,141,142,143,145,146,148,149,150,151,152,153,154,155,156,157,158,159,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_527()


class 게임진행1_527(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격28_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,108,109,110,111,112,113,116,118,119,120,122,123,126,127,129,130,131,133,136,137,139,140,142,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_528()


class 게임진행1_528(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격29_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,109,110,112,113,115,117,118,119,120,122,124,125,127,129,130,131,132,134,136,137,138,143,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_529()


class 게임진행1_529(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격30_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,112,113,114,115,116,117,119,121,122,123,124,125,126,127,129,130,131,132,133,135,136,137,139,140,141,142,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_530()


class 게임진행1_530(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격31_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,113,115,116,117,118,119,120,121,123,124,125,126,128,129,130,131,132,133,134,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_531()


class 게임진행1_531(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격32_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,131,132,133,134,135,136,137,138,140,141,143,144,145,146,147,148,149,150,152,153,154,155,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_532()


class 게임진행1_532(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격33_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,105,106,107,108,109,111,112,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,145,146,147,148,149,150,151,152,153,154,156,157,158,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_533()


class 게임진행1_533(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격34_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,110,111,112,113,114,116,118,119,121,122,123,124,125,126,127,128,130,131,133,134,135,136,137,138,139,140,141,142,143,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_534()


class 게임진행1_534(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격35_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,116,117,118,122,123,126,127,128,129,130,131,132,133,134,136,137,138,139,140,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_535()


class 게임진행1_535(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격36_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_536()


class 게임진행1_536(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격37_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_537()


class 게임진행1_537(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격38_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_538()


class 게임진행1_538(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격39_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,133,135,136,137,138,139,140,141,142,144,145,146,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[201], isEnable=True)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[211], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[215], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[218], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[220], isEnable=True)
        set_skill(triggerIds=[221], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[238], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[250], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_539()


class 게임진행1_539(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


class 스프링공격40_5(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=2) # arg2는 시간 (초)
        set_breakable(triggerIds=[102,103,104,105,106,107,108,109,110,112,113,114,116,117,119,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,163,164], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)
        set_skill(triggerIds=[202], isEnable=True)
        set_skill(triggerIds=[203], isEnable=True)
        set_skill(triggerIds=[204], isEnable=True)
        set_skill(triggerIds=[205], isEnable=True)
        set_skill(triggerIds=[206], isEnable=True)
        set_skill(triggerIds=[207], isEnable=True)
        set_skill(triggerIds=[208], isEnable=True)
        set_skill(triggerIds=[209], isEnable=True)
        set_skill(triggerIds=[210], isEnable=True)
        set_skill(triggerIds=[212], isEnable=True)
        set_skill(triggerIds=[213], isEnable=True)
        set_skill(triggerIds=[214], isEnable=True)
        set_skill(triggerIds=[216], isEnable=True)
        set_skill(triggerIds=[217], isEnable=True)
        set_skill(triggerIds=[219], isEnable=True)
        set_skill(triggerIds=[222], isEnable=True)
        set_skill(triggerIds=[223], isEnable=True)
        set_skill(triggerIds=[224], isEnable=True)
        set_skill(triggerIds=[225], isEnable=True)
        set_skill(triggerIds=[226], isEnable=True)
        set_skill(triggerIds=[227], isEnable=True)
        set_skill(triggerIds=[228], isEnable=True)
        set_skill(triggerIds=[229], isEnable=True)
        set_skill(triggerIds=[230], isEnable=True)
        set_skill(triggerIds=[231], isEnable=True)
        set_skill(triggerIds=[232], isEnable=True)
        set_skill(triggerIds=[233], isEnable=True)
        set_skill(triggerIds=[234], isEnable=True)
        set_skill(triggerIds=[235], isEnable=True)
        set_skill(triggerIds=[236], isEnable=True)
        set_skill(triggerIds=[237], isEnable=True)
        set_skill(triggerIds=[239], isEnable=True)
        set_skill(triggerIds=[240], isEnable=True)
        set_skill(triggerIds=[241], isEnable=True)
        set_skill(triggerIds=[242], isEnable=True)
        set_skill(triggerIds=[243], isEnable=True)
        set_skill(triggerIds=[244], isEnable=True)
        set_skill(triggerIds=[245], isEnable=True)
        set_skill(triggerIds=[246], isEnable=True)
        set_skill(triggerIds=[247], isEnable=True)
        set_skill(triggerIds=[248], isEnable=True)
        set_skill(triggerIds=[249], isEnable=True)
        set_skill(triggerIds=[251], isEnable=True)
        set_skill(triggerIds=[252], isEnable=True)
        set_skill(triggerIds=[253], isEnable=True)
        set_skill(triggerIds=[254], isEnable=True)
        set_skill(triggerIds=[255], isEnable=True)
        set_skill(triggerIds=[256], isEnable=True)
        set_skill(triggerIds=[257], isEnable=True)
        set_skill(triggerIds=[258], isEnable=True)
        set_skill(triggerIds=[259], isEnable=True)
        set_skill(triggerIds=[260], isEnable=True)
        set_skill(triggerIds=[261], isEnable=True)
        set_skill(triggerIds=[262], isEnable=True)
        set_skill(triggerIds=[263], isEnable=True)
        set_skill(triggerIds=[264], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 게임진행1_540()


class 게임진행1_540(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)
        set_breakable(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 공격중지05()


