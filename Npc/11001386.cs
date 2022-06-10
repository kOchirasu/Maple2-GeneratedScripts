using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001386: Ahas
/// </summary>
public class _11001386 : NpcScript {
    internal _11001386(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005386$ 
                // - Are you here to see me? 
                return true;
            case 30:
                // $script:1228164407005730$ 
                // - If the development project is a success, it'll bring wealth and fame to $map:02010063$. 
                return true;
            default:
                return true;
        }
    }
}
