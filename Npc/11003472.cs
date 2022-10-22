using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003472: Cathy Mart Lucky Wheel
/// </summary>
public class _11003472 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0710202510001866$
    // - Welcome! Pay 1 $item:30000869$ to spin $npc:11003472$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // functionID=1 
                // $script:0710202510001867$
                // - Welcome! Pay me 5 $itemPlural:30000869$, and I'll let you spin the $npc:11003472$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:0710202510001868$
                    // - Pay 5 $itemPlural:30000869$ to spin once.
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return 32;
                    // $script:0710202510001869$
                    // - Pay 50 $itemPlural:30000869$ to spin continuously.
                    case 1:
                        // TODO: goto 10
                        // TODO: gotoFail 32
                        return 32;
                    // $script:0710202510001870$
                    // - Pay 500 $itemPlural:30000869$ to spin continuously.
                    case 2:
                        // TODO: goto 100
                        // TODO: gotoFail 32
                        return 32;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0710202510001871$
                // - Spin the roulette for a chance to win great prizes!
                //   Come on, you know you want to!
                return 31;
            case (31, 1):
                // $script:0710202510001872$
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:0710202510001873$
                // - You don't have enough coins.
                //   Therefore, you need 5 <font color="#ffd200">$itemPlural:30000869$</font> to spin $npc:11003472$ once.
                return -1;
            case (40, 0):
                // functionID=1 
                // $script:0710202510001874$
                // - To take a spin on the $npc:11003472$, you need 5 <font color="#ffd200">$itemPlural:30000869$</font>. Clear the event dungeon to get $itemPlural:30000869$!
                return 40;
            case (40, 1):
                // $script:0710202510001875$
                // - If you have $itemPlural:30000869$ to burn, be sure to come to $map:02000064$!
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0710202510001876$
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                return 10;
            case (10, 1):
                // $script:0710202510001877$
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return -1;
            case (100, 0):
                // functionID=1 
                // $script:0710202510001878$
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                return 100;
            case (100, 1):
                // $script:0710202510001879$
                // - Roulette spin number $rouletteCurrent$! Good luck!
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
