using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000693: Ruru
/// </summary>
public class _11000693 : NpcScript {
    internal _11000693(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002796$ 
                // - $MyPCName$, welcome.
                return true;
            case 30:
                // $script:0831180407002799$ 
                // - $npcName:11000032[gender:0]$ is the only one who stayed with me when everyone else turned their backs.
                // $script:0831180407002800$ 
                // - So I'm going to stand by him, no matter what happens.
                return true;
            default:
                return true;
        }
    }
}
