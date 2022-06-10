using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004177: Eve
/// </summary>
public class _11004177 : NpcScript {
    internal _11004177(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010616$ 
                // - Yes? How may I help you?
                return true;
            case 10:
                // $script:0806025707010617$ 
                // - You want to join our squad? Listen, you seem nice, but I've already got two reliable partners. I don't think we need anyone else.
                return true;
            default:
                return true;
        }
    }
}
