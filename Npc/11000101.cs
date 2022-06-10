using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000101: Ray
/// </summary>
public class _11000101 : NpcScript {
    internal _11000101(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000396$ 
                // - Yo, man! Wassup!
                return true;
            case 20:
                // $script:0831180407000398$ 
                // - Hey yo, do you know what hip-hop represents?
                return true;
            default:
                return true;
        }
    }
}
