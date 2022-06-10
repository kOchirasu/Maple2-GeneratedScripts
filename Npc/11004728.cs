using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004728: Hide-and-Seek Wheel
/// </summary>
public class _11004728 : NpcScript {
    internal _11004728(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010204110002256$ 
                // - Spin $npc:11004728$ for just 1 $item:30001442$! 
                return true;
            case 30:
                // $script:1010204110002257$ functionID=1 
                // - Give us 5 $itemPlural:30001442$ for a chance to spin the $npc:11004728$. How about it? Feeling lucky? 
                switch (selection) {
                    // $script:1010204110002258$
                    // - (Pay 5 $item:30001442$ for 1 spin.)
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                    // $script:1010204110002259$
                    // - (Pay 50 $itemPlural:30001442$ for a bunch of spins in a row!)
                    case 1:
                        Id = 0; // TODO: 10 | 32
                        return false;
                    // $script:1010204110002260$
                    // - (Pay 500 $itemPlural:30001442$ for a bunch of spins in a row!)
                    case 2:
                        Id = 0; // TODO: 100 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:1010204110002261$ functionID=1 buttonSet=16 
                // - Wonderful! Are you ready to spin? 
                // $script:1010204110002262$ buttonSet=1 
                // - Here's hoping Lady Luck's on your side! 
                return true;
            case 32:
                // $script:1010204110002263$ functionID=1 
                // - You don't have enough coins. You need 5 $itemPlural:30001442$ to spin the $npc:11004728$ once. 
                return true;
            case 40:
                // $script:1010204110002264$ functionID=1 
                // - You need 5 $itemPlural:30001442$ to give the $npc:11004728$ a spin. Play Hide-and-Seek to get $itemPlural:30001442$! 
                // $script:1010204110002265$ 
                // - If you have $itemPlural:30001442$ to burn, be sure to come to $map:02000064$! 
                return true;
            case 10:
                // $script:1010204110002266$ functionID=1 buttonSet=16 
                // - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:1010204110002267$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck! 
                return true;
            case 100:
                // $script:1010204110002268$ functionID=1 buttonSet=16 
                // - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$! 
                // $script:1010204110002269$ buttonSet=17 
                // - Spin number $rouletteCurrent$! Good luck! 
                return true;
            default:
                return true;
        }
    }
}
