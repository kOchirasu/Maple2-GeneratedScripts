using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000012: Bogie
/// </summary>
public class _11000012 : NpcScript {
    internal _11000012(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000062$ 
                // - What seems to be the problem? 
                return true;
            case 40:
                // $script:0831180407000066$ 
                // - If I keep working like this, exhaustion's going to get me. And what's worse is that $npcName:11000252[gender:0]$ still won't appreciate all my hard work! You know, it's so hard to take care of $map:02000001$ by myself. 
                return true;
            default:
                return true;
        }
    }
}
