using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004169: Mark
/// </summary>
public class _11004169 : NpcScript {
    internal _11004169(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010593$ 
                // - What seems to be the problem?
                return true;
            case 10:
                // $script:0806025707010594$ 
                // - Guarding the armory is important work, but I'm glad Captain $npcName:11000119$ asked me to tag along.
                switch (selection) {
                    // $script:0806025707010595$
                    // - Are you on duty?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0806025707010596$ 
                // - Actually, I'm on leave at the moment. The captain asked me to be in his squad for Mushking Royale!
                return true;
            default:
                return true;
        }
    }
}
