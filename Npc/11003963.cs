using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003963: Runeblade
/// </summary>
public class _11003963 : NpcScript {
    internal _11003963(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010017$ 
                // - Are you versed in the way of the blade?
                return true;
            case 20:
                // $script:0614143707010018$ 
                // - I'd be grateful for the opportunity to speak with a peer...
                return true;
            default:
                return true;
        }
    }
}
