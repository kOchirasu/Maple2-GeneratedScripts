using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004230: Ruche
/// </summary>
public class _11004230 : NpcScript {
    internal _11004230(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010810$ 
                // - ... 
                return true;
            case 10:
                // $script:0806222707010811$ 
                // - <font color='#909090'>(The fox tilts its head inquisitively.)</font> 
                return true;
            default:
                return true;
        }
    }
}
