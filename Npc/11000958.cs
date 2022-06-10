using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000958: Ruman
/// </summary>
public class _11000958 : NpcScript {
    internal _11000958(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003319$ 
                // - Aww, my poor scaredy-cats!
                return true;
            case 20:
                // $script:0831180407003321$ 
                // - My babies are as precious as children to me. Hee hee.
                return true;
            default:
                return true;
        }
    }
}
