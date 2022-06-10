using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000977: Kunbasha
/// </summary>
public class _11000977 : NpcScript {
    internal _11000977(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003379$ 
                // - What's a human doing in a place like this?
                return true;
            case 20:
                // $script:0831180407003381$ 
                // - Only we kunkun can feel the flow of nature and foretell the weather. 
                return true;
            default:
                return true;
        }
    }
}
