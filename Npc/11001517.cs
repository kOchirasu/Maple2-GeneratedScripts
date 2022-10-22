using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001517: Lucky Wheel
/// </summary>
public class _11001517 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0204150510001434$
    // - Welcome, welcome!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0217184010001441$
                // - Would you like to spin the $npcName:11001517$?
                switch (selection) {
                    // $script:0217184010001442$
                    // - (Pay 50,000 mesos for 1 spin.)
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return 32;
                    // $script:0217184010001443$
                    // - (Pay 1 $item:30000522$ for 1 spin.)
                    case 1:
                        // TODO: goto 33
                        // TODO: gotoFail 34
                        return 34;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0217184010001444$
                // - Spin the wheel for a chance at great prizes! You know you want to.
                return 31;
            case (31, 1):
                // $script:0217184010001445$
                // - Here's hoping Lady Luck's on your side!
                return -1;
            case (32, 0):
                // $script:0217184010001446$
                // - It costs 50,000 mesos for a spin. If you don't have enough mesos, you can always use $itemPlural:30000522$ instead.
                return -1;
            case (33, 0):
                // functionID=1 
                // $script:0217184010001447$
                // - Spin the wheel for a chance at great prizes! You know you want to.
                return 33;
            case (33, 1):
                // $script:0217184010001448$
                // - Here's hoping Lady Luck's on your side!
                return -1;
            case (34, 0):
                // $script:0217184010001449$
                // - Spinning the roulette costs $itemPlural:30000522$. But don't fret! You can get 1 $item:30000522$ in your mailbox on weekdays and 5 of them on Saturdays and Sundays!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Roulette,
            (31, 1) => NpcTalkButton.Empty,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Roulette,
            (33, 1) => NpcTalkButton.Empty,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
