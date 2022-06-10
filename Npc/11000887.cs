using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000887: Grinika
/// </summary>
public class _11000887 : NpcScript {
    internal _11000887(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003250$ 
                // - What do I do? 
                return true;
            case 30:
                // $script:0831180407003253$ 
                // - Did you know Ten was a Kaka? So am I. Heh heh. 
                return true;
            default:
                return true;
        }
    }
}
