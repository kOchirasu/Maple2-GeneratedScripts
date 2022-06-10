using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004086: Singing Frog
/// </summary>
public class _11004086 : NpcScript {
    internal _11004086(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010295$ 
                // - Ribbit ribbit... 
                return true;
            case 10:
                // $script:0622133907010296$ 
                // - Ribbit ribbit... 
                return true;
            default:
                return true;
        }
    }
}
