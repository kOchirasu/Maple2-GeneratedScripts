using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000365: Luchen
/// </summary>
public class _11000365 : NpcScript {
    internal _11000365(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001508$ 
                // - Shush! What is it?
                return true;
            case 30:
                // $script:0831180407001510$ 
                // - Shush! Please leave quietly. I'm done for if they find out I'm here. 
                return true;
            default:
                return true;
        }
    }
}
