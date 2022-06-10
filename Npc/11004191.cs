using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004191: Holstatt
/// </summary>
public class _11004191 : NpcScript {
    internal _11004191(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0813101707010950$ 
                // - Huh? 
                return true;
            case 10:
                // $script:0813101707010951$ 
                // - I am sorry for misleading you. But surely you must see that I had no choice. 
                return true;
            default:
                return true;
        }
    }
}
