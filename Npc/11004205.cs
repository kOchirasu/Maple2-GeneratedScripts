using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004205: Mysterious Bladesman
/// </summary>
public class _11004205 : NpcScript {
    internal _11004205(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0813101707010958$ 
                // - Be on your guard. 
                return true;
            case 10:
                // $script:0813101707010959$ 
                // - There's no time to relax. 
                return true;
            default:
                return true;
        }
    }
}
