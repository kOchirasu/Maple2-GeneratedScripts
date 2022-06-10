using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000114: JJ
/// </summary>
public class _11000114 : NpcScript {
    internal _11000114(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000477$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:0831180407000478$ 
                // - What if $map:02000062$ and $map:02000001$ and everything else in the world collapses? 
                switch (selection) {
                    // $script:0831180407000479$
                    // - Don't worry.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180407000480$ 
                // - Really, $MyPCName$? Looking into this giant pit of doom doesn't fill you with the least little bit of doubt? 
                return true;
            default:
                return true;
        }
    }
}
