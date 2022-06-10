using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000421: Benielle
/// </summary>
public class _11000421 : NpcScript {
    internal _11000421(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001760$ 
                // - May I help you? 
                return true;
            case 30:
                // $script:0831180407001762$ 
                // - I came here with my daughter $npcName:11000420[gender:1]$ to start a new life. But if those turtles don't stop showing up, we'll have to move again. 
                return true;
            default:
                return true;
        }
    }
}
