using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000543: Wayne
/// </summary>
public class _11000543 : NpcScript {
    internal _11000543(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002314$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407002316$ 
                // - Safety is the primary concern for folks who work in places like this.
                return true;
            default:
                return true;
        }
    }
}
