using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000260: Leo
/// </summary>
public class _11000260 : NpcScript {
    internal _11000260(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001072$ 
                // - What seems to be the problem?
                return true;
            case 20:
                // $script:0831180407001074$ 
                // - I hope we nab $npcName:11000064[gender:0]$. He's caused so many people so much pain.
                return true;
            default:
                return true;
        }
    }
}
