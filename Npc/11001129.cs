using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001129: Greenman
/// </summary>
public class _11001129 : NpcScript {
    internal _11001129(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911192907003854$ 
                // - What? What is it?
                return true;
            case 30:
                // $script:0911192907003857$ 
                // - What? Can't you see I'm working? Leave me alone.
                return true;
            default:
                return true;
        }
    }
}
