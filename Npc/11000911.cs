using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000911: Manns
/// </summary>
public class _11000911 : NpcScript {
    internal _11000911(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003275$ 
                // - I don't want any questions.
                return true;
            case 20:
                // $script:0831180407003277$ 
                // - Please don't talk to me. I'm in the middle of doing the worst thing I can imagine.
                return true;
            default:
                return true;
        }
    }
}
