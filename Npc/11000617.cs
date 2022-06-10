using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000617: Marmut
/// </summary>
public class _11000617 : NpcScript {
    internal _11000617(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002520$ 
                // - This is troublesome...
                return true;
            case 20:
                // $script:0831180407002522$ 
                // - Hmph, I can't believe I have to investigate this!
                return true;
            default:
                return true;
        }
    }
}
