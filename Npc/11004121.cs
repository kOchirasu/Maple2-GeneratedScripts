using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004121: Green Hood
/// </summary>
public class _11004121 : NpcScript {
    internal _11004121(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010485$ 
                // - I'll let you know if I detect any unusual movement inside the blast radius. 
                return true;
            case 10:
                // $script:0720125407010486$ 
                // - See something, say something! 
                return true;
            default:
                return true;
        }
    }
}
