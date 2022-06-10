using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004439: Unknown Humanitas Soldier
/// </summary>
public class _11004439 : NpcScript {
    internal _11004439(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1206141607011970$ 
                // - ... 
                return true;
            case 10:
                // $script:1206141607011971$ 
                // - ... 
                return true;
            default:
                return true;
        }
    }
}
