using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000245: Cooper
/// </summary>
public class _11000245 : NpcScript {
    internal _11000245(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001043$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407001045$ 
                // - Safety is the primary concern for folks who work in places like this.
                return true;
            default:
                return true;
        }
    }
}
