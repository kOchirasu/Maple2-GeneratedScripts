using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000667: Lando
/// </summary>
public class _11000667 : NpcScript {
    internal _11000667(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002704$ 
                // - WHAT?!
                return true;
            case 30:
                // $script:0831180407002707$ 
                // - Mm? What? 
                switch (selection) {
                    // $script:0831180407002708$
                    // - What are you doing?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407002709$ 
                // - You're a curious sort, aren't you? As the old saying goes, ignorance is bliss.
                // $script:0831180407002710$ 
                // - Don't stick your nose where it doesn't belong.
                return true;
            default:
                return true;
        }
    }
}
