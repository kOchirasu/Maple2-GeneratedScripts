using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000487: Miyu
/// </summary>
public class _11000487 : NpcScript {
    internal _11000487(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002134$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407002137$ 
                // - Ah... Doesn't $npcName:11000406[gender:0]$ look handsome? As for you? Not so much.
                return true;
            default:
                return true;
        }
    }
}
