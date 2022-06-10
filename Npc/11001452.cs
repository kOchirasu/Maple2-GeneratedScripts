using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001452: Kalco
/// </summary>
public class _11001452 : NpcScript {
    internal _11001452(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000865$ 
                // - What seems to be the problem? 
                return true;
            case 10:
                // $script:1121222006000866$ 
                // - What seems to be the problem? 
                return true;
            default:
                return true;
        }
    }
}
