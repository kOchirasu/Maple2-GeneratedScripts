using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003551: 
/// </summary>
public class _11003551 : NpcScript {
    internal _11003551(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0902174710001914$ 
                // - Welcome! Pay 1 $item:30000878$ to spin $npc:11003551$!
                return true;
            case 30:
                // $script:0902174710001915$ functionID=1 
                // - Give us 3 $itemPlural:30000878$ for a chance to spin the $npc:11003551$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:0902174710001916$
                    // - (Pay 3 $item:30000878$ for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0902174710001917$
                    // - (Pay 30 $itemPlural:30000878$ for a bunch of spins in a row!)
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:0902174710001918$
                    // - (Pay 300 $itemPlural:30000878$ for a bunch of spins in a row!)
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0902174710001919$ functionID=1 buttonSet=16 
                // - Spin the roulette for a chance to win great prizes!
                //   Come on, you know you want to!
                // $script:0902174710001920$ buttonSet=1 
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return true;
            case 32:
                // $script:0902174710001921$ functionID=1 
                // - You don't have enough coins.
                //   Therefore, you need 3 <font color="#ffd200">$itemPlural:30000878$</font> to spin $npc:11003551$ once.
                return true;
            case 40:
                // $script:0902174710001922$ functionID=1 
                // - For one spin of $npcName:11003551$, you need 3 $itemPlural:30000878$. And guess what? You get $itemPlural:30000878$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating!
                // $script:0902174710001923$ 
                // - If you have $itemPlural:30000878$ to burn, be sure to come to $map:63000057$!
                return true;
            case 10:
                // $script:0902174710001924$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0902174710001925$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            case 100:
                // $script:0902174710001926$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0902174710001927$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            default:
                return true;
        }
    }
}
