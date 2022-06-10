using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000609: Coye
/// </summary>
public class _11000609 : NpcScript {
    internal _11000609(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002504$ 
                // - Ah... What do I do? 
                return true;
            case 10:
                // $script:0831180407002505$ 
                // - What do I do if $npcName:11000526[gender:0]$'s creditors come after me? How could he hang me out to dry like this?
                return true;
            default:
                return true;
        }
    }
}
