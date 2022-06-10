using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000096: Deke
/// </summary>
public class _11000096 : NpcScript {
    internal _11000096(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000375$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000378$ 
                // - I sailed here with my girlfriend, $npc:11000151[gender:1]$. We're going to check out the Empress's court. 
                switch (selection) {
                    // $script:0831180407000379$
                    // - So where is she?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000380$ 
                // - I'm sure she's around here somewhere. She got off before I did. Man, she was so excited, she pushed through the crowd and ran ashore. Guess she didn't notice she left me behind! Ha, ha... 
                return true;
            case 40:
                // $script:1219181807005430$ 
                // - We finally made it to $map:02000062$! My lady and I are gonna have so much fun! 
                return true;
            case 50:
                // $script:0809153207007162$ 
                // - We finally made it to $map:02000062$! My lady and I are gonna have so much fun! 
                return true;
            default:
                return true;
        }
    }
}
