using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000594: Lavi
/// </summary>
public class _11000594 : NpcScript {
    internal _11000594(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002382$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407002384$ 
                // - Everything in this world has energy, and lava has the most potent energy of all! 
                return true;
            default:
                return true;
        }
    }
}
