using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001364: Tara
/// </summary>
public class _11001364 : NpcScript {
    internal _11001364(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215222907005047$ 
                // - All of us here, together... It reminds me of the old days. 
                return true;
            case 10:
                // $script:1230171207005754$ 
                // - Okay, I admit it. You're a good person. I can't always be right, you know. Anyway, thank you for the help. 
                return true;
            default:
                return true;
        }
    }
}
