using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003250: Asimov
/// </summary>
public class _11003250 : NpcScript {
    internal _11003250(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008167$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0403155707008168$ 
                // - I've been waiting for you. 
                return true;
            default:
                return true;
        }
    }
}
