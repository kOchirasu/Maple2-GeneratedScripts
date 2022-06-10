using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003688: 
/// </summary>
public class _11003688 : NpcScript {
    internal _11003688(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1110142010001930$ 
                // - Spin $npc:11003688$ for just 1 $item:30001010$! 
                return true;
            case 30:
                // $script:1110142010001931$ functionID=1 
                // - Give us 3 $itemPlural:30001010$ for a chance to spin the $npc:11003688$. How about it? Feeling lucky? 
                switch (selection) {
                    // $script:1110142010001932$
                    // - (Pay 3 $item:30001010$ for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:1110142010001933$
                    // - (Pay 30 $itemPlural:30001010$ for a bunch of spins in a row!)
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:1110142010001934$
                    // - (Pay 300 $itemPlural:30001010$ for a bunch of spins in a row!)
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:1110142010001935$ functionID=1 buttonSet=16 
                // - Spin the wheel for a chance at great prizes! You know you want to. 
                // $script:1110142010001936$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side! 
                return true;
            case 32:
                // $script:1110142010001937$ functionID=1 
                // - You don't have enough coins. You need 3 $itemPlural:30001010$ to spin the $npc:11003688$ once. 
                return true;
            case 40:
                // $script:1110142010001938$ functionID=1 
                // - For one spin of $npcName:11003688$, you need 3 $itemPlural:30001010$. And guess what? You get $itemPlural:30001010$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating! 
                // $script:1110142010001939$ 
                // - If you have $itemPlural:30001010$ to burn, be sure to come to $map:63000057$! 
                return true;
            case 10:
                // $script:1110142010001940$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:1110142010001941$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck! 
                return true;
            case 100:
                // $script:1110142010001942$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:1110142010001943$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck! 
                return true;
            default:
                return true;
        }
    }
}
