using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003140: Jorge
/// </summary>
public class _11003140 : NpcScript {
    internal _11003140(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0222124707007951$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0224093607007961$ 
                // - Don't you just love the smell of my garden? My greatest joy is when I manage to reproduce extinct medicinal flowers. Heh... 
                return true;
            default:
                return true;
        }
    }
}
