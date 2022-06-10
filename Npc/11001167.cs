using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001167: Brynn
/// </summary>
public class _11001167 : NpcScript {
    internal _11001167(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1008163207004079$ 
                // - Where in the world is he?
                return true;
            case 30:
                // $script:1008163207004082$ 
                // - Have you seen my brother? He must be somewhere around here.
                return true;
            default:
                return true;
        }
    }
}
