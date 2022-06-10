using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003386: 2nd Anniversary Wheel of Joy
/// </summary>
public class _11003386 : NpcScript {
    internal _11003386(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622191110001844$ 
                // - Welcome! Pay 1 $item:30000782$ to spin $npc:11003386$! 
                return true;
            case 30:
                // $script:0622191110001845$ functionID=1 
                // - Welcome! Pay me 5 $itemPlural:30000782$, and I'll let you spin the $npcName:11003386$. How about it? Feeling lucky? 
                switch (selection) {
                    // $script:0622191110001846$
                    // - Pay 5 $itemPlural:30000782$ to spin once.
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0622191110001847$
                    // - Pay 50 $itemPlural:30000782$ to spin continuously.
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:0622191110001848$
                    // - Pay 500 $itemPlural:30000782$ to spin continuously.
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0622191110001849$ functionID=1 buttonSet=16 
                // - Spin the roulette for a chance to win great prizes!
Come on, you know you want to! 
                // $script:0622191110001850$ buttonSet=1 
                // - May Lady Luck blow you a kiss, $MyPCName$! 
                return true;
            case 32:
                // $script:0622191110001851$ functionID=1 
                // - You don't have enough coins.
Therefore, you need 5 <font color="#ffd200">$itemPlural:30000782$</font> to spin $npc:11003386$ once. 
                return true;
            case 40:
                // $script:0622191110001852$ functionID=1 
                // - For one spin of $npcName:11003386$, you need 5 $itemPlural:30000782$. And guess what? You get $itemPlural:30000782$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating! 
                // $script:0622191110001853$ 
                // - If you have $itemPlural:30000782$ to burn, be sure to come to $map:63000055$! 
                return true;
            case 10:
                // $script:0622191110001854$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:0622191110001855$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck! 
                return true;
            case 100:
                // $script:0622191110001856$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:0622191110001857$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck! 
                return true;
            default:
                return true;
        }
    }
}
