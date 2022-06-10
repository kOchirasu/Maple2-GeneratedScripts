using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003511: Premium Lucky Wheel
/// </summary>
public class _11003511 : NpcScript {
    internal _11003511(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809174410001880$ 
                // - Welcome! Pay 1 $item:30000875$ to spin the $npcName:11003511$!
                return true;
            case 30:
                // $script:0809174410001881$ functionID=1 
                // - Welcome! Pay me 5 $itemPlural:30000875$ and I'll let you spin the $npc:11003511$! How about it? Feeling lucky?
                switch (selection) {
                    // $script:0809174410001882$
                    // - Pay 5 $itemPlural:30000875$ to spin once.
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0809174410001883$
                    // - Pay 50 $itemPlural:30000875$ to spin continuously.
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:0809174410001884$
                    // - Pay 500 $itemPlural:30000875$ to spin continuously.
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0809174410001885$ functionID=1 buttonSet=16 
                // - Spin the roulette for a chance to win great prizes! Come on, you know you want to!
                // $script:0809174410001886$ buttonSet=1 
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return true;
            case 32:
                // $script:0809174410001887$ functionID=1 
                // - You don't have enough coins. You need 5 $itemPlural:30000875$ to spin the $npc:11003511$ once.
                return true;
            case 40:
                // $script:0809174410001888$ functionID=1 
                // - To spin the $npc:11003511$, you need 5 $itemPlural:30000875$. Clear a premium dungeon to get $itemPlural:30000875$.
                // $script:0809174410001889$ 
                // - If you have $itemPlural:30000875$ to burn, be sure to come to $map:02000064$!
                return true;
            case 10:
                // $script:0809174410001890$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0809174410001891$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            case 100:
                // $script:0809174410001892$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0809174410001893$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            default:
                return true;
        }
    }
}