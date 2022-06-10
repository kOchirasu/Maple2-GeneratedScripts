using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000080: Mimi
/// </summary>
public class _11000080 : NpcScript {
    internal _11000080(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000368$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000371$ 
                // - This place is connected to $map:02000001$ by the great Royal Road. Just stay on it, and you'll be there in no time.
                return true;
            default:
                return true;
        }
    }
}
