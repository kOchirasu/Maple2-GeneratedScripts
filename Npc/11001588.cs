using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001588: Rejan
/// </summary>
public class _11001588 : NpcScript {
    internal _11001588(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006076$ 
                // - I miss Calibre... 
                return true;
            case 10:
                // $script:0515180307006127$ 
                // - Can we ever go back to Calibre Island?
                return true;
            default:
                return true;
        }
    }
}
