using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004148: Marina
/// </summary>
public class _11004148 : NpcScript {
    internal _11004148(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010567$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0806025707010568$ 
                // - Ever since we were little, it's always been me, $npcName:11004149$ and the sea, hehe!
                return true;
            default:
                return true;
        }
    }
}
