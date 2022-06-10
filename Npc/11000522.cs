using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000522: Lennon
/// </summary>
public class _11000522 : NpcScript {
    internal _11000522(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002231$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0831180407002233$ 
                // - Ugh... 
                return true;
            default:
                return true;
        }
    }
}
