using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000298: Yord
/// </summary>
public class _11000298 : NpcScript {
    internal _11000298(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001185$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0831180407001187$ 
                // - What are you doing here? Traveling? I wish I could go on adventures too.
                return true;
            default:
                return true;
        }
    }
}
