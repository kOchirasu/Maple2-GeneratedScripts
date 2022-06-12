using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004317: Maple Spin
/// </summary>
public class _11004317 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:1001153510002189$
    // - Spin $npc:11004317$ for just 1 $item:30001202$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // functionID=1 
                // $script:1001153510002190$
                // - Give us 1 $item:30001202$ for a chance to spin the $npc:11004317$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:1001153510002191$
                    // - (Pay 1 $item:30001202$ for 1 spin.)
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                    // $script:1001153510002192$
                    // - (Pay 10 $itemPlural:30001202$ for a bunch of spins in a row!)
                    case 1:
                        // TODO: goto 10
                        // TODO: gotoFail 32
                        return -1;
                    // $script:1001153510002193$
                    // - (Pay 100 $itemPlural:30001202$ for a bunch of spins in a row!)
                    case 2:
                        // TODO: goto 100
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:1001153510002194$
                // - Wonderful! Are you ready to spin?
                return 31;
            case (31, 1):
                // $script:1001153510002195$
                // - Here's hoping Lady Luck's on your side!
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:1001153510002196$
                // - You don't have enough coins. You need 1 $itemPlural:30001202$ to spin the $npc:11004317$ once.
                return -1;
            case (40, 0):
                // functionID=1 
                // $script:1001153510002197$
                // - You need at least 1 $item:30001202$ to spin $npcName:11004317$. And you can get $itemPlural:30001202$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating!
                return 40;
            case (40, 1):
                // $script:1001153510002198$
                // - If you have $itemPlural:30001202$ to burn, be sure to come to $map:63000064$!
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:1001153510002199$
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                return 10;
            case (10, 1):
                // $script:1001153510002200$
                // - Spin number $rouletteCurrent$! Good luck!
                return -1;
            case (100, 0):
                // functionID=1 
                // $script:1001153510002201$
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                return 100;
            case (100, 1):
                // $script:1001153510002202$
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
