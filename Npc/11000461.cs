using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000461: Isabel
/// </summary>
public class _11000461 : NpcScript {
    internal _11000461(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002048$ 
                // - Can I help you?
                return true;
            case 50:
                // $script:0831180407002051$ 
                // - Others say Chief Hairdresser $npcName:11000255[gender:1]$ is the best, but I like $npcName:11000253[gender:0]$'s style.
                return true;
            default:
                return true;
        }
    }
}
