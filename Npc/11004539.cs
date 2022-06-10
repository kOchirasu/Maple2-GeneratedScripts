using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004539: Barricade Defender
/// </summary>
public class _11004539 : NpcScript {
    internal _11004539(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0104170807012621$ 
                // - Ah! You startled me!
                return true;
            case 10:
                // $script:0104170807012622$ 
                // - Ah! You startled me!
                // $script:0104170807012623$ 
                // - You better watch out who you sneak up on. I was two seconds away from tombstoning you!
                // $script:0104170807012624$ 
                // - If you have time to chat, you have time to fight!
                return true;
            default:
                return true;
        }
    }
}
