using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000696: Countless Steps
/// </summary>
public class _11000696 : NpcScript {
    internal _11000696(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002810$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407002812$ 
                // - I keep having nightmares. They wake me up all night... 
                return true;
            default:
                return true;
        }
    }
}
