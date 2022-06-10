using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001382: Zendal
/// </summary>
public class _11001382 : NpcScript {
    internal _11001382(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005382$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:1228164407005727$ 
                // - If you're thinking of investing in $map:02010036$, you're too late... friend. I was here first.
                return true;
            default:
                return true;
        }
    }
}
