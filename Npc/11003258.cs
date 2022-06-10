using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003258: Kaitlyn
/// </summary>
public class _11003258 : NpcScript {
    internal _11003258(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008191$ 
                // - What is it?
                return true;
            case 30:
                // $script:0403155707008192$ 
                // - This is why I don't like kids. They want to be heroes, but they can't even tie their shoes on their own.
                // $script:0403155707008193$ 
                // - But don't you think Professor $npcName:11003251[gender:0]$ is looking especially good lately? His skin has taken on a beautiful pasty sheen from all his hard work. I could stare at him all day...
                return true;
            default:
                return true;
        }
    }
}
