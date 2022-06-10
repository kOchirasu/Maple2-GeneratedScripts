using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001545: Bravos
/// </summary>
public class _11001545 : NpcScript {
    internal _11001545(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006113$ 
                // - Ugh. Now what?
                return true;
            case 10:
                // $script:0531170907006223$ 
                // - Hey! You know why they call me $npc:11001545[gender:0]$?
                switch (selection) {
                    // $script:0531170907006224$
                    // - No clue.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0531170907006225$ 
                // - 'Cause I'm so great I deserve a standing ovation! Haha! I can't believe you never heard of me. Anyway, you need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
                // $script:0607145407006336$ 
                // - Well what're you staring at? Did'ja have something to tell me, or do you just like the view?
                return true;
            default:
                return true;
        }
    }
}
