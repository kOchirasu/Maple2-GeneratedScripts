using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004180: Bella
/// </summary>
public class _11004180 : NpcScript {
    internal _11004180(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010622$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0806025707010623$ 
                // - Hahahaha!
                return true;
            default:
                return true;
        }
    }
}
