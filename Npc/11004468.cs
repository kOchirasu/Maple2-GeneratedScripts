using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004468: Rotala
/// </summary>
public class _11004468 : NpcScript {
    internal _11004468(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012113$ 
                // - This is a placeholder line.
                return true;
            case 10:
                // $script:1227192907012114$ 
                // - This is a placeholder line.
                return true;
            default:
                return true;
        }
    }
}
