using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001709: Tinchai
/// </summary>
public class _11001709 : NpcScript {
    internal _11001709(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006961$ 
                // - Mm? Do you have something to say?
                return true;
            case 30:
                // $script:0728024507006989$ 
                // - I think there's more going on here than we realize. It's at times like this we have to keep a clear head. Got it?
                return true;
            default:
                return true;
        }
    }
}
