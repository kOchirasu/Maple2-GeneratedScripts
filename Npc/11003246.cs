using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003246: Frey
/// </summary>
public class _11003246 : NpcScript {
    internal _11003246(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008152$ 
                // - $MyPCName$.
                return true;
            case 30:
                // $script:0403155707008153$ 
                // - In times like this, you need to keep your wits about you.
                return true;
            default:
                return true;
        }
    }
}
