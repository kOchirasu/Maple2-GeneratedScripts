using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004346: Aiden
/// </summary>
public class _11004346 : NpcScript {
    internal _11004346(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011749$ 
                // - Why must the holidays always be so stressful...
                return true;
            case 10:
                // $script:1109213607011750$ 
                // - Why must the holidays always be so stressful...
                return true;
            default:
                return true;
        }
    }
}
