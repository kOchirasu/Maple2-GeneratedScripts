using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001953: Kay's Event Wheel
/// </summary>
public class _11001953 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:1128172510001803$
    // - Spin $npc:11001953$ for just 1 $item:30000610$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // functionID=1 
                // $script:1128172510001804$
                // - Give us 1 $item:30000610$ for a chance to spin $npc:11001953$. What do you say?
                switch (selection) {
                    // $script:1128172510001805$
                    // - (Pay 1 $item:30000610$ for 1 spin.)
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0612112710001842$
                    // - (Pay 10 $itemPlural:30000610$ for a bunch of spins in a row!)
                    case 1:
                        // TODO: goto 10
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0612112710001843$
                    // - (Pay 100 $itemPlural:30000610$ for a bunch of spins in a row!)
                    case 2:
                        // TODO: goto 100
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:1128172510001806$
                // - Spin the wheel for a chance at great prizes! You know you want to.
                return 31;
            case (31, 1):
                // $script:1128172510001807$
                // - Here's hoping Lady Luck's on your side!
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:1128172510001808$
                // - It looks like you don't have any $itemPlural:30000610$. You need at least 1 to spin $npc:11001953$!
                return -1;
            case (40, 0):
                // functionID=1 
                // $script:1128172510001809$
                // - You need at least 1 $item:30000610$ to spin $npc:11001953$. You know you can get $itemPlural:30000610$ by playing MC Kay's games, right?
                return 40;
            case (40, 1):
                // $script:1128172510001810$
                // - If you have $itemPlural:30000610$ to burn, be sure to come to $map:02000064$!
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0612103010001838$
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                return 10;
            case (10, 1):
                // $script:0612103010001839$
                // - Spin number $rouletteCurrent$! Good luck!
                return -1;
            case (100, 0):
                // functionID=1 
                // $script:0612103010001840$
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                return 100;
            case (100, 1):
                // $script:0612103010001841$
                // - Spin number $rouletteCurrent$! Good luck!
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
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            (10, 0) => NpcTalkButton.Roulette,
            (10, 1) => NpcTalkButton.RouletteSkip,
            (100, 0) => NpcTalkButton.Roulette,
            (100, 1) => NpcTalkButton.RouletteSkip,
            _ => NpcTalkButton.None,
        };
    }
}
