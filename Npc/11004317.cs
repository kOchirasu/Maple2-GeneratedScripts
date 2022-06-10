using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004317: Maple Spin
/// </summary>
public class _11004317 : NpcScript {
    internal _11004317(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1001153510002189$ 
                // - Spin $npc:11004317$ for just 1 $item:30001202$! 
                return true;
            case 30:
                // $script:1001153510002190$ functionID=1 
                // - Give us 1 $item:30001202$ for a chance to spin the $npc:11004317$. How about it? Feeling lucky? 
                switch (selection) {
                    // $script:1001153510002191$
                    // - (Pay 1 $item:30001202$ for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:1001153510002192$
                    // - (Pay 10 $itemPlural:30001202$ for a bunch of spins in a row!)
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:1001153510002193$
                    // - (Pay 100 $itemPlural:30001202$ for a bunch of spins in a row!)
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:1001153510002194$ functionID=1 buttonSet=16 
                // - Wonderful! Are you ready to spin? 
                // $script:1001153510002195$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side! 
                return true;
            case 32:
                // $script:1001153510002196$ functionID=1 
                // - You don't have enough coins. You need 1 $itemPlural:30001202$ to spin the $npc:11004317$ once. 
                return true;
            case 40:
                // $script:1001153510002197$ functionID=1 
                // - You need at least 1 $item:30001202$ to spin $npcName:11004317$. And you can get $itemPlural:30001202$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating! 
                // $script:1001153510002198$ 
                // - If you have $itemPlural:30001202$ to burn, be sure to come to $map:63000064$! 
                return true;
            case 10:
                // $script:1001153510002199$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:1001153510002200$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck! 
                return true;
            case 100:
                // $script:1001153510002201$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:1001153510002202$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck! 
                return true;
            default:
                return true;
        }
    }
}
