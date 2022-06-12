using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003511: Premium Lucky Wheel
/// </summary>
public class _11003511 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0809174410001880$
    // - Welcome! Pay 1 $item:30000875$ to spin the $npcName:11003511$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // functionID=1 
                // $script:0809174410001881$
                // - Welcome! Pay me 5 $itemPlural:30000875$ and I'll let you spin the $npc:11003511$! How about it? Feeling lucky?
                switch (selection) {
                    // $script:0809174410001882$
                    // - Pay 5 $itemPlural:30000875$ to spin once.
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0809174410001883$
                    // - Pay 50 $itemPlural:30000875$ to spin continuously.
                    case 1:
                        // TODO: goto 10
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0809174410001884$
                    // - Pay 500 $itemPlural:30000875$ to spin continuously.
                    case 2:
                        // TODO: goto 100
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0809174410001885$
                // - Spin the roulette for a chance to win great prizes! Come on, you know you want to!
                return 31;
            case (31, 1):
                // $script:0809174410001886$
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:0809174410001887$
                // - You don't have enough coins. You need 5 $itemPlural:30000875$ to spin the $npc:11003511$ once.
                return -1;
            case (40, 0):
                // functionID=1 
                // $script:0809174410001888$
                // - To spin the $npc:11003511$, you need 5 $itemPlural:30000875$. Clear a premium dungeon to get $itemPlural:30000875$.
                return 40;
            case (40, 1):
                // $script:0809174410001889$
                // - If you have $itemPlural:30000875$ to burn, be sure to come to $map:02000064$!
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0809174410001890$
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                return 10;
            case (10, 1):
                // $script:0809174410001891$
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return -1;
            case (100, 0):
                // functionID=1 
                // $script:0809174410001892$
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                return 100;
            case (100, 1):
                // $script:0809174410001893$
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
