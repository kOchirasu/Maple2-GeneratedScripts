using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004550: Office Guard
/// </summary>
public class _11004550 : NpcScript {
    internal _11004550(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0109163907012665$ 
                // - This is $npcName:11004401[gender:1]$'s office. I don't know what your business is, but you watch yourself around $npcName:11004401[gender:1]$.
                return true;
            case 10:
                // $script:0109163907012666$ 
                // - This is $npcName:11004401[gender:1]$'s office. I don't know what your business is, but you watch yourself around $npcName:11004401[gender:1]$.
                return true;
            default:
                return true;
        }
    }
}
