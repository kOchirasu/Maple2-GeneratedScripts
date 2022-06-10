using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000499: Gogh
/// </summary>
public class _11000499 : NpcScript {
    internal _11000499(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002172$ 
                // - Did... Did you come to see me?
                return true;
            case 30:
                // $script:0831180407002175$ 
                // - I thought that if we went deeper into the forest, we could keep $npcName:11000751[gender:1]$ safer...
                // $script:0831180407002176$ 
                // - Others pointed their fingers and called us cowards, but we didn't care. We just wanted to keep our charge safe... 
                return true;
            default:
                return true;
        }
    }
}
