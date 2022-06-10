using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000869: Hobb
/// </summary>
public class _11000869 : NpcScript {
    internal _11000869(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003142$ 
                // - How may I help you? 
                return true;
            case 20:
                // $script:0831180407003144$ 
                // - Please don't be too loud. I can't afford any distractions from my research. 
                return true;
            default:
                return true;
        }
    }
}
