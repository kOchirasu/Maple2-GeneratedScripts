using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004357: Evelyn
/// </summary>
public class _11004357 : NpcScript {
    internal _11004357(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011767$ 
                // - What a relief.
                return true;
            case 10:
                // $script:1109213607011768$ 
                // - Thank you very much for helping us, $MyPCName$.
                // $script:1120173007011847$ 
                // - And... forgive $npcName:11004349[gender:0]$. I was the one who messed up, venting my anger in my diary...
                return true;
            default:
                return true;
        }
    }
}
