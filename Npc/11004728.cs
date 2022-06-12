using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004728: Hide-and-Seek Wheel
/// </summary>
public class _11004728 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:1010204110002256$
    // - Spin $npc:11004728$ for just 1 $item:30001442$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // functionID=1 
                // $script:1010204110002257$
                // - Give us 5 $itemPlural:30001442$ for a chance to spin the $npc:11004728$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:1010204110002258$
                    // - (Pay 5 $item:30001442$ for 1 spin.)
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                    // $script:1010204110002259$
                    // - (Pay 50 $itemPlural:30001442$ for a bunch of spins in a row!)
                    case 1:
                        // TODO: goto 10
                        // TODO: gotoFail 32
                        return -1;
                    // $script:1010204110002260$
                    // - (Pay 500 $itemPlural:30001442$ for a bunch of spins in a row!)
                    case 2:
                        // TODO: goto 100
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:1010204110002261$
                // - Wonderful! Are you ready to spin?
                return 31;
            case (31, 1):
                // $script:1010204110002262$
                // - Here's hoping Lady Luck's on your side!
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:1010204110002263$
                // - You don't have enough coins. You need 5 $itemPlural:30001442$ to spin the $npc:11004728$ once.
                return -1;
            case (40, 0):
                // functionID=1 
                // $script:1010204110002264$
                // - You need 5 $itemPlural:30001442$ to give the $npc:11004728$ a spin. Play Hide-and-Seek to get $itemPlural:30001442$!
                return 40;
            case (40, 1):
                // $script:1010204110002265$
                // - If you have $itemPlural:30001442$ to burn, be sure to come to $map:02000064$!
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:1010204110002266$
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                return 10;
            case (10, 1):
                // $script:1010204110002267$
                // - Spin number $rouletteCurrent$! Good luck!
                return -1;
            case (100, 0):
                // functionID=1 
                // $script:1010204110002268$
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                return 100;
            case (100, 1):
                // $script:1010204110002269$
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
