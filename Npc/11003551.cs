using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003551: 
/// </summary>
public class _11003551 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0902174710001914$
    // - Welcome! Pay 1 $item:30000878$ to spin $npc:11003551$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // functionID=1 
                // $script:0902174710001915$
                // - Give us 3 $itemPlural:30000878$ for a chance to spin the $npc:11003551$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:0902174710001916$
                    // - (Pay 3 $item:30000878$ for 1 spin.)
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0902174710001917$
                    // - (Pay 30 $itemPlural:30000878$ for a bunch of spins in a row!)
                    case 1:
                        // TODO: goto 10
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0902174710001918$
                    // - (Pay 300 $itemPlural:30000878$ for a bunch of spins in a row!)
                    case 2:
                        // TODO: goto 100
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0902174710001919$
                // - Spin the roulette for a chance to win great prizes!
                //   Come on, you know you want to!
                return 31;
            case (31, 1):
                // $script:0902174710001920$
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:0902174710001921$
                // - You don't have enough coins.
                //   Therefore, you need 3 <font color="#ffd200">$itemPlural:30000878$</font> to spin $npc:11003551$ once.
                return -1;
            case (40, 0):
                // functionID=1 
                // $script:0902174710001922$
                // - For one spin of $npcName:11003551$, you need 3 $itemPlural:30000878$. And guess what? You get $itemPlural:30000878$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating!
                return 40;
            case (40, 1):
                // $script:0902174710001923$
                // - If you have $itemPlural:30000878$ to burn, be sure to come to $map:63000057$!
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0902174710001924$
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                return 10;
            case (10, 1):
                // $script:0902174710001925$
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return -1;
            case (100, 0):
                // functionID=1 
                // $script:0902174710001926$
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                return 100;
            case (100, 1):
                // $script:0902174710001927$
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
