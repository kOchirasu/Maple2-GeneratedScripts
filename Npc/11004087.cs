using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004087: Cheeky Frog
/// </summary>
public class _11004087 : NpcScript {
    internal _11004087(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010298$ 
                // - Ribbit ribbit! 
                return true;
            case 10:
                // $script:0622133907010299$ 
                // - Ribbit ribbit! 
                return true;
            default:
                return true;
        }
    }
}
