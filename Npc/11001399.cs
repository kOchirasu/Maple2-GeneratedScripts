using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001399: Grizzle
/// </summary>
public class _11001399 : NpcScript {
    internal _11001399(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005399$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:1228164407005733$ 
                // - After that red sandstorm, a weird ruin popped out from the dunes. I can't wait to see what kind of secrets it holds!
                return true;
            default:
                return true;
        }
    }
}
