using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000281: Konadu
/// </summary>
public class _11000281 : NpcScript {
    internal _11000281(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001095$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407001097$ 
                // - You see that guard over there? I'm telling you, no respect for scholars or history. He keeps harassing me for researching instead of sticking to his own tasks. He has no idea... 
                return true;
            default:
                return true;
        }
    }
}
