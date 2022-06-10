using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000152: Mary
/// </summary>
public class _11000152 : NpcScript {
    internal _11000152(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000647$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000649$ 
                // - Everyone's in a festive mood because of the court, and they're not even on the mainland where the court is being held. I wonder how excited the mainlanders must be!
                return true;
            default:
                return true;
        }
    }
}
