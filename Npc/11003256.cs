using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003256: Note from Kaitlyn
/// </summary>
public class _11003256 : NpcScript {
    internal _11003256(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008182$ 
                // - <font color="#909090">($npcName:11003254[gender:1]$'s name is signed on this note.)</font> 
                return true;
            case 30:
                // $script:0403155707008183$ 
                // - <font color="#909090">($npcName:11003254[gender:1]$ has left this scrawled note in a hurry.)</font> 
                return true;
            default:
                return true;
        }
    }
}
