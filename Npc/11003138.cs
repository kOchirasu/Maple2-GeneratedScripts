using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003138: 
/// </summary>
public class _11003138 : NpcScript {
    internal _11003138(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 30:
                // $script:0212230610001824$ 
                // - Welcome!
Pay me 3 $itemPlural:30000745$, and I'll let you spin $npc:11003138$.
How about it? Feeling lucky? 
                switch (selection) {
                    // $script:0212230610001825$
                    // - Pay 3 $itemPlural:30000745$ to spin once.
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0212230610001826$
                    // - Pay 30 $itemPlural:30000745$ to spin 10 times.
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:0212230610001827$
                    // - Pay 300 $itemPlural:30000745$ to spin 100 times.
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0212230610001828$ functionID=1 buttonSet=16 
                // - Spin the wheel for a chance at great prizes! You know you want to. 
                // $script:0212230610001829$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side! 
                return true;
            case 32:
                // $script:0212230610001830$ 
                // - It seems like you're a little short. You need 3 $itemPlural:30000745$ to spin the $npc:11003138$. 
                return true;
            case 40:
                // $script:0212230610001831$ 
                // - To take a spin on the $npc:11003138$, you need 3 $itemPlural:30000745$. But there's good news! Starting April 25th, you can get 3 $itemPlural:30000745$ in your Mailbox once per day, right when you first log in! You'll also get bonus coins based on your cumulative playtime. As if that weren't enough, even more coins will be given to you if you join any of the various events we're hosting! 
                // $script:0212230610001832$ 
                // - If you have $itemPlural:30000745$ to burn, be sure to come to $map:02000360$! 
                return true;
            case 10:
                // $script:0212230610001833$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:0212230610001834$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck! 
                return true;
            case 100:
                // $script:0212230610001835$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:0212230610001836$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck! 
                return true;
            default:
                return true;
        }
    }
}
