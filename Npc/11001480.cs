using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001480: Tara
/// </summary>
public class _11001480 : NpcScript {
    internal _11001480(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0106111607005767$ 
                // - What?
                return true;
            case 10:
                // $script:0106111607005768$ 
                // - Light and darkness... The war between the Lumarigons and the Kargons isn't over yet.
                //   All hope lies on $npcName:11001472[gender:1]$ recovering soon. She alone can save the Lumarigons.
                return true;
            default:
                return true;
        }
    }
}
