using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001899: MC Kay
/// </summary>
public class _11001899 : NpcScript {
    internal _11001899(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109185407007370$ 
                // - Ladies and gentlemen! Are you ready for some action-packed racing?
                return true;
            case 30:
                // $script:1109185407007373$ 
                // - Are you joining today's race? Good luck!
                return true;
            default:
                return true;
        }
    }
}
