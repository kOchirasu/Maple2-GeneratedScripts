using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000885: Rabiette
/// </summary>
public class _11000885 : NpcScript {
    internal _11000885(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003245$ 
                // - Where am I right now? Sniff, sniff... 
                return true;
            case 30:
                // $script:0831180407003248$ 
                // - Sniff... Human, have you been to the moon? There are no stars or moon here... 
                return true;
            default:
                return true;
        }
    }
}
