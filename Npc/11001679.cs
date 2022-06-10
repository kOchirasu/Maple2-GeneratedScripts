using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001679: Bravos
/// </summary>
public class _11001679 : NpcScript {
    internal _11001679(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006447$ 
                // - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck. 
                return true;
            case 30:
                // $script:0629000607006450$ 
                // - Do you know why I'm called $npcName:11001545[gender:0]$? 
                switch (selection) {
                    // $script:0629000607006451$
                    // - You want to ask me that? Right now?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0629000607006453$ 
                // - You're no fun. Forget it. 
                switch (selection) {
                    // $script:0706165507006639$
                    // - How are you feeling?
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:0629000607006454$ 
                // - Wh-what? You worried about me? Don't! Look... You're giving me goosebumps! 
                // $script:0629000607006456$ 
                // - What's with the intense stare? Spit it out or sc-scram!
<font color="#909090">(He's blushing.)</font> 
                return true;
            default:
                return true;
        }
    }
}
