using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003472: Cathy Mart Lucky Wheel
/// </summary>
public class _11003472 : NpcScript {
    internal _11003472(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0710202510001866$ 
                // - Welcome! Pay 1 $item:30000869$ to spin $npc:11003472$!
                return true;
            case 30:
                // $script:0710202510001867$ functionID=1 
                // - Welcome! Pay me 5 $itemPlural:30000869$, and I'll let you spin the $npc:11003472$. How about it? Feeling lucky?
                switch (selection) {
                    // $script:0710202510001868$
                    // - Pay 5 $itemPlural:30000869$ to spin once.
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:0710202510001869$
                    // - Pay 50 $itemPlural:30000869$ to spin continuously.
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:0710202510001870$
                    // - Pay 500 $itemPlural:30000869$ to spin continuously.
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0710202510001871$ functionID=1 buttonSet=16 
                // - Spin the roulette for a chance to win great prizes!
                //   Come on, you know you want to!
                // $script:0710202510001872$ buttonSet=1 
                // - May Lady Luck blow you a kiss, $MyPCName$!
                return true;
            case 32:
                // $script:0710202510001873$ functionID=1 
                // - You don't have enough coins.
                //   Therefore, you need 5 <font color="#ffd200">$itemPlural:30000869$</font> to spin $npc:11003472$ once.
                return true;
            case 40:
                // $script:0710202510001874$ functionID=1 
                // - To take a spin on the $npc:11003472$, you need 5 <font color="#ffd200">$itemPlural:30000869$</font>. Clear the event dungeon to get $itemPlural:30000869$!
                // $script:0710202510001875$ 
                // - If you have $itemPlural:30000869$ to burn, be sure to come to $map:02000064$!
                return true;
            case 10:
                // $script:0710202510001876$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0710202510001877$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            case 100:
                // $script:0710202510001878$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
                // $script:0710202510001879$ buttonSet=17 
                // - Roulette spin number $rouletteCurrent$! Good luck!
                return true;
            default:
                return true;
        }
    }
}
