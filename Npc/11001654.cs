using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001654: Festival Lucky Wheel
/// </summary>
public class _11001654 : NpcScript {
    internal _11001654(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0615152810001560$ 
                // - Spend $itemPlural:30000554$ to spin the $npc:11001654$!
                return true;
            case 30:
                // $script:0615152810001561$ 
                // - Give us 3 $itemPlural:30000554$ for a chance to spin the $npc:11001654$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:0620113310001566$
                    // - (Pay 3 $itemPlural:30000554$ for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0125175010001818$
                    // - Pay 30 $itemPlural:30000554$ to spin 10 times.
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:0125175010001819$
                    // - Pay 300 $itemPlural:30000554$ to spin 100 times.
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0615152810001562$ functionID=1 buttonSet=16 
                // - Spin the wheel for a chance at great prizes! You know you want to.
                // $script:0615152810001563$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side!
                return true;
            case 32:
                // $script:0620113310001567$ 
                // - It seems like you're a little short. You need 3 $itemPlural:30000554$ to spin the $npc:11001654$.
                return true;
            case 40:
                // $script:0615152810001564$ 
                // - For 1 spin of the $npcName:11001654$, you need 3 $itemPlural:30000554$. You'll get 3 $itemPlural:30000554$ in your mailbox every day just for logging in. You'll also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also award coins for joining in!
                // $script:0615152810001565$ 
                // - If you have $itemPlural:30000554$ to burn, be sure to come to $map:63000032$!
                return true;
            case 10:
                // $script:0125175010001820$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0125175010001821$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            case 100:
                // $script:0125175010001822$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0125175010001823$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            default:
                return true;
        }
    }
}
