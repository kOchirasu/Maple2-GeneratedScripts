using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001654: Festival Lucky Wheel
/// </summary>
public class _11001654 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0615152810001560$
    // - Spend $itemPlural:30000554$ to spin the $npc:11001654$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0615152810001561$
                // - Give us 3 $itemPlural:30000554$ for a chance to spin the $npc:11001654$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:0620113310001566$
                    // - (Pay 3 $itemPlural:30000554$ for 1 spin.)
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0125175010001818$
                    // - Pay 30 $itemPlural:30000554$ to spin 10 times.
                    case 1:
                        // TODO: goto 10
                        // TODO: gotoFail 32
                        return -1;
                    // $script:0125175010001819$
                    // - Pay 300 $itemPlural:30000554$ to spin 100 times.
                    case 2:
                        // TODO: goto 100
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 
                // $script:0615152810001562$
                // - Spin the wheel for a chance at great prizes! You know you want to.
                return 31;
            case (31, 1):
                // $script:0615152810001563$
                // - Here's hoping Lady Luck's on your side!
                return -1;
            case (32, 0):
                // $script:0620113310001567$
                // - It seems like you're a little short. You need 3 $itemPlural:30000554$ to spin the $npc:11001654$.
                return -1;
            case (40, 0):
                // $script:0615152810001564$
                // - For 1 spin of the $npcName:11001654$, you need 3 $itemPlural:30000554$. You'll get 3 $itemPlural:30000554$ in your mailbox every day just for logging in. You'll also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also award coins for joining in!
                return 40;
            case (40, 1):
                // $script:0615152810001565$
                // - If you have $itemPlural:30000554$ to burn, be sure to come to $map:63000032$!
                return -1;
            case (10, 0):
                // functionID=1 
                // $script:0125175010001820$
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                return 10;
            case (10, 1):
                // $script:0125175010001821$
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return -1;
            case (100, 0):
                // functionID=1 
                // $script:0125175010001822$
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                return 100;
            case (100, 1):
                // $script:0125175010001823$
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
