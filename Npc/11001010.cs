using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001010: Thurman
/// </summary>
public class _11001010 : NpcScript {
    internal _11001010(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003446$ 
                // - What do I do now?
                return true;
            case 30:
                // $script:0831180407003449$ 
                // - Do you think the pirates will pay their tab if I ask nicely?
                return true;
            default:
                return true;
        }
    }
}
