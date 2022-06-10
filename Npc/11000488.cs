using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000488: Hari
/// </summary>
public class _11000488 : NpcScript {
    internal _11000488(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002138$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407002141$ 
                // - Rumor has it $npcName:11000406[gender:0]$ likes bad girls. I'd better become one, and quick!
                return true;
            default:
                return true;
        }
    }
}
