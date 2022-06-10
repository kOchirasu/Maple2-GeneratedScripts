using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001953: Kay's Event Wheel
/// </summary>
public class _11001953 : NpcScript {
    internal _11001953(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1128172510001803$ 
                // - Spin $npc:11001953$ for just 1 $item:30000610$!
                return true;
            case 30:
                // $script:1128172510001804$ functionID=1 
                // - Give us 1 $item:30000610$ for a chance to spin $npc:11001953$. What do you say?
                switch (selection) {
                    // $script:1128172510001805$
                    // - (Pay 1 $item:30000610$ for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0612112710001842$
                    // - (Pay 10 $itemPlural:30000610$ for a bunch of spins in a row!)
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:0612112710001843$
                    // - (Pay 100 $itemPlural:30000610$ for a bunch of spins in a row!)
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:1128172510001806$ functionID=1 buttonSet=16 
                // - Spin the wheel for a chance at great prizes! You know you want to.
                // $script:1128172510001807$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side!
                return true;
            case 32:
                // $script:1128172510001808$ functionID=1 
                // - It looks like you don't have any $itemPlural:30000610$. You need at least 1 to spin $npc:11001953$!
                return true;
            case 40:
                // $script:1128172510001809$ functionID=1 
                // - You need at least 1 $item:30000610$ to spin $npc:11001953$. You know you can get $itemPlural:30000610$ by playing MC Kay's games, right?
                // $script:1128172510001810$ 
                // - If you have $itemPlural:30000610$ to burn, be sure to come to $map:02000064$!
                return true;
            case 10:
                // $script:0612103010001838$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0612103010001839$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck!
                return true;
            case 100:
                // $script:0612103010001840$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0612103010001841$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck!
                return true;
            default:
                return true;
        }
    }
}
