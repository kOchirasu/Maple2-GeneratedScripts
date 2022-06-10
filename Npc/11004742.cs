using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004742: 
/// </summary>
public class _11004742 : NpcScript {
    internal _11004742(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1024162710002270$ 
                // - Spin $npc:11004742$ for just 1 $item:30001446$!
                return true;
            case 30:
                // $script:1024162710002271$ functionID=1 
                // - Give us 2 $itemPlural:30001446$ for a chance to spin the $npc:11004742$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:1024162710002272$
                    // - (Pay 2 $item:30001446$ for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:1024162710002273$
                    // - (Pay 20 $itemPlural:30001446$ for a bunch of spins in a row!)
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:1024162710002274$
                    // - (Pay 200 $itemPlural:30001446$ for a bunch of spins in a row!)
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:1024162710002275$ functionID=1 buttonSet=16 
                // - Wonderful! Are you ready to spin?
                // $script:1024162710002276$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side!
                return true;
            case 32:
                // $script:1024162710002277$ functionID=1 
                // - You don't have enough coins. You need 2 $itemPlural:30001446$ to spin the $npc:11004742$ once.
                return true;
            case 40:
                // $script:1024162710002278$ functionID=1 
                // - You need 2 $itemPlural:30001446$ to give the $npc:11004742$ a spin. Play Hide-and-Seek to get $itemPlural:30001446$!
                // $script:1024162710002279$ 
                // - If you have $itemPlural:30001446$ to burn, be sure to come to $map:02000064$!
                return true;
            case 10:
                // $script:1024162710002280$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:1024162710002281$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck!
                return true;
            case 100:
                // $script:1024162710002282$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:1024162710002283$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck!
                return true;
            default:
                return true;
        }
    }
}
